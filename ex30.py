people = 30
cars = 40
trucks = 15

if cars > people:
    print("we should take the cars.")
    #should print "we should take the cars
elif cars < people:
    print("We should not take the cars.")
    #doesn't evaluate
else:
    print("We can't decide.")
    #if both values are equal, go to here.

if trucks > cars:
    print("That's too many trucks.")
    #this won't evaluate
elif trucks < cars:
    print("Maybe we could take the trucks.")
    #this will print
else:
    print("We still can't decide.")
    #This won't evaluate.

if people > trucks:
    print("Alright, let's just take the trucks.")
    #This will print out
else:
    print("Fine, let's just stay home then.")
    #This won't print out


"""
What does elif do?
else if: next condition to be met
else is for all other cases
if conditions are met, these work


"""