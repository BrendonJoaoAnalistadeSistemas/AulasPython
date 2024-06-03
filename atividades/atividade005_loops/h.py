# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 02/06/2024.
# H) Faça um programa que imprima os valores no intervalo definidos pelo usuário.
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

# Importando as bibliotecas do sistema.
import os


# Limapndo o terminal.
os.system('clear')

# Imprimindo título.
print('.'*79)
print('INTERVALO EXCLUINDO NÚMEROS')
print('.'*79)

# Entrada de dados.
while True:
    print('-'*79)
    inicio = input('Digite o início do seu intervalo: ')
    final = input('Digite o final do seu intervalo: ')
    excluir_1 = input('Digite o 1º número que será excluido: ')
    excluir_2 = input('Digite o 2º número que será excluido: ')
    excluir_3 = input('Digite o 3º número que será excluido: ')
    print('-'*79)
    if not(inicio.isnumeric() and final.isnumeric()):
        print('Entrada inválida.')
        print('Por favor digite apenas números.')
    elif (not(excluir_1.isnumeric() and excluir_2.isnumeric() 
              and excluir_3.isnumeric())):
        print('Você só pode excluir números do seu intervalo.')
    else:
        break

# Processamento de dados.
for i in range(int(inicio), int(final)):
    