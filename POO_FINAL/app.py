from class_endereco import Endereco
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_produto import Produto
from class_funcionario import Funcionario
from class_funcionario import Garcom
from class_funcionario import Entregador
from class_pedido import Delivery
from class_pedido import Mesa

def menu_principal():  # MENU PRINCIPAL
    print('''
        MENU Principal:
        [1] - Controle de vendas
        [2] - Cadastrar pratos no cardápio
        [3] - Remover um prato do caedápio
        [4] - Pesquisar pratos no cardápio
        [5] - Gerenciar funcionários
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def menu_pedido():
    print('''
        MENU Vendas:
        [1] - Abrir novo pedido
        [2] - Adicionar item ao pedido
        [3] - Remover item do pedido
        [4] - Listar itens do pedido em detalhes
        [5] - Finalizar pedido e imprimir
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def menu_funcionario():
    print('''
        MENU Funcionários:
        [1] - Cadastrar funcionário
        [2] - Remover funcionário
        [3] - Pesquisar funcionario
        [s] - Sair
    ''') 
    return str(input('Escolha uma opção: '))

def menu_servico():
    print('''
        MENU Serviço:
        [1] - Mesa
        [2] - Delivery
        [s] - Sair
    ''') 
    return str(input('Escolha uma opção: '))      


def pedido_adicionar_delivery():
    str_nomeCD = str(input('Informe o nome do cliente: '))
    endereco_pedido = cadastrar_endereco()
    codido_pedido = int(len(pedidos)) + 1
    entregador_cpf = int(input('Informe o CPF do entregador responsável: '))
    entregador = buscar_funcionario_por_cpf(entregador_cpf)
    if isinstance(entregador, Entregador):
        pedido = Delivery(str_nomeCD, codido_pedido, endereco_pedido)
        pedido.entregador = entregador  # Associa o entregador ao pedido
        return pedido
    else:
        print("Entregador não encontrado!")
        return None
    
def associar_entregador_pedido_delivery(pedido_delivery, cpf_entregador):
    entregador = buscar_funcionario_por_cpf(cpf_entregador)
    if entregador and isinstance(entregador, Entregador):
        pedido_delivery.entregador = entregador
    else:
        print("Entregador não encontrado!")

def pedido_adicionar_mesa():
    str_nomeC = str(input('Informe o nome do cliente: '))
    int_numeroM = int(input('Qual a mesa?: '))
    codido_pedido = int(len(pedidos)) + 1
    garcom_cpf = int(input('Informe o CPF do garçom responsável: '))
    garcom = buscar_funcionario_por_cpf(garcom_cpf)
    if isinstance(garcom, Garcom):
        pedido = Mesa(str_nomeC, int_numeroM, codido_pedido)
        pedido.garcom = garcom  # Associa o garçom ao pedido
        return pedido
    else:
        print("Garçom não encontrado!")
        return None
    
def associar_garcom_pedido_mesa(pedido_mesa, cpf_garcom):
    garcom = buscar_funcionario_por_cpf(cpf_garcom)
    if garcom and isinstance(garcom, Garcom):
        pedido_mesa.garcom = garcom
    else:
        print("Garçom não encontrado!")

def pedido_adicionar_item():
    int_pedido_selecionado = int(input('Informe o código do pedido para adicionar um novo item: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_produto = int(input('Informe o código do produto para adicionar ao pedido: '))
        produto = buscar_produto_por_codigo(int_codigo_produto)
        if produto:
            int_quantidade_item = int(input('Informe a quantidade do item:'))
            novo_item_pedido = ItemPedido(produto, int_quantidade_item)
            pedido.adicionar_item_ao_pedido(novo_item_pedido)
        else:
            print("Não foi possível adicionar este produto, pois o código do produto não existe!")
        #return Pedido(codido_pedido, endereco_pedido)
    else:
        print("Pedido inexistente")
        return False
    
def pedido_remover_item():
    int_pedido_selecionado = int(input('Informe o código do pedido para remover um item selecionado: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_produto = int(input('Informe o código do produto para remover deste pedido ' + str(pedido._codigo_pedido) + ': '))
        # Verifica se o produto existe no pedido
        item_existe = any(item._produto._codigo_produto == int_codigo_produto for item in pedido._itens_pedidos)
        
        if item_existe:
            quantidade_remover = int(input('Informe a quantidade que deseja remover do produto ' + str(int_codigo_produto) + ': '))
            pedido.remover_item_pedido(int_codigo_produto, quantidade_remover)
            print(f"{quantidade_remover} unidades do produto {int_codigo_produto} removidas com sucesso.")
        else:
            print(f"Produto {int_codigo_produto} não encontrado no pedido.")
    else:
        print("Pedido inexistente")

def pedido_listar_items():
    int_pedido_selecionado = int(input('Informe o código do pedido para mais detalhes: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        pedido = pedidos[int_pedido_selecionado]
        pedido.toString()
    else:
        print("Pedido inexistente")
        return False

def pedido_finalizar():
    int_codigo_finalizar = int(input('Informe o código do pedido a ser finalizado: '))    
    pedido_selecionado = pedidos[int_codigo_finalizar]
    pedido_selecionado._status = "1"
    pedido_selecionado.toString()
    del pedidos[int_codigo_finalizar]

def cadastrar_endereco():
    str_cep = str(input('Informe o cep do endereço: '))
    str_rua = str(input('Informe a rua: '))
    int_num = int(input('Informe o número: '))
    str_complemento = str(input('Informe o complemento do endereço: '))
    str_bairro = str(input('Informe o bairro: '))
    str_cidade = str(input('Informe a cidade: '))
    endereco = Endereco(str_cep, str_rua, int_num,
                        str_complemento, str_bairro, str_cidade)
    return endereco

def cadastrar_produto():
    int_codigo = int(input('Informe o código identificador do produto: '))
    str_nome = str(input('Qual o nome/descrição do produto? '))
    flt_preco = float(input('Informe o valor (ex. 0.00): '))
    return Produto(int_codigo, str_nome, flt_preco)

def remover_produto():
    int_codigo_remocao = int(input('Informe o código do produto para remoção: '))
    produto_remover = estoque_produtos[int_codigo_remocao]
    print("Produto (" + produto_remover._descricao + ") removido!") 
    del estoque_produtos[int_codigo_remocao]

def buscar_produto_por_codigo(int_codigo_produto):
    # Verifica se existe produto cadastrado
    for chave in estoque_produtos.keys():
        if chave == int_codigo_produto:
            return estoque_produtos[int_codigo_produto]
    return False

def buscar_pedido_por_codigo(int_codigo_pedido):
    # Verifica se existe produto cadastrado
    for chave in pedidos.keys():
        if chave == int_codigo_pedido:
            return pedidos[int_codigo_pedido]
    return False

def cadastrar_funcionario():
    str_nomeF = str(input('Informe o nome do funcionário: '))
    int_cpf = int(input('Qual o cpf do funcionário: '))
    int_telefone = int(input('Qual o número de telefone do funcionário? '))
    flt_salario = float(input('Informe o salario (ex. 0.00): '))
    str_funcao = str(input('''Area de trabalho:'''))
    return Funcionario(str_nomeF, int_cpf, int_telefone, flt_salario, str_funcao)

def remover_funcionario():
    int_cpf_remover = int(input('Informe o cpf do funcionario para remoção: '))
    funcionario_remover = funcionario_lista[int_cpf_remover]
    print("Funcionario (" + str(funcionario_remover._nome) + ") removido!") 
    del funcionario_lista[int_cpf_remover]

def buscar_funcionario_por_cpf(int_cpf):
    funcionario = funcionario_lista.get(int_cpf, None)
    if funcionario:
        print("Funcionário encontrado:")
        print("> CPF: " + str(funcionario._cpf))
        print("> Nome: " + funcionario._nome)
        print("> Telefone: " + str(funcionario._telefone))
        print("> Salário: " + str(funcionario._salario))
        print("> Área de trabalho: " + funcionario._funcao)

        # Exibe gorjetas se for Garçom ou Entregador
        if isinstance(funcionario, Garcom):
            print("> Total de Gorjetas: " + str(funcionario.total_gorjetas))
        elif isinstance(funcionario, Entregador):
            print("> Total de Gorjetas: " + str(funcionario.total_gorjetas))
    else:
        print("Funcionário não encontrado!")
    return funcionario

# Aplicação de exemplo disciplina POO - UFRB
# Sistema de controle de pedidos
# Professor Guilherme Braga Araújo

funcionario_lista = {}
estoque_produtos = {}
pedidos = {}

while True:
    # menu_principal
    opcao_escolhida = menu_principal()
    # verificando escolha
    # opc sair
    if (opcao_escolhida == "s"):
        break
    # opc 1
    elif (opcao_escolhida == "1"):
        while True:
            opcao_escolhida = menu_pedido()
            # opc menu vendas - novo pedido1
            if (opcao_escolhida == "1"):
                while True:
                    opcao_escolhida = menu_servico()
                    if (opcao_escolhida == "1"):
                        pedido = pedido_adicionar_mesa()
                        
                        if (pedido):
                            # adiciona pedido ao sistema
                            pedidos[pedido._codigo_pedido] = pedido
                    elif(opcao_escolhida == "2"):
                        pedido = pedido_adicionar_delivery()
                        
                        if (pedido):
                            # adiciona pedido ao sistema
                            pedidos[pedido._codigo_pedido] = pedido
                    else:
                # Volta para o menu principal
                        break                            
            # opc menu vendas - adicionar item    
            elif (opcao_escolhida == "2"):
                pedido_adicionar_item()
            elif (opcao_escolhida == "3"):
                pedido_remover_item()
            elif (opcao_escolhida == "4"):
                pedido_listar_items()
            elif (opcao_escolhida == "5"):
                pedido_finalizar()
            else:
                # Volta para o menu principal
                break
               
    # opc 2
    elif (opcao_escolhida == "2"):
        produto = cadastrar_produto()
        if (produto):
            # adiciona produto ao nosso estoque
            estoque_produtos[produto._codigo_produto] = produto
    # opc 3
    elif (opcao_escolhida == "3"):
        remover_produto()
    # opc 4
    elif (opcao_escolhida == "4"):
        int_codigo_produto = int(input('Informe o código do produto para busca: '))
        produto_pesquisa = buscar_produto_por_codigo(int_codigo_produto)
        if (produto_pesquisa):
            print("Produto encontrado:")
            print(">Código=" + str(produto_pesquisa._codigo_produto))
            print(">Descricao=" + (produto_pesquisa._descricao))
            print(">Valor=" + str(produto_pesquisa._preco))
        else:
            print("Produto não cadastrado/encontrado.")

    elif(opcao_escolhida == "5"):
        while True:
            opcao_escolhida = menu_funcionario()
            if (opcao_escolhida == "1"):
                funcionario = cadastrar_funcionario()
                if (funcionario):
                   funcionario_lista[funcionario._cpf] = funcionario
            #opc 6
            elif (opcao_escolhida == "2"):
                int_cpfr = int(input('Informe o cpf do funcionário para remoção: '))
                funcionario_pesquisaR = buscar_funcionario_por_cpf(int_cpfr)
                if(funcionario_pesquisaR):
                  remover_funcionario()
                else:
                   print("Funcionário não cadastrado/encontrado.")
            #opc 7
            elif (opcao_escolhida == "3"):
                int_cpf = int(input('Informe o CPF do funcionário para busca: '))
                buscar_funcionario_por_cpf(int_cpf)
            else:
                # Volta para o menu principal
                break            
