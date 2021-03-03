import os

galao = float(input("Litros do Galão:"))
quantidade = int(input("Quantidade de Garrafas: "))
garrafas = []
resposta = ""

for q in range(1, quantidade+1):
    cont = float(input(f"Litros da garrafa %i :" %q))
    garrafas.append(cont)

garrafas.sort(reverse=True)
for garrafa in garrafas:
    if galao-garrafa >=0:
        galao = galao - garrafa
        resposta = resposta + f"%.2fL, " % garrafa

print(f"Usamos as garrafas de: %s" %resposta)
print(f"Sobrou: %2fL" %galao)