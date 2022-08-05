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
class Command:
	def __init__(this):
		this.line=""
		this.command=""
		this.option=""
		this.other=""
		this.commands = []
		this._TEST1()
	def listOfCommands(this):
		for command in this.commands:
			print(command)
	def addCommand(this, command):
		this.commands.append(command)
	def _TEST1(this):
		this.commands.append("TEST 1")
		this.commands.append("TEST 2")
		this.commands.append("TEST 3")

