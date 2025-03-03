def log_decorator(func):
     def wrapper():
        print("Message avant")
        func()
        print("Message après")

    return wrapper
 
@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
