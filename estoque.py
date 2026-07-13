class Estoque:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def buscar_produto(self, nome):

        for produto in self.produtos:

            if produto.nome.lower() == nome.lower():

                return produto

        return None

    def remover_produto(self, nome):

        produto = self.buscar_produto(nome)

        if produto:

            self.produtos.remove(produto)

            return True

        return False

    def alterar_quantidade(self, nome, nova_quantidade):

        if nova_quantidade < 0:
            return False

        produto = self.buscar_produto(nome)

        if produto:

            produto.quantidade = nova_quantidade

            return True

        return False

    def listar_produtos(self):

        return self.produtos