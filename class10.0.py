#condição código maior
tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

#condição código mais simplificado
tempo = int(input('Quantos anos tem o seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')