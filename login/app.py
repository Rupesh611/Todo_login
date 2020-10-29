from flask import Flask, request , jsonify

from flask_restful import Resource, Api , reqparse

from front import *
from controller import *
app = Flask(__name__)
key = 'secret'

api= Api(app)

# if password has special characters we need to encode them
#connect(host ="mongodb+srv://akash:akash@cluster0.zqitl.mongodb.net/dbname?retryWrites=true&w=majority")

#view
api.add_resource(register,'/register')

#view
api.add_resource(login,'/login')


api.add_resource(info,'/info')

#app.run(port = 5000, debug=True)