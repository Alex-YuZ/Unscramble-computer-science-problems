"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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

# Extract the calling, receiving number and their corresponding duration time from calls dataset \
# and transform into a list
call_lists = list(zip(col_list(0, calls), map(int, col_list(3, calls)))) \
            + list(zip(col_list(1, calls), map(int, col_list(3, calls))))

# initialize a new dict object to store the number and duration time.
call_dict = {}
for i, j in call_lists:
    call_dict[i] = call_dict.get(i, 0) + j
        
# find the maximun value of duration in the keys of call_dict.
max_key = max(call_dict, key=lambda x: call_dict[x])
max_duration = max(call_dict.values())

# format the print-out string        
max_duration_sf = "{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(max_key,max_duration)

print(max_duration_sf)
