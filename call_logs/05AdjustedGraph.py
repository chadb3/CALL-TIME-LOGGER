from math import *
from datetime import *
in_file1 = ["complete_log.txt",'r']
in_file2 = ["complete_log2.txt",'r']

#get call with numbering. 
#get call date.
#get call time
#get time of first call.
#if first call is after 12:00 (am) then the call should be for the previous day.
#otherwise it should get the call for the first day, and then count to the next "shift" (or call 1)
file_info = open(in_file1[0],in_file1[1])
call_info = open(in_file2[0],in_file2[1])
day = [0,0,0,0,0,0,0]
day_str = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
month = [0,0,0,0,0,0,0,0,0,0,0,0]
month_str =["January","February","March","April","May","June","July","August","September","October","November","December"]
split_string = ""
string_a = ""
split_call_info = []
#['Call#: 1', 'Call Time: 18:00:15', 'Call Date: 07/08/19', ' Time Since Previous Call: 0:00:00 (H:mm:ss)\n']
#['Call#: 2', 'Call Time: 18:45:22', 'Call Date: 07/08/19', ' Time Since Previous Call: 0:45:07 (H:mm:ss)\n']
#['Call#: 3', 'Call Time: 18:48:54', 'Call Date: 07/08/19', ' Time Since Previous Call: 0:03:31 (H:mm:ss)\n']
#['Call#: 4', 'Call Time: 18:53:32', 'Call Date: 07/08/19', ' Time Since Previous Call: 0:04:38 (H:mm:ss)\n']
#['Call#: 5', 'Call Time: 22:27:09', 'Call Date: 07/08/19', ' Time Since Previous Call: 3:33:36 (H:mm:ss)\n']
#['Call#: 6', 'Call Time: 05:42:45', 'Call Date: 07/09/19', ' Time Since Previous Call: 7:15:35 (H:mm:ss)\n']
# split_call_info[0][0] = 'Call#: 1 (of the very first call)
# split_call_info[0][2] = 'Call Date: 01/02/19' (of the very first call)
for str_info in file_info:
    split_string = str_info.split('\t')
    split_call_info.append(split_string)
   
#print(split_call_info[0][2])

call_number_str = ""
call_time_str = ""
call_date_str = ""
just_date_string = ""
just_time_hour_string = ""
just_call_number = ""
just_month_number_int = 0;
day_of_week = 0
kount = 1
for line in split_call_info:
    call_number_str = line[0].split(' ' )
    #should just get the number 1,2,3
    just_call_number = call_number_str[1]
    call_time_str = line[1].split(' ')
    #this should pull the hour 18-06   
    just_time_hour_string = call_time_str[2][0]+call_time_str[2][1]
    call_date_str = line[2].split(' ')
    #gets the date 07/08/19
    just_date_string = call_date_str[2]
    just_month_number_int = int(just_date_string[0] + just_date_string[1])
    just_month_number_int-=1;
    month[just_month_number_int]+=1;    
    if(int(just_call_number)==1):
        #if call is between 00 - 6
        if(int(just_time_hour_string)<=6):
            date_obj = datetime.strptime(just_date_string,'%m/%d/%y')
            day_of_week = date_obj.weekday()
            day_of_week-=1
            if(day_of_week<0):
                day_of_week = 6
            day[day_of_week]+=1
            #if(day_of_week==1):
                #print("{}: first call on (Wed) Tuesday: {}".format(kount,call_time_str[2]))
                #kount+=1
                #print(line)
            #print(day_of_week)                
            #print(date_obj)
            #reduce day here
        else:
            date_obj = datetime.strptime(just_date_string,'%m/%d/%y')
            day_of_week = date_obj.weekday()
            day[day_of_week]+=1
            #if(day_of_week==1):
                #print("{}: Normal Tuesday first call: {}".format(kount,call_time_str[2]))
                #kount+=1
                #print(line)
            #print(day_of_week)
    else:
        day[day_of_week]+=1;
        #if(day_of_week==1):
            #print("{}: Additional Tuesday: {}".format(kount,call_time_str[2]))
            #kount+=1
                #print(line)
        #print(just_call_number)
    #print(just_date_string)
    #print(time_hour_string)   
    #print(call_number_str[1])
    #print(call_time_str[2])
    #print(call_date_str[2])

print("\n\n********** Calls for shift (adjusted for shift, and not day) **********\n")
for i,j in zip(day_str,day):
    print("{}: {}".format(i,j))
print("\n")
print("*"*111)
print("\n\n********** Number Of Calls Per Month *********\n")
for i,j in zip(month,month_str):
    print("{}: {}".format(j,i))


input = input("\n\n\nHIT ENTER TO END! ")