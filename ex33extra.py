#convert the previous while loop into a callable function

def while_loop:
    i = 0
    j = input('> Insert the length of the loop here')
    k = input("> This is the incrementor")
    numbers = []

    while i < j:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += k
        print("Numbers now: ", numbers)
        print(f"at the bottom is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


