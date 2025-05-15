'''You're on your way to the market when you hear beautiful music coming from a nearby street 
performer. The notes come together like you wouln't believe as the musician puts together 
patterns of tunes. As you wonder what kind of algorithm you could use to shift octaves by 8 
pitches or something silly like that, it dawns on you that you have been watching the musician 
for some 10 odd minutes. You ask, "how much do people normally tip for something like this?" The 
artist looks up. "It's always gonna be about tree fiddy."

It was then that you realize the musician was a 400 foot tall beast from the paleolithic era! The 
Loch Ness Monster almost tricked you!

There are only 2 guaranteed ways to tell if you are speaking to The Loch Ness Monster: A) it is a 
400 foot tall beast from the paleolithic era; B) it will ask you for tree fiddy.

Since Nessie is a master of disguise, the only way accurately tell is to look for the phrase "tree 
fiddy". Since you are tired of being grifted by this monster, the time has come to code a solution 
for finding The Loch Ness Monster. Note that the phrase can also be written as "3.50" or 
"three fifty". Your function should return true if you're talking with The Loch Ness Moster, false 
otherwise.'''

import re
def is_loch_ness_monster(string):
    pattern= r"tree fiddy|three fifty|3\.50"
    result=re.search(pattern,string)
    if result==None:
        return False
    return True

#Check it out on: https://www.codewars.com/kata/reviews/5c3e9a5ea4a1490001076a03/groups/6825f943857b6aaef5154bee