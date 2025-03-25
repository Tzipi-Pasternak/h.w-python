from time import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        return end - start
    return wrapper


@time_decorator
def func(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(f"Execution Time: {func(1000000):.6f} seconds")



def cache_decorator(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper


@time_decorator
@cache_decorator
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


@time_decorator
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(f"Execution time with cache: { fib_cached(35):.6f} seconds")
print(f"Execution time without cache: { fib(35):.6f} seconds")