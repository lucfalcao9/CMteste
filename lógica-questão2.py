ano = int(input('Digite o ano do seu nascimento: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))
