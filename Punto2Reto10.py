def producto_punto(lista1, lista2):
    # Se revisa que las listas tengan el mismo tamaño
    if len(lista1) != len(lista2):  
        return 0
    # Se inicializa el valor del producto punto en 0
    producto_punto = 0  
    # Se itera sobre las dos listas al mismo tiempo
    for i in range(len(lista1)):  
         # Se calcula el producto de los elementos de las dos listas y se suman
        producto_punto += lista1[i] * lista2[i] 
    return producto_punto


if __name__ == "__main__":
    # Se crea una lista vacía
    lista1 = []  
    #Se crea una lista vacía
    lista2 = []  
    # Pide el tamaño que va a tener los vectores
    n = int(input("Ingrese el tamaño de las listas: "))  
    # Ingresa todos los valores que van a estar dentro del vector1
    for i in range(n):  
        valor = float(input("Valores de la lista 1: "))
        # Se agrega cada valor a la lista 1
        lista1.append(valor)  
    # Ingresa todos los valores que van a estar dentro del vector2
    for j in range(n):  
        valor = float(input("Valores de la lista 2: "))
        # Se agrega cada valor a la lista 2
        lista2.append(valor) 
    # Se llama a la función producto punto 
    producto_punto_listas = producto_punto(lista1, lista2)  
    print(lista1)
    print(lista2)
     # Se imprime el producto punto entre los dos vectores
    print("El producto punto de los vectores 1 y 2 es:", producto_punto_listas) 
