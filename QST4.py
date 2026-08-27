opcao = 0
while opcao != 3:
    print("Escolha uma das opções abaixo: ")  
    print("[1] Converter Celsius para Fahrenheit")
    print("[2] Converter Fahrenheit para Celsius")
    print("[3] Sair")
    opcao = int(input("Sua opção: "))
    match (opcao):
        case 1:
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = (celsius*9/5) + 32
            print(f"{celsius:.2f} graus em Celsius é igual a {fahrenheit:.2f} graus em Fahrenheit")
        case 2:
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit:.2f} graus em Fahrenheit é igual a {celsius:.2f} graus em Celsius")
        case 3:
            print("Saindo...")
            break    
        case _:
            print("Opção inválida! Tente novamente!")
    
