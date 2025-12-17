'''
Demonstração de variáveis e atribuição em Python.
Explora nomenclatura, tipos básicos e operações.
'''

# Atribuição simples
name = 'Fulano da Silva'
age = 25
height = 1.75
is_learning_python = True

# Exibindo valores
print('=== Informações Pessoais ===')
print(f'Nome: {name}')
print(f'Idade: {age}')
print(f'Altura: {height}m')
print(f'Estudando Python: {is_learning_python}')

# Exibindo tipos
print('\n=== Tipos das Variáveis ===')
print(f'Tipo de "name": {type(name)}')
print(f'Tipo de "age": {type(age)}')
print(f'Tipo de "height": {type(height)}')
print(f'Tipo de "is_learning_python": {type(is_learning_python)}')

# Atribuição múltipla
x, y, z = 10, 20, 30
print(f'\n=== Atribuição Múltipla ===')
print(f'x = {x}, y = {y}, z = {z}')

# Trocando valores
print('\n=== Troca de Valores ===')
print(f'Antes: x = {x}, y = {y}')
x, y = y, x
print(f'Agora: x = {x}, y = {y}')

# Mesma variável, tipos diferentes (tipagem dinâmica)
print('\n=== Tipagem Dinâmica ===')
variable = 100
print(f'variable = {variable}, tipo: {type(variable)}')

variable = 'Agora é um texto'
print(f'variable = {variable}, tipo: {type(variable)}')

variable = 3.14
print(f'variable = {variable}, tipo: {type(variable)}')