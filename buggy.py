
def fixed_code():
    x = 1
    y = 0
    try:
        z = x/y
    except ZeroDivisionError:
        z = 0
    return z