class Processo:
    def __init__(self, nome: str, tempo_chegada: int, duracao: int):
        if tempo_chegada < 0 or duracao <= 0:
            raise ValueError("Tempo de chegada e duração devem ser positivos.")
        self.nome = nome
        self.tempo_chegada = tempo_chegada
        self.duracao = duracao

    def __str__(self) -> str:
        return f'{self.nome} (Chegada: {self.tempo_chegada}, Duração: {self.duracao})'