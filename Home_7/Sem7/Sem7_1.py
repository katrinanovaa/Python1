file = open('data.txt', mode = 'r', encoding = 'UTF-8')

for el in file:
    print(el)
    
file.close()       #если не закрыть, то может файл остаться не закрытым и помешать дальнейшей работе ОС
