
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.item_cardapio import ItemCardapio




#adição de restaurante na classe Restaurante
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

#adição de bebidas na classe Bebida
bebida_suco = Bebida('Suco de Melancia', 6.50, 'Grande')

#adição de pratos na classe Prato
prato_paozinho = Prato('Pãozinho', 2.50, 'O melhor pão da cidade')

#adição de item no cardápio
restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_paozinho)

#aplicando descontos
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()


'''restaurante_praca.receber_avaliacao('Gui', 3.8)
restaurante_praca.receber_avaliacao('Lais', 4.5)
restaurante_praca.receber_avaliacao('Emy', 2)
restaurante_mexicano.alterar_status()'''

def main ():


    restaurante_praca.exibir_cardapio()
    #Restaurante.listar_restaurantes()
    








if __name__ == '__main__':
    main()