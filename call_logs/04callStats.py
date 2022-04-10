import operator
in_file = ["complete_log.txt",'r']
file_info = open(in_file[0],in_file[1])

split_str = ""
new_info =[]
new_info_date = []
for info in file_info:
    #print(info)
    split_str = info.split('\t')
    new_info.append(split_str[0])
    new_info_date.append(split_str[2])
    
int_count = 0
shift_count = 0
call_count = 0
call_shift_count = 0
call_list = []
for info2 in new_info:
    str_int = info2.split(' ')
    if(str_int[1] == '1'):
        #print(str_int)
        shift_count+=1
        call_count+=1
        call_shift_count +=1
    else:
        call_count+=1
        call_shift_count +=1
    call_list.append(int(str_int[1]))

print("\n\nNumber of Shifts (with calls): {}\n\n".format(shift_count))
print("\n\nComputing Call Total, Averages, Median, and Mode\n\n")
print("TOTAL CALLS: {}".format(call_count))
print("\nAverage Calls per shift: {0:.3f}\n\n".format(call_count/max(shift_count,1)))
#print("\n\nComputing Call Median\n\n")
#print("{}".format(call_list))
#print([index for index, value in enumerate(call_list) if value == 1])
counts = 0
list_of_totals_for_median = []
lenList = len(call_list)
list_of_dates = []
for i in range(lenList):
    if(call_list[i]==1):
        counts+=1
    else:
        counts+=1
    if(i+1<lenList and call_list[i+1]==1 or i+1>=lenList):
        list_of_totals_for_median.append(counts)
        list_of_dates.append(new_info_date[i])
        counts = 0
        #print(list_of_totals_for_median)
#print(list_of_totals_for_median)
sortedList = list_of_totals_for_median[:] #need to do this so that it makes it by value, and so that the sort below does not sort this list to match dates to calls counts.
if(len(sortedList)==0):
	sortedList.append(0)
sortedList.sort()
#print(list_of_totals_for_median)
#doing math to figure out mode
#make a list of lists [[1,2,3],[1],[1,2,3,4,5]]
#compute the counts of each value
#find the most common one. 
#MEDIAN START HERE-----------------------------------------------------------------------------------------------------------------------------
mode_val = sortedList[0]
count_k = 0

for i in sortedList:
    aa = sortedList.count(i)
    if(aa > count_k):
        count_k = aa
        mode_val = i

#end figuring out mode
#print(sortedList)
#END MEDIAN -------------------------------------------------------------------------------------------------------------------------------------
median_val=0
if(len(sortedList)>0):
    if(len(sortedList)&1==0):
        nt=0
        index1 = int(len(sortedList)/2)
        index2 = index1 - 1
        val1 = sortedList[index1]
        val2 = sortedList[index2]
        median_val = (val1 + val2) / 2
        median_val = int(median_val)
        
    else:
        nt=1
        index_of_median = int((len(sortedList)-1)/2)
        median_val=sortedList[index_of_median]
else:
    print("LIST IS ZERO SIZE")
print("Median calls per shift = {}\n\n".format(median_val))
print("Mode: {} Calls (shift)    (count: {} nights)\n\n".format(mode_val,count_k))
print("Most Calls on 1 shift = {} \n\n".format(sortedList[len(sortedList)-1]))
        
#print(len(sortedList))

print("OTHER STATS\n\n")
final_val = sortedList[len(sortedList)-1]
#loop to final val getting the counts up until then


#print(new_info_date)
#print(final_val+1)
#print(sortedList)
#print(call_list)
#print(list_of_dates)
loc = list_of_totals_for_median[:]
lod = list_of_dates[:]
loc_lod = zip(lod,loc)
loc_lod = list(loc_lod)
loc_lod2 = sorted(loc_lod,key = operator.itemgetter(1))
#print(loc_lod2[6][1])

#print("z"*69)
#for m,date in zip(lod,loc):
    #print("{} - {}".format(m,date))
    


for i in range(1,final_val+1):
    if(sortedList.count(i)!=0):
        print("    {}    nights with    {}    CALLS      {}".format(sortedList.count(i),i, loc_lod2[len(sortedList) - sortedList[::-1].index(i)-1][0]))
        print()
        print("-"*70)
    #print(sortedList.count(i))

input = input("\n\nHIT ENTER TO END! ")
