######Loops #######

#While
'''''
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition +=2

else:  #Es opcional
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

my_condition = 10
while my_condition < 20:
    my_condition =+ 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break
    print(my_condition)

print("La ejecucion continua")
'''

#For

my_list = [41, 35, 24, 62, 30, 30, 28]

for element in my_list:
    print(element)



my_tuple = (41, 1.77, "Medrano", "Omar", "Medrano")
for element in my_tuple:
    print(element)

my_set = {"Omar", "Medrano", 41}
for element in my_set:
    print(element)


my_dict= {"Nombre":"Omar", "Apellido":"Medrano", "Edad":31, 1:"Python"}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")