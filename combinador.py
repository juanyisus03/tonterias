import time

def ordenar(array: list, numMax):
    arrayOrdenado = []
    palabras = []
    
    for i in range(numMax):
        for index in range(len(array) - 1, -1, -1):
            if len(array[index]) == i+1:
                palabras.append(array.pop(index))
        palabras.sort()
        arrayOrdenado.extend(palabras.copy())
        palabras.clear()
    
    return arrayOrdenado
        

def increase_array(arr, numMax):
    n = len(arr)
    i = n - 1  # Comenzar desde la última posición
    while i >= 0:
        arr[i] += 1  # Aumentar en 1 el valor en la posición actual
        if arr[i] == numMax:  # Si el valor es numMax, cambiarlo a 0 y mover a la siguiente posición
            arr[i] = 0
            i -= 1  # Mover a la siguiente posición
            if i < 0:  # Si la primera posición llega a 4, aumentar la longitud del array
                arr.insert(0, 0)  # Insertar un 0 al inicio del array
                break  # Detener el bucle
        else:
            break  # Si no es numMax, detener el bucle
    return arr

# Inicializar array con longitud 1
arr = [0]

# Array de caracteres
caracteres = list("1234567891")

# Conjunto para almacenar las combinaciones únicas
combinaciones_set = set()
timeStart = time.time()
# Incrementar el array hasta que su longitud sea la de los caracteres
while len(arr) <= len(caracteres):
    isValido = True
    for num in arr:
        if arr.count(num) > 1: #Comprueba que lo números no estén repetidos
            isValido = False
    if isValido:
        combinacion = ''.join(caracteres[i] for i in arr)
        combinaciones_set.add(combinacion)  # Agregar la combinación al conjunto de combinaciones únicasNo 
    increase_array(arr, len(caracteres)) # Incrementar el array
    

# Convertir el conjunto a lista para mantener el orden de inserción
combinaciones = ordenar(list(combinaciones_set), len(caracteres))


timeEnd = time.time()

timeTotal = timeEnd - timeStart

# Imprimir las combinaciones resultantes
print(combinaciones)
print("El programa tardó: " + "{:02d}:{:02d}".format(int(timeTotal) // 60, int(timeTotal) % 60))
