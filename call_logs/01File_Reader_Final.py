#************************** IMPORTS ***********************************************
from glob import glob
import os
#************************** IMPORTS ***********************************************
#This reads in a a list of call files 
#and logs them to two files
#complete_log: full call log. may add a second logic to count out the calls and make it more readable...
#complete_log2: simplified output for potential graphing
commands = ['\nstart', 'help','clear','print','\n']
list_of_times_calls = []
file_contents = []
list_of_files = ''
bool_File_Read = False
write_to_file_full_data = "complete_log.txt"
write_to_file2_partial_data = "complete_log2.txt"

def getReadFiles():
	global bool_File_Read
	global list_of_files
	global list_of_times_calls
	global file_contents
	
	list_of_times_calls = [] # resets the values here so that they don't get read in again (even after the move)
	file_contents = [] # resets the values here so that they don't get read in again (even after the move)
	
	list_of_files = glob('calls_????????.txt')
	if(len(list_of_files)==0):
		return 0
	bool_File_Read = True
	return 1

def readFiles():
	
	
	split_call = ""
	
	for file in list_of_files:
		open_file = open(file,'r')
		with open_file as past_calls:
			for pastCall in past_calls:
				file_contents.append(pastCall.strip()) # ***** For Appending to the full call list that would be appended to the end of the full log "Call#: 2	Call Time: 20:18:04	Call Date: 06/02/19	 Time Since Previous Call: 1:15:04 (H:mm:ss)"
				split_call=pastCall.strip().split("\t")
				list_of_times_calls.append("{}\t{}".format(split_call[2],split_call[1])) # For Appending to a different list to potentially graph just date of call and time of call
		open_file.close()	
	
	return 2

def writeFiles():
	file_of_Logs = open(write_to_file_full_data,"a+")
	file_of_call_and_times = open(write_to_file2_partial_data,'a+')
	
	for itm in file_contents:
		file_of_Logs.write(itm+"\n")
	
	for itm2 in list_of_times_calls:
		file_of_call_and_times.write(itm2+'\n')
	
	file_of_Logs.close()
	file_of_call_and_times.close()
	return 3
	
def moveFile():
	path = "loggedCalls/"
	for file in list_of_files:
		os.rename(file,path+file)
	return 4

#Remove last file from list as it is likely still open for the call logger. 
#new goal: add flag to ignore it, and run it anyway. 
def excludeLastFile():
	global list_of_files
	if(bool_File_Read==False):
		print("*** READ FILES IN FIRST ***")
		print(" **** TYPE: READ ****")
		return -1
	if(len(list_of_files)<2):
		print(" *** HOLD OFF ON OPERATION ***")
		print(" ***** OR RUN \"START 2 \" *****")
		return -2
	else:
		length = len(list_of_files)
		print("Removed: {}".format(list_of_files[length-1]))
		list_of_files.remove(list_of_files[length-1])
		print()
		
	return 0
	
def main():
	print("Hello, Welcome to my program!\nType \"START\" to read in all of the logs, and it will add them to the complete logs\nType\"HELP\" to get a list of commands\n\n"+"*"*80+"\n")
	while(True):
		User_Input_Raw = input("%--> ")
		User_Input = User_Input_Raw.lower().split()
		if(User_Input[0] == 'exit' or User_Input[0] == 'quit'):
			break
		if(User_Input[0] == 'exclude' or User_Input[0] == 'remove'):			
			excludeLastFile()
		if(User_Input[0] == 'start' and len(User_Input)==1):
			one = getReadFiles()
			two = excludeLastFile()
			if(two==0):
				three = readFiles()
				four = writeFiles()
				five = moveFile()
		if(User_Input[0] == 'start' and len(User_Input)>1):
			if(User_Input[1] == '2'):
				one = getReadFiles()
				if(one  == 1):
					readFiles()
					writeFiles()
					moveFile()
				else:
					print("\n\n *** NO FILES TO OPERATE ON! *** \n\n")
		if(User_Input[0] == 'print'):
			print(file_contents)
			print(list_of_times_calls)
		if(User_Input[0] == 'clear'):
			print("\n"*300)
		if(User_Input[0] == 'help'):
			for command in commands:
				print(command)

		
	return True
	
if __name__ == "__main__":
    main()
