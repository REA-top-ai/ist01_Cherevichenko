def null_decorator(func):
    return func

@null_decorator
def greeting():
    return 'hello'


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'hello'

def add_data(func):
    def wrapper():
        return '<data>' + func() + '</data>'
    return wrapper


def add_name(func):
    def wrapper():
        return '<name>' + func() + '</name>'
    return wrapper

@add_data
@add_name
def app_name():
    return 'Calc'


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'Trace: calling {func.__name__}()',
              f'with {args} and {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'Trace: {func.__name__}()',
              f'returned {original_result}')
        
        return original_result
    return wrapper

@trace
def say_hello(name, text):
    return f'{name}, {text}'
















