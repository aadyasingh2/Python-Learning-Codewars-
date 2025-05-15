'''Take an array and remove every second element from the array. 
Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!'''

def remove_every_other(my_list):
    z=[]
    for i in range(len(my_list)):
        if i %2==0:
            z.append(my_list[i])
    return z
        

# Check it out on: https://www.codewars.com/kata/reviews/5769b390cdd98d7959000ab9/groups/5c1d43bd5117316e510001fe