import re
import initiate
import pickle
import testing


def set_dir(filename: str):
    """
    Creates a the file path
    :param filename: name of file
    :return: path to file
    """
    return "ocr_sagen/" + filename + ".txt"


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
        # print(titles[0])
        # print(line)
        add = True
        for item in cat:
            if item + ".\n" == line:
                # print(line)
                add = False
                break
            if item[4:] + ".\n":
                # print(line)
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


def parse_trier_umgebung(text: list, titles: list, categories: list):
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
    page_memory = []
    for sage in text:
        add = True
        if titles[i] + ".\n" in sage:
            mem = False
            if "page_marker" in s[-1]:
                page_memory = []
                page_memory.append(s[-2])
                page_memory.append(s[-1])
                del s[-2:]
                mem = True
            sort_sagen.append(s)
            s = []
            s.append(titles[i])
            if mem:
                s.append(page_memory[0])
                s.append(page_memory[1])
            i += 1
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
            s.append("page_marker_ocr" + str(page + 28) + "\n")
            s.append("page_marker_book" + str(page) + "\n")
            page += 1
    return sort_sagen


def parse_lothringen(text: list, titles: list):
    """
    Extracts all tales from the book Sagen und Bilder aus Lothringens Vorzeit, cleans them and adds page numbers
    :param text: List of every line in the book (except beginning)
    :param titles: List of tale titles
    :return: List of lists where one list contains one tale
    """
    sort_sagen = []
    i = 0
    s = []
    page = 1
    page_memory = []
    for sage in text:
        add = True
        if titles[i] + ".\n" in sage or titles[i] + ". \n" in sage or titles[i] + "\n" in sage:
            mem = False
            if "page_marker" in s[-1]:
                page_memory = []
                page_memory.append(s[-2])
                page_memory.append(s[-1])
                del s[-2:]
                mem = True
            sort_sagen.append(s)
            s = []
            s.append(titles[i])
            if mem:
                s.append(page_memory[0])
                s.append(page_memory[1])
            i += 1
        if not re.search(r"-+ Page \d+-+", sage):
            if not re.search(r"-*\d+-*", sage):
                if not re.search(r"-+", sage):
                    if not re.search(r"―+", sage):
                        if not re.search(r"!+", sage):
                            if not re.search(r"\w\s\n", sage):
                                if add:
                                    s.append(sage[:-1])
        else:
            s.append("page_marker_ocr" + str(page + 20) + "\n")
            s.append("page_marker_book" + str(page) + "\n")
            page += 1
    return sort_sagen


def parse_elsass(text: list, titles: list):
    pass


def write_tale(name: str, text_list: list):
    with open("parsed_sagen/" + name + ".pkl", "wb") as f:
        pickle.dump(text_list, f)


def parse_trier_umgebung_full():
    """
    Manages parsing and writes book trier und umgebung to pickle
    :return: None
    """
    name, titles, categories, dict = initiate.trier_und_umgebung()
    text = read_text(name)
    sep_text = parse_trier_umgebung(text, titles, categories)
    del sep_text[0]
    print_tale(sep_text)
    write_tale(name, sep_text)
    print(testing.test_trier_umgebung(sep_text))


def parse_lothringen_full():
    """
    Manages parsing and writes book lothringen to pickle
    :return: None
    """
    name, titles = initiate.lothringen()
    text = read_text(name)
    sep_text = parse_lothringen(text, titles)
    del sep_text[0]
    print_tale(sep_text)
    write_tale(name, sep_text)


def parse_oberelsass_full():
    """
    Manages parsing and writes book oberelsass to pickle
    :return: None
    """
    pass


def parse_unterelsass_full():
    """
    Manages parsing and writes book unterelsass to pickle
    :return: None
    """
    pass


def print_tale(book: list):
    """
    Prints list of lists in readable format
    :param book: list of lists of tale book
    :return: None
    """
    for tale in book:
        print(tale)


def parse():
    """
    Main function to parse raw data and prepare for XML-creation
    :return: None
    """
    book_names = {1: "Trier und Umgebung", 2: "Lothringen", 3: "Oberelsass", 4: "Unterelsass"}
    book = book_names[2]
    if book == "Trier und Umgebung":
        print("Parsing Trier und Umgebung")
        parse_trier_umgebung_full()
    elif book == "Lothringen":
        print("Parsing Lothringen")
        parse_lothringen_full()
    elif book == "Oberelsass":
        parse_oberelsass_full()
    elif book == "Unterelsass":
        parse_unterelsass_full()


parse()
