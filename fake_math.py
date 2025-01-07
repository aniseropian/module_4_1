def divide(first, second):
    """Divides first by second, returns 'Ошибка' if division by zero."""
    try:
        result = first / second
        return result
    except ZeroDivisionError:
        return "Ошибка"
