a = (1,1.2, 'hello')
a = {'a':1, 'b' 1.2, 'c': 'hello'}
a = (1,1.1, 'a', [4,5,6], {'a':1, b':2}, None, True)
a =()
b = tuple()
b = (1,)
a = [1, 2.1,3] # это список list
tuple(a) # (1, 2.1,3)
b = tuple('abc') # ('a, 'b, 'c)
a = (1,2.1, 'd') в кортеже можно обращаться к элементу по индексу
a[0] # 1
a[2] # 'd'
a = (1,1.1,'a')
print(a) # (1,1.1, 'a')
prent((1,1.1, 'a')) # (1,1.1,'a')
a = (1,1.1,'a')
a[0] # 1
a[1] # 1.1
a[2] # 'a'
a[3] # Ошибка вышли за границы
a[-1] # a
a[-2] # 1.1
a[-3] # 1
a[-4] # Ошибкаб вышли за границы
a = (1,2,3,)
b = (4,5,6,)
c = a * b
print (c) # (1,2,3,1,2,3)
a *= b # Теперь "a" равно (1,2,3,1,2,3)
a = (1,2,3) # Это одномерный кортеж
b = ((1,2,3), (4,5,6), (7,8,9))
b = ((1,2,3), (4,5,6) (7,8,9))
b[0] # Получение 1-ого кортежа (1,2,3)
b[0][0] # Получение первого элемента "1" из 1-ого кортежа (1,2,3)
b[-1][-1] # Получение последнего элемента "9" из последнего кортежа (7,8,9)
heip(tuple) # Информация о кортежах
a = (1,2,1)
a.count(1) # 2. Возвращает сколько раз в кортеже встретилось передаваемое значение. В примере вернется 2, так как в кортеже 2 единицы
a.index(2) # 1. Возвращает индекс, где передаваемое значение стоит в кортеже. В примере вернется 1, так как значение 2 в кортеже стоит на 1-ом индексе
a = (1,2,[1,2,3])
a[2][0] = 10 # Теперь "a" (1,2,[10,2,3]),  та как внутри кортежа мы можем обратиться к изменяемому типу, хотя a[1
 = 10 нам не позволит сделать
a = [1,2,3,] # Создали список
b = (1,2,a) #Передали "a" в кортеж "b" = (1,2,[1,2,3])
a[1] = 20 #Теперь "a" равно [1,20,3].
print(b) # (1,2,[1,20,3]), так как "a" это список который внутри кортежа "b".
a = {'a':1} # Словарь из одного элемента (ключ "a", значение 1)
a = {'a':1, 'b':2} # Словарь из двух элементов (ключ "a" значение 1, ключ "b", значение 2)
a = dict([['a',1],['b',2]]) # Это создаст словарь {'a':1, 'b':2}
a = dict(a=1, b=2) # Это создаст словарь {'a':1, 'b':}
a = {}
b = dict()
a = dict([['a',1],['b'2]]) # Передан список списков. Это создаст словарь {'a':1, 'b':2}
a = dict((('a',1), ('b',2))) № Передан кортеж кортежей . Это создаст словарь {'a':1, 'b':2}
a = {1:'a', 1.1:'b','c':3,(1,2);[1,2,3], frozenset
