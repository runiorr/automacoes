import sys, time
from os import walk, mkdir, path, replace

start = time.time()

current_path = path.dirname(path.abspath(__file__)) + '/'

folder_files = next(walk(current_path))[-1]

extensions = set([path.splitext(file)[-1] for file in folder_files if not (path.splitext(file)[-1] == '')])

if (len(extensions) == 1):
    print("Nada para ser arquivado em {}".format(current_path))
    sys.exit()

folder_name = lambda ext: current_path + ext + "_folder/"

def make_dir(ext):
    try:
        if (ext == ''):
            return
        mkdir(folder_name(ext))
        print("Pasta "+ ext +" criada")
    except FileExistsError:
        print("Pasta "+ ext +" já existe")

[make_dir(ext) for ext in extensions]

arquivos = 0

def transfer(file):
    if (len(file.split('.')) < 2):
        print("arquivo {} não possui extensão".format(file))
        return
    if (file == "arquivador.py"):
        return
    ext_folder = "." + file.split('.')[-1] + '_folder/'
    replace(current_path + file, current_path + ext_folder + file)
    global arquivos
    arquivos += 1

[transfer(file) for file in folder_files]

end = time.time()
print("O script demorou {} segundos para organizar {} arquivos\n".format(end - start, arquivos))
