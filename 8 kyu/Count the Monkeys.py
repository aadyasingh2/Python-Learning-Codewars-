'''You take your son to the forest to see the monkeys. 
You know that there are a certain number there (n), 
but your son is too young to just appreciate the full number, 
he has to start counting them from 1.

As a good parent, you will sit and count with him. 
Given the number (n), populate an array with all numbers up to and 
including that number, but excluding zero.'''

def monkey_count(n):
    x=[]
    for i in range(1,n+1):
        x.append(i)
    return x

#Check it out on: https://www.codewars.com/kata/reviews/56f82bc43f8e9c3e2100001e/groups/6201766553dac20001294296