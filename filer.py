from os import walk, mkdir, path, replace

current_path = path.dirname(path.abspath(__file__)) + '/'

folder_content = []
for (dirpath, dirnames, filenames) in walk(current_path):
    folder_content.extend(filenames)
    break

extensions = []
for file in folder_content:
    extensions.append(file.split('.')[1])
extensions = set(extensions)

for ext in extensions:
    try:
        dir_name = current_path + str(ext) + "_folder"
        mkdir(dir_name)
    except FileExistsError:
        print("Directory "+ ext +" already exists")

for file in folder_content:
    ext_folder = file.split('.')[1] + '_folder/'
    filename = str(file)
    if (filename == "filer.py"):
        continue
    replace(current_path + filename, current_path + ext_folder + filename)



