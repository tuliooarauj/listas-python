class Conta:
    #Método construtor
    def __init__(self, numero, saldo, limite):
        self._numero = numero
        self._saldo = saldo
        self._limite = limite
    
    def creditar(self, valor):
        self._saldo += valor
    
    def debitar(self, valor):
        self._saldo -= valor
    
    #Getters & Setters

    def get_numero(self):
        return self._numero
    
    def get_saldo(self):
        return self._saldo

    def get_limite(self):
        return self._limite
    
    def set_limite(self, limite):
        if limite < 0:
            print('Valor inválido!')
        else:
            self._limite = limite
        