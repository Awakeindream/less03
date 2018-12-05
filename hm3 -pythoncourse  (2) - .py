# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits): 
    number = number*(10**ndigits)+0.4 
    number = number//1 
    return number/(10**ndigits) 
print(my_round(5435225.45646654, 5)) 



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

lucky_ticket = lambda x :(lambda x : 'yes' if sum(x[:3]) == sum(x[3:]) else 'no')(map(int, list(str(x)))) 
print(lucky_ticket(365453))

# normal 

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fib(n,m):
  import math
  while n <= m :
    a = int((((1 + math.sqrt(5))/2)**n-((1 - math.sqrt(5))/2)**n)/(math.sqrt(5)))
    print (a)
    n += 1

x = fib(7,12)
print ("="*50)


def fib1(n1,m1):
  a1 = 0
  b1 = 1
  q1 = 0
  while q1 < m1 :
    a1 = a1 + b1
    b1 = a1 - b1
    q1 += 1
    if q1 >= n1 : print (a1)
    else : continue
    
fib(7,12)




# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

bubble = [45, 2, 13, 12, -101, 7.5, 3, -1, -4.3, 4, 0]

def srt(list):
    print (bubble)
    lst = []
    while len(bubble) > 0 :
        a = bubble[0]
        for i in bubble :
            if i <= a :
                a = i
        bubble.remove(a)
        lst.append(a)
    print (lst)

srt(bubble)



# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

bubble = [45, 2, 13, 12, -101, 7.5, 3, -1, -4.3, 4, 0]
def filt(arg, obj):
    print (obj)
    print ('='*60)
    lst = []
    for i in obj : 
        if i != arg : 
            lst.append(i)
    print (lst)
            
filt(4, bubble)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math


 
A1, A2, A3, A4 = (2, 3), (0, 2), (4, 1), (6, 2)


def isparall(a, b, c, d):
    
#Параллелограмм
#p1 = False, p2 = False
#Противополжные стороны параллельны и равны
    
    ab = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    cb = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    cd = math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
    ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
    if ab == cd and cb == ad:
        print('Равенство сторон: верно')
        p1 = True
    else:
        print('Противоположные стороны не равны')
    
    
    hO1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    hO2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)
    if hO1 == hO2:
        print('Равенство половин диагоналей: верно')
        p2 = True
    else:
        print('Половины диагоналей НЕ равны')

    if p1 and p2:
        print('Вершины A1%s, A2%s, A3%s, A4%s\nобразуют параллелограмм' %
              (a, b, c, d))
    else:
        print('Вершины не образуют параллелограмм')

isparall(A1, A2, A3, A4)


# lesson3-2, hard
# не смог тут все сделать сам, пришлось немного подсмотреть что б понять идею


def tolist(path):
    '''
    Возвращает массив строк из файла path
    '''
    with open(path, encoding='UTF-8') as lister:
        nlist = [elems for elems in lister]
        nlist = [[el.strip() for el in elem if len(el)] for
                 elem in [elems.split(' ') for elems in nlist]]
        return nlist


def couple(header, values):
    '''
    Возвращает массив словарей с ключами из
    header и соответсвующими им значениями из
    values
    '''
    nlist = [list(zip(header, value)) for value in values]
    nlist = [{elem[0]: elem[1] for elem in elems} for elems in nlist]
    return nlist


def merge(file1, file2):
    '''
    Возвращает общую таблицу из file1 и file2
    в виде списка из словарей по каждому сотруднику
    '''
    persons_list = tolist(file1)  # Создание списка строк из табл.№1
    houres_list = tolist(file2)  # Создание списка строк из табл.№2
    header_p = persons_list.pop(0)  # Выделение заголовка из табл.№1
    header_h = houres_list.pop(0)  # Выделение заголовка из табл.№2
    '''
    Создание пары заголовок - значение для каждого сотрудника
    в каждой таблице
    '''
    personal = couple(header_p, persons_list)
    hourse = couple(header_h, houres_list)
    '''
    Слияние таблиц
    '''
    for el in personal:
        for e in hourse:
            if (el['Фамилия'] == e['Фамилия'] and
               el['Имя'] == e['Имя']):
                el.update(e)

    return personal


def calc_pay(tabl):
    '''
    Расчёт зарплаты
    '''
    for person in tabl:
        pay = int(person['Зарплата'])
        h_need = int(person['Норма_часов'])
        h_fact = int(person['Отработано_часов'])
        h_pay = int(pay / h_need)

        if h_fact == h_need:
            person['Расчёт'] = '%s' % (pay)
        elif h_fact > h_need:
            person['Расчёт'] = '%s' % (pay + (h_fact-h_need) * h_pay*2)
        else:
            person['Расчёт'] = '%s' % (h_pay * h_fact)

    return tabl


personal = calc_pay(merge('workers.txt', 'hourse_of.txt'))

with open('calc_pay.txt', 'w', encoding='UTF-8') as pay_list:
    header = '{:<10}{:<12}{:<10}\n'.format('Имя', 'Фамилия', 'Расчёт')
    body = '\n'.join(['{:<10}{:<12}{:<10}'.format(pers['Имя'], pers['Фамилия'],
                                                  pers['Расчёт'])
                      for pers in personal])

    print(header + body)

    pay_list.write(header + body)
