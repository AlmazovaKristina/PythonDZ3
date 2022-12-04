task2 = input('Введите числа через пробел и запятую: ')
task2 = task2.strip().split(', ')
#task2 = [2, 3, 4, 5, 6]
my_list = []
g = 0
if len(task2) % 2 == 0:
    g = int(len(task2) / 2)
else:
    g = int(len(task2) / 2 + 1)

for i in range(g):
    my_list.append(int(task2[i]) * int(task2[-i-1]))
print(my_list)
