# Crie um programa que faça o computador jogar Jokenpô com você.

import random

tipo = 'pedra', 'papel', 'tesoura'
pc = str(random.choice(tipo))

escolha = str(input('Escolha: pedra, papel ou tesoura: '))

print('     JO     ')
print('     KEN    ')
print('     PO     ')

print('Você escolheu: \033[0;30;46m{}\033[m e o computador escolheu: \033[0;30;45m{}\033[m!'.format(
    escolha, pc))

if escolha == 'pedra' and pc == 'pedra' or escolha == 'papel' and pc == 'papel' or escolha == 'tesoura' and pc == 'tesoura':
    print('\033[0;34;40mEmpate\033[m')
elif escolha == 'pedra' and pc == 'tesoura' or escolha == 'tesoura' and pc == 'papel' or escolha == 'papel' and pc == 'pedra':
    print('Você \033[0;30;42mganhou\033[m')
elif escolha == 'pedra' and pc == 'papel' or escolha == 'tesoura' and pc == 'pedra' or escolha == 'papel' and pc == 'tesoura':
    print('Você \033[0;30;41mperdeu\033[m')
elif escolha != 'pedra' or escolha != 'papel' or escolha != 'tesoura':
    print('Escolha novamente!')
