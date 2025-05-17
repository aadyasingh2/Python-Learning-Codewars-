'''In this kata you are required to, given a string, 
replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3'''

def alphabet_position(text):
    x=[]
    for i in text:
        if i.isalpha():
            if i.isupper():
                x.append(str(ord(i)-64))
            else:
                x.append(str(ord(i)-96))
    y=" ".join(x)
    return y
                

# Check it out on:  https://www.codewars.com/kata/reviews/546f92300e7b08fe6100001c/groups/6827018835e546d94156587e