import argparse
import csv
import os
from icrawler.builtin import GoogleImageCrawler 
from Iterator import SimpleIterator

def arg_pars() -> tuple:
    """
    Parsing keyword from command promp 
    :return: args 
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('keyword', type = str, help = 'Keyword for searching')
        parser.add_argument('save_dir_path', type = str, help = 'Path to directory for saving images')
        parser.add_argument('path', type = str, help = 'Path to annotation file')
        args = parser.parse_args()
        return args
    except:
        raise SyntaxError("Invalid data")

def image_downloader(keyword: str, dir_path: str) -> None:
    """
    Downloading images from Google using keyword
    :param keyword: word that we need to found
    :param dir_path: path to our directory
    """
    google_crawler = GoogleImageCrawler(storage={'root_dir': dir_path})
    google_crawler.crawl(keyword = keyword, max_num = 50)

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
            rel_path = os.path.relpath(img_file, cur_dir)  
            writer.writerow([abs_path, rel_path])


if __name__ == "__main__":
    try:
        args = arg_pars()
        keyword = args.keyword
        save_path = args.save_dir_path
        annot_path = args.path
        image_downloader(keyword, save_path)
        downloaded_files = get_dir_files(save_path)
        make_annot(annot_path, downloaded_files)
        iterator = SimpleIterator(annot_path)
        for i in iterator:
            print(i)
    except Exception as e:
        print(e)