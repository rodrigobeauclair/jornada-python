"""
Exercício: Variáveis e tipos de dados
Cria variáveis para produto de e-commerce e demonstra operações básicas.
"""

name_product = 'Camisa'
price = 29.90
quantity = 7
is_available = True
total_stock_value = price * quantity

# Exibição das informações do produto
print('=== Informações do Produto ===')
print(f'Produto: {name_product}')
print(f'Preço unitário: R$ {price:.2f}')
print(f'Quantidade: {quantity}')
print(f'Disponível: {is_available}')
print(f'Valor total em estoque: R$ {total_stock_value:.2f}')

# Exibição dos tipos
print('\n=== Tipos das Variáveis ===')
print(f'Tipo de "name_product": {type(name_product)}')
print(f'Tipo de "price": {type(price)}')
print(f'Tipo de "quantity": {type(quantity)}')
print(f'Tipo de "is_available": {type(is_available)}')
print(f'Tipo de "total_stock_value": {type(total_stock_value)}')