import datetime, calendar

while True:
    try:
        dia     = int(input("Dia (1-31): "))
        mes     = int(input("Mês (1-12): "))
        ano     = int(input("Ano (4 dígitos): "))
        hora    = int(input("Hora   (0-23): "))
        minuto  = int(input("Minuto (0-59): "))
        segundo = int(input("Segundo(0-59): "))

        data_hora = datetime.datetime(ano, mes, dia, hora, minuto, segundo)
        break
    except (ValueError, TypeError):
        print("Data / hora inválida! Tente novamente.\n")

opcoes = {
    "1": "segundos",
    "2": "minutos",
    "3": "horas",
    "4": "dias",
    "5": "meses",
    "6": "anos"
}

while True:
    print(
        "\nO que deseja acrescentar?"
        "\n1 – Segundos"
        "\n2 – Minutos"
        "\n3 – Horas"
        "\n4 – Dias"
        "\n5 - Meses"
        "\n6 - Anos"
    )
    codigo = input("Escolha 1, 2, 3, 4, 5 ou 6: ").strip()
    if codigo in opcoes:
        break
    print("Opção inválida! Tente novamente.\n")

while True:
    try:
        quantidade = int(input(f"Quantos {opcoes[codigo]} deseja acrescentar? "))
        break
    except ValueError:
        print("Digite um número inteiro.\n")

if codigo == "1":
    nova_data_hora = data_hora + datetime.timedelta(seconds=quantidade)

elif codigo == "2":
    nova_data_hora = data_hora + datetime.timedelta(minutes=quantidade)

elif codigo == "3":
    nova_data_hora = data_hora + datetime.timedelta(hours=quantidade)

elif codigo == "4":
    nova_data_hora = data_hora + datetime.timedelta(days=quantidade)
# Deus que coisa chata
elif codigo == "5":
    total_meses = (data_hora.month - 1) + quantidade
    novo_ano    = data_hora.year  + total_meses // 12
    novo_mes    = (total_meses % 12) + 1

    ultimo_dia  = calendar.monthrange(novo_ano, novo_mes)[1]
    novo_dia    = min(data_hora.day, ultimo_dia)

    nova_data_hora = data_hora.replace(year=novo_ano, month=novo_mes, day=novo_dia)

elif codigo == "6":
    try:
        nova_data_hora = data_hora.replace(year=data_hora.year + quantidade)
    except ValueError:
        nova_data_hora = data_hora.replace(year=data_hora.year + quantidade, day=28)

else:
    nova_data_hora = data_hora

print("\nData-hora original :", data_hora.strftime("%d/%m/%Y %H:%M:%S"))
print("Nova data-hora      :", nova_data_hora.strftime("%d/%m/%Y %H:%M:%S"))
