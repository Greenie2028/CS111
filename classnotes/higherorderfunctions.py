def hello_func():
    print("Hello")
    return 7

def goodbye_func():
    print("Goodbye")
    return "byebye"

# my_func_list = [hello_func, goodbye_func]
# for func in my_func_list:
    #print(func.__name__)
    #print(f"Running {func.__repr__()}")
    # Functions are classes

# def func_printer(func):
#     print(f"Running {func.__name__}")
#     result = func()
#     print(f"Result was: {result}")

def tracer(func):
    def traced_func():
        print(f"Running {func.__name__}")
        result = func()
        print(f"Result was: {result}")

    return traced_func

better_goodbye_func = tracer(goodbye_func)
better_goodbye_func()


# Might be useful for debugging or logging
