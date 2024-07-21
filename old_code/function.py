#why fucntions

# Functions can make a program smaller by eliminating repetitive code. 
# Later, if you make a change, you only have to make it in one place.

#Function parameters are the names listed in the function's definition. 
#Function arguments are the real values passed to the function.

#Syntax:
def my_function():
    print("Hello from a function") 


#Calling a Function:
def my_function():
    print("Hello from a function")

#my_function()

#return
#send the function's result back to the caller

#Addition
def add_two_numbers(a,b=5):
    return a+b

answer = add_two_numbers(1,10)
print("Answer =",answer)