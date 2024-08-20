class cliente:
    def __init__(self, cpf, nome, telefone):
        self.__cpf = cpf
        self.__nome = nome
        self.__telefone = telefone
        
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
