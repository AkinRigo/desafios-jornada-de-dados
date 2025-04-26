# Dada a lista ["maçã", "banana", "cereja"]e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65},
# calcule o preço total da lista de compras.

total = 0

frutas =["banana","maçã","cereja"]
valor = {"banana": 0.30,"maçã": 0.45,"cereja": 0.65}

def compras():
  global total
  for fruta in frutas:
    total+= valor[fruta]

compras()
print(total)    