print("Ввод в консоль 1 и 2:")
first=int(input('Введите первое число: '))
second=int(input('Введите второе число: '))
third=int(input('Введите третье число: '))
if first == second and first == third :
    print("Вывод на консоль 1:")
    print(3)
elif first == second or first == third or second == third:
    print('Вывод на консоль 2:')
    print(2)
else:
    print("Вывод на консоль 1:")
    print(0)

