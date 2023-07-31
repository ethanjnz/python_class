num1 = 42 #variable decleration int
num2 = 2.3 #variable decleration float
boolean = True #variable decleration boolean
string = 'Hello World' #variable decleration string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable decleration, lists
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable decleration, dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable decleration, tuple
print(type(fruit)) #log statement
print(pizza_toppings[1])  #log statement, access value
pizza_toppings.append('Mushrooms') #add value to pizza_topping
print(person['name']) #log statement, access dictionary value
person['name'] = 'George' #change value of dictionary
person['eye_color'] = 'blue' #change value of dictionary
print(fruit[2]) #log statement, access value of tuple

if num1 > 45:  # if statement
    print("It's greater") #log statement
else: #else statement
    print("It's lower") #log statement

if len(string) < 5: #if statement, length check
    print("It's a short word!") #log statement
elif len(string) > 15: #else if statement, length check
    print("It's a long word!") # log statement
else: #else statement
    print("Just right!") #log statement

for x in range(5): #loop, 0 to 4
    print(x) #log x 
for x in range(2,5): #loop, 2 to 4
    print(x) #log x
for x in range(2,10,3): # loop, expected output: 2,5,8
    print(x) #log x
x = 0 #variable decleration
while(x < 5): #while loop, must be less than 5
    print(x) #log x
    x += 1 # increment x by 1

pizza_toppings.pop() #delete a value at end of list
pizza_toppings.pop(1) #delete the value at the [1] index ->sausage

print(person) #log statement, print dictionary
person.pop('eye_color') #remove eye color key from person dictionary
print(person) #log statement

for topping in pizza_toppings: #for loop iterating through list 
    if topping == 'Pepperoni': #if statement indicating if index == perpperoni
        continue #skip the index
    print('After 1st if statement') #log statement every loop
    if topping == 'Olives': #if index == "olives" 
        break #stop the for loop

def print_hello_ten_times(): # function called print_hello_ten_times
    for num in range(10): # for loop iterating 0 -9
        print('Hello') #print hello each loop

print_hello_ten_times() #function call

def print_hello_x_times(x): #declare a function called print_hello_x_times, parameter of x
    for num in range(x): # for loop that collects the argument 
        print('Hello') #log hello 4 times

print_hello_x_times(4) # calls the function and passes the argument of 4 

def print_hello_x_or_ten_times(x = 10): # delcare a function called print_hello_x_or_ten_times and has a parameter
    for num in range(x): # for loop that runs 
        print('Hello', x) # log hello 10 times then print hello 4 times

print_hello_x_or_ten_times() # call the function and pass in the argument of null
print_hello_x_or_ten_times(4) # call the function and pass in the argument of 4


"""
Bonus section
"""

# print(num3) # nameError: name <num3> is not defined
# num3 = 72 # variable declared
# fruit[0] = 'cranberry' # "tuple" object does not support item assignment
# print(person['favorite_team'])  # key error: favorite_team
# print(pizza_toppings[7]) #index out of range
#   print(boolean)  # unexpected indentation
# fruit.append('raspberry') # cannot append a tuple
# fruit.pop(1) # cannot pop a tuple