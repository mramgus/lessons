immutable_var = (1,2, "apple", True, 2.5)
print("Immutable tuple: ",immutable_var)
print(type(immutable_var))
# immutable_var[0]=20    Здесь пробую изменить  элемент, на число 20, и при выводе кортеж на экран,
# выдает ошибку TypeError: 'tuple' object does not support item assignment. Это означает что картеж не подерживает обращение по элементам
mutable_list = [1,2,"a","b","Modified"]
print("Mutable list: ", mutable_list)
print(type(mutable_list))
mutable_list.append(True)
print("Mutable list: ", mutable_list)
mutable_list[1]=50 # меняем второй элемент на 50
print("Mutable list: ", mutable_list)
