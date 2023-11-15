######Functions#######

def my_function ():
    print("Esto es una funcion")

my_function ()
my_function ()
my_function ()


def sum_two_values (first_number: int, second_number: int):
    print(first_number + second_number)

sum_two_values (5 , 7)
sum_two_values (53434 , 74543545)
sum_two_values ("5", "7")
sum_two_values (1.4, 5.2)

def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value
my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")
print_name(surname= "Medrano", name= "Omar")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
print_name_with_default("Omar", "Medrano")
print_name_with_default("Omar", "Medrano", "Medranuco")


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "Medranuco")
print_upper_texts("Hola")