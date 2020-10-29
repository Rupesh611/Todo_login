from flask_restful import Resource, Api , reqparse
from flask import Flask, request , jsonify
import sys
# sys.path is a list of absolute path strings
sys.path.append('C:\\Users\\Rupesh Gupta\\PycharmProjects\\collab_project\\Todo\\login')
print(sys)
from loginmodel import *

from model import copytodo
#ctodo = copytodo()

class register(Resource):
    def post(self):
        response = request.get_json(force=True)
       # print(response)
        inform = info(Age =response['info']['Age'], Born = response['info']['Born'])
        registering = User(Username=response['username'], Password=response['password'],information=inform).save()
        copytodo.add_people(response['username'])
        return "succesfully registered"