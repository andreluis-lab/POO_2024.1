class Funcionario:

    def __init__(self, nome, cpf, telefone, salario, funcao):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.salario = salario
        self.__funcao = funcao

    @property
    def _funcao(self):
        return self.__funcao

    @_funcao.setter
    def _funcao(self, value):
        self.__funcao = value


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

    @property    
    def _salario(self):
        return self.salario
    
    @_salario.setter
    def _salario(self, value):
        self.salario = value

    
class Garcom(Funcionario):
    def  __init__(self, cpf, nome,telefone, salario):
        super().__init__(cpf, nome, telefone, salario)
        self.__total_gorjetas = 0.0
        
    @property
    def total_gorjetas(self):
        return self.__total_gorjetas

    def adicionar_gorjeta(self, valor):
        self.__total_gorjetas += valor

class Entregador(Funcionario):
    def __init__(self, cpf, nome,telefone, salario):
        super().__init__(cpf, nome, telefone, salario)
        self.__total_gorjetas = 0.0
        
    @property
    def total_gorjetas(self):
        return self.__total_gorjetas

    def adicionar_gorjeta(self, valor):
        self.__total_gorjetas += valor   

class Gerente(Funcionario):
    def __init__(self, cpf, nome,telefone, salario):
        super().__init__(cpf, nome, telefone, salario)  

class Telefonista(Funcionario):
    def __init__(self, cpf, nome,telefone, salario):
        super().__init__(cpf, nome, telefone, salario)
