def my_function1(*args):
    print(args)


def my_function2(**kwargs):
    print(kwargs)


if __name__ == '__main__':
    my_function1(1, "hey", 3)
    my_function2(name="Alice", age=25, hey=10)
