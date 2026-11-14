from flask import Flask, request, jsonify
from flask_cors import CORS
from app import add_customer

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Customer Registration API is running."
    })


@app.route("/register", methods=["POST"])
def register_customer():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Please send valid customer information."
        }), 400

    email = data.get("email", "")
    name = data.get("name", "")
    phone = data.get("phone", "")

    success, message = add_customer(email, name, phone)

    if success:
        return jsonify({
            "success": True,
            "message": message
        }), 201

    status_code = 409 if message == "Duplicate email address." else 400

    return jsonify({
        "success": False,
        "message": message
    }), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
