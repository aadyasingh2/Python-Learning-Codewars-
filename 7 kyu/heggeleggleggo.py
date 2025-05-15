'''Insert an egg after each consonant. 
If there are no consonants, there will be no eggs. 
Argument will consist of a string with only alphabetic characters and possibly some spaces.'''

import re
def heggeleggleggo(word):
    pattern=r"[^aeiouAEIOU ]"
    new=""
    for x in word:
        res=re.search(pattern,x)
        if res==None:
            new+=x
        else:
            new=new+x+"egg"
    return new
        
# Check it out: https://www.codewars.com/kata/reviews/5ff4ec199536210001f69015/groups/68263ad954f5490bdbc329f1