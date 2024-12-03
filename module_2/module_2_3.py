my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i_elem = 0
print('Вывод на консоль: ')
while i_elem < len(my_list):
    elem = my_list[i_elem]
    i_elem +=1
    if elem == 0:
        continue
    elif elem < 0:
        break
    else:
        print(elem)
