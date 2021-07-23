def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10)


print(sum_digit(123))
print(sum_digit(987))
