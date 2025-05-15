'''Your boss decided to save money by purchasing some cut-rate 
optical character recognition software for scanning in the text
of old novels to your database. At first it seems to capture words
okay, but you quickly notice that it throws in a lot of numbers at
random places in the text.

Examples (input -> output)
'! !'                 -> '! !'
'123456789'           -> ''
'This looks5 grea8t!' -> 'This looks great!'
Your harried co-workers are looking to you for a solution to take 
this garbled text and remove all of the numbers. Your program will 
take in a string and clean out all numeric characters, and return a 
string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.'''

def string_clean(s):
    """
    Function will return the cleaned string
    """
    x=""
    for i in s:
        if i.isnumeric()==False:
            x+=i
    return x

# Check it out on: https://www.codewars.com/kata/reviews/57e1e62bd8d1c76a24000083/groups/6825eb38857b6aaef5154a0b