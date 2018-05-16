print("""You enter a game show with three doors. 
Do you pick door #1, #2, or #3?""")

door = input("> ")

if door == "1":
    print("I'll allow you to switch your choice.")
    print("Let me reveal what's behind another door.")
    print("There is nothing behind door three.")
    print("Do you choose to switch from your original selection to door 2?")

    door = input("> ")

    if door == "1":
        print("There is only a giftbox here!")
        print("Better luck next time.")

    elif door == "2":
        print("You've found a car!")
        print("Good job!")

    else:
        print("Please enter one or two this time.")
        door = input("> ")

elif door == "2":
    print("I'll allow you to switch your choice.")
    print("Let me reveal what's behind another door.")
    print("There is nothing behind door three.")
    print("Do you choose to switch from your original selection to door 1?")

    door = input("> ")

    if door == "1":
        print("You only found a giftbox.")
        print("Better luck next time.")

    elif door = "2":
        print("You've found a car!")
        print("Good job!")

    else:
        print("Please enter one or two this time.")
        door = input("> ")

elif door = "3":
    print("I'll allow you to switch your choice.")
    print("Let me reveal what's behind another door.")
    print("There is nothing behind door one.")
    print("Do you choose to switch from your original selection to door 2?")

    if door == "2":
        print("You only found a giftbox.")
        print("Better luck next time.")

    elif door = "3":
        print("You've found a car!")
        print("Good job!")

    else:
        print("Please enter one or two this time.")
        door = input("> ")

else:
    print("Oh no! Try again!")
    