'''In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.'''

def high_and_low(numbers):
    x=[int(i) for i in (numbers.split(" "))]
    final=sorted(x,reverse=True)
    print(final)
    del final[1:len(final)-1]
    if len(final)==1:
        final.append(final[0])
    return " ".join(map(str,final))

# Check it out on: https://www.codewars.com/kata/reviews/5557d51de2da64b93200001b/groups/68270c2f06d1549b787d5874
