#Recursividade
def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)

print(potencia(2, 3))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))


def contar_digitos(numero):
    if numero == 0:
        return 0
    else:
        return 1 + contar_digitos(numero // 10)

print(contar_digitos(12345))




