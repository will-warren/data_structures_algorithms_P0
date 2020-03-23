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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def find_first_text():
    return texts[0]

def find_last_call():
    return calls[len(calls)-1]


first_text_data = find_first_text()
last_call_data = find_last_call()

print("First record of texts, {} texts {} at time {}".format(first_text_data[0], first_text_data[1], first_text_data[2]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last_call_data[0], last_call_data[1], last_call_data[2], last_call_data[3]))

