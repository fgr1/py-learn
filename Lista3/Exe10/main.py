from datetime import datetime

def confirm_data(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            data = datetime.strptime(entrada, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida\n")

data1 = confirm_data("Digite a primeira data (dd/mm/aaaa): ")
data2 = confirm_data("Digite a segunda data (dd/mm/aaaa): ")

diff = abs((data2 - data1).days)

print(f"\nDias entre as datas: {diff}.")
