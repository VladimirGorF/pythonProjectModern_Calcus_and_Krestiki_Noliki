import easygui
import view
import Calcus_Simple

msg = 'Выберите действие'
title = 'Меню выбора дальнейшего действия'
options = ['Калькулятор', 'Выход из программы']
user_choice = easygui.buttonbox(msg, title, options)

while user_choice == options[0]:  ## функция запрашивает у пользователя выражение для решения на калькуляторе, сразу убирает пробел и возвращает переменную как строку
    example_expression = view.get_numeric_expression()
    print(example_expression)

    resault = Calcus_Simple.Calcus(example_expression)
    print(resault)

    msg = 'Пример: ' + str(example_expression) + 'Результат вычисления равен ' + str(resault)
    title = 'Меню выбора дальнейшего действия'
    options = ['Калькулятор', 'Выход из программы']
    user_choice = easygui.buttonbox(msg, title, options)



if user_choice == options[1]: ## функция вывода на экран ссообщения и выход из программы
    view.exit()
    quit()


