# Пункты задачи:
# 1. Создать переменную calls = 0 вне функций.
# 2. Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных
# двух функциях.
# 3. Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# 4. Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# 5. Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# 6. Вывести значение переменной calls на экран(в консоль).


calls = 0  # 1


def count_calls():  # 2
    global calls
    calls += 1


def string_info(string):  # 3
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result


def is_contains(string, list_to_search):  # 4
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
