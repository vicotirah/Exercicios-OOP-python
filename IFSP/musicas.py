
class Musica:

    musicas = []

    def __init__(self, nome, artista, duracao):
        self._nome = nome.title()
        self._artista = artista
        self._duracao = int(duracao)  
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self._nome} | {self._artista} | {self._duracao}'
    
    @classmethod
    def listar_musicas(cls):
        print(f"{'Nome da Música'.ljust(25)} | {'Artista'.ljust(25)} | Duração")

        for musica in cls.musicas:
            print(f'{musica._nome.ljust(25)} | {musica._artista.ljust(25)} | {musica._duracao}')


musica1 = Musica('Bohemian Rhapsody', 'Queen', 355)
musica2 = Musica('Imagine', 'John Lennon', 183)
musica3 = Musica('Shape of You', 'Ed Sheeran', 234)

Musica.listar_musicas()