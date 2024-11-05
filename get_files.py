from icrawler.builtin import GoogleImageCrawler

def image_downloader(keyword: str, dir_path: str) -> None:
    """
    Downloading images from Google using keyword
    :param keyword: word that we need to found
    :param dir_path: path to our directory
    """
    google_crawler = GoogleImageCrawler(storage={'root_dir': dir_path})
    google_crawler.crawl(keyword = keyword, max_num = 50)

