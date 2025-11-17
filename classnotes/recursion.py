def tracer(some_func):
    func_id = [0]
    def new_traced_func(*args):
        id = func_id[0]
        func_id[0]+=1
        print(f"Calling {some_func.__name__} with {args}")
        result = some_func(*args)
        print(f"{id}: returning {result}")

    return new_traced_func

@tracer
def recursive_printing(str,num=1):
    print(str[0:num])
    if len(str) >= num:
        recursive_printing(str,int(num*1.1)+1)

def flipped(str,num=1):
    if len(str) >= num:
        flipped(str,int(num*1.1)+1)
    print(str[0:num])

recursive_printing("Hello World!")
# recursive_printing("Hello World")
# my_str = "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
# flipped(my_str)
# recursive_printing(my_str)