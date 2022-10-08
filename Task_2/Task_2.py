# 2.Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.

n = int(input("Введите число: "))
i = 2 
list1 = []
entered_number = n
while i <= n:
    if n % i == 0:
        list1.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {entered_number} приведены в списке: {list1}") 