# PPHA 30535
# Spring 2021
# Homework 1

# Jessie Zou
# wenwen959

# Due date: Sunday April 10th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.
SnackBox=['Coke','Chips','Chocolate Bar','Gummies']
n=0
for snacks in SnackBox:
    print('The value at position' ,n,'is',snacks)
    n=n+1

# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results of these
# four tests.
test_one='radar'
test_two='A man, a plan, a canal, Panama!'
test_three='Apple'
test_four="This isn't a palindrome"

test=[test_one,test_two,test_three,test_four]
for item in test:
    if item == item[::-1]: #Reverse code [::-1] is copied from StackOverflow 
        print(item, 'is a palindrome')
    else:
        print(item, 'is not a palindrome')

# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice = input('Please pick a vegetable I have available: ')
while choice not in available_vegetables:
    choice = input('Please pick a vegetable I have available: ')
    
    if choice in available_vegetables:
        print('You can have', choice)


# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".
family = ['Wenwen','Xixi','Baobao','Nini']
new_list = [ppl.lower() for ppl in family if ppl[0]=='A' or ppl[0]=='B' ] #Representing initial letter
#code string[0] is refered to Grepper website
print(new_list)

# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]
start_list = [3, 5, 7, 9, 11, 13]
final_list = list(reversed([num*2 for num in start_list])) #Reverse list code reversed() is refered
#to realpython.com website
print(final_list)

# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']
new_dict = {short_names[i]:long_names[i] for i in range(len(short_names))} #Convert list to dictionary code
#list[i]:list[i] is refered to PythonGuide website
print(new_dict)

#Reference used:
#https://stackoverflow.com/questions/931092/reverse-a-string-in-python
#https://www.codegrepper.com/code-examples/python/how+to+get+the+first+letter+of+a+string+in+python
#https://realpython.com/python-reverse-list/
#https://pythonguides.com/python-creates-a-dictionary-from-two-lists/
