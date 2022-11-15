from random import randint
import time

listS = [['-' for j in range(3)] for i in range(3)]


def PrintGame():
    for i in range(3):
        print("  ".join(listS[i]))
    print('')
PrintGame()

print('Начинается увлекательная игра Нолики-Крестики. Приготовьтесь! ')
print('Вводите поочередно координты позиции(номер строки и столбца), в которую Вы хотите поставить крестик.')
print()
time.sleep(1)

def EndGame():
    count = 0
    for i in range(3):
        for j in range(3):
            if listS[i][j] == '-':
                count += 1
    if count == 0:
        return False

def Check_Winner():
    check = 0
    for i in range(3):
        sum = ''
        for j in range(3):
            sum += listS[i][j]
        if sum == 'XXX':
            print('Игрок победил по строкам!')
            check = 1
            break
        elif sum == '000':
            print('Компьютер победил по строкам!')
            check = 1
            break
        else:
            sum = ''
            for j in range(3):
                sum += listS[j][i]
            if sum == 'XXX':
                print('Игрок победил по столбцам!')
                check = 1
                break
            elif sum == '000':
                print('Компьютер победил по столбцам!')
                check = 1
                break

    sum = ''
    for i in range(3):
        sum += listS[i][i]
        if sum == 'XXX':
            print('Игрок победил по диагонали 1!')
            check = 1
            break
        elif sum == '000':
            print('Компьютер победил по диагонали 1!')
            check = 1
            break

    sum = ''
    i = 0
    j = 2
    while j >= 0:
        sum += listS[i][j]
        j -= 1
        i += 1
        if sum == 'XXX':
            print('Игрок победил по диагонали 2!')
            check = 1
            break
        elif sum == '000':
            print('Компьютер победил по диагонали 2!')
            check = 1
            break
    if check == 1:
        return check


try:

    while True:
        i = randint(1, 3)
        j = randint(1, 3)
        time.sleep(1)
        while listS[i - 1][j - 1] != '-':
            i = randint(1, 3)
            j = randint(1, 3)
        else:
            listS[i - 1][j - 1] = '0'
        print('Ход искусственного интеллекта:')
        PrintGame()
        if Check_Winner() == 1:
            break

        EndGame()
        if EndGame() == False:
          print('Игра закончена Ничьей!')
          break

        i = int(input('Введите строку от 1 до 3 '))
        j = int(input('Введите столбец от 1 до 3 '))
        while listS[i - 1][j - 1] != '-':
            print('Это поле уже занято, введите новые координаты!')
            i = int(input('Введите строку от 1 до 3 '))
            j = int(input('Введите столбец от 1 до 3 '))
        else:
            listS[i - 1][j - 1] = 'X'
        print('Ваш ход:')
        PrintGame()
        if Check_Winner() == 1:
            break
except:
    print('Вы жульничаете! Начните игру снова!')