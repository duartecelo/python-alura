# DESAFIO 5
from parte4 import Livro

# DESAFIO 6
quarto_livro = Livro('Um Monte de Abobrinha', 'Ciclano', 2000)
quarto_livro.emprestar()
quarto_livro._disponivel
disponibilidade = 'disponível' if quarto_livro._disponivel else 'indisponível/alugado'
print()
print(f'O livro {quarto_livro._titulo} está {disponibilidade}')

# DESAFIO 7
for livro_disponivel in Livro.verificar_disponibilidade(2005):
    print(f'\n{livro_disponivel._titulo}')
print()