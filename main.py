'''
Author: Christopher Cox
Email: chris15588@gmail.com
Description: This program's purpose is to help demonstrate some basic principles
    of Python coding, and to serve as a reference guide for later programs.
'''

# -- Defining Variables --
'''
What are variables? If you've ever taken a math class, you probably already have
an idea of what they are. Basically, a varaible is something in programming that
can be used to store many different types of data, so it can be used later.

There are many different ways to use variables, and almost every modern program
uses them. Some coding languages have something called "strict typing" which
means you have to specify what 'type' of data you are putting into the variable.
These types include: integers, strings, doubles, floats, bytes... etc. Sounds
complicated, right? Well you're in luck! Python is a very flexible language
that allows you to define variables without specifying a type.

Since python doesn't have strict typing, all that is required to define a variable
and the data in it is a variable name and the data you want to put it in.
The syntax is as follows:
'''

variableName = 200;

'''
Above you can see that I created a variable called 'variableName' and assigned it the
value of 200. 'variableName' is a bad example for how variables should be named, because
the name doesn't really explain what the variable is holding.

Programs can grow very large in size and be filled with hundreds, or even thousands of
variables. To help make it easier on you and any other programmers who are working
with your code, you should give your variables meaningful names. Now, you don't have
to go into insane detail and write a novel for each variable name, but instead try
to condense while still conveying the information. If you don't feel like you can do
that, then use notes like I am doing now. Notes are ignored by the Python interpreter,
so you can write notes in your program all day, and it will not change the functionality
of your program one bit.

Lets practice with variables a bit, and use the built-in Python function to print a message
to the screen.
'''

# using the print function with a string literal
print("This is being printed using a string literal!")

# Now I will store the string in a variable, then 'pass' it to the print function
myMessage = "This is a message stored in a variable!";
print(myMessage)

'''
So variables are great and all, but they don't seem very useful if all you can do with them
is type in the numbers in the code (quick note: when you see any value being given to a variable
such as 200 or "some text", those are called 'literals'), so how about we get some user input?
Python made this task very easy with a function called input (functions will be covered later).

Functions basically allow you to run 'blocks' of code by a name. Functions are a lot more capable
than what I just mentioned, but for the sake of this lecture we will just use them in their simplest
form.

So below this, I am going to define a variable called userInput, and use the input function to
assign a value to that variable once the user submits it.

!Very Important! => When you are defining a variable, everything on the right side of the = sign
(called the assignment operator) executes first. so if you do 'result = 5 + 3', the result variable
will be holding 8, not 5 + 3. The same goes with functions, so if I called the input() function
in a variable, the program will wait for user input, THEN store it in the variable.

Here is an example of just that:
'''

# Notice how I put a string literal inside the input function. Whatever you put in there will be
# printed out for the user to see. Think of it as a prompt.
userInput = input("Please enter something: ")

# At this point, there is the user's input stored in the userInput function, so let's print it out
# using some fancier methods with the print function
print("You typed:", userInput)

'''
Now, this might look complicated at first, but all I did was add another "argument" to the print
function. An argument is basically extra data passed to a function so it can complete its task.
The print function requires at least one argument (which is the text to be printed), but what
if a function requires more than one argument? Well, I demonstrated it right above this comment
block. All you do is use a comma! The print function is designed to be dynamic in the way that
it takes arguments, so it can take an infinite amount of arguments. The print function automatically
adds spaces between arguments too. This can be helpful in the situation we are in, because we want
to combine a string literal with a variable containing a string. Try to practice it more on your own!

You can have as many print and input functions as you would like.

Alright, now to get into something a bit more intense. Arrays, or as Python call them: "lists".
Lists can be viewed as a 'list' of data held under one variable. Lists are useful for many things
like: holding student grades, friend's names, a list of food you like etc. The syntax takes a little
getting used to, but with practice they will come easy to you. Below I will define a basic list
holding a few different numbers.
'''

someNumbers = [10, 20, 4, 12]

'''
As you can see, I used square brackets on either side, and seperated each piece of data using a comma.
So now you might be asking: "How can we access this data?" or "Are we able to change this data like other
variables?".

To answer the first question: we can access each individual portion of the list using something called an
index. On a basic list, each item in the list has an index that uses integers. So what index would you use
access the first element in the list? If you guessed 1, then you're close, but it's actually 0! Many
coding languages follow this practice, so it's something you will get used to. This also means that even
though this list has 4 elements in it, to access the last element you must use the index of 3.

Let's practice a bit with indexes and their syntax.
'''

# Printing the first element in the list
print(someNumbers[0])

# Priting the last element in the list
print(someNumbers[3])

# Changing the second element, then printing it
someNumbers[1] = 15
print(someNumbers[1])

'''
Lists have much more functionality than this, so if you're interested check out:
https://docs.python.org/3/tutorial/datastructures.html

So now this gets us into our next, and probably most advance topic: looping

Looping can be intimidating for some because it requires a sort of special thinking,
but with practice anyone can get the hang of it

Before I get into loops, I have to explain something called a boolean. Whenever you
hear or see that word, you should immediately think true or false (or 1 or 0 if you're
into digital logic!). Booleans are a data type used in every language I can think of
and are used in looping and decision structures (which will be covered next).
Boolean literals are specified in Python by typing True or False (and they are case
sensitive)

To define a boolean in a variable, the syntax is the same as above:
'''

pythonIsFun = True

# They can be printed, too:
# Test your knowledge a little bit by adding your own string literals to this message
# without adding another print function (hint: look to like 80)
print(pythonIsFun)

'''
This is not the only way to define booleans, however. They are more commonly produced
through something called a "boolean expression" which is basically a set of logic that
the computer interprets and spits out a true of false for evaluation. These expressions
can be very sort, or unpleasantly long. I am going to type a few boolean expressions below
and print their results. I am also going to express a practice where you can reassign variables
too. (Not that big of a deal, but it might be clarifying for some)

Here is a basic list of boolean operators that can be used in bolean expressions
Comparison Operators:
<          - Less than
>          - Greater than
<=         - Less than or equal to
>=         - Greater than or equal to
==         - Is equal
!=         - Isn't equal

And here are the operators that allow us to chain boolean operators together
Boolean operators:
x or y     - If either x or y is true, then the statement returns true
x and y    - Both x and y must be true for this statement to return true
not x      - If x is true, then the statement returns false (and vice versa)
'''

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

'''
To break down what I just typed above, think of it in sections and try to read it like
the computer would. So, starting from the left side, the first statement is:
'True and True'. If you look up to my explanation of the and operator, you can see
that in order for and to return true, both arguments must be true. Since both
of our arguments are true, we can substitute True in the place of "True and True".
So, our new statement looks like: 'True or False'. When looking at the explanation
of the or operator, if any of its arguments are true, then it returns true, so the
statement 'True or False' will return true, and that is our answer! Let's print it out
and confirm it
'''

print(myExpression)

'''
Now, when I mentioned substitution, that is just my way of 'solving' boolean expressions
without the help of a computer. As aforementioned, these expressions can get horribly long,
so that method helps me from having computation errors. Also keep in mind that they usually
won't say True of False! ;)

Onto what you have all been waiting for.. Looping! The reason I brought up boolean expressions
so abruptly is because we use them to control how our loops behave. Starting with one of the simplest
loops, the while loop:

while (boolean - expression):
    loop body

So, lets say I wanted to print out a message five times? I could do it this way:
'''

print("I used CTRL + V here")
print("I used CTRL + V here")
print("I used CTRL + V here")
print("I used CTRL + V here")
print("I used CTRL + V here")

'''
Or, I could be cool and use a while loop.
'''

sentinalValue = 1

while (sentinalValue <= 5):
    print("I used a while loop here")
    sentinalValue += 1

'''
So I feel I must explain what I just did. You probably recognized the while loop sytax right off the bat,
but what about the variable and the new += operator? Let me explain:
A sentinal is one way to control how your loop.. Loops. Its job is to be updated at a certain point in
the loop, and the boolean expression that controls the loop should coincide with it.

I used a sentinal value by incrementing it by one each time the loop executes and checking to see if the
value of less than or equal to 5. If I increase or decrease that number, then the loop will count will
change. Now, don't think that this is the way you should do every loop. Python gives the programmer
a generous amount of freedom in the way that they write their boolean expressions, so have fun with it!

As for the += operator, that is basically another way of writing:
sentinalValue = sentinalValue + 1

Sorry to bring it up again, but remember how everything on the right side of the equals sign runs first?
Well, it doesn't change here. Whatever value is stored in sentinalValue is having 1 added to it, then
stored back in sentinalValue. Weird, right? It is something you will see frequently.

Lastly, this is an important note that will apply to loops, and the next item I'm about to show you:
identing. Look back up to the while loop, drag your mouse over the empty space infront of print() 
and sentinalValue statements. It's spaces, not tabs! This is more important than it looks, and it 
is one of the major things (syntax wise) that sets Python apart from languages like C or Java.
Instead of using brackets to specify the size of the loop body, you must indent each line consistenly.
(I choose four spaces, and many common text editors like brackets or vim can convert tabs to 4 spaces).
Now, if you're thinking you can skip this step, I have some bad news for you. The Python interpreter
will not be able to execute your program if it encounters what it calls an "indentation error", so
make sure your indentation is consistent, and you're not using tabs.

Another issue about indentation errors is that they might not necessarily be a syntax error, so the
program will seem to run like normal, but encounter what we call a 'logic error'.

here is an example (I am typing it in a note because it is an infinite loop if I ran it!):

sentinalValue = 1

while (sentinalValue <= 5):
    print("I used a while loop here")
sentinalValue += 1

Notice how 'sentialValue += 1' is no longer indented, so that means it is not a part of the loop body.
In turn, this means as the loop is executing, the sentinal will not be incremented, and the loop will
run forever. (and that's bad)

Alright, so now for one of the biggest things in any programming langues: control structures.

Even if you haven't programmed before, you have probably heard of if statements. If statements are
just as they sound: if this is true, do this. To accompany if statements, there are also else statements
which can be read as if this is true, do this. If not, then do this. Much like loops, they are controlled
by boolean expressions, so lets wrap up this novel of text by combining a few parts of this lecture into
one:
'''

# Get user input
uInput = input("Please enter a number between 1 and 10: ")

# 'Convert' the string input into a number
# keep in mind that this will error out if they user enters something
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