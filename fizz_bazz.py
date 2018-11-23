def fizbaz():
    num = input("Please type number:")
    if num % 15 == 0:
        print("FizzBazz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Bazz")
    else:
        print(num)

fizbaz()
