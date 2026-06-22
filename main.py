# Importa a classe Produto do arquivo produto.py
from produto import Produto

# Importa a classe Estoque do arquivo estoque.py
from estoque import Estoque

# Cria um estoque vazio para armazenar os produtos
estoque = Estoque()

# Loop principal do sistema
# Enquanto o usuário não escolher sair, o menu continuará aparecendo
while True:

    # Exibe o menu de opções
    print('\n===== SISTEMA DE ESTOQUE =====')
    print('1- Adicionar produto.')
    print('2- Remover produto.')
    print('3- Alterar quantidade.')
    print('4- Consultar estoque.')
    print('5- Sair.')

    # Recebe a opção escolhida pelo usuário
    opção = input('Escolha uma opção:')

    # ADICIONAR PRODUTO
    if opção == '1':

        # Solicita o nome do produto
        nome = input('Digite o nome do produto:')

        try:

            # Solicita a quantidade e converte para inteiro
            quantidade = int(
                input('Digite a quantidade do produto:')
            )

            # Impede que o usuário cadastre quantidades negativas
            if quantidade < 0:
                print('Quantidade inválida!')

                # Volta para o início do menu
                continue

            # Cria um objeto Produto com os dados informados
            produto = Produto(nome, quantidade)

            # Adiciona o produto ao estoque
            estoque.adicionar_produto(produto)

            print('Produto adicionado com sucesso!')

        # Executado caso o usuário digite letras ao invés de números
        except ValueError:
            print('Digite apenas números!')

    # REMOVER PRODUTO
    elif opção == '2':

        # Solicita o nome do produto que será removido
        nome = input('Digite o produto que deseja remover:')

        # Tenta remover o produto do estoque
        if estoque.remover_produto(nome):

            # Executado se a remoção foi realizada com sucesso
            print('Produto removido!')

        else:

            # Executado se o produto não existir
            print('Produto não encontrado!')

    # ALTERAR QUANTIDADE
    elif opção == '3':

        # Solicita o nome do produto que será alterado
        nome = input(
            'Digite o produto que deseja alterar a quantidade:'
        )

        try:

            # Recebe a nova quantidade
            nova_quantidade = int(
                input('Nova quantidade: ')
            )

            # Tenta atualizar a quantidade do produto
            if estoque.alterar_quantidade(
                nome,
                nova_quantidade
            ):

                # Executado se o produto foi encontrado
                print('Quantidade atualizada.')

            else:

                # Executado se o produto não existir
                print('Produto não encontrado!')

        # Executado caso o usuário digite algo diferente de números
        except ValueError:
            print('Digite apenas números!')

    # CONSULTAR ESTOQUE
    elif opção == '4':

        # Verifica se existem produtos cadastrados
        if len(estoque.produtos) == 0:

            print('Estoque vazio!')

        else:

            # Percorre todos os produtos cadastrados
            for produto in estoque.listar_produtos():

                # Exibe as informações de cada produto
                print(produto)

    # SAIR DO SISTEMA
    elif opção == '5':

        print('Encerrando Sistema...')

        # Encerra o loop principal
        break

    # OPÇÃO INVÁLIDA
    else:

        # Executado quando o usuário digita uma opção inexistente
        print('Opção inválida!')