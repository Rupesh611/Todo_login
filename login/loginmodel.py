
from mongoengine import *

class info(EmbeddedDocument):

	Age = StringField()
	Born = StringField()

class User(Document):

	Username = StringField(max_length= 20, required= True)
	Password  = StringField(max_length=10 , min_length= 6, required = True)
	information = (EmbeddedDocumentField(info))