salario = float(input('Qual o seu salário? R$'))

dez = salario * 0.10
quinze = salario * 0.15

if salario >= 1250.00:
    print('Parabéns, você receberá um aumento de {:.2f} reais!'.format(dez))
else:
    print('Parabéns, você receberá um aumento de {:.2f} reais!'.format(quinze))