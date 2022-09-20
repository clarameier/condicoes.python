veloc = float(input('Digite quantos a quantos km está o seu carro: '))
velocex = veloc - 80
multa = velocex * 7
if veloc >= 81:
    print('Seu carro está acima da velocidade permitida, que é de 80km/h, portanto você está recebendo uma multa de {:.2f} reais!'.format(multa))
else:
    print('Você não receberá nenhuma multa por estar dirigindo na velocidade permitida, obrigada!')