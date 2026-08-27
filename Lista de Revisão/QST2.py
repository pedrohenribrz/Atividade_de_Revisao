media = 0
for c in range(1, 4):
    nota = float(input("Digite as notas: "))
    media += nota
media /= 3
if media >= 7:
    print(f"Aprovado! sua média foi {media:.2f}")
if 4 <= media < 7:
    print(f"Reposição! sua média foi {media:.2f}")
if media < 4:
    print(f"Reprovado! sua média foi {media:.2f}")
