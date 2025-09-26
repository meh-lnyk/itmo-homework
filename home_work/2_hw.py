def task_1() -> None:
    var_int: int = 1
    var_float: float = 1.0
    var_str: str = "one"
    var_list: list = [1, 1.0, "one"]
    var_bool: bool = True

    print("Task 1:")
    print(type(var_int))
    print(type(var_float))
    print(type(var_str))
    print(type(var_list))
    print(type(var_bool))

task_1()
print()

def task_2():
    a = [1, 2, 3, 5, 8, 13, 21]
    print("Task 2:")
    print(a[:3])
    print("Those are Fibonacci numbers")

task_2()
print()

def task_3(num: float) -> float:
    print("Task 3:")
    return num * num

print(task_3(55))
