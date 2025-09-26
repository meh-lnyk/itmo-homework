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

    if month_num > 12:
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


def call_func(task_num: int) -> None:
    if task_num == 1:
        max_num()
    elif task_num == 2:
        dif_by_135()
    elif task_num == 3:
        season_name()
    else:
        print("Incorrect input!")


def choose_task() -> None:
    print(" Task 1: print the bigger number")
    print(" Task 2: are the numbers different by 135?")
    print(" Task 3: print the name of the season")
    print("Choose a task:")

    try:
        task_num: int = int(input())
    except ValueError:
        print("Incorrect input, please try again.")
        return

    call_func(task_num)


choose_task()
