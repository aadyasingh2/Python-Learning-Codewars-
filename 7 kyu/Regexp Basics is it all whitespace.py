'''Implement String#whitespace?(str) (Ruby), String.prototype.whitespace(str)
(JavaScript), String::whitespace(str) (CoffeeScript), or whitespace(str) (Python),
which should return true/True if given object consists exclusively of zero or more 
whitespace characters, false/False otherwise.

'''

import re
def whitespace(string):
    pattern=r"\A\s*\Z"
    matching=re.fullmatch(pattern,string)
    if matching==None:
        return False
    return True

#Check it out on: https://www.codewars.com/kata/reviews/56805d49949a4ad6f900001b/groups/68260190857b6aaef5154d05