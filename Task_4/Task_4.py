# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.    
#     *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²

from random import randint 
# Подготовка 

k = int(input('Введите натуральную степень k:'))
my_str = ""

# Создаем степени для полинома 
for i in range(k, 2, -1):
     a = randint(0, 10)    
     my_str = my_str+(f'{a}*x^{i} + ')
     
else:
     a = randint(0, 10)
     if a !=0:
            my_str = my_str + (f'{a}*x')
     a = randint(0, 10)
     if a !=0:
           my_str = my_str + (f'{a} = 0')
# Записываем полином в файл
my_file = open("__my_file.txt","w")
my_file.write(my_str)
my_file.close()     


