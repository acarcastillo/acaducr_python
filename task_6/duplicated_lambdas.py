
# Funcion que elimina los duplicados y recibe una lista
def delete_duplicated(lista):
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista

def call_delete_duplicated():
    lista_sin_repetidos= delete_duplicated([3, 5, 1, 3, 7, 9, 2, 5, 3, 1])
    lista_sin_repetidos.sort()
    print(f"La lista original sin elementos repetidos es: {lista_sin_repetidos}")

call_delete_duplicated()

#MISMO EJEMPLO ANTERIOR PERO USANDO LAMBDAS:
delete_duplicated = lambda lista: sorted(list(set(lista)))
call_delete_duplicated = lambda: print(f"La lista original sin elementos repetidos es: {', '.join(map(str, delete_duplicated([3, 5, 1, 3, 7, 9, 2, 5, 3, 1])))}")
call_delete_duplicated()

