#Dictionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Omar", "Apellido":"Medrano", "Edad":31, 1:"Python"}

my_dict = {
     "Nombre":"Omar",
     "Apellido":"Medrano",
     "Edad":31,
     "Lenguajes":{"Python", "Swift", "Kotlin"},
     1:1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

my_dict["Calle"] = "Medranuco"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Omar" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
#print(my_dict.fromkeys)