'''Complete the code which should return true if the given object is a single 
ASCII letter (lower or upper case), false otherwise.'''

import re
def is_letter(s):
    pattern=r"[a-zA-Z]{1}"
    res=re.fullmatch(pattern,s)
    if res==None:
        return False
    return True
    
#Check it out on: https://www.codewars.com/kata/reviews/5dfb8f3bbb266200016ee35b/groups/68260457857b6aaef5154d6e