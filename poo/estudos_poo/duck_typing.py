class Numero:
    
    def __init__(self, valor):
        self._valor = valor

    def dobrar(self):
        return self._valor * 2

class Texto:

    def __init__(self, palavra):
        self._palavra = palavra
    
    def dobrar(self):
        return self._palavra * 2
    
# Duck Typing: aceita objeto de qualquer tipo,
# desde que tenha o comportamento dobrar()

def duplicar(objeto):
    return objeto.dobrar()

numero = Numero(2)
texto = Texto('Dois')

print(duplicar(numero))
print(duplicar(texto))