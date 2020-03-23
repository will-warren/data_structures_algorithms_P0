"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from Task1 import collect_uniq_phone_nums

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

UNIQ_NUMS = collect_uniq_phone_nums()

def total_time_for_num():
    nums_and_times = []
    
    for phone in UNIQ_NUMS:
        total_time = 0
        for record in calls:            
            if(phone in record):
                total_time += int(record[3])
        
        nums_and_times.append((phone, total_time))

    total_time = 0
    return nums_and_times

# find max
def find_max_time_on_phone():
    times_for_all_nums = total_time_for_num()
    max_talker = ("", 0)
    for line in times_for_all_nums:
        if(line[1] > max_talker[1]):
            max_talker = line

    return max_talker

max_talker = find_max_time_on_phone()
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_talker[0], max_talker[1]))