import re
def to_cents(amount):
    pattern=r"\A\$[0-9]+\.[0-9{2}]"
    result=re.fullmatch(pattern,amount)
    if result==None:
        return "None"
    else:
        return int(amount[1::])*100
print(to_cents("$0.69"))