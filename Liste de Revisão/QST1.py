num = int(input("Digite um número: "))
print(f"Números pares até {num}:")
for c in range(1, num):
    if c % 2 == 0:
        print(c, end=' ')
print(f"\nNúmeros impares até {num}:")
for c in range(1, num):
    if c % 2 == 1:
        print(c, end=' ')
