from flask import Flask, request, jsonify
from img2table.ocr import EasyOCR
from img2table.document import PDF
import pandas as pd
import openpyxl
import os
import time
from werkzeug.utils import secure_filename

# -------------------- Flask App -------------------- #
app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"

# -------------------- OCR -------------------- #
# Initialize EasyOCR with English and CPU only
easyocr = EasyOCR(lang=["en"], kw={"gpu": False})

# -------------------- Routes -------------------- #
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Marksheet OCR API is running. Use POST /upload-marksheet to upload a PDF or image."
    })

@app.route('/upload-marksheet', methods=['POST'])
def upload_marksheet():
    if 'marksheet' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['marksheet']

    # Validate file type
    if not file.filename.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg')):
        return jsonify({'error': 'Invalid file type. Only PDF or images allowed.'})

    # Save uploaded file
    uploads_dir = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(uploads_dir, exist_ok=True)
    filename = secure_filename(file.filename)
    filepath = os.path.join(uploads_dir, filename)
    file.save(filepath)

    # Process marksheet
    marksheet_json = process_marksheet_json(filepath)

    # Cleanup uploaded file
    try:
        os.remove(filepath)
    except:
        pass

    return jsonify({'marksheet': marksheet_json, 'message': 'File processed successfully'})

# -------------------- Processing Function with Confidence -------------------- #
def process_marksheet_json(filepath):
    try:
        # Generate unique Excel filename
        excel_file = f"tables_{int(time.time())}.xlsx"
        # Convert PDF/image to Excel using OCR
        pdf = PDF(src=filepath)
        pdf.to_xlsx(excel_file, ocr=easyocr, implicit_rows=True, borderless_tables=False, min_confidence=30)

        # Load Excel
        wb = openpyxl.load_workbook(excel_file, data_only=True)
        sheet = wb.active

        # Extract headers
        headers = [cell.value if cell.value else f"Unnamed_{i}" for i, cell in enumerate(sheet[1])]

        # Extract rows with confidence
        data = []
        for row in sheet.iter_rows(min_row=2):
            row_data = {}
            for i, cell in enumerate(row):
                header = headers[i]
                value = cell.value
                # Try to get confidence from cell comment (img2table stores confidence there)
                confidence = cell.comment.text if cell.comment else None
                row_data[header] = {
                    "value": value,
                    "confidence": float(confidence) if confidence else None
                }
            data.append(row_data)

        # Filter only SUBJECT and TOTAL MARKS columns
        specific_column_names = ["SUBJECT", "TOTAL MARKS"]
        filtered_data = []
        for row in data:
            filtered_row = {col: row[col] for col in row if any(spec_col.lower() in col.lower() for spec_col in specific_column_names)}
            filtered_data.append(filtered_row)

        # Cleanup Excel
        try:
            os.remove(excel_file)
        except:
            pass

        return filtered_data

    except Exception as e:
        return {"error": str(e)}

# -------------------- Main -------------------- #
if __name__ == '__main__':
    app.run(debug=True)
