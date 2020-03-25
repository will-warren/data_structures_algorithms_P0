"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def total_times_by_num():
    call_times_by_number = {}

    for record in calls:            
        call_duration = int(record[3])
        caller = record[0]
        callee = record[1]
        call_times_by_number[caller] = call_times_by_number.get(caller, 0) + call_duration
        call_times_by_number[callee] = call_times_by_number.get(callee, 0) + call_duration
    
    return call_times_by_number

# find max
def find_max_time_on_phone():
    times_for_all_nums = total_times_by_num()
    max_talker = ("", 0)
    for item in times_for_all_nums.items():
        if(item[1] > max_talker[1]):
            max_talker = item

    return max_talker

max_talker = find_max_time_on_phone()
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*max_talker))