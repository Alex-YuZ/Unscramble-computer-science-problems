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
def col_set(idx, data):
    val_list = [item[idx] for item in data]
    return set(val_list)

send_calls_uniq = col_set(0, calls)
receive_calls_uniq = col_set(1, calls)
send_texts_uniq = col_set(0, texts)
receive_texts_uniq = col_set(1, texts)

telemarketers = send_calls_uniq - receive_calls_uniq - send_texts_uniq - receive_texts_uniq

telemarketers_fs = "These numbers could be telemarketers: \n{}".format('\n'.join(sorted(list(telemarketers))))
print(telemarketers_fs)