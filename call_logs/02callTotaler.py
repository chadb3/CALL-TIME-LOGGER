
file_in = ["complete_log.txt",'r']
file_out = ["z_comp_log_w_numbering_total.txt", 'w+']
call_str = ""
call_list = []
count = 1

unNumberedInfo = open(file_in[0],file_in[1])

for unCountedCall in unNumberedInfo:
	call_str = "Call: {} == {}".format(count,unCountedCall)
	call_list.append(call_str)
	count+=1

unNumberedInfo.close()
count = 0
numberedInfo = open(file_out[0],file_out[1])
Total_Number_Of_Calls = len(call_list)
call_str = "TOTAL NUMBER OF CALLS: {}\n\n".format(Total_Number_Of_Calls)
numberedInfo.write(call_str)
for item in call_list:
	print(item)
	numberedInfo.write(item)
	
numberedInfo.close()
input = input("\n\nHIT ENTER TO END! ")
