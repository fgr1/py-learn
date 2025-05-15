disciplina = input("Digite o nome da disciplina: ")

NOTAS = 4
nota_1 = float(input(f"Digite a 1ª nota: "))
nota_2 = float(input(f"Digite a 2ª nota: "))
nota_3 = float(input(f"Digite a 3ª nota: "))
nota_4 = float(input(f"Digite a 4ª nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / NOTAS

print(f"Média da {disciplina} = {media:.2f}")
