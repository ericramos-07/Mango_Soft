# Mango_Soft

This project is part of a thesis on "A CNN-Based Philippine Mango Classification and Quality Assessment with Price Estimation using Random Forest Regression." The application uses a Flask API to serve a machine learning model that estimates mango prices based on classification, assessment, and historical price data.

## Prerequisites

Make sure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

## Installation

1. **Clone the repository**  
   Open your terminal and clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Mango_Soft.git

2. Navigate to the project folder
   cd Mango_Soft

3. Open the project in Visual Studio Code (VS Code)
   Open VS Code and load the project folder.

4. Create a virtual environment
   In your terminal, create a virtual environment to manage dependencies:
   python -m venv .venv

5. Activate the virtual environment
   - On Windows
     .venv\Scripts\activate
   - On Mac/Linux
     source .venv/bin/activate

6. Install dependencies
   With the virtual environment activated, install the required packages using requirements.txt:
   pip install -r requirements.txt

## Running the Application

1. Start the Flask API
   In the terminal, run:
   py main.py
   This will start the Flask server at http://127.0.0.1:5000/.

2. Test the API
   The /predict endpoint can be accessed to make predictions on mango prices. You can use a tool like Postman or curl to send a POST request. Example JSON payload:
   {
    "Year": 2024,
    "Type_Carabao": 1,
    "Type_Indian": 0,
    "Type_Pico": 0,
    "Class_Class A": 1,
    "Class_Class B": 0,
    "Class_Class C": 0,
    "Class_Class D": 0,
    "Class_Class E": 0,
    "Month_January": 1,
    "Month_February": 0,
    "Month_March": 0,
    "Month_April": 0,
    "Month_May": 0,
    "Month_June": 0,
    "Month_July": 0,
    "Month_August": 0,
    "Month_September": 0,
    "Month_October": 0,
    "Month_November": 0,
    "Month_December": 0
   }

3. Shut down the server
   To stop the server, press Ctrl + C in the terminal.


