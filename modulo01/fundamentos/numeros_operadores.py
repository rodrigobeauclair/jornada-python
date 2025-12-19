"""
Números e Operadores em Python.
Demonstra integers, floats, operadores aritméticos e conversões.
"""

# ===== TIPOS NUMÉRICOS =====

# Integers (int) - números inteiros
age = 35
quantity = 100
negative = -50
big_number = 1_000_000  # Underscores para legibilidade

print("=== INTEGERS ===")
print(f"Age: {age}, tipo: {type(age)}")
print(f"Big number: {big_number}")

# Floats - números decimais
price = 29.90
height = 1.75
scientific = 3.14e2  # Notação científica: 314.0

print("\n=== FLOATS ===")
print(f"Price: {price}, tipo: {type(price)}")
print(f"Scientific: {scientific}")

# ===== OPERADORES ARITMÉTICOS =====

print("\n=== OPERADORES BÁSICOS ===")
a, b = 10, 3

print(f"{a} + {b} = {a + b}")      # Adição
print(f"{a} - {b} = {a - b}")      # Subtração
print(f"{a} * {b} = {a * b}")      # Multiplicação
print(f"{a} / {b} = {a / b}")      # Divisão (sempre float)

print("\n=== OPERADORES ESPECIAIS ===")
print(f"{a} // {b} = {a // b}")    # Divisão inteira
print(f"{a} % {b} = {a % b}")      # Módulo (resto)
print(f"{a} ** {b} = {a ** b}")    # Potência

# ===== PRECEDÊNCIA DE OPERADORES =====

print("\n=== PRECEDÊNCIA ===")
result = 2 + 3 * 4 ** 2 / 2 - 1
print(f"2 + 3 * 4 ** 2 / 2 - 1 = {result}")
# 1. 4 ** 2 = 16
# 2. 3 * 16 = 48
# 3. 48 / 2 = 24.0
# 4. 2 + 24.0 = 26.0
# 5. 26.0 - 1 = 25.0

# Com parênteses para clareza
result = 2 + ((3 * (4 ** 2)) / 2) - 1
print(f"Com parênteses: {result}")

# ===== OPERADORES DE ATRIBUIÇÃO COMPOSTOS =====

print("\n=== OPERADORES COMPOSTOS ===")
x = 10
print(f"x inicial: {x}")

x += 5   # x = x + 5
print(f"x += 5: {x}")

x -= 3   # x = x - 3
print(f"x -= 3: {x}")

x *= 2   # x = x * 2
print(f"x *= 2: {x}")

x /= 4   # x = x / 4
print(f"x /= 4: {x}")

# ===== CONVERSÃO ENTRE TIPOS =====

print("\n=== CONVERSÕES (CASTING) ===")

# Float para int (trunca, não arredonda!)
price = 29.90
price_int = int(price)
print(f"int({price}) = {price_int}")

# Int para float
age = 35
age_float = float(age)
print(f"float({age}) = {age_float}")

# String para número
text = "100"
number = int(text)
print(f'int("100") = {number}')

# Número para string
value = 42
text = str(value)
print(f"str(42) = '{text}', tipo: {type(text)}")

# Arredondamento
value = 3.7
print(f"round({value}) = {round(value)}")
print(f"round(3.14159, 2) = {round(3.14159, 2)}")

# ===== OPERAÇÕES MISTAS =====

print("\n=== INT + FLOAT = FLOAT ===")
result = 10 + 5.5
print(f"10 + 5.5 = {result}, tipo: {type(result)}")

# ===== FUNÇÕES MATEMÁTICAS BUILT-IN =====

print("\n=== FUNÇÕES MATEMÁTICAS ===")
print(f"abs(-10) = {abs(-10)}")
print(f"pow(2, 3) = {pow(2, 3)}")
print(f"max(10, 20, 5) = {max(10, 20, 5)}")
print(f"min(10, 20, 5) = {min(10, 20, 5)}")

# ===== MÓDULO MATH =====

import math

print("\n=== MÓDULO MATH ===")
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.ceil(3.1) = {math.ceil(3.1)}")   # Arredonda para cima
print(f"math.floor(3.9) = {math.floor(3.9)}") # Arredonda para baixo
print(f"math.factorial(5) = {math.factorial(5)}")

# ===== PROBLEMA DE PRECISÃO COM FLOATS =====

print("\n=== PRECISÃO DE FLOATS ===")
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")
print(f"É igual a 0.3? {result == 0.3}")

# Solução: math.isclose()
print(f"math.isclose(result, 0.3)? {math.isclose(result, 0.3)}")

# Ou arredondamento
print(f"round(result, 10) == 0.3? {round(result, 10) == 0.3}")

# ===== EXEMPLOS PRÁTICOS =====

print("\n=== EXEMPLOS PRÁTICOS ===")

# Verificar se número é par
number = 10
is_even = number % 2 == 0
print(f"{number} é par? {is_even}")

# Calcular desconto
original_price = 100
discount_percent = 15
discount_amount = original_price * (discount_percent / 100)
final_price = original_price - discount_amount
print(f"Preço original: R$ {original_price:.2f}")
print(f"Desconto ({discount_percent}%): R$ {discount_amount:.2f}")
print(f"Preço final: R$ {final_price:.2f}")

# Dividir conta entre pessoas
total_bill = 150.75
people = 4
per_person = total_bill / people
print(f"Conta total: R$ {total_bill:.2f}")
print(f"Por pessoa ({people}): R$ {per_person:.2f}")