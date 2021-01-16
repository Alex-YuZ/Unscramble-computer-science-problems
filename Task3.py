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
# PART A.
def call_dict(data):
    """
    Generate a dictionay with sending call as the key and a list of receiving calls as values 
    
    Paramaters:
    -----------
    data: a two_dimensional list
    
    Returns:
    --------
    dict. Transform certain cols into a dictionary object.
    
    
    """
    result = dict()
    for item in calls:
        if not result.get(item[0]):
            result[item[0]] = []
            result[item[0]].append(item[1])
            
        else:
            result[item[0]].append(item[1])
            
    return result

def starts_with(prefix, data_dict):
    """
    Generate a list of receiving calls from a given prefix of sending calls.
    
    Paramaters:
    -----------
        prefix: str. A given prefix string to match with.
        data_dict: dict. A dictionaty containing sending call as the key and receiving call lists as values.
    
    Returns:
    --------
        list. Receiving call lists with a match.
    
    """
    result = []
    for key, val in data_dict.items():
        if key.startswith(prefix):
            result += val
        
    return result
            

data_dict = call_dict(calls)

uniq_vals = set(starts_with('(080)', data_dict))

res = set()
for i in uniq_vals:
    if i.startswith('('):
        ends_loc = i.find(')')
        res.add(i[: ends_loc+1])
    elif i.startswith(('7', '8', '9')):
        res.add(i[:4])
        
codes_fs = "The numbers called by people in Bangalore have codes: \n{}".format('\n'.join(sorted(list(res))))
print(codes_fs)


# PART B.

count = 0

for answer in starts_with('(080)', data_dict):
    if answer.startswith('(080)'):
        count += 1

total_calls = len(starts_with('(080)', data_dict))
count_pct = round(count/total_calls * 100, 2)

pct_fs = "{} percent of calls from fixed lines in Bangalore are calls to other \
fixed lines in Bangalore.".format(count_pct)

print(pct_fs)