'''Complete the function that receives as input a string, and produces outputs according to the following table:

Input	Output
"Jabroni"	"Patron Tequila"
"School Counselor"	"Anything with Alcohol"
"Programmer"	"Hipster Craft Beer"
"Bike Gang Member"	"Moonshine"
"Politician"	"Your tax dollars"
"Rapper"	"Cristal"
anything else	"Beer"   '''


def get_drink_by_profession(param):
    
    match (param.title()):
        case "Jabroni":
            return "Patron Tequila"
        case "School Counselor":
            return "Anything with Alcohol"
        case "Programmer":
            return "Hipster Craft Beer"
        case "Bike Gang Member":
            return "Moonshine"
        case "Politician":
            return "Your tax dollars"
        case "Rapper":
            return "Cristal"
        case _:
            return "Beer"
        
#Check it out: https://www.codewars.com/kata/reviews/5e72114a76b67f0001b0388a/groups/62bdc27c9087ab0001e814fc
        