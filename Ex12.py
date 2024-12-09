import os

def lista_arquivos_recusivamente(diretorio):
    arquivos = []
    for item in os.scandir(diretorio):
        if item.is_file():
            arquivos.append(item.path)
        elif item.is_dir():
            arquivos.extend(lista_arquivos_recusivamente(item.path))
    return arquivos

arquivos = lista_arquivos_recusivamente("./Pasta 1")
print(arquivos)
