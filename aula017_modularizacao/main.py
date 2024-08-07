# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Professor: Sebastião Marcos.
# Data: 06/08/2024.

import os

from pacote.modulo_somar import somar
from pacote.subpacote.modulo_multiplicar import multiplicar
from pacote.modulo_divisao import dividir

while True:
    os.system('cls')
    
    a = input('Entre com o valor de A: ')
    b = input('Entre com o valor de B: ')
    
    if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
        print('Por favor, entre com um número válido.')
        continue
    
    a = float(a)
    b = float(b)
    
    resultado_soma = somar(a, b)
    resultado_produto = multiplicar(a, b)
    resultado_divisao, erro = dividir(a, b)
    
    print('-'*79)
    print('CÁLCULOS MATEMÁTICOS')
    print('='*79)
    print(f'Cálculo da soma {resultado_soma}')
    print(f'Cálculo do produto: {resultado_produto}')
    print(f'Cálculo da divisão: {resultado_divisao}, {erro}')
    print('-'*79)
    
    sair = input('Deseja sair do programa? (s/n): ').strip().lower()
    if sair == 's':
        print('Saindo do programa...')
        break