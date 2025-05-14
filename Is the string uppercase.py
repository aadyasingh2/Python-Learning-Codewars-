''' Is the string uppercase?
Task
Create a method to see whether the string is ALL CAPS.

Examples (input -> output)
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True
In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase
letter so any string containing no letters at all is trivially considered to be in ALL CAPS.'''

def is_uppercase(inp):
    flag=True
    for i in inp:
        if i.islower():
            return False
    else:
        return flag

#Check it out:https://www.codewars.com/kata/reviews/57059fdddbf09446a800006b/groups/6825022654f5490bdbc30990