'''Basic regex tasks. Write a function that takes in a numeric code 
of any length. The function should check if the code begins with 1, 2, 
or 3 and return true if so. Return false otherwise.

You can assume the input will always be a number.'''

import re 
def validate_code(code):
    pattern = r"\A[123]"
    text = str(code)
    result=re.match(pattern,text)
    if result==None:
        return False
    else:
        return True

# Check it out on: https://www.codewars.com/kata/reviews/56a29076db22b376ea000007/groups/6825f440bd673b95cccd0350