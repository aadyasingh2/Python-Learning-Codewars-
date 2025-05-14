''' Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john" '''

def name_shuffler(str_):
    array=str_.split(" ")
    temp=array[0]
    array[0]=array[1]
    array[1]=temp
    return " ".join(array)

#Check it out:  https://www.codewars.com/kata/reviews/559d176593c2ebe903000097/groups/6824ff4854f5490bdbc30936