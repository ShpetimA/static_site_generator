import os
import shutil

def copy_dir_conent(path, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    files = os.listdir(path) 
    for file in files:
        file_path = os.path.join(path, file)
        dest_path = os.path.join(dest, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest)
        else:
            copy_dir_conent(file_path, dest_path)
