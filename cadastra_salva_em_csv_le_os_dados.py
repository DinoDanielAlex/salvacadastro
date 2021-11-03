import csv
from os import close
with open('users.csv', 'w', encoding='utf-8') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Daniel', 'Alexandre', 'daniel.alex6435@outlook.com', 'Masculino'])
def leitura():
    with open ('users.csv', 'r', encoding='utf-8') as arquivo_open:
        leitor = arquivo_open.read()
        print(leitor)
        arquivo_open.close()

header = ['nome', 'sobrenome']
dados = []
opt = input('Oque deseja fazer?\n 1 - Cadastrar\n  0 - Sair\n')
while opt != '0':
    nome = input('Qual seu nome?')
    sobrenome = input('Qual seu sobrenome?')
    dados.append([nome, sobrenome])
    opt = input('Oque deseja fazer?\n 1 - Cadastrar\n 0 - Sair\n')
print(dados)


with open('users.csv','w', newline='') as arquivo_csv:
    writer= csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerows(dados)
with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)

opt2 = input('Ler ?')
if opt2 == 'Sim':
    print(leitura())
else :
    
    print('Ok, Tchau')

