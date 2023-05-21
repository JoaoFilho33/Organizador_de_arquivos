import os
import shutil
import re
from utils import systemCall, menu

menu()
caminho_novoDir = input("Informe o caminho para a criação do novo diretório: ")

if os.path.exists(caminho_novoDir):
    print("O caminho existe")
else:
    print("O diretório não existe")

nome_novoDir = input("Informe o nome do novo diretório: ")

systemCall(caminho_novoDir, nome_novoDir)

padrao = re.compile(nome_novoDir, re.IGNORECASE) # define um padrão para a busca
lista_arquivos = os.listdir('.')
for arquivo in lista_arquivos:
    print(arquivo)
    if arquivo.endswith('.txt'):
        if padrao.search(arquivo): # procura um arquivo com o padrão pré-estabelecido
                shutil.move(arquivo, nome_novoDir)
                print("entrou")