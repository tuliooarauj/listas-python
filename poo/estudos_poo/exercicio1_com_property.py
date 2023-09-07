class Conta:
    def __init__(self, numero, saldo, limite) -> None:
        self._numero = numero
        self._saldo = saldo
        self._limite = limite
    
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
            print('Valor inválido')
        else:
            self._saldo = saldo
            
    @saldo.deleter
    def saldo(self):
        del self._saldo

    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, limite):
        if limite < 0:
            print('Valor inválido')
        else:
            self._limite = limite
    
    @property
    def saldo_disponivel(self):
        return self._saldo + self._limite
    
    

conta_a = Conta('123-x', 0.00, 0.00)
conta_b = Conta('234-y', 0.00, 0.00)
conta_c = Conta('456-z', 0.00, 0.00)

conta_a.creditar(35.00)
conta_b.creditar(50.00)

#PRE TRANSFERENCIA
print(conta_a.__dict__)
print(conta_b.__dict__)
print(conta_c.__dict__)
print(conta_c.saldo_disponivel)

print('\n==============\n')

conta_c.creditar(conta_a.saldo + conta_b.saldo)
conta_a.debitar(conta_a.saldo)
conta_b.debitar(conta_b.saldo)

conta_c.limite = 1000

#POS TRANSFERENCIA
print(conta_a.__dict__)
print(conta_b.__dict__)
print(conta_c.__dict__)
print(conta_c.saldo_disponivel)

print('\n==============\n')

#POS REMOCAO
del conta_a.saldo

print(conta_a.__dict__)
print(conta_b.__dict__)
print(conta_c.__dict__)