import random
import string

string = ''.join(random.choices(string.ascii_lowercase, k=5))
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listed_str = list(string)
random.shuffle(listed_str + mylist)
x= (listed_str + mylist)
random.shuffle(x)

def remove_spaces(string):
    return string.replace(" ", "")
     
password = " ".join(str(x) for x in x)

print(remove_spaces(password))
