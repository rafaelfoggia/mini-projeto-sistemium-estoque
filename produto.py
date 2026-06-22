# Classe responsável por representar um produto do estoque
class Produto:

    # Método executado quando um novo produto é criado
    def __init__(self, nome, quantidade):

        # Guarda o nome do produto
        self.nome = nome

        # Guarda a quantidade disponível
        self.quantidade = quantidade

    # Define como o produto será exibido ao usar print()
    def __str__(self):

        # Retorna uma string formatada
        return f"{self.nome} - {self.quantidade} unidades"