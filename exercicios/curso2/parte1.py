class Restaurante:                          # 
    nome = ''                               # 
    categoria = ''                          # FOI
    ativo = False                           # FEITO
                                            # EM
restaurante_praca = Restaurante()           # AULA
restaurante_praca.nome = 'Gourmet'          #
restaurante_praca.categoria = 'Italiana'    #

restaurante_praca.categoria = 'Italiana' # parte1 - ex. 1
restaurante_praca.nome # parte1 - ex. 2
print(f'\no restaurante está ativo' if restaurante_praca.ativo else '\no restaurante está inativo') # parte1 - ex. 3
categoria = restaurante_praca.categoria # parte1 - ex. 4
restaurante_praca.nome = 'Bistrô' # parte1 - ex. 5

restaurante_pizza = Restaurante() # parte1 - ex. 6.1
restaurante_pizza.nome = 'Pizza Place' # parte1 - ex. 6.2
restaurante_pizza.categoria = 'Fast Food' # parte1 - ex. 6.3
if restaurante_pizza.categoria == 'Fast Food': pass # parte1 - ex. 7
restaurante_pizza.ativo = True # parte1 - ex. 8

print(f'\nNome do restaurante: {restaurante_praca.nome}\nCategoria do restaurante: {restaurante_praca.categoria}') # parte1 - ex. 9