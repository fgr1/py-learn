import datetime

while True:
    try:
        dia  = int(input("Dia (1-31): "))
        mes  = int(input("Mês (1-12): "))
        ano  = int(input("Ano (4 dígitos): "))
        # Verifica se a data é válida
        data = datetime.date(ano, mes, dia)
        break
    except (ValueError, TypeError):
        print("Data inválida! Tente novamente.\n")

while True:
    print(
        "\nComo deseja exibir a data?"
        "\n1 – Simples      (ex.: 10/08/1990)"
        "\n2 – Abreviada    (ex.: 10/ago/1990)"
        "\n3 – Completa     (ex.: 10 de agosto de 1990)"
    )
    codigo = input("Escolha 1, 2 ou 3: ").strip()
    if codigo in ("1", "2", "3"):
        break
    print("Código inválido! Digite 1, 2 ou 3.\n")

meses_abrev  = ["jan", "fev", "mar", "abr", "mai", "jun",
                "jul", "ago", "set", "out", "nov", "dez"]
meses_compl  = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
                "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

dia  = f"{data.day:02d}"
mesN = data.month
ano  = f"{data.year}"

if codigo == "1":
    resultado = f"{dia}/{mesN:02d}/{ano}"

elif codigo == "2":
    resultado = f"{dia}/{meses_abrev[mesN-1]}/{ano}"

else:
    resultado = f"{dia} de {meses_compl[mesN-1]} de {ano}"

print("\nData formatada:", resultado)
