def inverter_string(s):
    string_invertida = ""  # Variável para armazenar a string invertida
    i = len(s) - 1  # Define o índice inicial como o último caractere da string
    while i >= 0:  # Continua o loop enquanto o índice for maior ou igual a 0
        string_invertida += s[i]  # Adiciona o caractere da posição 'i' à string invertida
        i -= 1  # Decrementa o índice para mover para o próximo caractere à esquerda
    return string_invertida  # Retorna a string invertida

string = input("Informe uma string: ")  # Solicita ao usuário que informe uma string
string_invertida = inverter_string(string)  # Chama a função para inverter a string
print("String invertida:", string_invertida)  # Exibe a string invertida
