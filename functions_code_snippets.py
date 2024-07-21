#code snippets for understanding the concepts
#you can copy and run each exmaples separately to understand(play with inputs)
#functions

#functions
#example:
#A simple function without any parameters
def my_function():
    print("Hello from a function")

#calling a function
my_function()

#example:
#A simple function without any parameters
def greet():
    print("Hello")
    print("How are you?")

greet()#calling a function

#example:
#function with a parameter 'name'
def greet(name):
    print("Hello",name)
    print("How are you?")

greet("Ronaldo")#calling a function

#example:
#function with two parameters 'a' and 'b'
def add_two_num(a,b):
    result = a + b
    print("Sum =",result)

add_two_num(2,4)#calling a function with arguments 2 and 4

#example:
#function with a return statement
def add_two_num(a,b):
    result = a + b
    return result

two_sum = add_two_num(2,4)
print("Result =",two_sum)

#example:
#function with a optional/deafult parameter b = 4
def add_two_num(a,b = 4):
    result = a + b
    return result

two_sum = add_two_num(2)#not passing argument 'b' so it will take b = 4
#note that you can change the value of 'b' by sending the argumnet of your choice as shown below
two_sum = add_two_num(2,10) #now b = 10

