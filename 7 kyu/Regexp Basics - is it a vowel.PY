'''Implement the function which should return true if given object is a vowel 
(meaning a, e, i, o, u, uppercase or lowercase), and false otherwise.'''

import re
def is_vowel(s): 
    pattern=r"[aeiouAEIOU]{1}"
    res=re.fullmatch(pattern,s)
    if res==None:
        return False
    return True

#Check it out on: https://www.codewars.com/kata/reviews/5e318aaafd283d0001e16b8e/groups/6826033a857b6aaef5154d45