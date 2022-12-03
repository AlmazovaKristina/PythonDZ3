task4 = int(input('Введите число'))
my_list = []
while task4 > 0:
    division = task4 // 2
    multiplication = division * 2
    result = task4 - multiplication
    my_list.append(result)
    task4 = division
print(my_list[::-1])
