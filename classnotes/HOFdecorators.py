def tracer(func):
    def traced(a,b):
        print(f"Calling {func.__name__}({a}, {b})")
        result = func(a,b)
        print(f"Result is {result}")
        return result
    return traced

@tracer
def add(a,b):
    return a + b

@tracer
def subtract(a,b):
    return a -b

print(add(4,7))

print(subtract(4,7))
