import os

def systemCall (caminho, nomeDir):
    try:
        os.chdir(caminho) # acessa o diretório
        os.mkdir(nomeDir) # cria um novo diretório
        print(f"O diretório '{nomeDir}' foi criado com sucesso")
    except OSError as erro:
        print(f"Erro ao criar o diretório '{nomeDir}'")

def menu():
    print("A princípio você deve informar o diretório")