import argparse

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