class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = Carrinho()
    
    def adicionar_ao_carrinho(self, produto):
        self.carrinho.adicionar_produto(produto)
    
    def ver_total_compra(self):
        return self.carrinho.calcular_total()
    
# =========================
# TESTE DO SISTEMA
# =========================

# Criando produtos
produto1 = Produto("Notebook", 2500.00)
produto2 = Produto("Mouse", 50.00)
produto3 = Produto("Teclado", 120.00)

# Criando cliente
cliente = Cliente("João Silva")

# Adicionando produtos ao carrinho
cliente.adicionar_ao_carrinho(produto1)
cliente.adicionar_ao_carrinho(produto2)
cliente.adicionar_ao_carrinho(produto3)

# Calculando total
total = cliente.ver_total_compra()
print(f"Total da compra: R$ {total:.2f}")  # Total da compra: R$ 2670.00

