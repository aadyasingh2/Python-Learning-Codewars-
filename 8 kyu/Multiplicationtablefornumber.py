'''Your goal is to return multiplication table for number that is always an integer from 1 to 10.

For example, a multiplication table (string) for number == 5 looks like below:

1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50
P. S. You can use \n in string to jump to the next line.

Note: newlines should be added between rows, but there should be no trailing newline at the end.
If you're unsure about the format, look at the sample tests.'''

def multi_table(number):
    table=""
    for i in range(1,10):
        table+=str(i)+" * "+str(number)+" = "+str(i*number)+"\n"
    table+=str(10)+" * "+str(number)+" = "+str(10*number)
    return table

#Check it out: https://www.codewars.com/kata/reviews/5a3131b016f1018d3c0015c8/groups/5fd22abba2948e0001d27232