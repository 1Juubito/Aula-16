# Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas.
# Armazene os dados em um dicionário com listas
# Ao encerrar o cadastro, apresente:
# O total de cadastros efetuados
# A média das idades das pessoas
# Uma lista de mulheres com menos de 30 anos
# Uma lista de homens com idade acima da média

cadastro = {'nome':[], 'sexo':[], 'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO')
        continue

    nome = input('Qual o nome?')
    sexo = input('Qual o sexo?')
    ano = input('Qual o ano de nascimento?')
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)
total_cadastros = 0
for i in cadastro['nome']:
    total_cadastros += 1
print(f"Total de cadastros: {total_cadastros}")

# Calcula as idades e a média
idades = [2024 - int(ano) for ano in cadastro['ano']]
media_idades = sum(idades) / total_cadastros
print(f"Média de idades: {media_idades:.2f}")

# Filtra mulheres com menos de 30 anos e homens com idade acima da média
mulheres_jovens = [cadastro['nome'][i] for i in range(total_cadastros) if cadastro['sexo'][i] == 'F' and idades[i] < 30]
homens_acima_media = [cadastro['nome'][i] for i in range(total_cadastros) if cadastro['sexo'][i] == 'M' and idades[i] > media_idades]

print(f"Mulheres com menos de 30 anos: {mulheres_jovens}")
print(f"Homens com idade acima da média: {homens_acima_media}")