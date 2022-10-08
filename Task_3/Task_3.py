# 3.Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.


set_of_numbers = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {set_of_numbers}")
second_set_of_numbers = []
[second_set_of_numbers.append(i) for i in set_of_numbers if i not in second_set_of_numbers]
print(f"Список из неповторяющихся элементов: {second_set_of_numbers}")    