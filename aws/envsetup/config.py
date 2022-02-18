import boto3
import os
import time
import string
from random import choice
from configparser import ConfigParser


def generate_random_names(length=8, chars=string.digits):
	"""Credit to Devin Leung"""
	return ''.join([choice(chars) for i in range(length)])


def vpn_server_names() -> object:
	for i in range(1):
		print("vpn_server_" + generate_random_names(4))


def client(self):
	connect = create_session().client(self)
	return connect


def resource(self):
	connect = create_session().resource(self)
	return connect

# def getAccessKeys(access_key_id, secret_access_key):
#    pass


def serverStartUpScripts(self):
	pass


# Reference RapidWire
def serverCleanUps(self):
	if os.path.isfile(""):
		os.remove(self)
	elif os.path.isfile(""):
		os.remove("")
	pass


def checkOS():
	operating_system = ""
	if os.name == "posix":
		operating_system = "Linux"
	elif os.name == "nt":
		operating_system = "windows"
	return operating_system



def shell(self):
	sh = os.system(self)
	return sh


def CheckFilepath(filename):
	if os.path.exists(filename):
		print("Agreement Policy Found ....")
	else:
		return False



def realTime():
	return time.ctime()


def command(self):
	return os.system(self)


def wrongOptions(self):
	return self


def display(self):
	for i in self:
		print(i)


def choices(self):
	option = input(self)
	return option


def server_name():
	ServerNames = vpn_server_names()
	return ServerNames


def create_session():

	cfg = ConfigParser()
	cfg.read('aws_configure_file.ini')
	#cfg.sections()
	aws_id = cfg.get('default', 'aws_access_key_id')
	aws_secret = cfg.get('default', 'aws_secret_access_key')
	region_zone = cfg.get('default', 'regional_zone')

	session = boto3.Session(aws_access_key_id=aws_id, aws_secret_access_key=aws_secret, region_name=region_zone)
	return session



#----------------------------------------------------------------------------
""" IMAGES OF AWS """

ImageIdUbuntu = ["ami-0ca5c3bd5a268e7db",
				 "ami-0047c52ed2f1519a3",
				 "ami-007d3f6486d9d3e6c",
				 "ami-008dcc948fb88a63a"
				 ]

ImageIdDebian = ["ami-97b790ef",
				 "ami-b4f8edcd",
				 "ami-cbad0eb3",
				 "ami-818eb7b1"
				 ]

ImageIdCentos = ["ami-00a092bd80d7ff7dd",
				 "ami-00b6409ca5f35471f",
				 "ami-00d11f107a772bf8d",
				 "ami-010afb7ef35a5c1ea"
				 ]

ImageIdAmazon = ["ami-036c394a8b6e11a45",
				 "ami-03920bf5f903e90d4",
				 "ami-041fcb43d4730cf32",
				 "ami-05a8e8d7f6573b136",
				 ]

BOOLEAN = True
#d8bb48