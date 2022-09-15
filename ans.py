#1. We have n=100 houses in a row. How much time will it take to reach the 56th
#house(write down answer in time complexity)?

ans:
I am assuming that 100 houses are in array and in sorted order.
so the time complexcity will be O(1) .
so to reach the 56th house the time complexcity will be constant.


2.#s=”Evol Group” reverse this string using list slicing.

s = "Evol Group"[::-1]
print(s)

#3.How to generate a random number between 5 to 15.
import random
print(random.randint(5,15))

#4.WAP to print pattern.
rows = int(input("Enter the number of rows:"))
for i in range(rows,0,-1):
    for j in range(0,i):
        print("*",end = " ")

    print("\n")    

#5. What will be The answer of print(True+5)?
The answer of print(True+5) will be 6.
Because True means 1 and False means 0.


#6. In django for what purpose models.py is used.
Models are used for storing and maniputalting the data.
It contains many essential fields and behaviors of the data .
Each models map to a single database table.
Each model is a python class that subclass of django.db.models


#7. Explain render() of django with parameters.
In django render() is used for combining  a template with a context dictionary  and returns a Httpresponse object.
render() function takes multiple parameters but it can take two mandotory parameters i.e request and template_name.
The other parameters are context,content_type,status and using.
Bydefault these parameters are None.

#8. Write django ORM to retrieve book name which have category of ‘textbook’

#Table fields: id, name, category
class Book(models.Model):
ans:
bookname = Books.objects.filter(name__icontains = bookname)


######
1. Create a To-Do app with Create, Read, Update, Delete Functionality using
Class Based Views(CBV).