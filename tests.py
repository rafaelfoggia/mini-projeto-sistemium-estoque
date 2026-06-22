# Importa as classes necessárias
from produto import Produto
from estoque import Estoque


# Cria estoque para testes
estoque = Estoque()

# Cria produto de teste
mouse = Produto("Mouse", 10)

# Adiciona produto
estoque.adicionar_produto(mouse)

# Verifica se foi adicionado
assert len(estoque.produtos) == 1

# Verifica busca
assert estoque.buscar_produto("Mouse") == mouse

# Atualiza quantidade
estoque.alterar_quantidade("Mouse", 20)

# Verifica atualização
assert mouse.quantidade == 20

# Remove produto
estoque.remover_produto("Mouse")

# Verifica remoção
assert len(estoque.produtos) == 0

print("Todos os testes passaram!")