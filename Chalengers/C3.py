user = int(input('Digite o ano: '))
if user% 4 == 0:
    print('Este ano é bissexto!')
elif user% 4 != 0:
    print('Este ano não é bissexto!')