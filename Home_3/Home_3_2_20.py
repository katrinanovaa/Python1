# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине 
# элемент к заданному числу X. Пользователь вводит это число с клавиатуры,
# список можно считать заданным. Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

elements = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
num_el = len(elements)    
zad_number = int(input("Введите число: "))

Raznica_num_min = None 
idx = None
for i in range(num_el):
    Raznica = abs(elements[i] - zad_number)
    if Raznica_num_min is None or Raznica < Raznica_num_min:
        Raznica_num_min = Raznica
        idx = i
    else: 
        continue
print(f"Самое ближайшее число: {elements[idx]}")
