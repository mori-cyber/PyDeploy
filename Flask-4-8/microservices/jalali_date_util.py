from flask import Flask, jsonify
# from khayyam import JalaliDate
from khayyam import JalaliDatetime

app = Flask(__name__)

@app.route("/today", methods=['GET'])
def get_today():
    try:
        today = JalaliDatetime.now().strftime('%Y-%m-%d')
        return jsonify({"today": today})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8082, debug=True, host="0.0.0.0")
