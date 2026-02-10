nasc=int(input('Qual o seu ano de nascimento?'))
ano=2026
idade=(nasc-ano)*(-1)
print('Sua idade atual é {} anos!'.format(idade))
arquivo=open('idade.txt','w')
arquivo.write('Ano de nascimento: {} e sua '.format(nasc))
arquivo.write('idade: {} anos!'.format(idade))
arquivo.close()
input('\nPressione ENTER para sair...')






