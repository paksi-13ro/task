def print_params(a = 1, b = 'String', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [50, 'hello', 6.25]
values_dict = {'a': 'world', 'b': 8, 'c':[5,2,3]}
print_params(*values_list)
print_params(**values_dict)

valures_list_2 = [54.42, 'Строка']
print_params(*valures_list_2, 42)