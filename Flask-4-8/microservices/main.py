import requests
import io
from flask import Flask, jsonify, send_file

app = Flask(__name__)

hafez_url = "http://127.0.0.1:8081/fal"
khayyam_url = "http://127.0.0.1:8082/today"
qr_code_url = "http://127.0.0.1:8083/generate"

def fale_hafez():
    response = requests.get(hafez_url)
    response.raise_for_status()
    return response.json().get("fal")

def rooz_shomar_khayam():
    response = requests.get(khayyam_url)
    response.raise_for_status()
    return response.json().get("today")

def qr_code(data):
    try:
        response = requests.post(qr_code_url, json={"data": data})
        response.raise_for_status()
        if response.status_code == 200:
            return io.BytesIO(response.content)
        else:
            print(f"QR code service returned status code {response.status_code} with message: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return None

@app.route("/", methods=['GET'])
def root():
    try:
        fal_hafez = fale_hafez()
        khayam_result = rooz_shomar_khayam()
        result_data = f"Tafaol: {fal_hafez}, Today: {khayam_result}"
        qr_code_image = qr_code(result_data)
        if qr_code_image:
            return send_file(qr_code_image, mimetype='image/png')
        else:
            return jsonify({"error": "Failed to generate QR code"}), 500
    except Exception as e:
        print(f"Error in root endpoint: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8080)
