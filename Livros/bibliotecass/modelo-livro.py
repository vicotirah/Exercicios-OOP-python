
'''Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.'''

class Livro:

    livros = []

    def __init__(self, titulo, autor, publicado):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._publicado = int(publicado)
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._publicado} | {self.disponivel}'

    '''Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.'''

    @classmethod
    def listar_livros(cls):
        print(f"{'Título'.ljust(25)} | {'Autor'.ljust(25)} | {'Publicação'.ljust(6)} | Status")
        for livro in cls.livros:
           print(f"{livro._titulo.ljust(25)} | {livro._autor.ljust(25)} | {str(livro._publicado).ljust(10)} | {livro.disponivel}") 

    '''Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.'''
    
    @property
    def disponivel(self):
        return 'Disponível' if self._disponivel else 'Indisponível'

    def emprestar(self):
        self._disponivel = not self._disponivel

    '''Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.'''

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._publicado == ano and livro._disponivel]
        return livros_disponiveis




'''Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.'''



