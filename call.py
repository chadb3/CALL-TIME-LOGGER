import os
from time import *
from datetime import timedelta, datetime, date
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

callText = "\tCall#: {}\tCall Time: {}\tCall Date: {}\t Time Since Previous Call: {} (H:mm:ss)\t"

callDate = ""

callTime = ""

lastCallDate = ""

lastCallTime = ""

time_current_call =0

time_previous_call = 0

time_delta = 0 

username = ""

eccCalled = False

# Generate files if they don't already exists
# the log file 
def genFiles():
	logFileName = "0callHistory.txt"
	file_directory = "./call_logs/"	
	FFF = file_directory + logFileName
	try:
		a=open(FFF,'r')
		a.close()
		print("\nLog File: \"{}\" Exists\n\t".format(logFileName))
		return 1
	except: 
		a=open(FFF,'w')
		a.close()
		print("\n\tLog-file: \"{}\" was created in the following dir: \"{}\"\n\t".format(logFileName,file_directory))
		return 0
	return True

def manual(strCommandIn):
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
def logStats(txtIn):
	file_directory = "./call_logs/"
	logFileName = "0callHistory.txt"
	fullPath = file_directory+logFileName
	fileWriter = open(fullPath,'a')
	fileWriter.write(txtIn+"\n")
	fileWriter.close()
	return 1

#write to file for logging 
def writeFile(arrIn, fileName):
	writeSuccessful = True 
	#File path for work computer***************************************************************

	file_directory = "./call_logs/"
	#**************************************************************************************

	fullPath = file_directory+fileName
	fileWriter = open(fullPath,'w')
	#does something
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
	global callCount
	global listOfCalls
	global time_current_call
	global time_previous_call
	global time_delta
	global eccCalled
	callCount+=1
	#sets the time for the first call (only to be used once the second call happens)
	if(callCount==1):
		time_current_call = time()
		
	#setting up the values for the delta
	#only enters if call count is more than 1 as with 0 calls it is a 0 delta 
	elif(callCount>1 and eccCalled == False):
		time_previous_call = time_current_call
		time_current_call = time()
		#compute time delta
		time_delta = time_current_call - time_previous_call
	else:
		time_current_call = time()
		time_delta = time_current_call - time_previous_call
		
		
#need debug strings in above i am still getting odd behavior when testing "calls" where i did not get a chance to epc it. the epc doesn't match the cd (current  delta).		
#Above is incorrect. This appears to work fine. The bug is in currentDelta  	
	
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
	eccCalled = False
	return True
		
#defines how to print to console for viewing pleasure!	
def printToConsole():
	print("\n")
	for call in listOfCalls:
		print(call)
	print("\n")
	return True
	
def removeCall(callNumber_2_remove):
	#callText = "\tCall#: {}\tCall Time: {}\tCall Date: {}\t Time Since Previous Call: {} (H:mm:ss)\t"
	global listOfCalls
	global callCount
	#local bool to determin if value changed or not
	localBool = False
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
	global time_current_call
	global time_previous_call
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
		localBool = True
	if(localBool):
		#updates the list of calls without the removed call, now no need to manually renumber.
		listOfCalls = tempListOfCalls
		print("\n\tRemoved call {} successfully (before renumber)\n".format(callNumber_2_remove))
		localBool = False
		time_current_call = time()
		time_previous_call = time()
	else:
		print("\n\tCall {} NOT FOUND\n".format(callNumber_2_remove)) 
	return False
	#do something 

# Function to end the "current call"
# this causes the time from last call to be more accurate
# Even though I don't use it for anything. 
def ecc():
	global time_current_call
	global time_previous_call
	global eccCalled
	if(callCount >=1 and eccCalled == False):
		print("\n*** Ended Call ***")
		time_previous_call=time()
		print("Call Duration: {}\n".format(str(timedelta(seconds=time_previous_call-time_current_call))[:7]))
		time_current_call = time()
		eccCalled = True
	else:
		print("no call to end...")

def openFile(fileName):
	global listOfCalls
	global callCount
	global time_current_call
	global time_previous_call
	filepath = "./call_logs/"
	print("\nattempting to read from: {}".format(fileName))
	print("\nSTARTING FILE READING\n")
	file_openFile = open(filepath+fileName,"r")
	txt = file_openFile.read()
	lines=txt.split("\n")
	item = []
	for line in lines:
		if(line!=''):
			print(line)
			listOfCalls.append(line)
			item.append(line.strip().split("\t"))
			callCount+=1
	time_current_call = time()
	time_previous_call = time()
	
def fileCreator():
	fileSize = 0
	fileName = input("\nHit \"ENTER\" for DEFAULT File Name: ")
	logStats("[ "+str(datetime.now())+" ]  "+"fileCreator: FILENAME INPUT = \"{}\" ".format(fileName))	
	fileExtension=".txt"
	lenFileName = len(fileName)
	if(lenFileName>0):
		if(lenFileName<4 or fileName[lenFileName-4:lenFileName]!=".txt"):
			fileName=fileName+fileExtension
			logStats("[ "+str(datetime.now())+" ]  "+"fileCreator: CUSTOM FILENAME: \".txt\" ADDED! ")
		else:
			fileName=fileName
			logStats("[ "+str(datetime.now())+" ]  "+"fileCreator CUSTOM FILENAME: \".txt\" DETECTED (NOT ADDED)! ")
		logStats("[ "+str(datetime.now())+" ]  "+"fileCreator: CUSTOM FILENAME: "+fileName)	
	if(len(fileName)==0):
		date_for_file = date.today()
		fileName = "calls_{}"+fileExtension
		fileName=fileName.format(date_for_file.strftime("%m%d%Y"))
		logStats("[ "+str(datetime.now())+" ]  "+"fileCreator: DEFAULT FILENAME chosen (empty string): "+fileName)	
	try:
		print("\n***********************************\nTrying to open: {}\n***********************************\n".format(fileName))
		logStats("[ "+str(datetime.now())+" ]  "+"fileCreator: TRYING TO DETERMINE IF \"{}\" ALREADY EXISTS!".format(fileName))
		open("./call_logs/"+fileName,"r")
		print("{} Detected already. Please choose next action\n".format(fileName))
		fileSize = os.path.getsize("./call_logs/"+fileName)
		if(fileSize>0):
			print("File size indicates *** DATA IS PRESENT! ***\nSize: {} BYTES\n".format(fileSize))
			logStats("[ "+str(datetime.now())+" ]  "+"fileCreator: \"{}\" DETECTED: {} BYTES!".format(fileName,fileSize))	
		else:
			print("File size indicates *** NO DATA! ***\n")
			logStats("[ "+str(datetime.now())+" ]  "+"fileCreator: {} DETECTED, BUT NO DATA PRESENT!"+fileName)	
		print("CHOOSE AN OPTION:")
		print("1. Open\n2. Overwrite")
		ans = input("input decision: ")
		logStats("[ "+str(datetime.now())+" ]  "+"fileCreator: \"OPEN or OVERWRITE\" INPUT = \"{}\" ".format(ans))	
		ans = ans.strip().lower()
		if(ans == "1" or ans =="1." or ans=="open" or ans=="1.open" or ans =="1. open"):
			#print("READING FROM FILE!")
			openFile(fileName)
			logStats("[ "+str(datetime.now())+" ]  "+"fileCreator: OPEN FILE CHOSEN!")	
		elif(ans=="2" or ans =="2." or ans == "overwrite" or ans =="2.overwrite" or ans =="2. overwrite"):
			logStats("[ "+str(datetime.now())+" ]  "+"filecreator: OVERWRITE FILE CHOSEN!")	
			print("\nOVERWRITING FILE - I HOPE THERE WASN\'T ANYTHING IMPORTANT!!!\n")
			writeFile(listOfCalls, fileName)
			print("FILE OVERWRITTEN!")
		else:
			logStats("[ "+str(datetime.now())+" ]  "+"fileCreator: REDO! (BAD USER INPUT!)")	
			print("\nDO YOU KNOW WHAT YOU ARE DOING???? REDO!\n")
			fileCreator()
	except:
		logStats("[ "+str(datetime.now())+" ]  "+"fileCreator: CREATING FILE \"{}\"! (AKA FILE NOT FOUND!)".format(fileName))	
		writeFile(listOfCalls, fileName)
		printStr = "\nFile: \"{}\" Created!\n".format(fileName)
		print(printStr)
	return fileName

#main entry point to the script
def main():
	#do something
	fileName = fileCreator() 
	genFiles()
	print("\n\n*******************************************************************************************")
	print("*************************** TYPE Y or YES to LOG A CALL ***********************************")
	print("*******************************************************************************************")
	print("***************************** TYPE HELP FOR COMMAND LIST **********************************")
	print("*******************************************************************************************\n\n")
	logStats("[ "+str(datetime.now())+" ]  "+"SESSION START - "+fileName)
	call_str_1 = "Call Logger> "
	call_str_2 = "Call {}> "
	call_str_current = call_str_1
	while True:	
		str_val=input(call_str_current)
		str_lower = str_val.lower()
		#print(str_lower)
		if(str_lower=='y' or str_lower == 'yes' or str_lower == '(y)' or str_lower == '(y)es'): # or str_lower == ''
			logStats("[ "+str(datetime.now())+" ]  "+"Command: "+str_val)
			newCall()
			call_str_current = call_str_2.format(callCount)
			printToConsole()
			writeFile(listOfCalls, fileName)
		elif(str_lower=='write'):
			logStats("[ "+str(datetime.now())+" ]  "+"Command: "+str_val)
			n_bool = writeFile(listOfCalls, fileName)
			if(n_bool):
				print("\n\tFile Written Successfully\n")
				
		elif(str_lower=='exit' or str_lower=='quit'):
			logStats("[ "+str(datetime.now())+" ]  "+"Command: "+str_val)
			if(c1 % 100 == 0):
				# Easter Egg  Exit :^)
				print("\n*** HAS A GOOD DAY :^) ***\n")
				logStats("[ "+str(datetime.now())+" ]  "+"SESSION END - "+"Easter Egg Exit :^)")
				sleep(5)
			else:
				# "Normal" Exit
				print("\n*** HAVE A GOOD DAY :) ***\n")
				logStats("[ "+str(datetime.now())+" ]  "+"SESSION END - "+"Normal Exit :)")
				sleep(2.5)
			break
		elif(str_lower=='help' or str_lower=='list' or str_lower =='ls'):
			#print("\n***COMMANDS***\n1. Yes - yes, a log new call\n2. Exit - quits \n3. Quit - quits\n4. Write -writes to file\n5. Help - Help?\n6. Remove - remove call at index (not yet implemented)\n7. rm - remove call at index (not yet implemented)\n8. ls - help?")
			print(" ")
			for group in commandList:
				for item in group:
					print(item)
			print(" ")
		elif(str_lower == 'print'):
			logStats("[ "+str(datetime.now())+" ]  "+"Command: "+str_val)
			printToConsole()
		elif(str_lower == 'cd' or str_lower == 'current delta'):
			logStats("[ "+str(datetime.now())+" ]  "+"Command: "+str_val)
			currentDelta()
		elif(str_lower == 'boom'):
			logStats("[ "+str(datetime.now())+" ]  "+"Command: "+str_val)
			boom()
		elif(str_lower[0:3] == 'man'):
			a=str_lower.split()
			logStats("[ "+str(datetime.now())+" ]  "+"Command: "+str_val)
			if(a[0]=='man'):
				manual(str_lower)
		elif(str_lower == "about"):
			logStats("[ "+str(datetime.now())+" ]  "+"Command: "+str_val)
			pirntAbout()
		elif(str_lower == 'top'):
			logStats("[ "+str(datetime.now())+" ]  "+"Command: "+str_val)
			printTop()
		elif(str_lower[0:2] == "rm"):
			a=str_lower.split()
			logStats("[ "+str(datetime.now())+" ]  "+"Command: "+str_val)
			if(len(a)>1):
				removeCall(a[1])
				if(call_str_current!=call_str_1):
					if(callCount-1!=-1):
						call_str_current = call_str_2.format(callCount)
					else:
						call_str_current = call_str_1
		elif(str_lower[0:3] == "ecc" or str_lower[0:3] == "epc"):
			ecc()
			call_str_current = call_str_1
			logStats("[ "+str(datetime.now())+" ]  "+"Command: "+str_val)	
		else:
			clean_str_val = " ".join(str_val.split())
			if(len(clean_str_val)>0):
				logStats("[ "+str(datetime.now())+" ]  "+call_str_current+clean_str_val)

if __name__ == "__main__":
	main()
