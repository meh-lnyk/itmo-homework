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


def call_func(task_num: int) -> None:
    if task_num == 1:
        max_num()
    else:
        print("Incorrect input!")


def choose_task() -> None:
    print(" Task 1: print the bigger number")
    print("Choose a task:")

    try:
        task_num: int = int(input())
    except ValueError:
        print("Incorrect input, please try again.")
        return

    call_func(task_num)


choose_task()
