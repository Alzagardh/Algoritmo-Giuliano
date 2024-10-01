# print("Olá Mundo!")

# n1 = int(input("Digite um numero: "))
# n2 = int(input("Digite um numero: "))
# soma = n1 + n2
# print(soma)

# numero = int(input("Digite um numero: "))
# if numero % 2 == 0:
#     print(f"O numero {numero} é par")
# else:
#     print(f"O numero {numero} é impar")

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)

print(f"A média das notas é: {media:.2f}")
