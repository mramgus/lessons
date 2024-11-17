# Работа со словарями
my_dict={"Rasul":1977, "Kamila": 1980, "Zuhra": 1981, "Magomed": 1985}
print("Dict: ", my_dict)
print("Existing value:",my_dict["Rasul"])
print("Not existing value:", my_dict.get("Anton"))
del my_dict ["Zuhra"]
my_dict.update({"Denis":1977, "Max":1969})
print("Modified dictionary: ",my_dict)
# Работа с множествами
my_set={1,2,1,4,"Яблоко",13.2, "Яблоко"}
print("Set: ",my_set)
my_set.update({"Груша",(1,2,3.4)})
print(my_set.discard(1))
print("Modified set: ",my_set)