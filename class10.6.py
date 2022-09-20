km = float(input('Qual a distância da sua viagem em Km? '))

pass1 = 0.50 * km
pass2 = 0.45 * km

if km <= 200:
    print('O preço da sua passagem será de {:.2f} reais.'.format(pass1))
else:
    print('O preço da sua passagem será de {:.2f} reais.'.format(pass2))
