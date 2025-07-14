import time

tempo = 0 
fim = int(input("Digite quantos segundos quer contar: "))

while tempo <= fim:
    print(f"{tempo} segundo(s) ")
    time.sleep(1) # Espera 1 segundo
    tempo += 1
print("Tempo finalizado! ")
