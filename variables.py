#Variables
my_variable="My String variable"
print(my_variable)
my_int_variable=5
print(my_int_variable)

my_boolean_variable=True
print(my_boolean_variable)

#Algunas funciones del sistema
print(len(my_variable))


#Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Ángel", "Rodríguez", "angelrgo", 50
print("Me llamo:",name, surname, ". Mi edad es:",age, ". Y mi alias: ",alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))
