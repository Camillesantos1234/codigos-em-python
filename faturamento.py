faturamento = [  #define uma lista de faturamento diario
    22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0,
    42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838,
    2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667,
    18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221,
    13220.495, 8414.61
]

dias_com_faturamento = [f for f in faturamento if f > 0]# Cria uma lista com os dias que tiveram faturamento
menor_valor = min(dias_com_faturamento)# Calcula o menor valor de faturamento
maior_valor = max(dias_com_faturamento)# Calcula o maior valor de faturamento
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento) # Calcula a média dos dias com faturamento
dias_acima_da_media = sum(1 for f in faturamento if f > media_mensal)# Conta quantos dias tiveram faturamento acima da média

print("Menor valor de faturamento:", menor_valor) # Exibe o menor valor de faturamento
print("Maior valor de faturamento:", maior_valor) # Exibe o maior valor de faturamento
print("Número de dias com faturamento acima da média:", dias_acima_da_media)# Exibe quantos dias o faturamento foi maior que a média

