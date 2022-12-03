task1 = input('Введите числа через пробел')
task1 = task1.strip().split(' ')
max_num = 0
for i in range(len(task1)):
    task1[i] = int(task1[i])
    if i % 2 > 0:
        max_num = max_num + task1[i]
print(task1)
print(max_num)
