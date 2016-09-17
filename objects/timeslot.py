import time


def current_milli_time():
    """
    :return: Time in milliseconds (integer)
    """
    return int(round(time.time() * 1000))


print current_milli_time()

# create time slots with object properties like this (here we have 1 object, but should be used
# with a list of objects (as object):
slots = {current_milli_time(): {'prop1': 12, 'prop3': 'toto'},
         current_milli_time() + 100: {'prop1': 14, 'prop3': 'titi', 'prop2': []}}
print slots

# Note: in case of slot of 1 second:     3 last digits are rounded to 0 [Int(x/1000) * 1000]
