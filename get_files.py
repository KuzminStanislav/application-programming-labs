import os

from icrawler.builtin import GoogleImageCrawler

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