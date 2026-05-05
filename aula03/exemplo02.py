idade = int(input('digite a idade: '))  # 19
 #>, <, >=, <=, ==, !=


if idade >= 18:
  print('você é adulto')
else: 
  print('você é menor de idade')


# classificação por pontos 
pontos = int(input(' informe os pontos: '))
if pontos >= 100:
    total = pontos + 10
    print(f'Excelente! agora vocÊ tem {total} pontos')
elif pontos >=50:
    total = pontos + 5 
    print(f'Bom desempenho.Você tem {pontos} pontos')
else: 
    print(f'treine mais. Pontuação {pontos} pontos')
    print('fim!')
