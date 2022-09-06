import os
from datetime import *
#from datetime import timedelta, datetime, date
from random import randint
import re
# XML notes: import xml.etree.ElementTree as ET
class Command:
	def __init__(this,command="",command_type="",command_options=[],command_alias=[],command_help=""):
		this._command=command
		# System - internal command called automatically or part of commands below. (not including logging that is)
		# Command - command from user input
		# None-User input
		this._command_type=command_type
		this._command_options=command_options
		this._command_alias=command_alias
		this._command_help=command_help
	def getCommand(this):
		return this._command
	def getCommandType(this):
		return this._command_type
	def getCommandOptions(this):
		return this._command_options
	def getCommandHelp(this):
		return this._command_help
	def run(this, input):
		try:
			return this._command[input]
		except:
			try:
				return this._command_alias[input]
			except:
				print("No Command")
	def printCommand(this):
		print(this._command)


