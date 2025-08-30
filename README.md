## 📄 Marksheet Extraction API (FastAPI + OCR + LLM) ##

This project is an **AI-powered marksheet extraction API** built using **FastAPI**, **OCR (EasyOCR + img2table)**, and **LLMs**.  
It allows you to upload a marksheet (image or PDF) and get structured **JSON output** containing candidate details, subject-wise marks, and confidence scores.

---
## Demo ##
## marksheet ##
![images (3)](https://github.com/user-attachments/assets/fff7f552-fca3-4009-bf22-536638b248de)
## API Page ##
![IMG-20250830-WA0008](![API](https://github.com/user-attachments/assets/825cdd9e-644b-4c5b-8865-9b80b5dbd683)
)
## JSON output 1 ##
![Screenshot_2025-08-30-22-37-36-06_99c04817c0de5652397fc8b56c3b3817](https://github.com/user-attachments/assets/bb6eb2a4-0454-4b58-afdc-1294ef36e88a)
## JSON output ##
![json](https://github.com/user-attachments/assets/562a6221-36e6-4709-b1bf-d801cdf28fc8)





## 🚀 Features ##
- Extract:
  - Candidate details (Name, Roll No, Registration No, DOB, etc.)
  - Institution & Board/University info
  - Subject-wise marks (subject, max marks, obtained marks, result)
- Confidence scores for extracted fields.
- REST API endpoints built with **FastAPI**.
- Easily extendable for new formats or boards.

---

## 🛠️ Tech Stack ##
- **FastAPI** (API framework)
- **EasyOCR** (OCR engine)
- **img2table** (Table detection & parsing)
- **LLM integration** (text correction & structuring)
- **Uvicorn** (ASGI server)

---

## 📂 Project Structure ##
Marksheet-Extraction-API--FastAPI---OCR---LLM-/
│── app.py # Main FastAPI app
│── requirements.txt # Project dependencies
│── utils/ # Helper functions (OCR, parsing, LLM, etc.)
│── samples/ # Example marksheets
│── output/ # Extracted JSON samples
│── README.md # Project documentation

 ## Create virtual environment ##
 python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

## Install dependencies ##
pip install -r requirements.txt

## Run the API ##
API will be available at:
  Running on http://127.0.0.1:5000
 (Swagger UI)
 
 ## Example Request (using Python) ##
 import requests

url =  Running on http://127.0.0.1:5000
files = {"file": open("samples/marksheet.jpeg", "rb")}
response = requests.post(url, files=files)

print(response.json())

## Example JSON Response ##
{
  "candidate": {
    "name": "Rahul Sharma",
    "father_name": "Suresh Sharma",
    "dob": "15-07-2003",
    "roll_no": "123456",
    "registration_no": "REG2023XYZ",
    "board": "CBSE",
    "institution": "Delhi Public School"
  },
  "subjects": [
    {"subject": "Maths", "max_marks": 100, "marks_obtained": 89},
    {"subject": "Physics", "max_marks": 100, "marks_obtained": 76},
    {"subject": "Chemistry", "max_marks": 100, "marks_obtained": 82}
  ],
  "confidence": {
    "name": 0.95,
    "roll_no": 0.92,
    "subjects": 0.90
  }
}
