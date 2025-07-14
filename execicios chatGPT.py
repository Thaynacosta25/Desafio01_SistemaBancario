import random # modulo para gerar numeros aleatorios

#Gera numero segreto entre 1 e 20
numero_secreto = random.randint(1, 20)

tentativas = 0 # Contador de tentativas
palpite = 0 # Inicializa palpite

while palpite != numero_secreto:
    palpite = int(input("Tente adivinhar o numero (1 a 20): "))
    tentativas += 1 

    if palpite < numero_secreto:
        print("Tente um numero maior!")
    elif palpite > numero_secreto:
        print("Tente um numero menor!")

print(f"Parabens! voce acertou em {tentativas} tentativas")