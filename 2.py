# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую
# сумму двух целых неотрицательных чисел. Из всех арифметических 
# операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

def sum_numbers(number_A, number_B):
    if number_B == 0:
        return number_A
    return sum_numbers(number_A + 1, number_B - 1)
print(sum_numbers(0,0))
print(sum_numbers(0,2)) 
print(sum_numbers(3,0))
 
