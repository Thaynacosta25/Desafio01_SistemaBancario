#AND = para ser True tudo tem que ser True
#OR = para ser True apenas um tem que ser True
print(True and True)
print(True and False)
print(False and False)
print(False or True)
print(True or True) 
print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saque >= saldo and saque <= limite or conta_especial and saldo >= saque

print(exp)

exp_2 = (saque >= saldo and saque <= limite) or (conta_especial and saldo >= saque)

print(exp_2)

# Outro exemplo mais inchuto

conta_normal_com_saldo_suficiente = saque >= saldo and saque <= limite

conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(exp_3)