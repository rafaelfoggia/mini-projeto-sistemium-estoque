from produto import Produto


def cadastrar(estoque, nome, quantidade):

    produto = Produto(nome, quantidade)

    estoque.adicionar_produto(produto)


def listar(estoque):

    return estoque.listar_produtos()


def buscar(estoque, nome):

    return estoque.buscar_produto(nome)


def remover(estoque, nome):

    return estoque.remover_produto(nome)


def alterar_quantidade(estoque, nome, nova_quantidade):

    return estoque.alterar_quantidade(
        nome,
        nova_quantidade
    )