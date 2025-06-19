#String

#message = """Hellow's World"""


#print(message)

#Advanced concept - strings

#message = ' Felicia, Sithole '


#print(message.strip()) #Remove leading and trailing whitespace
#print(message.lower()) #Convert all characters to lowercase
#print(message.split(',')) #Split the string into a list based on the coma
#print(message.upper()) #Convert all characters to uppercase
#print(message.replace("e" , "a")) #replaces a specified phrase with another specified phrase




#Numeric Data - integer (class int) are whole numbers and floats (class float) are decimal numbers
#num = 3

#print(type(num))

#num2 = 3.14444

#print(type(num2))




#Variable - is a symboling name or identifier used to store data or values in a computor
#my_variable = 10
#total_count = 0
#user = "John"

#Invalid
#second_variable = 10
#user-name = 20



#Operators on numeric data
#Addition (+)
#Subtraction (-)
#Multiplication (*)
#Division (/)
#Modulus (%) - is a remainder after you divide
#Exponent (**)

#x = 10
#y = 2

#print(x+y)
#print(x-y)
#print(x*y)
#print(x/y)
#print(x%y)
#print(5%2)
#print(x**y)

#x = 10
#x -= 2

#print(x)





#Operators with Strings
#str1 = 'Felicia'
#str2 = 'Sithole'

# print(str1 + ' ' + str2 + ' ' + str1)
# print(str1 * 8)




# Control Statement - are fundamental components of programming language that allow us to control the flow of execution based on certain conditions 
# if, else if and else statemet

# num = 0

# if num > 0:
    # print("This number is positive")
# elif num == 0:
    # print("This number is zero")
# else:
    # print("This number is negative")
    
    
    
    
    
#Control Statements
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))

# if num1 > num2: 
    # print(num1, "is greater than", num2)
# elif num2 > num1:
    # print(num2, "is greater than", num1)
# else:
    # print("Both numbers are equal")
    
    
    



#Loops (for loop and while loop)
# fruits = ['apples', 'banana', 'cherry']

# for fruit in fruits:
    # print(fruit)
    
# numbers = ['1', '2', '3', '4', '7']
# for number in numbers:
    # print(number)
    
#Using a while loop to count from 1 to 5    
# count = 1

# while count <= 5:
    # print(count)
    # count += 1 #Increments the count by 1
    
    
    
    
#Loop Control Statements
# fruits = ['apple', 'banana', 'cherry', 'date']

# for fruit in fruits:
    # if fruit == "cherry":
        # break # Exits the loop if cherry is found
    # print(fruit)
    
# print()

# for fruit in fruits:
    # if fruit == "cherry":
        # continue # Skips the value in this condition is cherry and move to the iteraction which is date
    # print(fruit)
    
# print()

# for fruit in fruits:
    # if fruit == "cherry":
        # pass # Placeholder, no action is needed for cherry (in case you are changing the data or doing some transformation on the data we have or values we say that when it reach cherry do not do anything to it just leave it as it is)
    # print(fruit)
    
    
count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break # Exist the loop when the count is released - 3