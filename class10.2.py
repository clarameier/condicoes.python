p1 = float(input('Digite a primeira nota da sua prova: '))
p2 = float(input('Digite a segunda nota da sua prova: '))
media = (p1 + p2)/2
print('A sua média foi {:.1f}'.format(media))
if media >= 6.9:
    print('Parabéns, você passou direto!')
    print('Bom descanso!')
else:
    print('Poxa, infelizmente você está de recuperação!')
    print('Bons estudos e boa sorte.')
