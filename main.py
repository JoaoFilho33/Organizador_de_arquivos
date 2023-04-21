import os
import shutil
import re
from utils import systemCall


#caminhoDir = input("Informe o caminho para o diretório Ex(/caminho/para/diretório): ")

caminho_novoDir = input("Informe o caminho para a criação do novo diretório: ")

if os.path.exists(caminho_novoDir):
    print("O caminho existe")
else:
    print("O diretório não existe")

nome_novoDir = input("Informe o nome do novo diretório: ")

systemCall(caminho_novoDir, nome_novoDir)

caminhoAbs = os.path.dirname(os.path.realpath(caminho_novoDir))

lista_arquivos = os.listdir('.')
for arquivo in lista_arquivos:
    print(arquivo)
    if arquivo.endswith('.jpg'):
        nome_arquivo, extensao = os.path.splitext(arquivo) # obter apenas o nome do arquivo sem estensão (ex: .mp3)
        print(nome_arquivo)
        padrao = re.compile(nome_arquivo, re.IGNORECASE)
        print(padrao)
        if padrao.search(nome_arquivo):
                shutil.move(arquivo, nome_novoDir)
                print("entrou")