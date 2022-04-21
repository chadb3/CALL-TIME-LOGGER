from time import *
from datetime import timedelta
from random import randint

def pirntAbout():
	print_str = """   *******************************************************************************************
   *                               ABOUT: Call Logger                                        *
   *******************************************************************************************
   * Call logger is a Python script meant to alleviate the time it takes for me to record    *
   * when a call comes in. It will more accurately log the time & date of the call.          *
   * Current stretch goals include: Client Account, Client Name, what product, priority,    *
   * and auto gen the priority 1 email for me… Why?! you may ask. Because FUN                *
   *******************************************************************************************
   * Features: Accurate Time and Date Logging (often difficult to do by hand quickly)        *
   * Features cont: Menu system with many commands                                           *
   * Features cont: call count, and writes to a file                                         *
   ******************************************************************************************* """
	print("\n\n"+print_str+"\n\n")
	return 0
	
def printTop():
	print("\n\n*******************************************************************************************")
	print("*************************** TYPE Y or YES to LOG A CALL ***********************************")
	print("*******************************************************************************************")
	print("***************************** TYPE HELP FOR COMMAND LIST **********************************")
	print("*******************************************************************************************\n\n")
	return 0
	
def printStats():
	
	return 0

c1 = randint(0,551)

commandYes = ["*Commands to log a new call*", "\t1. Yes", "\t2. Y"]
commandQuit = ["*Commands to quit the program*","\t1. Exit", "\t2. Quit"]
commandLogging = ["*Commands to manually write to file*","\t1. Write"]
commandRemove = ["*Commands to remove a call*","\t1. Remove", "\t2. RM", "\tUse Like: \"rm 2\" to remove call 2"]
commandsHelp = ["*Commands dealing with LISTS & HELP*","\t1. List","\t2. Help","\t3. LS", "\t4. Man"]
commandsPrint = ["*Commands to dealing with output*", "\t1. Print", "\t2. CD (current delta)", "\t3. Boom", "\t4. About", "\t5. Top"]
commandList = [commandYes,commandQuit,commandLogging,commandRemove,commandsHelp, commandsPrint]

listOfProducts = ["A", "B", "C", "D", "E", "F", "G"]

listOfProducts.sort()
listOfCalls=[]

callCount=0
#pulled from file to be added to...
cumulativeCallCount = 0
#***********************************

callData = []

callText = "\tCall#: {}\tCall Time: {}\tCall Date: {}\t Time Since Previous Call: {} (H:mm:ss)\t"

callDate = ""

callTime = ""

lastCallDate = ""

lastCallTime = ""

time_current_call =0

time_previous_call = 0

time_delta = 0 

username = ""


# Generate files if they don't already exists
# the log file 
def genFiles():
	logFileName = "0callStats.txt"
	file_directory = "./call_logs/"	
	FFF = file_directory + logFileName
	try:
		a=open(FFF,'r')
		a.close()
		print("Log File Exists")
		return 1
	except: 
		a=open(FFF,'w')
		a.close()
		print("\n\tLog-file: \"{}\" was created in the following dir: \"{}\"\n\t".format(logFileName,file_directory))
		return 0
	return True

def manual(strCommandIn):
	#a = len(strCommandIn)
	a = strCommandIn.split()
	if(len(a)==1):
		print("\n* Type: man <command> *\n")
	
	return True

def boom():
	print("\n"*10)
	return True


#function for getting the current delta
#Otherwise you would need get a call to see the delta.
#Sometimes it is nice to know how long it has been since the last call...
def currentDelta():
	#a = current "call" If I were to get another call... a represents the time if I were to get a call at the point of calling the function. the previous call is already saved in time_current_call, and time_previous_call is more of a temp storage...
	a = time()
	# time of the current call is actually the time of the previous one ... it would actually make more since to put b above a..., but in this context it doesn't matter much. Just confusing if you are trying to follow it...
	b = time_current_call
	c = a - b
	#if b == 0 then there wasn't a previous call... (aka no calls at all)
	if(b==0):
		print("\n\t*** NO DELTA ***\t\n")
	else:
		local_time_string = str(timedelta(seconds=c))
		time_sub_string=local_time_string[:7]
		print("\n\t* Current Delta: {} (H:mm:ss) *\n".format(time_sub_string))
	
	return True



#logs the total calls
def logStats():
	file_directory = "./call_logs/"
	logFileName = "0callStats.txt"
	fullPath = file_directory+logFileName
	fileWriter = open(fullPath,'w')
	return 1

# Gets the running call total
def getStats():
	global cumulativeCallCount
	file_directory = "./call_logs/"
	logFileName = "0callStats.txt"
	fullPath = file_directory+logFileName
	fileReader = open(fullPath,'r')
	z=fileReader.readline()
	cumulativeCallCount = int(z)
	fileReader.close()
	#print(z)
	return 1




#write to file for logging 
#if file exists open?
def writeFile(arrIn, fileName):
	writeSuccessful = True 
	fileExtension=".txt"
	fileName=fileName+fileExtension
	#File path for work computer***************************************************************

	file_directory = "./call_logs/"
	#**************************************************************************************

	fullPath = file_directory+fileName
	fileWriter = open(fullPath,'w')
	#do something
	for call in arrIn:
		fileWriter.write(call+"\n")
		
	#close file
	fileWriter.close()
	if(writeSuccessful == False):
		print("\n\t{} Write Failed! COMPLETE SYSTEM FAILURE!".format(fileName))
	return writeSuccessful
#Defines a new call
#When called, it will create a new call
# Gets time
# Gets Date
# Gets a a time and date of the call to keep for reference. **
# I also clear callDate, and callTime for some reason.(?)
def newCall():
	#increase call count
	global callData
	global callCount
	global listOfCalls
	global time_current_call
	global time_previous_call
	global time_delta
	callCount+=1
	#sets the time for the first call (only to be used once the second call happens)
	if(callCount==1):
		time_current_call = time()
	
	#setting up the values for the delta
	#only enters if call count is more than 1 as with 0 calls it is a 0 delta 
	if(callCount>1):
		time_previous_call = time_current_call
		time_current_call = time()
		#compute time delta
		time_delta = time_current_call - time_previous_call
		
		
		
	
	
	#set up the call time
	callTime = strftime("%X")
	
	#set up the call date
	callDate = strftime("%x")
	
	#logging date and time of the call for printing purposes.
	lastCallDate = strftime("%x")
	lastCallTime = strftime("%X")
	local_time_string = str(timedelta(seconds=time_delta))
	time_sub_string=local_time_string[:7]
	#sets the string of the call. (LOCAL VAR)
	newCalltxt =(callText.format(callCount, callTime, callDate, time_sub_string))
	
	#adds the call to the list
	listOfCalls.append(newCalltxt)
	
	#sets the call and date back to "" not sure if needed, but it makes me feel better
	callDate = ""
	callTime = ""
	return True
	
	
	
#defines how to print to console for viewing pleasure!	
def printToConsole():
	#print('\n'*51)
	#print("*"*100)
	print("\n")
	for call in listOfCalls:
		print(call)
	print("\n")
	return True
	#Somebody do something
	
def removeCall(callNumber_2_remove):
	#callText = "\tCall#: {}\tCall Time: {}\tCall Date: {}\t Time Since Previous Call: {} (H:mm:ss)\t"
	global callData
	global listOfCalls
	global callCount
	#holds a list of call numbers. Ultimately not used, as I use an index to renumber anyway. Requires 2 splits. 
	callNumStrLst=[]
	#holds a list of call times split out of the original. requires 2 splits. 
	timeStrLst=[]
	#holds the list of dates split out from the original. Requires 2 splits.
	dateStrLst=[]
	#holds a list of deltas split out of the original. Requires 3 splits and a strip() to properly format....
	deltaStrLst=[]
	#this will house the updated list before making the old list = this one.
	tempListOfCalls=[]
	actualIndex = int(callNumber_2_remove) - 1
	if(callCount >= 1 and actualIndex >= 0 and actualIndex < callCount):
		del listOfCalls[actualIndex]
		callCount = callCount - 1
		#I'll do it this way for now until I can find a better way...
		for i in listOfCalls:
			#separates out the call to renumber 
			callNumStrLst.append(i.strip().split("\t")[0].split(": ")[1])
			#time string list
			timeStrLst.append(i.strip().split("\t")[1].split(": ")[1])
			#date time list
			dateStrLst.append(i.strip().split("\t")[2].split(": ")[1])
			#delta list
			deltaStrLst.append(i.strip().split("\t")[3].split(": ")[1].split("(H:")[0].strip())
		for i in range(0,len(callNumStrLst)):
			tempListOfCalls.append(callText.format(i+1,timeStrLst[i],dateStrLst[i],deltaStrLst[i]))
	#updates the list of calls without the removed call, now no need to manually renumber.
	listOfCalls = tempListOfCalls
	print("\n\tRemoved call {} successfully (before renumber)\n".format(callNumber_2_remove)) 
	return False
	#do something 


#main entry point to the script
def main():
	#do something
	fileName = input("\nEnter file name for logging: ")
	#print(len(fileName))
	genFiles()
	print("\n\n*******************************************************************************************")
	print("*************************** TYPE Y or YES to LOG A CALL ***********************************")
	print("*******************************************************************************************")
	print("***************************** TYPE HELP FOR COMMAND LIST **********************************")
	print("*******************************************************************************************\n\n")
	while True:
		str_val=input("Call Logger> ")
		str_lower = str_val.lower()
		#print(str_lower)
		if(str_lower=='y' or str_lower == 'yes' or str_lower == '(y)' or str_lower == '(y)es'): # or str_lower == ''
			newCall()
			printToConsole()
			writeFile(listOfCalls, fileName)
		if(str_lower=='write'):
			n_bool = writeFile(listOfCalls, fileName)
			if(n_bool):
				print("\n\tFile Written Successfully\n")
				
		if(str_lower=='exit' or str_lower=='quit'):
			if(c1 % 100 == 0):
				#Easter Egg  Exit :^)
				print("\n*** HAS A GOOD DAY :^) ***\n")
				sleep(5)
			else:
				#"Normal" Exit
				print("\n*** HAVE A GOOD DAY :) ***\n")
				sleep(2.5)
			break
		if(str_lower=='help' or str_lower=='list' or str_lower =='ls'):
			#print("\n***COMMANDS***\n1. Yes - yes, a log new call\n2. Exit - quits \n3. Quit - quits\n4. Write -writes to file\n5. Help - Help?\n6. Remove - remove call at index (not yet implemented)\n7. rm - remove call at index (not yet implemented)\n8. ls - help?")
			print(" ")
			for group in commandList:
				for item in group:
					print(item)
			print(" ")
		if(str_lower == 'print'):
			printToConsole()
		if(str_lower == 'cd' or str_lower == 'current delta'):
			currentDelta()
		if(str_lower == 'boom'):
			boom()
		if(str_lower[0:3] == 'man'):
			a=str_lower.split()
			if(a[0]=='man'):
				manual(str_lower)
		if(str_lower == "about"):
			pirntAbout()
		if(str_lower == 'top'):
			printTop()
		if(str_lower[0:2] == "rm"):
			a=str_lower.split()
			if(len(a)>1):
				removeCall(a[1])

			


if __name__ == "__main__":
	main()
	
	
	
#Notes for refactor 
# use split on the user input so I can have options right away input[0] = COMMAND input[1] = OPTION 
# for fun have a class that has all of the stored strings LOL
# make a CALL object for the calls.
# make a container for the CALLS
	#This will be for removing calls such that I can easily renumber the calls
	#This will also allow for "other modifications" more easily.




