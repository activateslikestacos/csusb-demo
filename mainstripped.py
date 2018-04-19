'''
Author: Christopher Cox
Email: chris15588@gmail.com
Description: This program's purpose is to help demonstrate some basic principles
    of Python coding, and to serve as a reference guide for later programs.
'''

# --- Variable Definition ---

# Variable definition example
variableName = 200;

# --- Using Print Function ---

# using the print function with a string literal
print("This is being printed using a string literal!")

# --- Using print function with variables ---

# Now I will store the string in a variable, then 'pass' it to the print function
myMessage = "This is a message stored in a variable!";
print(myMessage)

# --- User Input & print function arguments ---

# Notice how I put a string literal inside the input function. Whatever you put in there will be
# printed out for the user to see. Think of it as a prompt.
userInput = input("Please enter something: ")

# At this point, there is the user's input stored in the userInput variable, so let's print it out
# using some fancier methods with the print function
print("You typed:", userInput)

# --- Lists & Indexing ---

# List syntax example
someNumbers = [10, 20, 4, 12]

# Printing the first element in the list
print(someNumbers[0])

# Priting the last element in the list
print(someNumbers[3])

# Changing the second element, then printing it
someNumbers[1] = 15
print(someNumbers[1])

# --- Booleans ---

# Boolean literal example
pythonIsFun = True

# They can be printed, too:
# Test your knowledge a little bit by adding your own string literals to this message
# without adding another print function (hint: look to like 80)
print(pythonIsFun)

# Remember that whatever is on the right side of the equals side runs first!
myExpression = 10 > 5

print(myExpression)

# Just like math, whatever is in paranthesis is calculated first
# the ** operator is the power operator, so I am taking 4 to the power of 2 (16)
myExpression = (10 / 2) + 3 == (4 ** 2) / 2

print(myExpression)

# Now some examples of the boolean operators
# I am using literals here to help visualize what is happening here
myExpression = True and True or False   # What do you think this one will come out to?

print(myExpression)

# --- Basic Looping ---

# Which is better?
print("I used CTRL + V here")
print("I used CTRL + V here")
print("I used CTRL + V here")
print("I used CTRL + V here")
print("I used CTRL + V here")

# Or:
sentinalValue = 1

while (sentinalValue <= 5):
    print("I used a while loop here")
    sentinalValue += 1

# --- Control Structures ---

# Get user input
uInput = input("Please enter a number between 1 and 10: ")

# 'Convert' the string input into a number
# keep in mind that this will error out if the user enters something
# that isn't a number. Preventing that is not difficult, but is outside
# the scope of this lecture
uInput = int(uInput)

# Check to see if the user inputted a number inbetween 1 and 10 (1, 10)
# By using the not operator I was able to specify a boolean expression
# where if the input was correct, the expression would evaluate to true,
# so the not operator inverses that
if (not (uInput > 1 and uInput < 10)):
    print("You didn't enter a number between 1 and 10!")
else:
    # If we get into this block of code, the number has checked out
    # Now check if the inputted number matches our special number
    
    # I'll just put it in a variable for easy readability
    specialNumber = 3
    
    # This is an example of a nested if statement. It is simply an if statement
    # inside another if statement. The difficulty of nested if statements would
    # be keeping proper indentation. If you are having trouble wrapping your head
    # around this, try breaking the program down into seperate parts. I will
    # explain this more in the lecture if we have time.
    if (specialNumber == uInput):
        print("You guessed the correct number!")
    else:
        print("Sorry! You guessed incorrectly. The number was:", specialNumber)