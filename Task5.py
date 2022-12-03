task5 = int(input('Введите число'))
summa = 1
summa2 = 0
my_list = []
my_list2 = [0]
while task5 > 0:
    result = summa + summa2
    summa = summa2
    summa2 = result
    my_list.append(summa2)
    task5 = task5 - 1
for i in range(len(my_list)):
    my_list2.append(my_list[i])
    if i % 2 > 0:
        my_list2.insert(0, my_list[i] * (-1))
    else:
        my_list2.insert(0, my_list[i])
print(my_list2)
