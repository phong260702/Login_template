from flask import Flask
from flask_cors import CORS
import flask
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello"
@app.route("/login", methods = ["POST"])
def login():
    if flask.request.method == "POST":
        username = flask.request.form['username']
        password = flask.request.form['password']
        with open("user.json", "r") as f:
            data = json.load(f)
            for x in data:
                if (x["username"] == username and x["password"] == password):
                    print("Success")
                    return "Email: " + username + " <br> " + "Password: " + password
        return "Invalid username or password"

@app.route('/users', methods=["GET"])
def users():
    print("Testing GET")
    with open("user.json", "r") as f:
        data = json.load(f)
        return flask.jsonify(data)


@app.route('/users', methods=["POST"])
def dele():
    print("Testing DELETE")
    print(flask.request.form['username'])
    with open("user.json", "r") as f:
        data = json.load(f)
        for i in range(len(data)):
            if data[i]["username"] == flask.request.form['username']:
                deleted = data[i]
                del data[i]
                with open("user.json", "w") as f2:
                    data = json.dump(data, f2)
                return deleted
    return "No value"
@app.route('/users', methods=["PUT"])
def add_user():
    print("Testing PUT")
    with open("user.json", "r+") as f:
        data = json.load(f)
        username = flask.request.form['username']
        for x in data:
            if x["username"] == username:
                return "Duplicate"

        password = flask.request.form['password']
        data2 = { "username" : username,
                 "password": password}
        data.append(data2)
        with open("user.json", "w") as f2:
            data = json.dump(data, f2)

    return data2


if __name__ == "__main__":
    app.run(port = 12345, debug= True, host="0.0.0.0")

