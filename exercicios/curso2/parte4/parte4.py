# DESAFIO 1.1
class Livro:
    livros = []                                          # DESAFIO 4.1.2
    # DESAFIO 1.2
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        self.__class__.livros.append(self)               # DESAFIO 4.1.3

    # DESAFIO 2.1
    def __str__(self):
        linha_superior = '______________________________________________________\n'
        linha_inferior = '\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'
        mensagem_formatada = f'Título: {self._titulo}\nAutor: {self._autor}\nAno de publicação: {self._ano_publicacao}'
        return linha_superior + mensagem_formatada + linha_inferior
    
    # DESAFIO 3.1
    def emprestar(self):
        self._disponivel = False

    # DESAFIO 4.1.1
    @staticmethod
    def verificar_disponibilidade(ano):
        lista_de_livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return lista_de_livros_disponiveis


# DESAFIO 2.2
primeiro_livro = Livro('A volta dos que não foram', 'Marcelo Duarte', 2005)
segundo_livro = Livro('Pelado de mão no bolso', 'DE AGUIAR, Marcelo', 2024)
print(primeiro_livro)
print(segundo_livro)

# DESAFIO 3.2
terceiro_livro = Livro('Blablabla', 'Fulano', 1999)
terceiro_livro.emprestar()
disponibilidade = 'disponível' if terceiro_livro._disponivel else 'indisponível/alugado'
print(f'O livro {terceiro_livro._titulo} está {disponibilidade}')

# DESAFIO 4.1.4
for livro_disponivel in Livro.verificar_disponibilidade(2005):
    print(f'\n{livro_disponivel._titulo}')