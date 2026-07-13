from estoque import Estoque
import servico_produto

estoque = Estoque()


def mostrar_menu():
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1- Adicionar produto.")
    print("2- Remover produto.")
    print("3- Alterar quantidade.")
    print("4- Consultar estoque.")
    print("5- Sair.")


def adicionar_produto():
    nome = input("Digite o nome do produto: ")

    try:
        quantidade = int(
            input("Digite a quantidade do produto: ")
        )

        if quantidade < 0:
            print("Quantidade inválida!")
            return

        servico_produto.cadastrar(
            estoque,
            nome,
            quantidade
        )

        print("Produto adicionado com sucesso!")

    except ValueError:
        print("Digite apenas números!")


def remover_produto():
    nome = input(
        "Digite o produto que deseja remover: "
    )

    if servico_produto.remover(
        estoque,
        nome
    ):
        print("Produto removido!")

    else:
        print("Produto não encontrado!")


def alterar_quantidade():
    nome = input(
        "Digite o produto que deseja alterar a quantidade: "
    )

    try:
        nova_quantidade = int(
            input("Nova quantidade: ")
        )

        if nova_quantidade < 0:
            print("Quantidade inválida!")
            return

        if servico_produto.alterar_quantidade(
            estoque,
            nome,
            nova_quantidade
        ):
            print("Quantidade atualizada.")

        else:
            print("Produto não encontrado!")

    except ValueError:
        print("Digite apenas números!")


def consultar_estoque():
    produtos = servico_produto.listar(estoque)

    if len(produtos) == 0:
        print("Estoque vazio!")

    else:
        for produto in produtos:
            print(produto)


def main():

    while True:

        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            adicionar_produto()

        elif opcao == "2":

            remover_produto()

        elif opcao == "3":

            alterar_quantidade()

        elif opcao == "4":

            consultar_estoque()

        elif opcao == "5":

            print("Encerrando Sistema...")

            break

        else:

            print("Opção inválida!")


if __name__ == "__main__":
    main()