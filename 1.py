import random
import tkinter as tk
from tkinter import *
import tkinter.font as font


#  1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

def task1():
    sourceString = 'Напишите програбвамму, удаляющую из текабвста все слова, содержащие "абв".'.split(' ')
    result = ''
    for x in sourceString:
        if 'абв' not in x:
            result += ' ' + x
    return result[1:]


# 2. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота "интеллектом"

def task2():
    print('Правила: На столе лежит 521 конфета. Играют два игрока делая ход друг после друга.\n'
          'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
          'Все конфеты оппонента достаются сделавшему последний ход.\n')

    def turnDetection():
        if random.randint(1, 2) == 1:
            act = player1
            print(f'Первый ход делает {player2}')
        else:
            print(f'Первый ход делает {player1}')
            act = player2
        return act

    def changePlayer(act):
        if act == player1:
            act = player2
        else:
            act = player1
        return act

    def pvp():
        turn = turnDetection()

        total = 221
        while total > 1:
            turn = changePlayer(turn)
            k = 0
            print(f'В куче осталось {total} конфет')
            while k < 1 or k > 28:
                k = int(input(f'Ход делает {turn}: '))
            total -= k

        print(f'\nВсе конфеты достаются {turn}')

    def pve():

        def aiTurn():
            if total < 29:
                return total
            for k in range(1, 29):
                if (total - k) % 29 == 0:
                    break
            print(f'Бот забирает {k} конфет')
            return k

        turn = turnDetection()
        total = 221
        while total >= 1:
            turn = changePlayer(turn)
            print(f'В куче осталось {total} конфет')
            k = 0
            if turn == player1:
                while k < 1 or k > 28:
                    k = int(input(f'Ход делает {turn}: '))
                    total -= k
            else:
                total -= aiTurn()

        print(f'\nВсе конфеты достаются {turn}')

    mode = int(input('1 - игра PvP\n2 - игра PvE\n'))
    player1 = input('Введите имя первого игрока: ')
    if mode == 1:
        player2 = input('Введите имя второго игрока: ')
        pvp()
    else:
        player2 = 'Бот'
        pve()


#  3. Создайте программу для игры в "Крестики-нолики".

def task3():
    global figure

    def setFigure(index):
        global figure
        btns[index].config(text=figure)
        if figure == 'X':
            figure = 'O'
        else:
            figure = 'X'
        btns[index].config(state=DISABLED)
        winList[index] = figure
        winCheck()

    def addBtn(num):
        btns.append(Button(mainFrame, width=17, height=8, padx=15, pady=15))
        btns[num].config(command=lambda: setFigure(num))
        btns[num]['font'] = font.Font(family='Helvetica', size=9, weight='bold')
        btns[num].grid(row=i, column=j)

    def winCheck():
        if winList[0] == winList[1] == winList[2] \
                or winList[3] == winList[4] == winList[5] \
                or winList[6] == winList[7] == winList[8] \
                or winList[0] == winList[3] == winList[6] \
                or winList[1] == winList[4] == winList[7] \
                or winList[2] == winList[5] == winList[8] \
                or winList[0] == winList[4] == winList[8] \
                or winList[2] == winList[4] == winList[6]:
            if figure == 'X':
                print(f'Победа O')
            else:
                print(f'Победа X')
            raise SystemExit

    root = tk.Tk()
    root.geometry('500x500')
    root.resizable(False, False)
    root.title('Крестики-нолики')

    mainFrame = Frame(root, padx=15, pady=10)

    winList = [x for x in range(9)]
    figure = 'X'
    btns = []
    index = -1
    for i in range(3):
        for j in range(3):
            index += 1
            addBtn(index)

    mainFrame.grid(row=0, column=0, sticky='ns')
    root.mainloop()

#  4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.

def task4():
    def crypt():
        global tempString

        def addToTemp(symbol, count):
            global tempString
            tempString += symbol + count + '|'

        fileIn = 'IN.txt'
        tempString = ''
        with open(fileIn, 'r') as area:
            data = area.read()
        for s in range(len(data)):
            if data[s] == data[s - 1]:
                continue
            count = 0
            for h in range(s, len(data)):
                if data[h] == data[s]:
                    count += 1
                else:
                    addToTemp(str(data[s]), str(count))
                    break
        addToTemp(str(data[s]), str(count))
        fileOut = 'CRYPTED.txt'
        with open(fileOut, 'w') as target:
            target.write(tempString[0:-1])

    def uncrypt():
        fileIn = 'CRYPTED.txt'
        with open(fileIn, 'r') as area:
            data = area.read().split('|')
        tempString = ''
        for i in data:
            count = int(i[1:])
            tempString += i[0] * count
        fileOut = 'UNCRYPTED.txt'
        with open(fileOut, 'w') as target:
            target.write(tempString)

    print('1. Зашифровать данные\n2. Расшифровать данные\n')
    choise = int(input('Что нужно сделать? '))
    if choise == 1:
        crypt()
    else:
        uncrypt()


# print(task1())
# task2()
# task3()
# task4()
