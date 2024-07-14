from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from dotenv import load_dotenv, find_dotenv

DATA_PATH = 'data/'
DB_FAISS_PATH = 'vectorstore/db_faiss'
load_dotenv(find_dotenv())

# Create vector database
def create_vector_db():
    loader = DirectoryLoader(DATA_PATH,
                             glob='*.pdf',
                             loader_cls=PyPDFLoader)

    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=700,
                                                   chunk_overlap=140)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
    create_vector_db()

