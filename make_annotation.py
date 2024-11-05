import csv
import os

def get_dir_files(dir_path: str) -> list:
    """
    Finding names of files in directory
    :param dir_path: path to our directory
    :return: list of file names 
    """
    try:
        paths_to_img = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                paths_to_img.append(os.path.join(root, file))
            return paths_to_img
    except:
        raise NotADirectoryError("Invalid directory")

def make_annot(annot_path: str, files: list) -> None:
    """
    Making annotation 
    :param annot_path: path to annotation
    :param files: list of files
    """
    cur_dir = os.path.dirname(annot_path)
    with open(annot_path, mode = 'w', newline= '', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Absolute path", "Relative path"])  
            
        for img_file in files:
            abs_path = os.path.abspath(img_file)  
            rel_path = os.path.relpath(os.path.join(cur_dir, img_file)) 
            writer.writerow([abs_path, rel_path])