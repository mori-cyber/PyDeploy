import qrcode
import io
from flask import Flask, request, send_file, jsonify

app = Flask(__name__)

@app.route("/generate", methods=['POST'])
def generate_qr():
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Create a QR code image
        img = qrcode.make(data)
        
        # Save the image to a BytesIO object
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8083, debug=True, host="0.0.0.0")
