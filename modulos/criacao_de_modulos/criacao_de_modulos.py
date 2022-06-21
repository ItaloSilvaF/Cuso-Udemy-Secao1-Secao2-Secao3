"""
Criação de Modulos
"""


def dobra_lista(lista):
    return [valor * 2 for valor in lista]


def multiplica_itens_lista(lista):
    contador = 1
    for valor in lista:
        contador *= valor
    return contador


def adiciona_final_em_lista(lista):
    lista.append('Final')
    return lista


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(dobra_lista(lista))
    print(multiplica_itens_lista(lista))
    print(adiciona_final_em_lista(lista))
