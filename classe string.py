curso = "pYtHon"

print(curso.upper()) # Ele vai converter todos os caracteres para MAIUSCULO

print(curso.lower()) # Ele vai converter todos os caracteres para minusculo

print(curso.title()) # Ele converte todo o caracteres para minusculo exeto a primeira letra

# ELIMINANDO ESPACO EM BRANCO
curso_1 = "     Java  "

print(curso_1.strip()) # Remove o espaco em branco da esquerda e da direita 

print(curso_1.lstrip()) # Remove o espaco da esquerda

print(curso_1.rstrip()) # Remove todo o espaco da direita

# JUNCAO E CENTRALIZACAO

curso_2 = "Prova"

print(curso_2.center(10, "#"))

print(".".join(curso_2))

