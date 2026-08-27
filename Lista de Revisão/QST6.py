contatos = [
    {"nome": "Pedro Henrique", "telefone": "82999999", "email": "pedrolegal@mail.com"},
    {"nome": "Roger Leôncio", "telefone": "82456781", "email": "roger@mail.com"},
    {"nome": "Miro de Castro", "telefone": "82679010", "email": "mirinho@mail.com"}
]

busca = input("Digite o nome do contato que deseja buscar: ")

encontrado = False

for contato in contatos:
    if busca.lower() in contato["nome"].lower():
        print("Contato encontrado!")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")
        econtrado = True
if not encontrado:
    print("O nome que busca não esta na lista de contatos!")    
