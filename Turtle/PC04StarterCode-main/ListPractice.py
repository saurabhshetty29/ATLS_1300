# ['We', 'are', 'learning', 'about', 'lists', 'today!']
"""                               STOP! READ!                 """
# Complete the bulleted tasks in this script and submit to gradescope when completee.

"""A list is a kind of DATA STRUCTURE. 
Basically, this means that it organizes a bunch of things into a single thing.

1. Define a list called `aList` by typing a bunch of strings inside square 
brackets [], and placing a comma after each string:"""
# write code here


"""2. Now, create a list called `rainbow` by typing the strings color names 
of the rainbow (in order) inside square brackets, just like above."""
# write code here


"""3. If you already know where something is in a list, you can access it! 
For example, this code will print the 2nd color of the rainbow:"""
print(rainbow[1]) # list indices start at 0!


"""4. Try accessing and printing the color "violet":"""
# write code here

"""As you might have noticed, `0` accesses the 1st element, `1` accesses 
the 2nd element, etc. (You'll get used to this one day.)

There is another way you can access the last value in a list. 
Can you search "Getting the last element of a python list"?

5. Using an Internet search, can you find how to access the value `violet` with the new way?"""
# write code here


"""You can use functions within the list type variable, such as `reversed`, to 
the values reverse a list. Check out
https://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python.

6. Reverse your rainbow, and put it in a variable called `rainbow_backwards`:"""
# write code here

"""7. From your reversed rainbow, can you access the value `violet` again?"""
# write code here

"""Now `for` some fun!

For loops use lists and ranges to repeat tasks. The simplest form is shown below, 
where the for loop repeats, or ITERATES, the print function for the same number 
of times as there are elements in `aList`"""

for item in aList:
    print("hi")
    
    
"""9. Run the following turtle graphics code to see how loops are used to 
iterate through values in a list:"""

import turtle

turtle.colormode(255)
win = turtle.Screen()
w = 400
h = 400
win.setup(width=w, height=h) 


for color in rainbow_backwards:
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()
    
turtle.done()

"""The for loop sequentially passes the values in the list or range into the iterator variable, `item`. Change the for loop below so that it prints each value stored to the variable `item`.

10. In just 2 lines of code, print the color names of the rainbow:"""
# write code here

