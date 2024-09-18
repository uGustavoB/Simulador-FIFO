from fifoSimulador import FIFO

def main():
    fifo = FIFO()
    # Adicionando processos manualmente
    numero_processos = int(input("Digite o número de processos: "))
    for i in range(numero_processos):
        nome = input(f"Digite o nome do processo {i+1}: ")
        tempo_chegada = int(input(f"Digite o tempo de chegada do processo {i+1}: "))
        duracao = int(input(f"Digite a duração do processo {i+1}: "))
        fifo.adicionar_processo(nome, tempo_chegada, duracao)

    print("\nAntes da execução:")
    print(fifo.fila)

    fifo.executar()

    print("\nApós a execução:")
    print(fifo.fila)

    print("\nRelatório de execução:")
    relatorio = fifo.gerar_relatorio()
    for item in relatorio:
        print(f'Processo: {item[0]}, Chegada: {item[1]}, Duração: {item[2]}, Tempo de Espera: {item[3]}, Tempo de Fim: {item[4]}')

if __name__ == "__main__":
   main()