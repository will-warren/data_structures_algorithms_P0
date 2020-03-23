"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# We know that telemarketers phone numbers start with 140.
# List all numbers that start with code 140

def find_all_telemarketers():
    all_telemarketers = []
    for record in calls:
        if(record[0].startswith('140') and ' ' not in record[0] and record[0] not in all_telemarketers):
            all_telemarketers.append(record[0])

    for record in texts:
        if(record[0].startswith('140') and ' ' not in record[0] and record[0] not in all_telemarketers):
            all_telemarketers.append(record[0])

    return all_telemarketers

def print_all_telemarketers(telemarketers):
    for tm in telemarketers:
        print(tm)
    

print("These numbers could be telemarketers: ")
print_all_telemarketers(find_all_telemarketers())