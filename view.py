import easygui

def exit(): # Выводит на экран сообщение о выходе
    easygui.msgbox(msg='До свидания!', title='Завершение работы с программой')

def get_numeric_expression(): # Запрашивает у пользователя ввод строки, убирает пробелы
    # global expression
    user_expression = easygui.enterbox(msg="Введите выражение", title='Блок пользователя')
    expression = user_expression.split()
    expression = ''.join(expression)
    return expression
