for numero in range(1, 31):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    elif numero % 7 == 0:
        print("Bang")
    else:
        print(numero)