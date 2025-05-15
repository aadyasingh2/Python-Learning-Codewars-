'''Implement String#digit? (in Java StringUtils.isDigit(String)), 
which should return true if given object is a single digit (0-9), false otherwise.'''

import re
def is_digit(n):
    #your code here
    pattern=r"[0-9]"
    text=str(n)
    res=re.fullmatch(pattern,text)
    if res==None:
        return False
    else:
        return True
    

#Check it out on: https://www.codewars.com/kata/reviews/569c0ab2269589c328000047/groups/6825f7a9819b01800f4def5f