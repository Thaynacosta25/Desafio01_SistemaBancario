saldo = 2000
saque = 1500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar saque")