# definição da classe
class Pedido:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor
    def __init__(self, codido_pedido, nome_cliente, garcom=None, entregador=None):
        self.__codigo_pedido = codido_pedido
        self.__status = 0  # 0 = aberto, 1 = finalizado/pago
        # criando uma estrutura map em python para armzenar itens do pedido
        self.__itens_pedidos = []
        self.__nome_cliente = nome_cliente
        self.__garcom = garcom  # Associar o garçom ao pedido
        self.__entregador = entregador  # Associando o entregador ao pedido
    
    @property
    def _garcom(self):
        return self.__garcom

    @_garcom.setter
    def _garcom(self, value):
        self.__garcom = value
    
    @property
    def _nome_cliente(self):
        return self.__nome_cliente

    @_nome_cliente.setter
    def _nome_cliente(self, value):
        self.__nome_cliente = value

    @property
    def _status(self):
        return self.__status

    @_status.setter
    def _status(self, value):
        self.__status = value

    @property
    def _codigo_pedido(self):
        return self.__codigo_pedido

    @_codigo_pedido.setter
    def _codigo_pedido(self, value):
        self.__codigo_pedido = value

    @property
    def _itens_pedidos(self):
        return self.__itens_pedidos

    @_itens_pedidos.setter
    def _itens_pedidos(self, value):
        self.__itens_pedidos = value

    def adicionar_item_ao_pedido(self, itempedido):
        self.__itens_pedidos.append(itempedido)

    def remover_item_pedido(self, codigo_produto, quantidade):
        for item in self.__itens_pedidos:
            if item._produto._codigo_produto == codigo_produto:
                if quantidade >= item._quantidade:
                    self.__itens_pedidos.remove(item)
                else:
                    item._quantidade -= quantidade
                break

    def quantidade_itens_pedido(self):
        return int(len(self.__itens_pedidos))
        # return self.__itens_pedidos.__sizeof__
    
    def calcular_subtotal(self):
        subtotal = 0.0
        for item in self.__itens_pedidos:
            subtotal += item._produto._preco * item._quantidade
        return subtotal

    def listar_itens(self):
        print("Itens do pedido:")
        for item in self.__itens_pedidos:
            print(f"Produto: {item._produto._descricao}, Quantidade: {item._quantidade}, Preço unitário: {item._produto._preco}, Subtotal: {item._produto._preco * item._quantidade}")
        print(f"Subtotal do pedido: {self.calcular_subtotal()}")

class Delivery(Pedido):
    def __init__(self, nome_cliente, codigo_pedido, endereco_entrega):
        super().__init__(codigo_pedido, nome_cliente)
        self.__endereco_entrega = endereco_entrega
        self.entregador = None  # Associando o entregador ao pedido

    @property
    def endereco_entrega(self):
        return self.__endereco_entrega

    @endereco_entrega.setter
    def endereco_entrega(self, value):
        self.__endereco_entrega = value

    def toString(self):
        print("** INÍCIO DAS INFORMAÇÕES DO PEDIDO **")
        print(f"NOME DO CLIENTE: {self._nome_cliente}\tCÓDIGO DO PEDIDO: {self._codigo_pedido}\tSTATUS DO PEDIDO: {self._status}")
        print(f"CEP ENDEREÇO PARA ENTREGA: {self.endereco_entrega._cep}\tRUA: {self.endereco_entrega._rua}\tBAIRRO/CIDADE PARA ENTREGA: {self.endereco_entrega._bairro}/{self.endereco_entrega._cidade}")
        print(f"QUANTIDADE DE ITENS DO PEDIDO: {self.quantidade_itens_pedido()}")
        self.listar_itens()
        
        dbl_preco_total = self.calcular_subtotal()
        print(f"PREÇO TOTAL DO PEDIDO SEM TAXA OPCIONAL (R$): {dbl_preco_total:.2f}")
        
        # Cálculo da gorjeta e atualização do valor na classe Entregador
        dbl_gorjeta = dbl_preco_total * 0.1
        if self.entregador:
            self.entregador.adicionar_gorjeta(dbl_gorjeta)
        
        dbl_preco_tEntrega = dbl_preco_total + dbl_gorjeta
        print(f"PREÇO TOTAL DO PEDIDO COM A GORJETA DO ENTREGADOR (R$): {dbl_preco_tEntrega:.2f}")
        print("** FIM DAS INFORMAÇÕES DO PEDIDO **")


class Mesa(Pedido):
    def __init__(self, nome_cliente, numero_mesa, codigo_pedido):
        super().__init__(codigo_pedido, nome_cliente)
        self.__numero_mesa = numero_mesa
        self.garcom = None  # Associando o garçom ao pedido

    @property
    def numero_mesa(self):
        return self.__numero_mesa

    @numero_mesa.setter
    def numero_mesa(self, value):
        self.__numero_mesa = value

    def toString(self):
        print("* INFORMAÇÕES DO PEDIDO PRESENCIAL *")
        print(f"NOME DO CLIENTE: {self._nome_cliente}\tCÓDIGO DO PEDIDO: {self._codigo_pedido}\tSTATUS DO PEDIDO: {self._status}")
        print(f"MESA N°: {self.numero_mesa}\tQUANTIDADE DE ITENS DO PEDIDO: {self.quantidade_itens_pedido()}")
        self.listar_itens()
        dbl_preco_total = self.calcular_subtotal()
        print(f"PREÇO TOTAL DO PEDIDO SEM TAXA OPCIONAL (R$): {dbl_preco_total:.2f}")
        
        # Cálculo da gorjeta e atualização do valor na classe Garcom
        dbl_gorjeta = dbl_preco_total * 0.1
        if self.garcom:
            self.garcom.adicionar_gorjeta(dbl_gorjeta)
        
        dbl_preco_tGarcom = dbl_preco_total + dbl_gorjeta
        print(f"PREÇO TOTAL DO PEDIDO COM A GORJETA DO GARÇOM (R$): {dbl_preco_tGarcom:.2f}")
        print("* FIM DAS INFORMAÇÕES DO PEDIDO *")
