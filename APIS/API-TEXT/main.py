from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def status():
    return "API TEXTO-VOZ"

if __name__ == "__main__":
    app.run(debug=True)