# Você foi contratado para desenvolver um programa que calcule a média de notas dos alunos de uma turma. 
# Para isso, você deverá criar uma lista com as notas de cada aluno e, em seguida, implementar uma função que calcule a média aritmética das notas. 
# Além disso, você deverá utilizar um loop while para pedir ao usuário que insira as notas dos alunos até que ele decida parar. 
# Por fim, você deverá utilizar um loop for para imprimir a média de cada aluno.

# a) Escreva o código para a função que calcule a média aritmética das notas.

# b) Escreva o código para o loop while que pede ao usuário que insira as notas dos alunos.

# c) Escreva o código para o loop for que imprime a média de cada aluno.


def calculo_notas(notas_alunos):
    resultado_notas = 0
    numero_notas = 0
    
    for valor in notas_alunos:
        resultado_notas += valor
        numero_notas += 1 
    
    media = resultado_notas / numero_notas
   
condicional = 's'
notas_aluno = []
aluno = input('Digite o nome do aluno: ')


while condicional == 's':
    notas = input('Digite as notas do aluno: ')
    notas_aluno.append(notas)
    condicional = input('Deseja adicionar mais notas: ')

 