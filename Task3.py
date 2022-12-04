task3 = input('Введите числа через запятую и пробел: ')
task3 = task3.strip().split(', ')
fractions = []
for i in task3:
    remainder = i.split('.')
    if len(remainder) > 1:
        fractions.append(float('0.' + remainder[1]))
print(fractions)
minf = fractions[0]
maxf = fractions[0]
for g in fractions:
    if g > maxf:
        maxf = g
    elif g < minf:
        minf = g
resalt = maxf - minf
print(maxf, minf)
print(resalt)
