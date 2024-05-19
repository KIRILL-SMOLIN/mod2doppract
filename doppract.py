    # Дополнительное практическое задание по модулю: "Базовые структуры данных."
    # Задание "Слишком древний шифр"

def count_pas(n):
    password = list()
    for i in range(1,n):
        for j in range(i+1,n):
            if n % (i + j) == 0:
                an = str(i) + str(j)
                password.append(an)
    return password

n = int(input('Быстрее вводим, что там выпало на первом камне? :'))
while (n < 3 or n > 20):
    n = int(input('сдурел в игрушки играть? правильный номер вводи :'))

result = str()
baseresult = count_pas(n)
for i in range(len(baseresult)):
    result += baseresult[i]
print('Вводим на втором камне:', result)
