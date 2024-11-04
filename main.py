from parser import arg_pars
from get_files import image_downloader
from get_files import get_dir_files
from make_annotation import make_annot
from icrawler.builtin import GoogleImageCrawler 
from Iterator import SimpleIterator

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