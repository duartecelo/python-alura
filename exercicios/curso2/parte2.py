# EXERCÍCIO 1 ----------------------------------------
class Carro:
    modelo = ''
    cor = ''
    ano = int

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
carro1 = Carro('Chevrolet Agile LTZ', 'Preto', '2015')

# EXERCÍCIO 2 ----------------------------------------
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    nota = int
    quantidade_funcionarios = int
    # EXERCÍCIO 3 ---------------------------------------#
    def __init__(self, nome, categoria):                 #
        self.nome = nome                                 #
        self.categoria = categoria                       #

    # EXERCÍCIO 4 ------------------------------------------------#
    def __str__(self):                                            #
        return f'Nome: {self.nome}\nCategoria: {self.categoria}'  #

restaurante1 = Restaurante('Abelhas da Maçã', 'Geral', 4.95, 3837)

#EXERCÍCIO 5
class Cliente:
    nome = ''
    cpf = ''
    idade = int
    telefone = int

    def __init__(self, nome, cpf, idade, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.telefone = telefone

cliente1 = Cliente('Marcelo', '00011122233', 18, 51987654321)
cliente2 = Cliente('Ciro', '33322211100', 38, 51912345678)
cliente3 = Cliente('Bernardo', '12312312312', 15, 51911112222)