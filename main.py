def decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)

    return wrapper


@decorator
def func_for_decorator(value:int) -> int:
    return value * 2

print(func_for_decorator([2,4]))
