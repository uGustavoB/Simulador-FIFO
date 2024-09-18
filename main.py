from fifoSimulador import FIFO

def main():
    fifo = FIFO()
    fifo.adicionar_processo('P1', 0, 3)
    fifo.adicionar_processo('P2', 2, 6)
    fifo.adicionar_processo('P3', 4, 4)

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