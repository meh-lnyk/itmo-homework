def max_num() -> None:
    try:
        num1: int = int(input("Insert the first number: "))
        num2: int = int(input("Insert the second number: "))
    except ValueError:
        print("Incorrect input, please try again.")
        return

    if num1 > num2:
        max_val = num1
    elif num2 > num1:
        max_val = num2
    else:
        max_val = None

    if max_val is not None:
        print(f"The bigger number is {max_val}")
    else:
        print("Numbers are equal!")


def dif_by_135() -> None:
    try:
        num1: int = int(input("Insert the first number: "))
        num2: int = int(input("Insert the second number: "))
    except ValueError:
        print("Incorrect input, please try again.")
        return

    print("Is the difference between the numbers 135?")
    if num1 - num2 == (135 or -135):
        print(" Yes")
    else:
        print(" No")


def season_name() -> None:
    try:
        month_num: int = int(input("Insert the month number: "))
    except ValueError:
        print("Incorrect input, please try again.")
        return

    print("The season is:")
    match month_num:
        case 1 | 2 | 12:
            print(" Winter")
        case 3 | 4 | 5:
            print(" Spring")
        case 6 | 7 | 8:
            print(" Summer")
        case 9 | 10 | 11:
            print(" Fall")
        case _:
            print("Incorrect input, please try again.")


def bigger_than_10() -> None:
    try:
        num_1: int = int(input("Insert the first number: "))
        num_2: int = int(input("Insert the second number: "))
        num_3: int = int(input("Insert the third number: "))
    except ValueError:
        print("Incorrect input, please try again.")
        return

    print("Are all the numbers bigger than 10?")
    if num_1 & num_2 & num_3 > 10:
        print(" Yes")
    else:
        print(" No")


def find_positive() -> None:
    user_input = input("Enter 5 numbers separated by spaces: ")
    input_list = user_input.split()
    try:
        num_list = [int(s) for s in input_list]
    except ValueError:
        print("All inputs must be integers!")
        return

    if len(num_list) == 5:
        num_pos = 0
        for num in num_list:
            if num > 0:
                num_pos += 1
        print(f"The number of positive integers in the list is {num_pos}")
    elif len(num_list) != 5:
        print("You must enter exactly 5 numbers.")
    else:
        print("Incorrect input!")


def call_func(task_num: int) -> None:
    if task_num == 1:
        max_num()
    elif task_num == 2:
        dif_by_135()
    elif task_num == 3:
        season_name()
    elif task_num == 4:
        bigger_than_10()
    elif task_num == 5:
        find_positive()
    else:
        print("Incorrect input!")


def choose_task() -> None:
    print(" Task 1: print the bigger number")
    print(" Task 2: are the numbers different by 135?")
    print(" Task 3: print the name of the season")
    print(" Task 4: are the numbers bigger than 10?")
    print(" Task 5: find positives in a list")
    print("Choose a task:")

    try:
        task_num: int = int(input())
    except ValueError:
        print("Incorrect input, please try again.")
        return

    call_func(task_num)


choose_task()
