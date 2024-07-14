from db_utils import get_employee_record
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
import streamlit as st

load_dotenv(find_dotenv())


DB_FAISS_PATH = 'vectorstore/db_faiss'
current_date = datetime.now().strftime("%d-%b-%Y")

system_prompt = (
"""
    Role: You are an assistant tasked with evaluating vacation leave requests based on the given document and given {user_data}. 
    Goal: If user is eligible for vacation, process the request. If they are not eligible, inform them only the main reason and ask them if they want to change the dates. 
    Assume all dates user enters are from 2024, unless year is specified. 
    Follow the document in order of steps
    Do not show user their data or the steps.
    Context: {context}
    User Data: {user_data}
    Current Date: {current_date}
"""
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
        MessagesPlaceholder("chat_history", optional=True)
    ]
)

def retrieval_qa_chain(llm, prompt, db, question, user_data, history):
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(db.as_retriever(search_kwargs={'k': 3}), question_answer_chain) 
    response = chain.invoke({"input":question, "user_data":user_data, "chat_history": history, "current_date":current_date})

    return response


def generate_response(question, user_data, history):
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    response = retrieval_qa_chain(llm, prompt,db, question, user_data, history)

    return response

def main():
    st.set_page_config(
    page_title="Vacation System",
    layout="centered"
    )
    #For testing purposes, the project assumes that the userID is within the frontend of the session. To test for other users from the database, change this id
    st.session_state['UserID'] = 3
    if "frontend_messages" not in st.session_state:
        st.session_state["frontend_messages"] = [{"role": "assistant", "content": "Hi, how may I help you"}]

    for msg in st.session_state.frontend_messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.frontend_messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        st.session_state["response"] = ""
        record = get_employee_record(st.session_state['UserID'])
        
        response = generate_response (prompt, record, st.session_state.frontend_messages)
        st.chat_message("assistant").write(response["answer"])
        st.session_state.frontend_messages.append({"role": "assistant", "content": response["answer"]})

if __name__ == '__main__':
    main()