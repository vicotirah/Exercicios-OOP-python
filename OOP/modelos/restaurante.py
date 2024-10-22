from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


class Restaurante:

    '''Representa um restaurante e suas características.'''

    restaurantes = []

    def __init__(self, nome, categoria):

        '''Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.'''
        
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []

        Restaurante.restaurantes.append(self)

    def __str__(self):

        '''Retorna uma representação em string do restaurante.'''

        return f'{self._nome} | {self._categoria} | {self._ativo}'

    @classmethod    
    def listar_restaurantes(cls):

        '''Exibe uma lista formatada de todos os restaurantes.'''

        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(15)} | Status")

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(15)} | {restaurante.ativo}')

    @property  #Modifica como o atributo é lido
    def ativo(self):

        '''Retorna um símbolo indicando o estado de atividade do restaurante.'''

        return '✔' if self._ativo else '✘'
    
    def receber_avaliacao(self, cliente, nota):

        '''Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).'''

        if 0 < nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property 
    def media_avaliacoes(self):

        '''Calcula e retorna a média das avaliações do restaurante.'''

        if not self._avaliacao:
            return 'Sem Avaliações'
        media_notas = round(sum(avaliacao._nota for avaliacao in self._avaliacao)/len(self._avaliacao), 1)
        return media_notas
    
    def adicionar_item_cardapio(self, item):

        '''Adiciona item no cardápio'''

        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

        ''' if isinstance(item, Prato):
            # Lógica para prato
                print(f'{item._nome} - R$ {item._preco:.2f} |  {item._descricao}')
            elif isinstance(item, Bebida):
            # Lógica para bebida
                print(f'{item._nome} - R$ {item._preco:.2f} |  {item._tamanho}')
            else:
                print('erro: item desconhecido')'''
            

    def exibir_cardapio(self):
        '''exibe o cardápio''' 

        print(f'\nCardápio do restaurante {self._nome}\n')

        for i,item in enumerate(self._cardapio, start=1):
            
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. {item._nome.ljust(20)} | R$ {item._preco:.2f} |  {item._descricao}'
                print(mensagem_prato)

            elif hasattr(item,'tamanho'):
                mensagem_bebida = f'{i}. {item._nome.ljust(20)} | R$ {item._preco:.2f} | {item._tamanho}'
                print(mensagem_bebida)




    #def para objetos
    def alterar_status(self):
        self._ativo = not self._ativo

    
