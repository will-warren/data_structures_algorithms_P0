"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# A
# find unique calls from (080) numbers
# sort that list in lexiographic (numerical?) order

def string_test(text, test):
  return text.startswith(test)


def grab_code(phone_number):
  # if fixed line, use regex, else use substring for first 4 digits (no one is calling a telemarketer, sneaky trick though ;) )
  return re.search(re.compile('^\(?\d*\)?'), phone_number).group() if string_test(phone_number, '(') else phone_number[:4]

def make_code_list():
  code_list = []

  for record in calls:
    call_code = grab_code(record[1])

    if(call_code not in code_list):
      code_list.append(call_code)

  list.sort(code_list)
  return code_list

def print_answer(codes):
  print("The numbers called by people in Bangalore have codes:")
  for code in codes:
    print(code)

codes = make_code_list()
print("Part A\n")
print_answer(codes)


# B
# Find all calls by fixed lines
# Find calls of those calls which are to fixed lines
# calculate percentage

def find_all_fixed_line():
  return [(record[0], record[1]) for record in calls if string_test(record[0], '(080)')]

def find_all_calls_to_fixed_line(call_list):
  return [record for record in call_list if string_test(record[1], '(080)')]

def find_percentage():
  all_calls_from_fixed_line = find_all_fixed_line()
  all_calls_to_fixed_line = find_all_calls_to_fixed_line(all_calls_from_fixed_line)

  return float(len(all_calls_from_fixed_line) / len(all_calls_to_fixed_line))

print("\n\nPart B\n")
print(f"{find_percentage():.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")