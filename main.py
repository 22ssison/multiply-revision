"""multiplies user inputs and recieves ourtpout"""

def get_int(txt):
    while True:
        try:
            integer = int(input(txt))
            return integer
        except ValueError:
            print()
            print("Invalid Input. Please enter a number.")


def get_user_input():
    print()
    num1 = get_int("Please enter the first number:\n> ")
    print()
    num2 = get_int("Please enter the second number:\n> ")
    print()
    num3 = get_int("Please enter the third number:\n> ")
    print()
    num4 = get_int("Please enter the fourth number:\n> ")
    print()
    num5 = get_int("Please enter the final number:\n> ")


