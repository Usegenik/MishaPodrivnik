#Miner_v3_betta Для сата UP-X
import pyautogui as root
import random
import time

        #KOD

selection = 0
numplay = 0
celnum = 0
rand = 0

#Работает на данном разрешении экрана 1680х1050
print(root.size())

numplay += 1
print(end='\n')
print('__________________________________________________')
print('         {==+==+==+==#Игра#==+==+==+==}')
print('             --------|№', numplay, '|--------')
print('__________________________________________________')
print(end='\n')

while True:

    # Рандомайзер нажатий на мины и установка количества нажатий
    celnum = (random.randint(2, 3))

    if celnum == 2:
        root.leftClick(549, 373, 0.2)
        print('Поле ввода значений.')
        root.press('backspace')
        print('Значение удалено.')
        root.write('2')

    elif celnum == 3:
        root.leftClick(549, 373, 0.2)
        print('Поле ввода значений.')
        root.press('backspace')
        print('Значение удалено.')
        root.write('3')

    elif celnum == 4:
        root.leftClick(549, 373, 0.2)
        print('Поле ввода значений.')
        root.press('backspace')
        print('Значение удалено.')
        root.write('4')

    elif celnum == 5:
        root.leftClick(549, 373, 0.2)
        print('Поле ввода значений.')
        root.press('backspace')
        print('Значение удалено.')
        root.write('5')
    print('Выбранно [', celnum, '] мин(ы)')

    #Кнопка играть
    root.leftClick(495, 448, 0.2)
    print('Игра начата!')

    # Генерация фигур
    selection = (random.randint(1, 7))

    if selection == 1:
        root.leftClick(890, 342, 0.2)
        print('Выбранна 6 ячейка на поле с минами')
        root.leftClick(975, 342, 0.2)
        print('Выбранна 7 ячейка на поле с минами')
        root.leftClick(890, 428, 0.2)
        print('Выбранна 11 ячейка на поле с минами')
        root.leftClick(975, 428, 0.2)
        print('Выбранна 12 ячейка на поле с минами')
        root.leftClick(492, 507, 0.2)
        print('Кнопка \'Забрать выйгрыш\' нажата!')
        numplay += 1
        print(end='\n')
        print('__________________________________________________')
        print('         {==+==+==+==#Игра#==+==+==+==}')
        print('             --------|№', numplay, '|--------')
        print('__________________________________________________')
        print(end='\n')

    elif selection == 2:
        root.leftClick(1145, 428, 0.2)
        print('Выбранна 14 ячейка на поле с минами')
        root.leftClick(1227, 428, 0.2)
        print('Выбранна 15 ячейка на поле с минами')
        root.leftClick(1145, 514, 0.2)
        print('Выбранна 19 ячейка на поле с минами')
        root.leftClick(1227, 514, 0.2)
        print('Выбранна 20 ячейка на поле с минами')
        root.leftClick(492, 507, 0.2)
        print('Кнопка \'Забрать выйгрыш\' нажата!')
        numplay += 1
        print(end='\n')
        print('__________________________________________________')
        print('         {==+==+==+==#Игра#==+==+==+==}')
        print('             --------|№', numplay, '|--------')
        print('__________________________________________________')
        print(end='\n')

    elif selection == 3:
        for i in range(3):
            rand = (random.randint(1, 25))

            if rand == 1:
                root.leftClick(890, 255, 0.2)
                print('Выбранна 1 ячейка на поле с минами')
            elif rand == 2:
                root.leftClick(975, 255, 0.2)
                print('Выбранна 2 ячейка на поле с минами')
            elif rand == 3:
                root.leftClick(1060, 255, 0.2)
                print('Выбранна 3 ячейка на поле с минами')
            elif rand == 4:
                root.leftClick(1145, 255, 0.2)
                print('Выбранна 4 ячейка на поле с минами')
            elif rand == 5:
                root.leftClick(1227, 255, 0.2)
                print('Выбранна 5 ячейка на поле с минами')
            elif rand == 6:
                root.leftClick(890, 342, 0.2)
                print('Выбранна 6 ячейка на поле с минами')
            elif rand == 7:
                root.leftClick(975, 342, 0.2)
                print('Выбранна 7 ячейка на поле с минами')
            elif rand == 8:
                root.leftClick(1060, 342, 0.2)
                print('Выбранна 8 ячейка на поле с минами')
            elif rand == 9:
                root.leftClick(1145, 342, 0.2)
                print('Выбранна 9 ячейка на поле с минами')
            elif rand == 10:
                root.leftClick(1227, 342, 0.2)
                print('Выбранна 10 ячейка на поле с минам')
            elif rand == 11:
                root.leftClick(890, 428, 0.2)
                print('Выбранна 11 ячейка на поле с минам')
            elif rand == 12:
                root.leftClick(975, 428, 0.2)
                print('Выбранна 12 ячейка на поле с минам')
            elif rand == 13:
                root.leftClick(1060, 428, 0.2)
                print('Выбранна 13 ячейка на поле с минам')
            elif rand == 14:
                root.leftClick(1145, 428, 0.2)
                print('Выбранна 14 ячейка на поле с минам')
            elif rand == 15:
                root.leftClick(1227, 428, 0.2)
                print('Выбранна 15 ячейка на поле с минам')
            elif rand == 16:
                root.leftClick(890, 514, 0.2)
                print('Выбранна 16 ячейка на поле с минам')
            elif rand == 17:
                root.leftClick(975, 514, 0.2)
                print('Выбранна 17 ячейка на поле с минам')
            elif rand == 18:
                root.leftClick(1060, 514, 0.2)
                print('Выбранна 18 ячейка на поле с минам')
            elif rand == 19:
                root.leftClick(1145, 514, 0.2)
                print('Выбранна 19 ячейка на поле с минам')
            elif rand == 20:
                root.leftClick(1227, 514, 0.2)
                print('Выбранна 20 ячейка на поле с минам')
            elif rand == 21:
                root.leftClick(890, 597, 0.2)
                print('Выбранна 21 ячейка на поле с минам')
            elif rand == 22:
                root.leftClick(975, 597, 0.2)
                print('Выбранна 22 ячейка на поле с минам')
            elif rand == 23:
                root.leftClick(1060, 597, 0.2)
                print('Выбранна 23 ячейка на поле с минам')
            elif rand == 24:
                root.leftClick(1145, 597, 0.2)
                print('Выбранна 24 ячейка на поле с минам')
            elif rand == 25:
                root.leftClick(1227, 597, 0.2)
                print('Выбранна 25 ячейка на поле с минам')
            root.leftClick(492, 507, 0.2)
            print('Кнопка \'Забрать выйгрыш\' нажата!')
            numplay += 1
            print(end='\n')
        print('__________________________________________________')
        print('         {==+==+==+==#Игра#==+==+==+==}')
        print('             --------|№', numplay, '|--------')
        print('__________________________________________________')
        print(end='\n')

    elif selection == 4:
        root.leftClick(890, 255, 0.2)
        print('Выбранна 1 ячейка на поле с минами')
        root.leftClick(975, 342, 0.2)
        print('Выбранна 7 ячейка на поле с минами')
        root.leftClick(1060, 255, 0.2)
        print('Выбранна 3 ячейка на поле с минами')
        root.leftClick(1145, 342, 0.2)
        print('Выбранна 9 ячейка на поле с минами')
        root.leftClick(1227, 255, 0.2)
        print('Выбранна 5 ячейка на поле с минами')
        root.leftClick(492, 507, 0.2)
        print('Кнопка \'Забрать выйгрыш\' нажата!')
        numplay += 1
        print(end='\n')
        print('__________________________________________________')
        print('         {==+==+==+==#Игра#==+==+==+==}')
        print('             --------|№', numplay, '|--------')
        print('__________________________________________________')
        print(end='\n')

    elif selection == 5:
        root.leftClick(1060, 428, 0.2)
        print('Выбранна 13 ячейка на поле с минами')
        root.leftClick(492, 507, 0.2)
        print('Кнопка \'Забрать выйгрыш\' нажата!')
        numplay += 1
        print(end='\n')
        print('__________________________________________________')
        print('         {==+==+==+==#Игра#==+==+==+==}')
        print('             --------|№', numplay, '|--------')
        print('__________________________________________________')
        print(end='\n')

    elif selection == 6:
        root.leftClick(975, 342, 0.2)
        print('Выбранна 7  ячейкана поле с минами')
        root.leftClick(1145, 342, 0.2)
        print('Выбранна 9  ячейкана поле с минами')
        root.leftClick(975, 514, 0.2)
        print('Выбранна 17 ячейка на поле с минами')
        root.leftClick(1145, 514, 0.2)
        print('Выбранна 19 ячейка на поле с минами')
        root.leftClick(492, 507, 0.2)
        print('Кнопка \'Забрать выйгрыш\' нажата!')
        numplay += 1
        print(end='\n')
        print('__________________________________________________')
        print('         {==+==+==+==#Игра#==+==+==+==}')
        print('             --------|№', numplay, '|--------')
        print('__________________________________________________')
        print(end='\n')

    elif selection == 7:
        root.leftClick(890, 255, 0.2) 
        print('Выбранна 1 ячейкана поле с минами')
        root.leftClick(1227, 255, 0.2)
        print('Выбранна 5 ячейкана поле с минами')
        root.leftClick(890, 597, 0.2) 
        print('Выбранна 21 ячейка на поле с минами')
        root.leftClick(1227, 597, 0.2)
        print('Выбранна 25 ячейка на поле с минами')
        root.leftClick(492, 507, 0.2)
        print('Кнопка \'Забрать выйгрыш\' нажата!')
        numplay += 1
        print(end='\n')
        print('__________________________________________________')
        print('         {==+==+==+==#Игра#==+==+==+==}')
        print('             --------|№', numplay, '|--------')
        print('__________________________________________________')
        print(end='\n')
