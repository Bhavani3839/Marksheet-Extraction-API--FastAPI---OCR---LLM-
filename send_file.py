import requests
import os

API_URL = "http://127.0.0.1:5000/upload-marksheet"
MARKSHEET_PATH = os.path.join("uploads", "download.jpeg")  # replace with your file name

def send_marksheet(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "rb") as f:
        response = requests.post(API_URL, files={"marksheet": f})

    try:
        print("Response from API:")
        print(response.json())
    except Exception as e:
        print(f"Failed to parse JSON: {e}")
        print(response.text)

if __name__ == "__main__":
    send_marksheet(MARKSHEET_PATH)
