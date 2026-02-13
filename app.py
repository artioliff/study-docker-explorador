# Olá! Este é o nosso código Python. 
# Pense nele como uma receita de bolo que o computador vai ler e fazer.

import time  # Aqui estamos pegando um relógio emprestado para contar o tempo.

# Função: Uma função é como uma tarefa que damos um nome.
# Aqui, a tarefa é "fazer_contagem_regressiva".
def fazer_contagem_regressiva():
    print("🚀 Preparando para decolagem! 🚀")
    print("Atenção tripulação!")
    
    # Loop: Um loop é quando pedimos para o computador repetir algo.
    # "range(10, 0, -1)" significa: comece do 10, vá até o 1, diminuindo de 1 em 1.
    for numero in range(10, 0, -1):
        print(f"{numero}...")  # O computador "fala" o número.
        time.sleep(1)  # O computador espera 1 segundo antes de continuar (para dar suspense!).
    
    print("0! 🌌 DECOLAR! 🌌")
    print("Estamos viajando pelo espaço sideral do Docker! ✨")

# Aqui é onde o programa realmente começa.
# Se este arquivo for o principal (o chefe), ele manda executar a tarefa de contagem regressiva.
if __name__ == "__main__":
    fazer_contagem_regressiva()
