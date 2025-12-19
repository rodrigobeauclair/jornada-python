"""
Strings - Trabalhando com Texto em Python.
Demonstra criação, manipulação, indexação e fatiamento de strings.
"""

# ===== CRIANDO STRINGS =====

print("=== CRIAÇÃO DE STRINGS ===")

# Aspas duplas
name = "Fulano"

# Aspas simples (equivalente)
city = 'Rio de Janeiro'

# Aspas triplas (multilinhas)
description = """
This is a multi-line
string that spans
several lines.
"""

print(f"Name: {name}")
print(f"City: {city}")
print(f"Description: {description}")

# ===== CARACTERES DE ESCAPE =====

print("\n=== CARACTERES DE ESCAPE ===")

# Nova linha
text = "Line 1\nLine 2"
print(text)

# Tab
text = "Name:\tRodrigo"
print(text)

# Aspas dentro de string
text = "He said \"Hello\""
print(text)

# Barra invertida literal
path = "C:\\Users\\Rodrigo"
print(path)

# Raw string (ignora escapes)
raw_path = r"C:\Users\Rodrigo"
print(f"Raw: {raw_path}")

# ===== CONCATENAÇÃO =====

print("\n=== CONCATENAÇÃO ===")

first_name = "Rodrigo"
last_name = "Beauclair"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Repetição
separator = "=" * 50
print(separator)

# ===== IMUTABILIDADE =====

print("\n=== IMUTABILIDADE ===")

original = "hello"
uppercase = original.upper()
print(f"Original: {original}")     # Não mudou!
print(f"Uppercase: {uppercase}")   # Nova string

# ===== INDEXAÇÃO =====

print("\n=== INDEXAÇÃO ===")

text = "Python"
#       012345   base 0

print(f"text[0] = {text[0]}")   # P
print(f"text[5] = {text[5]}")   # n

# Índices negativos
print(f"text[-1] = {text[-1]}")  # n (último)
print(f"text[-6] = {text[-6]}")  # P (primeiro)

# ===== SLICING (FATIAMENTO) =====

print("\n=== SLICING ===")

text = "Python Programming"

# Do início até posição 6 (não incluída)
print(f"text[:6] = '{text[:6]}'")        # Python

# Da posição 7 até o final
print(f"text[7:] = '{text[7:]}'")        # Programming

# Do 0 ao 6
print(f"text[0:6] = '{text[0:6]}'")      # Python

# Tudo (cópia)
print(f"text[:] = '{text[:]}'")          # Python Programming

# Com índices negativos
print(f"text[-11:] = '{text[-11:]}'")    # Programming
print(f"text[:-11] = '{text[:-11]}'")    # Python

# Com passo (step)
print(f"text[::2] = '{text[::2]}'")      # Pto rgamn
print(f"text[::-1] = '{text[::-1]}'")    # gnimmargorP nohtyP (invertido!)

# ===== CASOS PRÁTICOS =====

print("\n=== EXEMPLOS PRÁTICOS ===")

# Extrair primeiros 3 caracteres
code = "ABC12345"
prefix = code[:3]
print(f"Prefix: {prefix}")

# Extrair últimos 5
suffix = code[-5:]
print(f"Suffix: {suffix}")

# Inverter string
word = "Reversed"
reversed_word = word[::-1]
print(f"'{word}' invertido: '{reversed_word}'")

# Extrair domínio de email (simplificado)
email = "rodrigo@example.com"
at_index = email.index("@")
domain = email[at_index+1:]
print(f"Domínio de '{email}': {domain}")

# Pegar cada 2ª letra
text = "abcdefghij"
every_other = text[::2]
print(f"Cada 2ª letra de '{text}': '{every_other}'")