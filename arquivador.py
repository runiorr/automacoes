import sys
from os import walk, mkdir, path, replace

class error(Exception):
    def __init__(self, file):
        self.msg = file + " permanece no diretório " + current_path

current_path = path.dirname(path.abspath(__file__)) + '/'

folder_files = [files[2] for files in walk(current_path)][0]

if (len(folder_files) == 1):
    print("Nada para ser arquivado")
    sys.exit()

extensions = set([path.splitext(file)[1] for file in folder_files])

dir_name = lambda ext: current_path + ext + "_folder/"

def dir(ext):
    try:
        mkdir(dir_name(ext))
        print("Pasta "+ ext +" criada")
    except FileExistsError:
        print("Pasta "+ ext +" já existe")

ext = [dir(ext) for ext in extensions]

def transfer(file):
    try:
        ext_folder = "." + file.split('.')[-1] + '_folder/'
        if (file == "arquivador.py"):
            raise error(file) 
        replace(current_path + file, current_path + ext_folder + file)
    except error as e:
        print(e.msg)

file = [transfer(file) for file in folder_files]
