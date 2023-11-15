#tuples

my_tuple = tuple()
my_other_tuple = (35, 60, 30)


my_tuple = (41, 1.77, "Medrano", "Omar", "Medrano")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

#print(my_tuple[-6]) #Index error

print(my_tuple)
print(my_tuple.count("Medrano"))
print(my_tuple.index("Omar"))
print(my_tuple.index("Medrano"))

#tuples son valores inmutables, es decir valores fijo y no se pueden actualizar

#my_tuple[1] = 1.80 #tuple object does not support item assignment
print(my_tuple)

print(my_tuple + my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Medranuco"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

