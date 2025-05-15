'''Implement String#to_cents, which should parse prices expressed as $1.23 
and return number of cents, or in case of bad format return nil.

In this kata, for a price to be considered valid, it must start with a dollar 
sign ($), followed immediately by a decimal number with exactly 2 decimal digits.'''

import re
def to_cents(amount):
    pattern=r"^\$[0-9]+\.[0-9]{2}"
    result=re.fullmatch(pattern,amount)
    if result==None:
        return None
    else:
        x=result.group().strip("$")
        y=x.replace(".","")
        return int(y)
# Check it out on: https://www.codewars.com/kata/reviews/56852d421de798dd30000087/groups/6825ffbd54f5490bdbc3231e