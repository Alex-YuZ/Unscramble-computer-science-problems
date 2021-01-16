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
    val_list = [item[idx] for item in data]
    return val_list

# Extract the calling, receiving number and their corresponding duration time from calls dataset \
# and transform into a list
call_lists = list(zip(col_list(0, calls), map(int, col_list(3, calls)))) \
            + list(zip(col_list(1, calls), map(int, col_list(3, calls))))

call_dict = {}
for i, j in call_lists:
    if not call_dict.get(i):
        call_dict[i] = j
    else:
        call_dict[i] += j
        
# print(call_dict)

max_key = None
max_duration = 0

for key, val in call_dict.items():
    if val > max_duration:
        max_duration = val
        max_key = key
        
max_duration_sf = "{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(max_key, \
                                                                                                        max_duration)
print(max_duration_sf)
