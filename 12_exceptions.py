#### Exception Handling#####

numberOne = 5
numberTwo = 1
numberTwo = "5"

print(numberOne + numberTwo)

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")

else:  #opcional # se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")

finally: #opcional #se ejecuta siempre
    print("La ejecucion continua")


#Exceptiones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except TypeError:
    print("Se ha producido un error")
except ValueError:
    print("Se ha producido un error")


#Captura de la informacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
