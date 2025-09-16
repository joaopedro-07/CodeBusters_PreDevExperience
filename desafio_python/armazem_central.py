# João Gustavo, João Pedro e Gabriel Moreira

estoque_atual = {
     "canetas": 150,
     "cadernos": 95,
     "borrachas": 120,
     "apontadores": 100,
     "pastas": 70,
     "réguas": 85,
     "estojos": 90,
     "papéis A4": 200
}

movimentacoes_dia = [
     ("canetas", "Saída", 25),
     ("canetas", "Entrada", 5),
     ("cadernos", "Saída", 20),
     ("cadernos", "Entrada", 10),
     ("borrachas", "Saída", 5),
     ("borrachas", "Entrada", 10),
     ("apontadores", "Entrada", 20),
     ("apontadores", "Saída", 100),
     ("pastas", "Saída", 30),
     ("pastas", "Entrada", 5),
     ("réguas", "Saída", 40),
     ("réguas", "Entrada", 5),
     ("estojos", "Saída", 20),
     ("estojos", "Entrada", 25),
     ("papéis A4", "Saída", 50),
     ("papéis A4", "Entrada", 25),
]

print("Estoque atual:")
for produto, quantidade in estoque_atual.items():
    print(f"{quantidade} {produto}")

print("\nMovimentações:")
for produto, movimentacao, quantidade in movimentacoes_dia:
    print(f"{movimentacao} - {quantidade} {produto}")
    if produto in estoque_atual:
        if movimentacao == "Entrada":
          estoque_atual[produto] += quantidade
        elif movimentacao == "Saída":
          estoque_atual[produto] -= quantidade
    else:
       if movimentacao == "Entrada":
          estoque_atual[produto] = quantidade
       elif movimentacao == "Saída":
          pass
       
lista_reposicao = []

print("\nEstoque atualizado:")
for produto, quantidade in estoque_atual.items():
    print(f"{quantidade} {produto}")
    if quantidade <= 50:
      lista_reposicao.append(produto)

print("\nProdutos listados para reposição:")
for produto in lista_reposicao:
   print(produto.title())