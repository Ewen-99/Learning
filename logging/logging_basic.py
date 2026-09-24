import logging

## logging levels

# debug
# info
# warning (default level)
# error
# critical


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y

num_1 = 20
num_2 = 15
add_result = add(num_1, num_2)
# logging.debug('Add: {} + {} = {}.'.format(num_1, num_2, add_result))
# logging.warning('Add: {} + {} = {}.'.format(num_1, num_2, add_result))

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logging.debug('Add: {} + {} = {}.'.format(num_1, num_2, add_result))
