def for_loop:
    numbers = []
    for i in range(0, 6):
        print(f"At the top is {i}")
        numbers.append(i)
        print(f"At the bottom is {i}")

        print("Numbers now", numbers)
        print(f"at the bottom is {i}")

    print("The numbers")
    for num in numbers:
        print(numbers)