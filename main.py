import argparse
import re

def get_name_of_file() -> str:
    """
    Getting filename
    :return: name of file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='input name of your file')
    args = parser.parse_args()
    return args.filename

def read_file(filename: str) -> str:
    """
    Getting data from file
    :param filename: filename
    :return: file data
    """
    try:
        with open(filename, "r", encoding='utf-8') as file:
            return file.read()
    except:
        raise FileExistError("File doesn't exist")

def get_codes(data: str) -> list[str]:
    """
    Compilating list of codes
    :param data: original data
    :return: list of codes
    """
    pattern_for_split = r'\d+[)+]\n'
    split_data = re.split(pattern_for_split, data)
    pattern = r'\+7 927[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}'
    found_data = []
    for profiles in split_data:
        profiles = profiles.strip()
        codes = re.findall(pattern, profiles)
        if codes:
            found_data.append((profiles, codes))
    return found_data

def print_codes(found_data: list[tuple[str, str]]) -> None:
    """
    Printing list
    :param found_data: final list of codes
    :return: None
    """
    for profiles, codes in found_data:
        print(profiles)
        print()

def main():
    filename = get_name_of_file()
    data = read_file(filename)
    found_data = get_codes(data)
    print_codes(found_data)

if __name__ == "__main__":
    main()
