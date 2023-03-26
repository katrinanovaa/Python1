Count_monets = int(input("Введите количество монет: "))
pos_orel = 0
pos_reshka = 0
for i in range(Count_monets):
    position = int(input(f"Введите какая позиция {i+1}-ой монеты выпала, 0 или 1: "))
    if position == 0:
        pos_orel +=1
    else:
        pos_reshka +=1
print(f"Кол-во монет, чтобы перевернуть: {min(pos_orel, pos_reshka)} ")
