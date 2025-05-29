hex_digitos = "0123456789ABCDEF"

decimal = int(input("Digite um número: "))

if decimal == 0:
    print("Vvalor hexadecimal: 0")
else:
    resultado = ""

    while decimal > 0:
        resto = decimal % 16
        resultado = hex_digitos[resto] + resultado
        decimal //= 16

    print("Valor hexadecimal:", resultado)
