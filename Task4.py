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

# set of outgoing calls
# set of text numbers, and callees
def find_all_telemarketers():
    possible_telemarketers = set()
    not_telemarketers = set()

    for record in calls:
        possible_telemarketers.add(record[0])
        not_telemarketers.add(record[1])

    for record in texts:
        not_telemarketers.add(record[0])
        not_telemarketers.add(record[1])

    return sorted(possible_telemarketers - not_telemarketers)

print("These numbers could be telemarketers: ")
print("\n".join(find_all_telemarketers()))