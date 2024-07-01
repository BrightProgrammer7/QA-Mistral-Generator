# Question-Answer-Generation-App-using-Mistral-7B

## Overview
This project is a Question Answer Generation App that leverages the Mistral 7B model, Langchain, and FastAPI to generate answers to user-provided questions. The application processes PDF files to generate questions and answers, which are then saved in a CSV file.

## Features
- **Question Generation**: Generate questions based on the content of PDF files.
- **Answer Generation**: Generate answers to the generated questions using the Mistral 7B model.
- **API Integration**: FastAPI is used to create a robust and scalable API.
- **Chain of Thought**: Langchain is utilized to manage the flow of information and logic.
- **PDF Processing**: Extract text from PDF files for question and answer generation.
- **CSV Export**: Save the generated questions and answers in a CSV file.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/BrightProgrammer7/QA-Mistral-Generator.git
    cd QA-Mistral-Generator
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Start the FastAPI server:
    ```bash
    uvicorn app:app --reload
    ```
    or 
    ```bash
    python app.py
    ```
2. Access the API documentation at `http://127.0.0.1:8000/docs`.

3. Access the main application at `http://127.0.0.1:8000/index.html`.

## API Endpoints
- **GET /**: Renders the main index page.
- **POST /upload**: Upload a PDF file for processing.
    - **Parameters**:
        - `pdf_file`: The PDF file to be uploaded.
        - `filename`: The name of the PDF file.
- **POST /analyze**: Analyze the uploaded PDF file and generate a CSV file with questions and answers.
    - **Parameters**:
        - `pdf_filename`: The name of the uploaded PDF file.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
"# QA-Mistral-Generator" 
