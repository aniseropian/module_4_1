from math import inf

def divide(first, second):
    """Divides first by second, returns inf for division by zero."""
    try:
        result = first / second
        return result
    except ZeroDivisionError:
        return inf
