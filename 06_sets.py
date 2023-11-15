#sets

my_set = set()
print(type(my_set))

my_other_set = {}
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Omar", "Medrano", 41}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Medranuco")
print(my_other_set)

#Un set no es una estructura organizada
#Cuando guardas datos lo hace de una manera desorganizada y no puedes repetir elementos
my_other_set.add("Medranuco")
print(my_other_set)  #Un set no admite repetidos

print("Omar" in my_other_set )
print("Omare" in my_other_set )

my_other_set.remove("Omar")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

my_set = {"Omar", "Medrano", 41}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#" }))

print(my_new_set.difference(my_set))