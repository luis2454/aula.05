aluno= int(input("digite o numero de alunos: "))
soma = 0
i = 0
while i < aluno :
    nota = float(input("digite a nota"))
    soma = soma +  nota
    i +=1
media = soma / aluno
print(media)
