class Conta:

    #atributo de Classe -> Global
    _num_contas = 1

    def __init__(self, saldo):
        self._numero = Conta.gera_novo_numero()
        self._saldo = saldo
        Conta._num_contas += 1 #Incrementando o numero de contas sempre que um objeto for criado

    #método de Classe -> Global
    @classmethod
    def gera_novo_numero(cls):
        return cls._num_contas * 1234

    def creditar(self, valor):
        self._saldo += valor
    
    def debitar(self, valor):
        self._saldo -= valor
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('Saldo inválido')
        else:
            self._saldo = saldo

conta_1 = Conta(20)
conta_2 = Conta(30)

print(f'Conta 1: {conta_1.__dict__}')
print(f'Conta 2: {conta_2.__dict__}')