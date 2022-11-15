# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
import re
s = '-1+3*5-(3-2)+(2*4)-4/2+1' 


print(s)

def Calcus(s):
    s = re.split('', s)  # разбираем все на элементы массива
    pos = []
    neg = []
    index_par = []
    i_start = None
    i_finish = None


    def parenthesis():
        i_start = None
        i_finish = None
        for i in range(len(s)):
            if s[i] == '(':
                i_start = i + 1
                index_par.append(i_start)
            if s[i] == ')':
                i_finish = i
                index_par.append(i_finish)
                for i in range(i_start, i_finish - 1):  # cначала идем по умножению и делению
                    if s[i] == '*':
                        if s[i - 3] == '-':
                            neg.append(int(s[i - 1]) * int(s[i + 1]))  # Убираем в отрицательный
                        else:
                            pos.append(int(s[i - 1]) * int(s[i + 1]))  # Добавляем в позитивные

                for i in range(i_start, i_finish - 1):
                    if s[i] == '/':
                        if s[i - 3] == '-':
                            if s[i - 2] == '-':
                                pos.append(int(s[i - 1]) // int(s[i + 1]))  # Убираем в отрицательные
                            else:
                                neg.append(int(s[i - 1]) // int(s[i + 1]))  # Добавляем в позитивные

                sum = 0
                for i in range(i_start, i_finish):    # Сложение и вычитание       -(3-2)
                    if s[i].isdigit() and s[i - 1] != '*' and s[i - 1] != '/' and s[i + 1] != '*' and s[i + 1] != '/':
                        if s[i - 1] == '-':
                            sum -= int(s[i])
                        else:
                            sum += int(s[i])
                if s[i_start - 2] == '-':
                    if sum > 0:
                        neg.append(sum)
                    else:
                        pos.append(abs(sum))
                else:
                    if sum < 0:
                        neg.append(abs(sum))
                    else:
                        pos.append(sum)

    parenthesis()
    index_par.append(len(s))
    if len(index_par) < 2:
        index_par.insert(0, 0)
        index_par.insert(0, 0)

    for i in range(len(index_par)):
        if i == 0:
            i_start = 0
            i_finish = index_par[i]
        else:
            if i % 2 == 0:
                i_start = index_par[i - 1]
                i_finish = index_par[i]
            for i in range(i_start, i_finish - 1):  # cначала идем по умножению и делению
                if s[i] == '*':
                    if s[i - 2] == '-':
                        neg.append(int(s[i - 1]) * int(s[i + 1]))  # Убираем в отрицательный
                    else:
                        pos.append(int(s[i - 1]) * int(s[i + 1]))  # Добавляем в позитивные

            for i in range(i_start, i_finish - 1):
                if s[i] == '/':
                    if s[i - 2] == '-':
                        neg.append(int(s[i - 1]) // int(s[i + 1]))  # Убираем в отрицательные
                    else:
                        pos.append(int(s[i - 1]) // int(s[i + 1]))  # Добавляем в позитивные

            for i in range(i_start, i_finish - 1):  # Сложение и вычитание
                if s[i].isdigit() and s[i - 1] != '*' and s[i - 1] != '/' and s[i + 1] != '*' and s[i + 1] != '/':
                    if s[i - 1] == '-':
                        neg.append(int(s[i]))
                    else:
                        pos.append(int(s[i]))
            if s[i_finish - 1].isdigit() and s[i_finish - 1 - 1] != '*' and s[len(s) - 1 - 1] != '/':
                if s[i_finish - 1 - 1] == '-':
                    neg.append(int(s[i_finish - 1]))
                else:
                    pos.append(int(s[i_finish - 1]))


    return sum(pos) - sum(neg)  # возвращает результат вычислений


print(Calcus(s))
