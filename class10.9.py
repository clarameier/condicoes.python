reta1 = float(input('Diga o valor da sua reta 1: '))
reta2 = float(input('Diga o valor da sua reta 2: '))
reta3 = float(input('Diga o valor da sua reta 3: '))

if reta1 < reta2 + reta3 and reta2  < reta1 + reta3 and reta3  < reta1 + reta2:
    print('Oba! Os segmentos acima podem formar um triângulo!')
else:
    print('Poxa, os segmentos acima não podem formar um triângulo!')