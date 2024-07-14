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

- The system has three sample records in the database to demonstrate different scenarios of employee data. Following are the records for John and Alice.
  
   ID: 1, Name: John Doe, Join Date: January 1, 2023, Probation End Date: April 1, 2023, Probation Status: Not in probation, Remaining Paid Vacation Days: 15, Department ID: 1
  
   ID: 3, Name: Alice Smith, Join Date: June 20, 2024, Probation End Date: October 20, 2024, Probation Status: In probation, Remaining Paid Vacation Days: 30, Department ID: 2

- The system assumes that the User ID is within the frontend of the system therefore, the current session's userID is set inside the app.py file (line 60) for testing purposes. To test for other employees, change the User ID to that of the employee
  
## Screenshots

### John's Interaction

<img src="https://github.com/hareemfatima10/AI-vacation-eligibility/raw/main/screenshots/John_interaction.PNG" alt="John's Interaction" width="400" />

### Alice's Interaction

<img src="https://github.com/hareemfatima10/AI-vacation-eligibility/raw/main/screenshots/Alice_interaction.PNG" alt="Alice's Interaction" width="400" />
