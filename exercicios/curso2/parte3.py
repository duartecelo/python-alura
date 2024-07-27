# MÃO NA MASSA
class Pessoa:
    nome = ''
    idade = int
    profissao = ''

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nProfissão: {self.profissao}\n'

    def aniversario(self):
        self.idade += 1

    @classmethod
    def saudacao(self):
        return f'Olá, sou {self.nome}, tenho {self.idade} anos e trabalho como {self.profissao}\n'

# DESAFIOS 1 - 7
class ContaBancaria:
    
    # 1
    def __init__(self, titular, saldo):
        self._titular = titular # 4.5
        self._saldo = saldo     # 4.6
        self._ativo = False     # 4.7

    # 2.1
    def __str__(self):
        return f'Titular: {self.titular}\nSaldo: {self.saldo}\n'
    
    # 3.1
    @classmethod
    def ativar_conta(cls):
        cls.ativo = True

    # 4.1
    @property
    def titular(self):
        return self._titular
    # 4.2
    @property
    def saldo(self):
        return self._saldo
    # 4.3
    @property
    def ativo(self):
        return self._ativo

# 2.2
ContaBancaria.ativar_conta()
conta1 = ContaBancaria('Marcelo', 650)
conta2 = ContaBancaria('Elon Musk', 300000000000)
print(conta1)
print(conta2)

# 3.2
conta3 = ContaBancaria('Random1', 303)
print(conta3.ativo)

# 5
conta4 = ContaBancaria('Random2', 101)
print(conta4.titular)

print()
print()

# 6
class ClienteBanco:
    lista_de_clientes = []
    def __init__(self, nome, cpf, telefone, endereco, numero_da_conta):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.numero_da_conta = numero_da_conta
        ClienteBanco.lista_de_clientes.append(nome)
    
    # 7
    @classmethod
    def listar_clientes(cls):
        i = 1
        for cliente in cls.lista_de_clientes:
            print(f'Cliente {i}: {cliente}')
            i += 1