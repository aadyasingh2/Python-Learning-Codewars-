'''Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

case	return
name equals owner	" Hello boss"
otherwise	"Hello guest"               '''


def greet(name, owner):
    # Add code here
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"
    
#Check it out on: https://www.codewars.com/kata/reviews/58058ba934d14b2f15000006/groups/61decbedf176470001d684e4