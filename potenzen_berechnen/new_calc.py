# Aufgabe zu calculator.py
# Erweitern Sie das Programm um die Funktion der Berechnung der zweiten, dritten sowie n-ten Potenz einer Zahl 
# (z.B. 3^2 = 9, 4^3 = 64, 2^10 = 1024) an den vorgesehenen Stellen.
# Verwenden Sie für diese Berechnung sowie für die Berechnung der anderen Basisoperationen (Menüpunkte 2-4) eigene 
# Funktionen nach dem Beispiel von add(first_number, second_number). Beachten Sie dabei das DRY-Prinzip.


# function definitions
def request_an_int():
    my_input = input("Give me a number: ")
    my_int = int(my_input)
    return my_int


def request_another_int():
    my_input = input("Give me another number: ")
    my_int = int(my_input)
    return my_int


def add(first_number, second_number):
    res = first_number + second_number
    return res


def subtract(first_number, second_number):
    res = first_number - second_number
    return res


def multiply(first_number, second_number):
    res = first_number * second_number
    return res


def divide(first_number, second_number):
    if second_number != 0:
        res = first_number / second_number
        return res
    else:
        return "Error: Division by zero"


def power_of_two(number):
    res = number ** 2
    return res


def power_of_three(number):
    res = number ** 3
    return res


def power_of_n(number, n):
    res = number ** n
    return res


def print_options():
    print("What do you want to do?")
    print(" 0: Exit")
    print(" 1: Add")
    print(" 2: Subtract")
    print(" 3: Multiply")
    print(" 4: Divide")
    print(" 5: To the power of two")
    print(" 6: To the power of three")
    print(" 7: To the power of n")


def print_result(result):
    print("The result is: " + str(result))


# main program
print_options()
exit_requested = False
while not exit_requested:
    selection = input("Select an option: ")
    if selection == "0":
        print("Exiting")
        exit_requested = True
    elif selection == "1":
        print("You chose addition.")
        result = add(request_an_int(), request_another_int())
        print_result(result)
    elif selection == "2":
        print("You chose subtraction.")
        result = subtract(request_an_int(), request_another_int())
        print_result(result)
    elif selection == "3":
        print("You chose multiplication.")
        result = multiply(request_an_int(), request_another_int())
        print_result(result)
    elif selection == "4":
        print("You chose division.")
        result = divide(request_an_int(), request_another_int())
        print_result(result)
    elif selection == "5":
        print("You chose to the power of two.")
        number = request_an_int()
        result = power_of_two(number)
        print_result(result)
    elif selection == "6":
        print("You chose to the power of three.")
        number = request_an_int()
        result = power_of_three(number)
        print_result(result)
    elif selection == "7":
        print("You chose to the power of n.")
        number = request_an_int()
        n = request_another_int()
        result = power_of_n(number, n)
        print_result(result)
    else:
        print("This is not a valid option!")
        print_options()
