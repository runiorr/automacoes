from os import walk, mkdir, path, replace

current_path = path.dirname(path.abspath(__file__)) + '/'

(dirpath, dirnames, filenames) = next(walk(current_path))

extensions = set(map(lambda file:file[1], map(path.splitext, filenames)))

for ext in extensions:
    try:
        dir_name = current_path + ext + "_folder/"
        mkdir(dir_name)
        print("Pasta "+ ext +" criada")
    except FileExistsError:
        print("Pasta "+ ext +" já existe")

for file in filenames:
    ext_folder = "." + file.split('.')[-1] + '_folder/'
    if (file == "arquivador.py"):
        continue
    replace(current_path + file, current_path + ext_folder + file)
