from flask import Flask, request
from flask_cors import CORS, cross_origin
from User import User
import pymysql
import json


app = Flask(__name__)
CORS(app)
userData = []

@app.route('/data')
@cross_origin()
def data():
    return (
        {
            "Name" : "Sharath",
            "Age" : "Undefined"
        }
    )

@app.route('/addUser', methods=['POST'])
@cross_origin()
def addUser():
    user = request.get_json()
    userNew = User(user["name"], user["email"], user["password"])
    userData.append(userNew)
    return user, 200

@app.route('/listUser', methods=['GET'])
@cross_origin()
def listUsers():
    jsonStr = json.dumps([obj.__dict__ for obj in userData])
    return jsonStr

@app.route('/')
@cross_origin()
def index():
    return "You are stoopid"

if __name__ == '__main__':
    app.run(debug=True)