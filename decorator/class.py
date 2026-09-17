# Decorate with class

class decorator_class():
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('wrapper executed this before {}'.format(self.original_function.__name__))
        self.original_function(*args, **kwargs)

@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Alice', 30)