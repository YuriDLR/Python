nome = 'Murilo'
altura = float(input('Digite ua altura:'))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)

print('Nome:', nome)
print(f'Sua altura é: {altura:.2f}m')
print('Seu peso é:', peso)
print(f'Seu imc: {imc:.2f}')

