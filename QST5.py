produto = 0
listadeprodutos = [
    { 'nome': 'Requeijão', 'preco': '12R$' },
    
    { 'nome': 'Salame', 'preco': '15R$' }     
]

for produto in listadeprodutos:
    nome = produto['nome']
    preco = produto['preco']
    print(f"O preço do {nome} custa {preco}")
