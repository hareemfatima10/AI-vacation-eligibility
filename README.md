# AI Vacation Eligibility System

## Overview

Interactive dialogue system that assists employees to submit vacation requests using their data and company's SOPs. 
Made using Streamlit, LangChain, OpenAI and Faiss VectorStore.

## Prerequisites

Before you begin, ensure you have the following installed and set up:

- **Python:** Ensure Python 3.x is installed on your system. You can download Python from [python.org](https://www.python.org).
- **OpenAI API Key:** Obtain an API key from OpenAI.

## Installation

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/hareemfatima10/AI-vacation-eligibility.git
   cd AI-vacation-eligibility
   ```

2. Create a Python virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and store your OpenAI API key:
   ```
   OPENAI_API_KEY="Your key"
   ```

## Usage

To run the application, execute the following command:
```
streamlit run app.py
```

This command will open the project in another browser window.

## Assumptions

- The system assumes there are three sample records in the database to demonstrate different scenarios of employee data.
- The current session's userID is fixed for testing purposes but can be changed within the frontend.

## Screenshots
![John_interaction](screenshots/John_interaction.png)
