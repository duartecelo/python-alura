# EXERCÍCIO 1
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O número digitado é par')
else:
    print('O número digitado é ímpar')

# EXERCÍCIO 2
idade = int(input('Digite sua idade: '))
if 0 <= idade <= 12:
    print('Você é uma crinça')
elif 13 <= idade <= 18:
    print('Você é um adolescente')
else:
    print('Você é um adulto')

# EXERCÍCIO 3
nickname = input('Digite o nome de usuário: ')
password = input('Digite a senha: ')
if nickname == 'cleitinho' and password == '12345678':
    print('Login efetuado com sucesso')
else:
    print('Nome de usuário e/ou senha incorretos')

# EXERCÍCIO 4
coordX = int(input('Digite a coordenada X: '))
coordY = int(input('Digite a coordenada Y: '))
if coordX == 0 and coordY == 0:
    print('O ponto está sobre a origem do plano cartesiano')
elif coordX == 0:
    print('O ponto está sobre o eixo Y do plano cartesiano')
elif coordY == 0:
    print('O ponto está sobre o eixo X do plano cartesiano')
elif coordX > 0 and coordY > 0:
    print('O ponto está no 1° quadrante do plano cartesiano')
elif coordY > 0:
    print('O ponto está no 2° quadrante do plano cartesiano')
elif coordX < 0 and coordY < 0:
    print('O ponto está no 3° quadrante do plano cartesiano')
elif coordX > 0:
    print('O ponto está no 4° quadrante do plano cartesiano')
