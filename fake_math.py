def get_multiplied_digits(number):
    """
    Вычисляет произведение цифр числа рекурсивно.

    Args:
        number: Целое число.

    Returns:
        Произведение цифр числа.
    """
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)

result3 = get_multiplied_digits(12345)
print(result3)

result4 = get_multiplied_digits(0)
print(result4)

result5 = get_multiplied_digits(1000)
print(result5)

result6 = get_multiplied_digits(1)
print(result6)