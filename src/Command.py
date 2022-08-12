import os
from datetime import *
#from datetime import timedelta, datetime, date
from random import randint
import re
# proof of concept
#a=True
#i = 0
#while(a):
# n=input("A: ")
# i+=1
# if(i==10):
#  a=False
# print(n)
# end of proof of concept
# Notes: commands for "call"
# Y - new call
# yes - new call
# new call - new call
#:
class Command:
	def __init__(this):
		this.line=""
		this.command=""
		this.option=""
		this.other=""
		this.commands = []
		#this._TEST1()
	def listOfCommands(this):
		for command in this.commands:
			print(command)
	def addCommand(this, command):
		this.commands.append(command)
	def zAppendCommandTest(this):
		this.commands.append("TEST 1")
		this.commands.append("TEST 2")
		this.commands.append("TEST 3")
	def _getDateTime(this):
		return datetime.now()
	def zDateTimeTest(this):
		return this._getDateTime()
	def printHelp(this, command):
		print("Getting help for {}")
		return 0
