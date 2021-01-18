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
def col_set(data, *idx):
    """
    Convert a list with a given column index into a set pbject.
    
    Parameters:
    ----------
    idx: int. 
    data: list. The dataset of 2D lists
    
    Returns:
    --------
    a set
    
    """
    i, j = idx
    return set([item[i] for item in data]), set([item[j] for item in data])
    

# get the unique numbers from given column index from calls dataset
send_calls_uniq, receive_calls_uniq = col_set(calls, 0, 1)

# get the unique numbers from given column index from texts dataset
send_texts_uniq, receive_texts_uniq = col_set(texts, 0, 1)

# find the potential telemarketers numbers
telemarketers = send_calls_uniq - receive_calls_uniq - send_texts_uniq - receive_texts_uniq

# format the print-out string
telemarketers_fs = "These numbers could be telemarketers: \n{}".format('\n'.join(sorted(list(telemarketers))))

print(telemarketers_fs)