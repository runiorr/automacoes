#!/usr/bin/python3
import sys, time, argparse
from os import walk, mkdir, path, replace, getcwd

start = time.time()

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", dest="path", help="Pasta a ser organizada")
parser.add_argument("-e", "--extension", dest="extension", help="Tipo dos arquivos")

args = parser.parse_args()

if(args.path):
    if(args.path[-1] == '/'):
        current_path = args.path
    else:
        current_path = args.path + '/'
else:
    current_path = getcwd() + '/'

folder_files = next(walk(current_path))[-1]

if(args.extension):
    extensions = set(args.extension.split(','))
else:
    extensions = set([path.splitext(file)[-1].split('.')[1] for file in folder_files if not (path.splitext(file)[-1] == '')]) 

if (len(folder_files) == 1):
    print("Nada para ser arquivado em {}".format(current_path))
    sys.exit()

folder_name = lambda ext: current_path + ext + "_folder/"

pastas = 0

def make_dir(ext):
    try:
        if (ext == ''):
            return
        mkdir(folder_name(ext))
        global pastas
        pastas += 1
    except FileExistsError:
        return

[make_dir(ext) for ext in extensions]

arquivos = 0

ignorados = 0

def transfer(file):
    try:
        if (len(file.split('.')) < 2 or file.split('.')[0] == ''):
            global ignorados
            ignorados += 1
            return
        if (file == "file-organizer.py"):
            return   
        ext_folder = file.split('.')[-1] + '_folder/'
        replace(current_path + file, current_path + ext_folder + file)
        global arquivos
        arquivos += 1
    except:
        return

[transfer(file) for file in folder_files]

end = time.time()
print("\nO script demorou {:.5f} segundos\n{} arquivos transferidos\n{} pastas criadas\n{} arquivos ignorados\n".format(end - start, arquivos, pastas, ignorados))
