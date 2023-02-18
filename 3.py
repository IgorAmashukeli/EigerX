def sumDigits(number):
    if number < 0:
        return sumDigits(-number)
    if number == 0:
        return 0
    else:
        return sumDigits(number // 10) + number % 10