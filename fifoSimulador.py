import time
from typing import List, Tuple
from processo import Processo
from fila import Fila

class FIFO:
    def __init__(self):
        self.fila = Fila()
        self.relatorio = []

    def adicionar_processo(self, nome: str, tempo_chegada: int, duracao: int):
        """ Adiciona um novo processo à fila """
        try:
            processo = Processo(nome, tempo_chegada, duracao)
            self.fila.enfileirar(processo)
        except ValueError as e:
            print(f"Erro ao adicionar processo: {e}")

    def modificar_processo(self, posicao: int, nome: str = None, tempo_chegada: int = None, duracao: int = None):
        """ Modifica um processo na fila na posição especificada """
        if posicao < 1 or posicao > len(self.fila):
            print("Posição inválida.")
            return

        processo = self.fila.elemento(posicao)

        if nome is not None:
            processo.nome = nome
        if tempo_chegada is not None:
            if tempo_chegada < 0:
                print("Tempo de chegada inválido.")
                return
            processo.tempo_chegada = tempo_chegada
        if duracao is not None:
            if duracao <= 0:
                print("Duração inválida.")
                return
            processo.duracao = duracao

    def gerar_processos_automaticos(self, num_processos: int, max_tempo_chegada: int, max_duracao: int):
        """ Gera processos automáticos com parâmetros ajustáveis """
        import random
        for i in range(num_processos):
            nome = f'Processo_{i+1}'
            tempo_chegada = random.randint(0, max_tempo_chegada)
            duracao = random.randint(1, max_duracao)
            self.adicionar_processo(nome, tempo_chegada, duracao)

    def executar(self):
        """ Executa os processos em ordem FIFO e gera um relatório """
        tempo_atual = 0
        processos_ordenados = sorted([self.fila.desenfileirar() for _ in range(len(self.fila))], key=lambda p: p.tempo_chegada)
        
        for processo in processos_ordenados:
            if tempo_atual < processo.tempo_chegada:
                tempo_atual = processo.tempo_chegada

            tempo_espera = tempo_atual - processo.tempo_chegada
            tempo_fim = tempo_atual + processo.duracao
            self.relatorio.append((processo.nome, processo.tempo_chegada, processo.duracao, tempo_espera, tempo_fim))

            print(f'>> Executando {processo.nome} [Duração: {processo.duracao}s | Chegada: {processo.tempo_chegada}s] - Tempo Atual: {tempo_atual}s')

            tempo_atual = tempo_fim

            time.sleep(1)

    def calcular_tempos_medios(self) -> Tuple[float, float]:
        """ Calcula e retorna os tempos médios de espera e de turnaround """
        total_espera = sum(item[3] for item in self.relatorio)  # Tempo de espera
        total_turnaround = sum(item[4] - item[1] for item in self.relatorio)  # Tempo de fim - tempo de chegada
        num_processos = len(self.relatorio)

        tempo_medio_espera = total_espera / num_processos if num_processos > 0 else 0
        tempo_medio_turnaround = total_turnaround / num_processos if num_processos > 0 else 0

        return tempo_medio_espera, tempo_medio_turnaround

    def gerar_relatorio(self) -> List[Tuple[str, int, int, int, int]]:
        """ Gera um relatório com os detalhes dos processos """
        return self.relatorio