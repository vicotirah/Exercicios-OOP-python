
class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'

    @classmethod    
    def listar_restaurantes(cls):

        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Status")

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property  #Modifica como o atributo é lido
    def ativo(self):
        return '✔' if self._ativo else '✘'

    #def para objetos
    def alterar_status(self):
        self._ativo = not self._ativo

    
