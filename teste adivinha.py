import random

numero_secreto = random.randint(1, 10)

palpite = 0 
tentativa = 0

while palpite != numero_secreto:
    palpite = int(input("Tente adivinhar o numero de (1 ao 10): "))
    tentativa += 1

    if palpite < numero_secreto:
        print("Tente um numero maior!")
    elif palpite > numero_secreto:
        print("Tente um numero menor!")

print(f"Parabens voce acertou em {tentativa} tentativas")