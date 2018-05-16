"""
1. Every if statement must have an else.

2. If this else should never run because it doesn't make sense
then you must use a die function in the else that prints out an error
message and dies, just like we did in the last exercise.
This will find many errors.

3. Never nest if statements more than two deep and always try to do them one deep

4. treat if-statements like paragraphs, where each if-elif-else grouping
is like a set of sentences. Put blank lines before and after

5. Your boolean tests should be simple. If they are complex, move their calculations to variables earlier in
your function and use a good name for the variable

6. Make a game like so
"""

def treasure_room():
    print("Welcome to the treasure room!")
    print("Please answer each of the five questions correctly")
    print("to move onto the next room.")
    print("At the end of all five rooms, there is a good prize for you.")
    question1 = "What is 5 + 10?"
    question2 = "What is 5 + 2 - 3 + 6?"
    question3 = "What are the the prime numbers under 10?"
    question4 = ""
