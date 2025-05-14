# Write function to RemoveExclamationMarks which removes all exclamation marks from a given string.
def remove_exclamation_marks(s):
    #your code here
    x=""
    for i in s:
        if i=="!":
            continue
        else:
            x+=i
    return x
        
#Check it out on:https://www.codewars.com/kata/reviews/57fa28a64f0caf8b4b000044/groups/6824f126136ef193d0384fe5