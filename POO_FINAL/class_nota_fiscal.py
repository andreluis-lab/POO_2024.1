class NotaFiscal:
    def __init__(self, codigo_finalizar):
          self.__codigo_finalizar = codigo_finalizar
 
    @property
    def _codigo_finalizar(self):
        return self.__codigo_finalizar

    @_codigo_finalizar.setter
    def _codigo_finalizar(self, value):
        self.codigo_finalizar = value
