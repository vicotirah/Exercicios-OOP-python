'''Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.'''
from bibliotecass.exercicios import Livro


'''No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.'''
livro1 = Livro('Torto Arado', 'Itamar vieira Junior', 2019)
livro2 = Livro('Cem anos de solidão', 'Gabriel García Márquez', 1967)
livro3 = Livro('O Alquimista', 'Paulo Coelho', 1988)
livro4 = Livro('1984', 'George Orwell', 1949)

livro2.emprestar()
Livro.listar_livros()

'''No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.'''


livro_disponivel_ano = Livro.verificar_disponibilidade(2019)
print(f"Livros disponíveis em 2019: \n{', '.join(str(livro) for livro in livro_disponivel_ano)}")

'''Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.'''


