class Conta:
    def __init__(self, numero, saldo) -> None:
        self._numero = numero
        self._saldo = saldo
    
    def creditar(self, valor):
        self._saldo += valor
    
    def debitar(self, valor):
        self._saldo -= valor


    def get_numero(self):
        return self._numero
    
    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, saldo):
        if saldo < 0:
            print('Valor inválido')
        else:
            self._saldo = saldo

conta_a = Conta('123-x', 0.00)
conta_b = Conta('234-y', 0.00)
conta_c = Conta('456-z', 0.00)

conta_a.creditar(35.00)
conta_b.creditar(50.00)

#PRE TRANSFERENCIA
print(conta_a.__dict__)
print(conta_b.__dict__)
print(conta_c.__dict__)

print('\n==============\n')

conta_c.creditar(conta_a.get_saldo() + conta_b.get_saldo())
conta_a.debitar(conta_a.get_saldo())
conta_b.debitar(conta_b.get_saldo())

#POS TRANSFERENCIA
print(conta_a.__dict__)
print(conta_b.__dict__)
print(conta_c.__dict__)
