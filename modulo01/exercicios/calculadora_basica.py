"""
Programa que pede dois números ao usuário e exibe operações matemáticas básicas.
"""

print('=== CALCULADORA BÁSICA ===\n')

number1 = float(input('Digite o primeiro número: '))
number2 = float(input('Digite o segundo número: '))

print('\n=== RESULTADOS ===')
print(f'{number1} + {number2} = {(number1 + number2):.2f}')
print(f'{number1} - {number2} = {(number1 - number2):.2f}')
print(f'{number1} x {number2} = {(number1 * number2):.2f}')
print(f'{number1} / {number2} = {(number1 / number2):.2f}')
print(f'{number1} // {number2} = {(number1 // number2):.2f} (divisão inteira)')
print(f'{number1} % {number2} = {(number1 % number2):.2f} (resto)')
print(f'{number1} ** {number2} = {(number1 ** number2):.2f} (potência)')