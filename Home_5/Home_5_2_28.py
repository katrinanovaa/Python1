# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

a = 3
b = 3

def final_sum(a, b):
    if a == 0 and b == 0: 
        return 0
    if a !=0:
        return final_sum(a-1, b) + 1
    return final_sum(a, b-1) + 1

print(final_sum(a, b))