# Le o numero de celulas digitadas pelo usuario
cells = int(input("Informe o numero de celulas: "))

# Le o numero de dias de observacao
days = int(input("Informe o numero de dias: "))

# Inicializa o numero de dias, comecando pelo dia 1
counter = 1

# Loop que vai rodar enquanto o contador for menor ou igual ao numero de dias 
while counter <= days:
# A cada dia, a populacao de celulas dobra
    cells = cells * 2 
    # Exibe o resultado no formato pedido
    print("Day" + str(counter) + ": " + str(cells))

    # Incrementa ao contador para passar para o proximo dia
    counter += 1