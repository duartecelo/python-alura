# EXERCÍCIO 1
lista_1a10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_4nomes = ['Marcelo', 'Cleiton', 'Clóvis', 'João']
lista_anos = [2005, 2024]

# EXERCÍCIO 2
lista_teste1 = ['a', 'b', 'c']
for item in lista_teste1:
    pass

# EXERCÍCIO 3
totalImpares = 0
for i in range(0, 10):
    if i % 2 != 0:
        totalImpares += i



# EXERCÍCIO 4
for i in range(10, 0, -1):
    print(i)

# EXERCÍCIO 5
numero_tabuada = int(input('Digite um número: '))
print(f'A tabuada de {numero_tabuada} é:')
for i in range(1, 11):
    print(f'{numero_tabuada} x {i} = {numero_tabuada * i}')

# EXERCÍCIO 6
try:
    total = 0
    for numero in lista_1a10:
        total += numero
    print(total)
except:
    print('Um ou mais dos elementos da lista não é um número')

# EXERCÍCIO 7
try:
    soma = 0
    lista = lista_1a10
    for numero in lista:
        soma += numero
    print(soma / len(lista))
except ZeroDivisionError:
    print('A lista não pode ser vazia')