def fibonacci(n):
    sequencia = [0, 1]  # Inicia a sequência com os primeiros dois números
    while sequencia[-1] < n:  # Continua até o último número da sequência ser maior ou igual ao número informado
        sequencia.append(sequencia[-1] + sequencia[-2])  # Adiciona o próximo número à sequência (soma dos dois anteriores)
    return sequencia  # Retorna a sequência gerada

def pertence_fibonacci(n):
    sequencia = fibonacci(n)  # Gera a sequência de Fibonacci até alcançar ou ultrapassar o número informado
    return n in sequencia  # Verifica se o número está na sequência gerada

# Solicita ao usuário que informe um número
numero = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
