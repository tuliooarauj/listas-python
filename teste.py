def grau_polinomio(polinomio):
    return polinomio.count('^')

polinomios = [['10', '4x^2', '5x']]

polinomios_ordenados = sorted(polinomios, key=grau_polinomio)

print("Polinômios ordenados:")
for polinomio in polinomios_ordenados:
    print(polinomio)
