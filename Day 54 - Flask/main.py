def logging_decorator(function):
    def wraper(*args, **kwargs):
            print(f"You caleed {function.__name__}{args}")
            res = function(args[0], args[1], args[2])
            print(f"It returned: {res}")
    return wraper

@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1,2,3)
