import datetime

class Produto:
    def __init__(self, id, categoria, nome, preco, localizacao, produtos_estoque=None, produtos_vendidos=None):
        self.id = id
        self.categoria = categoria
        self.nome = nome
        self.preco = preco
        self.localizacao = localizacao
        self.produtos_estoque = produtos_estoque if produtos_estoque else []
        self.produtos_vendidos = produtos_vendidos if produtos_vendidos else []

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Vendidos:
    def __init__(self, quantidade, data_saida):
        self.quantidade = quantidade
        self.data_saida = data_saida

class EmEstoque:
    def __init__(self, quantidade, data_entrada):
        self.quantidade = quantidade
        self.data_entrada = data_entrada

class Localizacao:
    def __init__(self, deposito, setor, prateleira):
        self.deposito = deposito
        self.setor = setor
        self.prateleira = prateleira

produtos = []

def cadastrar_produto():
    id = input('Digite o ID do produto: ')
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    categoria = input('Digite a categoria do produto: ')
    deposito = input('Digite o depósito do produto: ')
    setor = input('Digite o setor do produto: ')
    prateleira = input('Digite a prateleira do produto: ')
    quantidade = int(input('Digite a quantidade em estoque: '))
    data_entrada = datetime.datetime.strptime(input('Digite a data de entrada do produto (YYYY-MM-DD): '), '%Y-%m-%d')
    
    produto = Produto(
        id=id,
        categoria=Categoria(id=id, nome=categoria),
        nome=nome,
        preco=preco,
        localizacao=Localizacao(deposito=deposito, setor=setor, prateleira=prateleira),
        produtos_estoque=[EmEstoque(quantidade=quantidade, data_entrada=data_entrada)]
    )
    
    produtos.append(produto)
    print(f'{produto.nome} cadastrado com sucesso!')

def consultar_produto(id):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None

def registrar_entrada(id, quantidade, data_entrada):
    produto = consultar_produto(id)
    if produto:
        produto.produtos_estoque.append(EmEstoque(quantidade=quantidade, data_entrada=data_entrada))
        print(f'Entrada de {quantidade} unidades do produto {produto.nome} registrada com sucesso!')
    else:
        print('Produto não encontrado.')

def registrar_saida(id, quantidade, data_saida):
    produto = consultar_produto(id)
    if produto:
        produto.produtos_vendidos.append(Vendidos(quantidade=quantidade, data_saida=data_saida))
        print(f'Saída de {quantidade} unidades do produto {produto.nome} registrada com sucesso!')
    else:
        print('Produto não encontrado.')

def gerar_relatorio_estoque():
    for produto in produtos:
        quantidade_estoque = sum(item.quantidade for item in produto.produtos_estoque)
        quantidade_vendida = sum(item.quantidade for item in produto.produtos_vendidos)
        print(f'Produto - {produto.nome}')
        print(f'Quantidade em estoque - {quantidade_estoque}')
        print(f'Quantidade vendida - {quantidade_vendida}')
        print('---------------------------------')

def consultar_historico_movimentacoes(id):
    produto = consultar_produto(id)
    if produto:
        print(f'Histórico de movimentações do produto {produto.nome}:')
        for entrada in produto.produtos_estoque:
            print(f'Entrada: {entrada.quantidade} unidades em {entrada.data_entrada}')
        for saida in produto.produtos_vendidos:
            print(f'Saída: {saida.quantidade} unidades em {saida.data_saida}')
    else:
        print('Produto não encontrado.')

def main():
    while True:
        print('====================')
        print('Sistema de Estoque')
        print('1 - Cadastrar Produto')
        print('2 - Registrar Entrada')
        print('3 - Registrar Saída')
        print('4 - Consultar Produto')
        print('5 - Gerar Relatório de Estoque')
        print('6 - Consultar Histórico de Movimentações')
        print('7 - Sair')
        print('====================')
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            id = input('Digite o ID do produto: ')
            quantidade = int(input('Digite a quantidade: '))
            data_entrada = datetime.datetime.strptime(input('Digite a data de entrada (YYYY-MM-DD): '), '%Y-%m-%d')
            registrar_entrada(id, quantidade, data_entrada)
        elif opcao == '3':
            id = input('Digite o ID do produto: ')
            quantidade = int(input('Digite a quantidade: '))
            data_saida = datetime.datetime.strptime(input('Digite a data de saída (YYYY-MM-DD): '), '%Y-%m-%d')
            registrar_saida(id, quantidade, data_saida)
        elif opcao == '4':
            id = input('Digite o ID do produto: ')
            produto = consultar_produto(id)
            if produto:
                print(f'Produto: {produto.nome}')
                print(f'Categoria: {produto.categoria.nome}')
                print(f'Preço: {produto.preco}')
                print(f'Localização: Depósito {produto.localizacao.deposito}, Setor {produto.localizacao.setor}, Prateleira {produto.localizacao.prateleira}')
            else:
                print('Produto não encontrado.')
        elif opcao == '5':
            gerar_relatorio_estoque()
        elif opcao == '6':
            id = input('Digite o ID do produto: ')
            consultar_historico_movimentacoes(id)
        elif opcao == '7':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()