from flask import Flask
from flask import request
import json
import jwt

key = 'secret'
from controller import contro

from mongoengine import connect

app = Flask(__name__)

c = contro.Controller()



@app.route("/Heading", methods=["POST"])
def addHeading():
    request_payload = request.get_json(force=True)
    val =contro.cred_check(request)
    if val == 1:

        ret_json = c.add_heading(request_payload,jwt.decode(request.headers['Authorization'], key, algorithms='HS256'))

        return json.dumps(ret_json)
    else:
        return val

@app.route("/Heading")
def getheading():
    val = contro.cred_check(request)
    if val == 1:
        return c.get_heading(jwt.decode(request.headers['Authorization'], key, algorithms='HS256'))
    else:
        return val

@app.route("/Task/<heading>", methods=["GET"])
def getTask(heading):
    val = contro.cred_check(request)
    if val == 1:
        return json.dumps(list(c.get_Task(heading,jwt.decode(request.headers['Authorization'], key, algorithms='HS256'))))
    else:
        return val

@app.route("/Task/<heading>", methods=["POST"])
def addtask(heading):

    request_payload = request.get_json(force=True)
    val = contro.cred_check(request)
    if val == 1:
        c.add_task(heading,request_payload,jwt.decode(request.headers['Authorization'], key, algorithms='HS256'))
        ret_json = {
            "msg": "Added Task"
        }
        return json.dumps(ret_json)
    else:
        return val

@app.route("/markTaskComplete/<heading>", methods=["POST"])
def marktaskcomplete(heading):
    val = contro.cred_check(request)
    if val == 1:
        request_payload = request.get_json(force=True)
        return json.dumps(c.mark_taskcomplete(heading,request_payload,jwt.decode(request.headers['Authorization'], key, algorithms='HS256')))
    else:
        return val







#LOGIN API
from flask import Flask, request , jsonify

from flask_restful import Resource, Api , reqparse

from login.front import *
from login.controller import *

key = 'secret'

api= Api(app)

disconnect()
connect(host ="mongodb+srv://rgupta:rgupta@cluster0.zidic.mongodb.net/user?retryWrites=true&w=majority")
#view
api.add_resource(register,'/register')


api.add_resource(login,'/login')


api.add_resource(info,'/info')



if __name__ == "__main__":
    app.run()


