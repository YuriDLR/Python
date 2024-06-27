peso_user = float(input('Digite seu peso: '))
altura_user = float(input('Digite sua altura: '))
imc_user = peso_user / (altura_user * altura_user)
formated_imc = round(imc_user, 2)
if formated_imc < 18.5:
    print('Você está abaixo do peso!')
    print('Seu imc é: ', formated_imc)
elif formated_imc >= 18.5 and formated_imc <= 24.9:
    print('Seu peso está normal!')
    print('Seu imc é:', formated_imc)
elif formated_imc >= 25.0 and formated_imc <=29.9:
    print('Você está com sobrepeso!')
    print('Seu imc é:', formated_imc)
elif formated_imc >= 30.0 :
    print('Você está com obesidade!')
    print('Seu imc é:', formated_imc)
else :
    print('ERROR')