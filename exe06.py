senha = int(input("digite sua senha: "))
cdg =1234
tentativs = 1
while senha != cdg and tentativs <3:
    senha = int(input("digite novamente: "))
    tentativs = tentativs+1
if senha == cdg :
    print("acesso liberado")
else :
    print("acesso bloquedo")


