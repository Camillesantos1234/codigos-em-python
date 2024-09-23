sp = 67836.43# Valor de SP
rj = 36678.66# Valor de RJ
mg = 29229.88# Valor de MG
es = 27165.48# Valor de ES
outros = 19849.53# Valor de outros estados
total = sp + rj + mg + es + outros# Soma o valor total

print("SP: {:.2f}%".format((sp / total) * 100))# Exibe a porcentagem de SP
print("RJ: {:.2f}%".format((rj / total) * 100))# Exibe a porcentagem de RJ
print("MG: {:.2f}%".format((mg / total) * 100))# Exibe a porcentagem de MG
print("ES: {:.2f}%".format((es / total) * 100))# Exibe a porcentagem de ES
print("Outros: {:.2f}%".format((outros / total) * 100))# Exibe a porcentagem de outros estados
