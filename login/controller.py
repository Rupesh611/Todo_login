import jwt
import json
from flask_restful import Resource, Api, reqparse
from flask import Flask, request, jsonify

from login.loginmodel import *

key = 'secret'


class login(Resource):
	def post(self):
		response = (request.get_json(force=True))
		val= token_Ret(response)
		val= val.decode('UTF-8')
		print(type(val))
		return (val)


# controller
def token_Ret(response):
	if authenticate(response['username'], response['password']):
		print(type(jwt.encode({'sub': response['username']}, key, algorithm='HS256')))
		return jwt.encode({'sub': response['username']}, key, algorithm='HS256')
	else:
		return ("Invalid credentials")


def authenticate(username, password):

	for user in User.objects(Username=username):
		if user.Password != password:
			return False
		else:
			return True


# controller
class info(Resource):
	def get(self):
		try:
			payload = jwt.decode(request.headers['Authorization'], key, algorithms='HS256')
			for user in User.objects:
				if user.Username == payload['sub']:

					return json.loads(user.information.to_json())
					break



		except jwt.ExpiredSignatureError:
			return 'Signature expired. Please log in again.'

		except jwt.InvalidTokenError:
			return 'Invalid token. Please log in again.'