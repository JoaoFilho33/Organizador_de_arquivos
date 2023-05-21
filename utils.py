import os

def systemCall (caminho, nomeDir):
    try:
        os.chdir(caminho) # acessa o diretório
        os.mkdir(nomeDir) # cria um novo diretório
        print(f"O diretório '{nomeDir}' foi criado com sucesso")
    except OSError as erro:
        print(f"Erro ao criar o diretório '{nomeDir}'")

def menu():
    obs = "Esse app consiste em orgarinizar os arquivos de um diretório\n"
    obs += "Você informa o nome de um arquivo, como o nome de um Artista, e o app buscará no diretório\n"
    obs += "todos as vezes em que ele se repetiu e irá mover para uma pasta de mesmo nome\n"
    obs += "Ex: buscar por: Safadão -> ele irá buscar por safadão e mover todos os arquivos para uma pasta com esse nome\n"
    print(obs)
    print("1 - Informe o caminho para o diretório desejado")
    print("2 - E o título a ser buscado no diretório")  
