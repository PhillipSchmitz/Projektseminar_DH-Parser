import re
import initiate


def set_dir(filename: str):
    """
    Creates a the file path
    :param filename: name of file
    :return: path to file
    """
    return "ocr_sagen/" + filename


def read_text(name: str):
    """
    Gets filepath from set_dir() and reads text from file into list
    :param name: name of file
    :return: list with lines as elements
    """
    path = set_dir(name)
    with open(path, "r", encoding="utf-8") as f:
        text = f.readlines()

    return text


def seperate_text(text: list, titles: list, cat: list):
    """
    Version 1 to extract text (not working properly)
    :param text: list containing lines as elements
    :param titles: list of tale titles
    :param cat: list of tale categories
    :return: list of lists containing title, category, page and text for each tale
    """
    sort_sage = []
    sage = []
    page = 1
    for line in text:
        #print(titles[0])
        #print(line)
        add = True
        for item in cat:
            if item + ".\n" == line:
                #print(line)
                add = False
                break
            if item[4:] + ".\n":
                #print(line)
                add = False
                break
        if not add:
            continue
        if titles[0] in line:
            sort_sage.append(sage)
            sage = []
            sage.append("name_marker" + line)
            del titles[0]
        elif re.search(r"----- \d+ / \d+ -----", line):
            sage.append("page_marker_ocr" + str(page + 28))
            sage.append("page_marker_book" + str(page))
            page += 1
        elif re.search(r"\d+", line):
            continue
        else:
            sage.append(line)
    return sage


def seperate_text_v2(text: list, titles: list, categories: list):
    """
    Version 2: works better (maybe no proper page insertion)
    Extracts tales from unsorted data
    :param text: list containing lines as elements
    :param titles: list of tale titles
    :param categories: list of tale categories
    :return: list of lists containing title, category, page and text for each tale
    """
    sort_sagen = []
    i = 0
    s = []
    page = 1
    for sage in text:
        add = True
        if titles[i] in sage:
            i += 1
            sort_sagen.append(s)
            s = []
        if not re.search(r"----- \d+ / \d+ -----", sage):
            if not re.search(r"\d+", sage):
                for cat in categories:
                    cat = cat + ".\n"
                    if sage == cat:
                        add = False
                        break
                    cat = cat[4:]
                    if sage == cat:
                        add = False
                        break
                if add:
                    s.append(sage)
        else:
            s.append("page_marker_ocr" + str(page+28))
            s.append("page_marker_book" + str(page))
            page += 1
    return sort_sagen


def main():
    """
    main function to parse raw data and prepare for xml-creation
    :return: None
    """
    name, titles, categories, dict = initiate.trier_und_umgebung()
    text = read_text(name)
    #sep_text = seperate_text(text, titles, categories)
    sep_text = seperate_text_v2(text, titles, categories)
    for item in sep_text:
        print(item)
    #print(len(sep_text))
main()