my_dict = {"Dmitriy": 1991, "Alex": 1996, "Roman": 1993}
print(my_dict)
print(my_dict["Roman"])
my_dict["Viktor"]=1992
print(my_dict["Viktor"])
my_dict.update({"Ksenia": 1998, "Anastasia": 1995})
print(my_dict)
a=my_dict.pop("Alex")
print(a)
print(my_dict)
my_set={1, 9, 19, 50, 50, 66, 77, 77, 99, True, "Tennis", "Rabota"}
print(my_set)
my_set.update({88, "Football"})
print(my_set)
my_set.remove(99)
print(my_set)