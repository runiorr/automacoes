import click
from os import walk, mkdir, path, replace, getcwd
from time import time

""" /home/runior/dev/file-order/files 
"""

@click.command()
@click.option('--path', '-p', help="Pasta a ser organizada", prompt="Diretório completo da pasta")
@click.option('--extension', '-e', help="Arquivos que serão organizados", prompt="Tipos de arquivos (ex: mp3, txt, pdf)")
def organizer(path, extension):
    '''
    Organiza arquivos pela suas extensões, criando pastas e movendo-os.
    '''
    start = time()

    path, extensions, folder_files = check_data(path, extension)

    folder_name = lambda ext: path + ext + "_folder/"
    [make_dir(ext.strip(), folder_name) for ext in extensions]

    [transfer(path, file) for file in folder_files]

    end = time()
    print("\nO script demorou {:.5f} segundos\n{} arquivos transferidos\n{} pastas criadas\n{} arquivos ignorados\n".format(end - start, arquivos, pastas, ignorados))

# Valida os dados passados
def check_data(path, extension):
    if(path):
        if(path[-1] == '/'):
            current_path = path
        else:
            current_path = path + '/'
    else:
        current_path = getcwd() + '/'

    folder_files = next(walk(path))[-1]

    if(extension):
        extensions = set(extension.split(','))
    else:
        extensions = set([path.splitext(file)[-1].split('.')[1] for file in folder_files if not (path.splitext(file)[-1] == '')]) 
    
    return current_path, extensions, folder_files

# Cria pastas para cada extensão encontrada
pastas = 0
def make_dir(ext, folder_name):
    try:
        if (ext == ''):
            return
        mkdir(folder_name(ext))
        global pastas
        pastas += 1
    except FileExistsError:
        return

# Transfere os arquivos
arquivos = 0
ignorados = 0
def transfer(path, file):
    try:
        if (len(file.split('.')) < 2 or file.split('.')[0] == ''):
            global ignorados
            ignorados += 1
            return
        if (file == "file-organizer.py"):
            return   
        ext_folder = file.split('.')[-1] + '_folder/'
        replace(path + file, path + ext_folder + file)
        global arquivos
        arquivos += 1
    except:
        return

