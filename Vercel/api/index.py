from flask import Flask, request, jsonify
import os

# the 'api.' part is needed since Vercel looks from the top level directory
from api.utilities import chain


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/generate_title", methods=["GET"])
def generate_title_endpoint():
    name = request.args.get("name")
    key = request.args.get("key")
    if key == os.environ.get("ENDPOINT_AUTH_KEY"):
        result = chain.generate_title(name)
        return jsonify({"result": result})
    else:
        return jsonify({"error": "not allowed"}), 401
