from fifoSimulador import FIFO
from tabulate import tabulate

def main():
    fifo = FIFO()
    numero_processos = int(input("Digite o número de processos: "))
    for i in range(numero_processos):
        nome = input(f"Digite o nome do processo {i+1}: ")
        tempo_chegada = int(input(f"Digite o tempo de chegada do processo {i+1}: "))
        duracao = int(input(f"Digite a duração do processo {i+1}: "))
        print("")
        fifo.adicionar_processo(nome, tempo_chegada, duracao)

    print("\nAntes da execução:")
    
    # Exibindo a fila em formato de tabela
    fila_lista = [[proc.nome, proc.tempo_chegada, proc.duracao] for proc in fifo.fila]
    print(tabulate(fila_lista, headers=["Nome", "Tempo de Chegada", "Duração"], tablefmt="fancy_grid"))
    
    print(" ")
    fifo.executar()

    print("\nApós a execução:")
    relatorio = fifo.gerar_relatorio()

    # Calculando os tempos médios
    tempo_medio_espera, tempo_medio_turnaround = fifo.calcular_tempos_medios()

    # Exibindo o relatório final
    print(tabulate(relatorio, headers=["Nome", "Tempo de Chegada", "Duração", "Tempo de Espera", "Tempo de Fim"], tablefmt="fancy_grid"))

    # Exibindo os tempos médios em uma nova tabela
    print("\nTempos Médios:")
    tempos_medios = [["Tempo Médio de Espera", f"{tempo_medio_espera:.2f}"],
                     ["Tempo Médio de Turnaround", f"{tempo_medio_turnaround:.2f}"]]
    print(tabulate(tempos_medios, headers=["Descrição", "Valor"], tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()