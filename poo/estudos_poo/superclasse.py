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


class Banco:
    def __init__(self):
        self._contas = {}

    @property
    def contas(self):
        return self._contas
    
    def existe_conta(self, numero):
        if self._contas.get(numero, None) is None:
            return False
        else:
            return True
    
    def get_conta(self, numero):
        if self.existe_conta(numero):
            return self._contas.get(numero)
        else:
            print(f'Conta {numero} inexistente')
    
    def cadastrar_conta(self, conta):
        if self.existe_conta(conta.numero):
            print(f'A conta nº {conta.numero} já existe.')
        else:
            self._contas.update({conta.numero: conta})

    def creditar(self, numero, valor):
        if self.existe_conta(numero):
            conta = self.get_conta(numero)
            conta.creditar(valor)
        else: 
            print(f'A conta nº {conta.numero} não existe.')

    def debitar(self, numero, valor):
        if self.existe_conta(numero):
            conta = self.get_conta(numero)
            conta.debitar(valor)
        else:
            print(f'A conta nº {conta.numero} não existe.')

    def render_juros(self, numero):
        if self.existe_conta(numero):
            conta = self.get_conta(numero)
            #Verificando se o obj conta é da classe Poupanca
            if isinstance(conta, Poupanca):
                conta.render_juros()
            else:
                print(f'Conta nº {conta.numero} não é do tipo poupança.')
        else:
            print(f'A conta nº {conta.numero} não existe.')


banco = Banco()
conta = Conta(100)

banco.cadastrar_conta(conta)
print('Conta cadastrada!')
print(banco.get_conta(conta.numero).__dict__)

banco.debitar(conta.numero, 20)
print('\nDebitou R$ 20 da conta')
print(banco.get_conta(conta.numero).__dict__)

banco.creditar(conta.numero, 100)
print('\nCreditou R$ 100 na Conta')
print(banco.get_conta(conta.numero).__dict__)