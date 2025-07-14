senha_correta = 1234

senha = ""

while senha != senha_correta:
    senha = int(input("Digite sua senha: ") )
    if senha != senha_correta:
        print("Senha incorreta. Tente novamente! ")
print("Acesso liberado!")
