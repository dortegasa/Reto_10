lista1 = []
num = int(input("Ingrese la cantidad de números que tendrá su arreglo: "))

# Solicitar los números y añadirlos a la lista1
for i in range(num):
    real = int(input("Ingrese los números reales para su primer arreglo: "))
    lista1.append(real)


ceros = lista1.count(0)  # Contar la cantidad de ceros en la lista
new_lista = []

# Recorremos cada elemento en la lista1 y los añadimos a la nueva lista (new_lista) excepto los ceros
for elemento in lista1:
    if elemento != 0:
        new_lista.append(elemento)

# Añadimos los ceros al final de la nueva lista
for i in range(ceros):
    new_lista.append(0)

print("lista:", new_lista)
