'''Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.'''
from livro import Livro
from main import *


'''No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.'''

Livro.emprestar(livro2)
Livro.listar_livros()

'''No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.'''

livro_disponivel_ano = Livro.verificar_disponibilidade(2019)
print(f"Livros disponíveis em 2019: \n{', '.join(str(livro) for livro in livro_disponivel_ano)}")



