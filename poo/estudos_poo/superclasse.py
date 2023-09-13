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


class Poupanca(Conta):
    def __init__(self, saldo, taxa_juros):
        super().__init__(saldo)
        self._taxa_juros = taxa_juros
    
    @property
    def taxa_juros(self):
        return self._taxa_juros
    
    @taxa_juros.setter
    def taxa_juros(self, taxa_juros):
        self._taxa_juros = taxa_juros
    
    def render_juros(self):
        super().creditar(self._saldo * self._taxa_juros)

poupanca = Poupanca(100, 0.10)
poupanca.creditar(20)
poupanca.render_juros()
print(poupanca.__dict__)