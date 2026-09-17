# First class functions and closure
# Prerequisite for decorators

## First class function
def square(x):
    return x*x

f = square  # f is a function object
print(f)    # decoration time: create a funciton
print(f(5)) # call time: function doesn't run without ()


## Closure
def greeting(msg):
    message = msg   # closure: memorize the local variables
    def saying():
        print(message)
    return saying   # return a funciton, not execute running immediately

say_hi = greeting('hi') # decoration time: create function with parameter
say_hello = greeting('hello')

say_hi()    # call time
say_hello()


## Application example: create html

def html_tag(tag):
    def wrapper(msg):
        print('<{0}>{1}<\{0}>'.format(tag, msg))
    return wrapper

print_h1 = html_tag('h1')
print_p = html_tag('p')

print_h1('This is a heading')
print_p('This is a paragraph')
