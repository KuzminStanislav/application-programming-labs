import csv
import os

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
            rel_path = os.path.relpath(img_file, cur_dir)  
            writer.writerow([abs_path, rel_path])