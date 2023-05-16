def calcular_promedio():
    n = int(input("Ingrese el número de valores que desea en el arreglo: "))
    arreglo = []
    suma = 0

    for i in range(n):
        numero = float(input("Ingrese el elemento: "))
        arreglo.append(numero)
        suma += numero

    promedio = suma / n
    return promedio

if __name__ == "__main__":
    promedio_arreglo = calcular_promedio()
    print("El promedio del arreglo es:", promedio_arreglo)
