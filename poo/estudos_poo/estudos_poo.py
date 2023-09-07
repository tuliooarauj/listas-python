class Conta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
        #self._saldo = saldo --> o '_' é utilizado para determinar que o atributo é privado.

    def creditar(self, saldo):
        self.saldo += saldo
    
    def debitar(self, saldo):
        self.saldo -= saldo

conta1 = Conta('123-x', 0.00)
conta2 = Conta('234-y', 100.00)

print('Valor inicial:')
print(conta1.__dict__)
print(conta2.__dict__)
print('=========================')

#REALIZANDO CRÉDITO NAS CONTAS

conta1.creditar(10)
conta2.debitar(90)

print('APÓS ALTERAÇÕES')
print(conta1.__dict__)
print(conta2.__dict__)

