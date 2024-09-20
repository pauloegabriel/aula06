print("\033[47m\033[50m\033[93m")

alunos = {
    'maria': 99,'Clovis': 88, 'Ana':77, 'Dio':66
    }

alunos["Clovis"] = 55 # modificação da matricula

print(alunos)

alunos.pop('Clovis') # remoção

print(alunos)

alunos['kiko'] = 44 # adição de valor

for nome, mat in alunos.items(): # iterando no dicionario
    print(f'matricula: {nome} nome {mat}')

alunosCopia = alunos.copy()
alunosCopia['Ana'] = 33
print('alunos', alunos)    
print('alunos copia', alunosCopia)