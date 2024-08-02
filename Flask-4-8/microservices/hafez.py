from flask import Flask, jsonify
import hafez

app = Flask(__name__)

@app.route("/fal", methods=['GET'])
def get_fal():
    try:
        omen = hafez.get_fal()
        interpretation = omen["interpretation"]
        return jsonify({"fal": interpretation})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8081, debug=True, host="0.0.0.0")
