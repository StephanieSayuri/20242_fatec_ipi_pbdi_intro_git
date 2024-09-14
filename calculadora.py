def somar (a, b):
    return a + b

def subtrair (a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def menu():
    texto = """
    1. Somar
    2. Subtrair
    3. Multiplicar
    4. Dividir
    0. Sair
    :  """
    op = -1
    while op!= 0:
        op = int(input(texto))

        if op != 0:
            a = int(input("digite o valor a: "))
            b = int(input("digite o valor b: "))

        if op == 1:
            c = somar(a, b)
        elif op == 2:
            c = subtrair(a, b)
        elif op == 3:
            c = multiplicar(a, b)
        elif op == 4:
            c = dividir(a, b)

        if op != 0:
            print(f"resultado é {c}")

menu()