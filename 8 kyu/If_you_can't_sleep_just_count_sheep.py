'''If you can't sleep, just count sheeps!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers. '''


def count_sheep(n):
    # your code
    string=""
    count=1
    for count in range(1,n+1):
        string=string+str(count)+" sheep..."
    return string
        
# Check it out: https://www.codewars.com/kata/reviews/5b3fcb04fec6700205000299/groups/6824c051ede5f0b7288a1189