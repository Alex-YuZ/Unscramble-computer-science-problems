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
def get_uniq(data):
    """
    Combine the sending and receiving numbers of the data and store the unique ones in a set object.
    
    Parameters:
    -----------
        data: a 2D list containing the records of texts and calls information.
        
    Returns:
    --------
        set: unique numbers
    
    """
    res = set()
    for itm in data:
        res.update(set([itm[0], itm[1]]))
        
    return res

texts_uniq = get_uniq(texts)
calls_uniq = get_uniq(calls)
uniq_both = texts_uniq | calls_uniq

# formatted string
uniq_fs = "There are {} different telephone numbers in the records.".format(len(uniq_both))

print(uniq_fs)