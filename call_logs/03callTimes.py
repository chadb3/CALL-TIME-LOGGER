from math import *
from datetime import *
in_file = ["complete_log2.txt",'r']
day = [0,0,0,0,0,0,0]
day_str = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
shift_hours = [0,0,0,0,0,0,0,0,0,0,0,0,0]
shift_hours_string = ['18:00','19:00','20:00','21:00','22:00','23:00','00:00','01:00','02:00','03:00','04:00','05:00','06:00']
call_info = open(in_file[0],in_file[1])

call_STR = ""
call_dates = []
call_times = []
just_call_times = []
just_call_dates = []
for i in call_info:
	#print("\\0")
	call_STR = i.split('\t')
	#new_i = call_STR.split('\t')
	call_dates.append(call_STR[0])
	call_times.append(call_STR[1])
#print(call_STR.split('\t'))	
for i,j in zip(call_dates,call_times):
	#print(i)
	i2 = i.split()
	just_call_dates.append(i2[2])
	#print(j)
	j2 = j.split()
	just_call_times.append(j2[2])

#print(call_date_time_list[0]) #isn't this just that call_info is maybe I can manipulate it there...

#for i,j in zip(just_call_dates, just_call_times):
	#print(i)
	#print(j)
    
 #try to find a way to change 06/01/2019 to Saturday 
 #https://stackoverflow.com/questions/22739015/convert-date-from-mm-dd-yyyy-to-another-format-in-python
 
for i in just_call_dates:
   date_obj = datetime.strptime(i,'%m/%d/%y')
   day_of_week = date_obj.weekday()
   day[day_of_week]+=1

total_01=0
print("\n\nCALL TOTALS per DAY OF WEEK:")
for i,j in zip(day_str,day):
    print("{}: {}".format(i,j))
    total_01+=j
print("Total: {}".format(total_01))

print("\n\n")

COUNT2=0
#Now to compute calls by hour. (6pm, 7pm, 8pm, 9pm, 10pm, 11pm, 12am, 1am, 2am, 3am, 4am, 5am, 6am)
for i in just_call_times:
    hour_list = i.split(':')
    hour_str=hour_list[0]
    if(hour_str=='18'or hour_str =='17'):
        shift_hours[0]+=1
        COUNT2+=1
    elif(hour_str=='19'):
        shift_hours[1]+=1
        COUNT2+=1
    elif(hour_str =='20'):
        shift_hours[2]+=1
        COUNT2+=1
    elif(hour_str=='21'):
        shift_hours[3]+=1
        COUNT2+=1
    elif(hour_str=='22'):
        shift_hours[4]+=1
        COUNT2+=1
    elif(hour_str=='23'):
        shift_hours[5]+=1
        COUNT2+=1
    elif(hour_str=='00'):
        shift_hours[6]+=1
        COUNT2+=1
    elif(hour_str=='01'):
        shift_hours[7]+=1
        COUNT2+=1
    elif(hour_str=='02'):
        shift_hours[8]+=1
        COUNT2+=1
    elif(hour_str=='03'):
        shift_hours[9]+=1
        COUNT2+=1
    elif(hour_str=='04'):
        shift_hours[10]+=1
        COUNT2+=1
    elif(hour_str=='05'):
        shift_hours[11]+=1
        COUNT2+=1
    elif(hour_str=='06'):
        shift_hours[12]+=1
        COUNT2+=1
        
print("CALLS PER \"HOUR\" (XX:00 -> XX:59):")
for i,j in zip(shift_hours,shift_hours_string):
    print("{}\t{}".format(j, i))
print("Total: {}".format(COUNT2))    
print("\n\n")

inputs = input("HIT ENTER TO END! ")