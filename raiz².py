n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

menor = n1
if n2 < n1:
    menor = n2

maior = n1
if n2 > n1:
    maior = n2

print(f'O quadrado do menor número é {menor ** 2}')
print(f'A raiz quadrada do maior número é {maior ** (1/2)}')
