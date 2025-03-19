"""multiplies user inputs and recieves ourtpout"""

# list
numbers = [] # in the main scope so that other functions can use the values inside.

# try and except function to deal with invalid user inputs. 
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
    numbers.append(num1)
    print()
    num2 = get_int("Please enter the second number:\n> ")
    numbers.append(num2)
    print()
    num3 = get_int("Please enter the third number:\n> ")
    numbers.append(num3)
    print()
    num4 = get_int("Please enter the fourth number:\n> ")
    numbers.append(num4)
    print()
    num5 = get_int("Please enter the final number:\n> ")
    numbers.append(num5)
    print()
    

def calculate():
    sum1 = numbers[0] * numbers[1]
    sum2 = sum1 * numbers[2]
    sum3 = sum2 * numbers[3]
    sum4 = sum3 * numbers[4]

    print()
    print(f"{numbers[0]} x {numbers[1]} = {sum1}")
    print()
    print(f"{sum1} x {numbers[2]} = {sum2}")
    print()
    print(f"{sum2} x {numbers[3]} = {sum3}")
    print()
    print(f"{sum3} x {numbers[4]} = {sum4}")
    print()



get_user_input()
print(numbers)
calculate()




