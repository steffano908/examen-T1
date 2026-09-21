import random

listaPokemon = []

def crearEntrenador(tupla, nombre, pokemon):
    ataque = random.randint(150, 250)
    vida = random.randint(500, 900)
    tupla.append((nombre, pokemon, ataque, vida))
    print(f'Entrenador {nombre} con {pokemon} agregado')


def ordenBurbuja(lis):
    for i in range(1, len(lis)):
        for j in range(len(lis) - 1):
            if lis[j][2] > lis[j + 1][2]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis


def listaEntrenador(tupla):
    print('\n--- LISTA DE ENTRENADORES ---')
    if len(tupla) == 0:
        print('No hay entrenadores')
        return
    ordenBurbuja(tupla)
    num = 1
    for x in tupla:
        print(f'{num}. {x[0]} | {x[1]} | Ataque: {x[2]} | Vida: {x[3]}')
        num = num + 1
    print()


def ordenSeleccion(lis):
    n = len(lis)
    for manoIzq in range(n):
        ind_min_val = manoIzq
        for vista in range(manoIzq, n):
            if lis[vista][3] < lis[ind_min_val][3]:
                ind_min_val = vista
        aux = lis[manoIzq]
        lis[manoIzq] = lis[ind_min_val]
        lis[ind_min_val] = aux
    return lis


def busquedabinaria(array, vida):
    menor = 0
    mayor = len(array)
    pos = None
    while menor < mayor:
        medio = (menor + mayor) // 2
        if array[medio][3] == vida:
            pos = medio
            break
        elif array[medio][3] < vida:
            menor = medio
            p = 1
            menor = menor + p
        else:
            mayor = medio
    return pos


def borraPorPokemon(tupla, vida):
    if len(tupla) == 0:
        print('No hay entrenadores')
        return
    ordenSeleccion(tupla)
    print('Lista ordenada por vida')
    pos = busquedabinaria(tupla, vida)
    if pos is None:
        print('No se encontro pokemon con esa vida')
        return
    eliminado = tupla.pop(pos)
    print('Se elimino:', eliminado)


def peleaPokemon(lista, n1, n2):
    if len(lista) < 2:
        print('Se necesitan al menos 2 pokemones')
        return
    p1 = None
    p2 = None
    num = 1
    for x in lista:
        if num == n1:
            p1 = x
        if num == n2:
            p2 = x
        num = num + 1
    if p1 is None or p2 is None:
        print('El numero es incorrecto')
        return
    factor1 = random.randint(0, 5)
    factor2 = random.randint(0, 5)
    daño1 = p1[2] * factor1
    daño2 = p2[2] * factor2
    vida1 = p1[3] - daño2
    vida2 = p2[3] - daño1
    print(f'{p1[0]} ({p1[1]}) hace {daño1} de daño')
    print(f'{p2[0]} ({p2[1]}) hace {daño2} de daño')
    if vida1 > vida2:
        print(f'Ganador: {p1[0]} con {p1[1]}')
        if p2 in lista:
            lista.remove(p2)
    elif vida2 > vida1:
        print(f'Ganador: {p2[0]} con {p2[1]}')
        if p1 in lista:
            lista.remove(p1)
    else:
        print('Empate, ambos pierden')
        if p1 in lista:
            lista.remove(p1)
        if p2 in lista:
            lista.remove(p2)
    print()


opc = ''
while opc != '5':
    print('========= MENU =========')
    print('1. Crear Entrenador')
    print('2. Listar Entrenadores')
    print('3. Borrar por Pokemon')
    print('4. Pelea Pokemon')
    print('5. Fin')
    opc = input('Seleccione una opcion: ')

    if opc == '1':
        print('CREAR ENTRENADOR')
        nombre = input('Ingrese nombre del entrenador: ')
        pokemon = input('Ingrese nombre del pokemon: ')
        crearEntrenador(listaPokemon, nombre, pokemon)
    elif opc == '2':
        listaEntrenador(listaPokemon)
    elif opc == '3':
        print('BORRAR POR POKEMON')
        vida = int(input('Ingrese vida a buscar: '))
        borraPorPokemon(listaPokemon, vida)
    elif opc == '4':
        print('PELEA POKEMON')
        listaEntrenador(listaPokemon)
        n1 = int(input('Ingrese numero del primer pokemon: '))
        n2 = int(input('Ingrese numero del segundo pokemon: '))
        peleaPokemon(listaPokemon, n1, n2)
    elif opc == '5':
        print('Saliendo del programa...')
    else:
        print('Opcion invalida')