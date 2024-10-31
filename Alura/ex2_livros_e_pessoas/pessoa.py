#Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão e adicione um método especial __str__ para imprimir uma representação em string da pessoa.

class Pessoa:

    pessoas =[]

    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._idade} | {self._profissao} '
    
    def aniversario(self, niver=1): # Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
        self._idade += niver
        return f'Parabéns pelos seus {self._idade} anos!'
    
    @property # Adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
    def saudacao(self):
        return f'Bem vindo(a) {self._profissao}!'

       
    


