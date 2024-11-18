def get_multiplied_digits(nomber):
    str_number = str(nomber)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


num = input('Введите целое число: ')
print(f'Произведение цифр числа {num} :', get_multiplied_digits(num))
