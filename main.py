from funciones import *

bandera = True

#lista_hardcodeada =  [
#    [1222, "fede", 19, "tos", 7],
#    [1322, "abril", 19, "tos", 4],
#    [1242, "agos", 24, "tos", 1],
#    [1225, "horacio", 57, "tos", 9],
#    [1111, "caro", 15, "tos", 8]
#]

lista_pacientes = []

while bandera:

    menu_input = menu()

    match menu_input:
        case 1:
            lista_pacientes = cargar_pacientes()
        case 2:
            printear_matriz(lista_pacientes)
        case 3:
            buscado = buscar_pacientes_num_hist_clinica(lista_pacientes)
            print(buscado)
        case 4:
            ordenamiento_opcion_4= ordenar_pacientes(lista_pacientes, orden = 1)
            printear_matriz(ordenamiento_opcion_4)
        case 5:
            maximus = max_dias_internado(lista_pacientes)
            print(maximus)
        case 6:
            minimus = min_dias_internado(lista_pacientes)
            print(minimus)
        case 7:
            mas_cinco = mas_cinco_dias_internado(lista_pacientes)
            printear_matriz(mas_cinco)
        case 8:
            promedio = promedio_dias_internados_de_pacientes(lista_pacientes)
            print(promedio)
        case 9:
            print("saliendo del programa")
            break
        case _:
            continue

