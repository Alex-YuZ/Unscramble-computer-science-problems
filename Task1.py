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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def col_list(idx, data):
    """
    Extract a certain column of the input 2D lists and store it in a list.
    
    Paramaters:
    ----------
    idx: int. A given column index
    data: list. The dataset of 2D lists
    
    Returns:
    --------
    list
    
    """
    val_list = [item[idx] for item in data]
    return val_list
    

# get the unique values in sending numbers column in the texts
send_texts_uniq = set(col_list(0, texts))

# get the unique values in receiving numbers column in the texts
receive_texts_uniq = set(col_list(1, texts))

# get the unique values in calling numbers column in the calls
send_calls_uniq = set(col_list(0, calls))
# get the unique values in receiving numbers column in the calls
receive_calls_uniq = set(col_list(1, calls))

# get the unique values in all four columns above
uniq_nums = send_texts_uniq | receive_texts_uniq | send_calls_uniq | receive_calls_uniq
# calculate the length of these unique values
uniq_length = len(uniq_nums)

# formatted string
uniq_fs = "There are {} different telephone numbers in the records.".format(uniq_length)

print(uniq_fs)