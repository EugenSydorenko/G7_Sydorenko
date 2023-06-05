# ---------1---------
def read_integer_input():
    user_input = input("Enter an integer: ")
    try:
        integer_value = int(user_input)
        return integer_value
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


num = read_integer_input()
if num:
    print("The entered integer is:", num)


# ---------2---------
def read_and_sum_inputs():
    input1 = input("Enter the first number: ")
    input2 = input("Enter the second number: ")

    try:
        num1 = int(input1)
        num2 = int(input2)
        result = num1 + num2
    except ValueError:
        result = input1 + input2
    return result


result = read_and_sum_inputs()
print("The result is:", result)


# ---------3---------
def read_integer_input():
    while True:
        user_input = input("Enter an integer: ")
        try:
            integer_value = int(user_input)
            print("Thank you for entering an integer!")
            return integer_value
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")


num = read_integer_input()
if num is not None:
    print("The entered integer is:", num)


# ---------4---------
class OnlyEvenError(Exception):
    pass


def check_digit(number):
    if number % 2 != 0:
        raise OnlyEvenError("Only even numbers are allowed.")
    return number


try:
    num = int(input("Enter a number: "))
    result = check_digit(num)
    print("The entered number is:", result)
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except OnlyEvenError as e:
    print("Error:", str(e))


# ---------5---------
def process_number(number):
    print('I will print something anyway')
    try:
        checked_number = check_digit(number)
        result = checked_number * 2
    except OnlyEvenError:
        result = number + 1
    return result


num = int(input("Enter a number: "))
result = process_number(num)
print("The processed result is:", result)
