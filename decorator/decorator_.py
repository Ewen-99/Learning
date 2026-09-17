#Decorators

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed before {}'.format(original_function.__name__))
        return original_function()  # call time: actually calling the original function
    return wrapper_function # decoration time: returns (create) the function with intended parameters

# prototype

def display():
    print('display function ran')

decorated_display = decorator_function(display) # building a wrapper function which contain the original function
decorated_display()

# using @
# The @decorator_function is equivalent to the following
# display = decorator_function(display)

@decorator_function
def display():
    print('display funciton ran')

display()

