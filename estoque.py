# Cria a lista vazia de produtos
class Estoque:
    def __init__(self):
        self.produtos = []  

# adiciona um novo produto para dentro da caixa
    def adicionar_produto(self, produto):
            self.produtos.append(produto)

    def buscar_produto(self, nome):
            
            # Olha um por um dentro da caixa
            for produto in self.produtos:

                # Compara os nomes (tudo em minúsculo)
                if produto.nome.lower() == nome.lower():

                    # Se achou, entrega o produto e para de procurar
                    return produto
                
            # Se revirou a caixa toda e não achou, devolve "nada" (None)  
            return None 

    def remover_produto(self, nome):
        # Procura o produto pelo nome usando a função buscar_produto()
        produto = self.buscar_produto(nome)

        # Verifica se encontrou algum produto
        if produto:

            # Remove o produto da lista de produtos
            self.produtos.remove(produto)

            # Retorna True para indicar sucesso
            return True

        # Se não encontrou, retorna False
        return False

    # Altera a quantidade de um produto
    def alterar_quantidade(self, nome, nova_quantidade):
        # Procura o produto
            produto = self.buscar_produto(nome)

            # Se encontrou
            if produto:

                # Atualiza a quantidade
                produto.quantidade = nova_quantidade

                # Indica sucesso
                return True

            # Produto não encontrado
            return False

    # Retorna todos os produtos
    def listar_produtos(self):

            # Retorna a lista inteira
            return self.produtos