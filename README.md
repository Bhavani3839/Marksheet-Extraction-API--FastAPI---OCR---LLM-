## 📄 Marksheet Extraction API (FastAPI + OCR + LLM) ##

This project is an **AI-powered marksheet extraction API** built using **FastAPI**, **OCR (EasyOCR + img2table)**, and **LLMs**.  
It allows you to upload a marksheet (image or PDF) and get structured **JSON output** containing candidate details, subject-wise marks, and confidence scores.

---
## Demo ##
![Marksheet Example](![images (3)](https://github.com/user-attachments/assets/fff7f552-fca3-4009-bf22-536638b248de)
)


## 🚀 Features
- Extract:
  - Candidate details (Name, Roll No, Registration No, DOB, etc.)
  - Institution & Board/University info
  - Subject-wise marks (subject, max marks, obtained marks, result)
- Confidence scores for extracted fields.
- REST API endpoints built with **FastAPI**.
- Easily extendable for new formats or boards.

---

## 🛠️ Tech Stack
- **FastAPI** (API framework)
- **EasyOCR** (OCR engine)
- **img2table** (Table detection & parsing)
- **PyPDF2 / pdf2image** (PDF → Image conversion)
- **LLM integration** (text correction & structuring)
- **Uvicorn** (ASGI server)

---

## 📂 Project Structure
Marksheet-Extraction-API--FastAPI---OCR---LLM-/
│── app.py # Main FastAPI app
│── requirements.txt # Project dependencies
│── utils/ # Helper functions (OCR, parsing, LLM, etc.)
│── samples/ # Example marksheets
│── output/ # Extracted JSON samples
│── README.md # Project documentation
