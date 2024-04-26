# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 26/04/2024.
# B) A empresa "DataMax" está desenvolvendo um novo software de análise estatística e precisa de uma funcionalidade que permita aos usuários inserir três números e, em seguida, exibir na tela qual é o maior número, qual é o menor número ou se os números são todos iguais.
# Essa funcionalidade é crucial para os analistas de dados da "DataMax" que trabalham com conjuntos de dados diversos e precisam rapidamente identificar as características básicas desses conjuntos, como a presença de outliers ou a uniformidade dos números.

# Importando as bibliotecas.
import os


# Limpando o terminal.
os.system('cls')

# Título.
print('.'*70)
print('Sistema Data Max')
print('Verificar se os números são iguais, maiores ou menores')
print('.'*70)

# Entrada/Declaração de variáveis.
print('-'*70)
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite um número: '))
numero3 = float(input('Digite um número: '))
resposta = ''
print('-'*70)

# Processamento
# Condicional para verificar se os numeros são iguais, maiores ou menores.
if numero1 == numero2 and numero2 == numero3:
    resposta = f'{numero1}, {numero2} e {numero3} são iguais'
elif numero1 > numero2 and numero1 > numero3:
    resposta = f'{numero1} é o maior número'
elif numero2 > numero1 and numero2 > numero2:
    pass