#Lists

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [41, 35, 24, 62, 30, 30, 28]
print(my_list)
print(len(my_list))

my_other_list = [41, 1.77, "Omar", "Medrano"]
print(my_other_list)

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
#print(my_other_list[-5]) #Index Error
#print(my_other_list[4]) #Index Error

print(my_list.count(30))

age, height, name, surname = my_other_list
print(height)

print(my_list + my_other_list)


my_other_list.append("Medranuco")
print(my_other_list)

my_other_list.insert(0, "Rojo")
print(my_other_list)

my_other_list.remove("Rojo")
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop()
print(my_list)
print(my_list.pop(2))
print(my_list.pop())

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

my_newlist = my_list.copy()
del my_list[0]
print(my_list)

my_list.clear()
print(my_list)
print(my_newlist)

my_newlist.reverse()
print(my_newlist.reverse())

my_second_list = [15, 20, 30]
print(my_second_list)
my_second_list.sort()
print(my_second_list)
my_second_list.reverse()
print(my_second_list)

print(my_second_list[1:2])