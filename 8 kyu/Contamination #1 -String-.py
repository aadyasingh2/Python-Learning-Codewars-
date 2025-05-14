''' An AI has infected a text with a character!!

This text is now fully mutated to this character.

Starting with the original text, and given a character, return the text once it has been mutated so that all of the characters in the original text have been replaced with the character.

If the text or the character are empty, return an empty string.
There will never be a case when both are empty as nothing is going on!!

Note: The character is a string of length 1 or an empty string.

Example
text before = "abc"
character   = "z"
text after  = "zzz"    '''

def contamination(text, char):
    x=""
    for i in text:
        if i.isascii():
            x+=char
    return x
#Check it out: https://www.codewars.com/kata/reviews/596fba6c74dd684086000004/groups/682500a977297f119552a81b