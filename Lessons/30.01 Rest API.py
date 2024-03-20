# creating a route
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Home"


# methods we can use: GET, POST, PUT, DELETE
# GET: Request data from a specified source
# POST: Create a source.
# PUT: Update a source
# DELETE: remove a source

if __name__ == "__main__":
    app.run(debug=True)
