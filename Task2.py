# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все 
# конфеты у своего конкурента?
import random
from random import randint   

def take_candy(name):
    while True:
        player_take = input(f'{name}, выберете количество конфет от 1 до 28: ')
        if not player_take.isnumeric():
            print(f'{name}, введите число.')
        elif not 1 < int(player_take) < 28:
            print(f'{name}, введите корректное число конфет! Попробуйте еще раз.')
        else:
            return int(player_take)
    
def player_info(name, taken, count, candys):
    print(f'Ходил {name}, взято конфет: {taken}, счет игрока: {count}. Осталость конфет: {candys}')

player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ') 

candys = int(input('Введите кол-во конфет: '))
while candys < 30:
    candys = int(input('Введите число больше 30: '))

flag = randint(0, 2)
if flag:
    print(f'Первый ход за игроком - {player_1}')
else:
    print(f'Первый ход за игроком - {player_2}')

count1 = 0
count2 = 0 

while candys > 28:
    if flag:
        taken = take_candy(player_1)
        count1 += taken
        candys -= taken
        flag = False
        player_info(player_1, taken, count1, candys)
    else:
        taken = take_candy(player_2)
        count2 += taken
        candys -= taken
        flag = True
        player_info(player_2, taken, count2, candys)

if flag:
    print(f'Выиграл {player_1}!')
else:
    print(f'Выиграл {player_2}!')

