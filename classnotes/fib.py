def cache(func):
    cached_vals = {}
    def cached_func(n):
        if n in cached_vals:
            return cached_vals[n]
        result = func(n)
        cached_vals[n] = func(n)
        return result
    return cached_func

@cache
def fib(n:int) -> int:
    # f(n) = f(n-1) + f(n-2)
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

# @cache doesn't allow the function to ask the question multiple times, saving the information. 
# It remembers what n = 3 was and immediatly returns it
print(fib(450))

