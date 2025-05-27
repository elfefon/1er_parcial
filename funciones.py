def menu() -> int:
    """
    Presentacion de menu.
    No ingresa nada, solo pide una opcion en forma de entero al usuario 
    y la retorna.
    """

    print("---Sistema de Gestion de Clinica--- \n" \
    "1. Cargar Pacientes \n" \
    "2. Mostrar todos los pacientes \n" \
    "3. Buscar pacientes por numero de historia clinica \n" \
    "4. Ordenar pacientes por numero de historia clinica \n" \
    "5. Mostrar paciente con mas dias d internacion \n" \
    "6. Mostrar paciente con menos dia d internacion \n" \
    "7. Cantidad de pacientes con mas de 5 dias de internacion \n" \
    "8. Promedio de dias de internacion de todos los pacientes \n" \
    "9. Salir \n"
    )

    opcion = input("Ingrese su opcion en numero:")

    while type(opcion) == str:

        if opcion.isdigit():  # validamos que sea numero
            opcion = int(opcion)

            if 1 <= opcion <= 9:
                return opcion  # retornamos la opcion elegida como int
            else:
                return None
        else:
            return None


def validacion_enteros(elemento:str) -> int:
    """
    ingresamos un elemento y nos fijamos si es un int.
    si lo es retornamos true, sino retornamos false
    """
    if elemento.isdigit():
        return True
    else:
        return False

def cargar_pacientes () -> list:
    """
    No ingresa nada. Solo retorna
    Pide cantidad de pacientes que desea ingresar el usuario, y pide los
    datos de estos, de uno en uno, y los agrega a una matriz.
    """
    
    cantidad = int(input("ingresa la cantidad de pacientes que desea agregar: "))
    contador = 0
    matriz_pacientes = []

    while contador < cantidad:
        
        num_historia_clinica = input("ingrese el numero de historia clinica: ")
        if validacion_enteros(num_historia_clinica):
            num_historia_clinica = int(num_historia_clinica)
        else:
            continue

        nombre_paciente = input("ingrese el nombre del paciente: ")

        edad_paciente = (input(f"ingrese la edad de {nombre_paciente}: "))
        if validacion_enteros(edad_paciente):
            edad_paciente = int(edad_paciente)
        else:
            continue

        diagnostico = input(f"ingrese el diagnostico de {nombre_paciente}: ")

        cantidad_dias_internacion = (input(f"ingrese cantidad de dias de internacion de {nombre_paciente}: "))
        if validacion_enteros(cantidad_dias_internacion):
            cantidad_dias_internacion = int(cantidad_dias_internacion)
        else:
            continue

        matriz_pacientes += [[num_historia_clinica, nombre_paciente, 
                            edad_paciente, diagnostico, cantidad_dias_internacion]
                            ]
        
        contador += 1

    return matriz_pacientes

def buscar_pacientes_num_hist_clinica(lista: list) -> list:
    """
    Ingresa una lista, y el usuario ingresa el numero de historial
    clinico de un paciente, y vamos comparando por indices este numero
    con la lista ingresada como parametro.
    retorna la lista con la informacion del paciente si es que encuentra,
    sino retorna que no encontro nada.
    """

    if lista == []:
        return print("Debe de ingresar una lista")

    num_hist_clinica = int(input("ingrese numero de historia clinica para buscar paciente: ")) 
    paciente_a_buscar = [num_hist_clinica]
    for i in range(len(lista)):
        for j in range(len(lista)):

            if lista[j][0] == paciente_a_buscar[0]:
                paciente_a_buscar = lista[j]
                return paciente_a_buscar

    return "no se encontro a ningun paciente con ese numero de historial medico."

def ordenar_pacientes (lista:list, orden: int) -> list:
    """
    ingresa una lista y el orden, el cual se compara y se
    reemplaza por un indice.
    hacemos un ordenamiento burbuja y ordenamos la lista
    dependiento del indice. 
    retornamos la lista ordenada.
    """

    if lista == []:
        return print("Debe de ingresar una lista")

    #orden por numero
    if orden == 1: 
        indice = 0
    #orden por edad (lei mal el enunciado y lo hice "generalizado")    
    elif orden == 2:
        indice = 2    
    #orden por dias internado (lei mal el enunciado y lo hice "generalizado") 
    elif orden == 3: 
        indice = 4


    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):

            if lista[j][indice] > lista[j + 1][indice]:

                aux = lista [j + 1] 
                lista [j + 1] = lista [j]
                lista[j] = aux

    return lista

def max_dias_internado(lista:list) -> list:
    """
    ingresa una lista, y buscamos su maximo en dias de internacion
    con un bucle for y retornamos el maximo.
    """
    if lista == []:
        return print("Debe de ingresar una lista")
    
    maximo = [0, "", 0, "", float("-inf")]

    for i in range(len(lista)):
        if lista[i][4] > maximo[4]:
            maximo = lista[i]

    return maximo

def min_dias_internado (lista: list) -> list:
    """
    ingresa una lista, y buscamos su minimo en dias de internacion
    con un bucle for y retornamos el minimo.
    """
    if lista == []:
        return print("Debe de ingresar una lista")
    
    minimo = [0, "", 0, "", float("inf")]

    for i in range(len(lista)):
        if lista[i][4] < minimo[4]:
            minimo = lista[i]

    return minimo

def mas_cinco_dias_internado(lista:list) -> list:
    """
    ingresa una lista, y buscamos los pacientes con mayor a 5 dias
    de internacion con un bucle for y retornamos la cantidad en manera
    de lista.
    """
    if lista == []:
        return print("Debe de ingresar una lista")
    
    maximo = [0, "", 0, "", 5]
    lista_creciente = []
    acumulador = 0

    for i in range(len(lista)):
        if lista[i][4] > maximo[4]:
            lista_creciente += [lista[i]]
            acumulador += 1

    return f"Son {acumulador} pacientes con mas de 5 dias",lista_creciente

def promedio_dias_internados_de_pacientes(lista:list) -> float:
    """
    ingresa una lista, y recorremos esta, y guardamos el numero
    de dias internados de los pacientes en un acumulador, y luego
    lo dividimos por la cantidad de pacientes recorridos, y por
    ultimo retornamos el porcentaje.
    """
    if lista == []:
        return print("Debe de ingresar una lista")
    
    acumulador = 0
    division = 0

    for i in range(len(lista)):
        acumulador += lista[i][4]
        division += 1

    return (acumulador / division)

def printear_matriz(lista:list) -> list:
    """
    ingresa una lista de lista y la retornamos como matriz
    """
    for i in range(len(lista)):
            print(lista[i])