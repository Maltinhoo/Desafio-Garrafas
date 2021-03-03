import os

galao = float(input("Litros do Galão:"))
quantidade = int(input("Quantidade de Garrafas: "))
garrafas = []
resposta = ""

for q in range(1, quantidade+1):
    cont = float(input(f"Litros da garrafa %i :" %q))
    garrafas.append(cont)