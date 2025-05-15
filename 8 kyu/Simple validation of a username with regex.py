'''Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore
Length should be between 4 and 16 characters (both included).

'''

import re
def validate_usr(username):
    text=username
    pattern = r"[a-z0-9_]{4,16}"
    result=re.fullmatch(pattern,text)
    if result==None:
        return False
    else:
        return True
    
# Check it out on:  https://www.codewars.com/kata/reviews/56a6420f333e5367f3000024/groups/6825f58451a1fbf76660a149