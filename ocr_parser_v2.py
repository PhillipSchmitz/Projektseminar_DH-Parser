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
            if not re.search(r"^-*\d+-*", sage):
                if not re.search(r"-+\s\n*", sage):
                    if not re.search(r"―+\s*\n", sage):
                        if not re.search(r"!+", sage):
                            if not re.search(r"^\w\s\n$", sage):
                                if not re.search(r"@", sage):
                                    if not re.search(r"\*", sage):
                                        if not re.search(r"•\s*\n", sage):
                                            if not re.search(r"—\s*\n", sage):
                                                if add:
                                                    s.append(sage[:-1])
        else:
            s.append("page_marker_ocr" + str(page + 20) + "\n")
            s.append("page_marker_book" + str(page) + "\n")
            page += 1
    return sort_sagen


def parse_elsass(text: list, titles: list):
    sort_sagen = []
    i = 0
    s = []
    page = 1
    page_memory = []
    for sage in text:
        add = True
        if titles[i] + ".\n" in sage or titles[i] + ". \n" in sage or titles[i] + "\n" in sage:
            print(sage)
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
            # print(i + 1)
            # print(titles[i])
        if not re.search(r"-+ Page \d+-+", sage):
            if not re.search(r"^-*\d+-*", sage):
                if not re.search(r"-+\s\n*", sage):
                    if not re.search(r"―+\s*\n", sage):
                        if not re.search(r"!+", sage):
                            if not re.search(r"^\w\s\n$", sage):
                                if not re.search(r"@", sage):
                                    if not re.search(r"\*", sage):
                                        if not re.search(r"•\s*\n", sage):
                                            if not re.search(r"—\s*\n", sage):
                                                if not re.search(r"[-—―\d]+\s*\n", sage):
                                                    if add:
                                                        s.append(sage[:-1])
        else:
            s.append("page_marker_ocr" + str(page + 20) + "\n")
            s.append("page_marker_book" + str(page) + "\n")
            page += 1
    print(len(sort_sagen))
    return sort_sagen
    # return ["!This is under construction!"]


def parse_geschichten_moseltal(text: list, titles: list):
    sort_sagen = []
    i = 0
    s = []
    page = 1
    page_memory = []
    for sage in text:
        add = True
        if titles[i] + ".\n" in sage or titles[i] + ". \n" in sage or titles[i] + "\n" in sage:
            print(sage)
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
            print(i + 1)
            print(titles[i])
        if not re.search(r"Page \d+", sage):
            if not re.search(r"-*\d+-*", sage):
                if not re.search(r"-+\s\n*", sage):
                    if not re.search(r"―+\s*\n", sage):
                        if not re.search(r"!+", sage):
                            if not re.search(r"^\w\s\n$", sage):
                                if not re.search(r"@", sage):
                                    if not re.search(r"\*", sage):
                                        if not re.search(r"•\s*\n", sage):
                                            if not re.search(r"—\s*\n", sage):
                                                if not re.search(r"[-—―\d]+\s*\n", sage):
                                                    if add:
                                                        s.append(sage[:-1])
        else:
            s.append("page_marker_ocr" + str(page + 20) + "\n")
            s.append("page_marker_book" + str(page) + "\n")
            page += 1
    print(len(sort_sagen))
    return sort_sagen

    # return ["!This is under construction"]


def write_tale(name: str, text_list: list):
    print(len(text_list))
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
    name, titles = initiate.oberelsass()
    text = read_text(name)
    sep_text = parse_elsass(text, titles)
    del sep_text[0]
    print_tale(sep_text)
    write_tale(name, sep_text)


def parse_unterelsass_full():
    """
    Manages parsing and writes book unterelsass to pickle
    :return: None
    """
    name, titles = initiate.unterelsass()
    text = read_text(name)
    sep_text = parse_elsass(text, titles)
    del sep_text[0]
    print_tale(sep_text)
    write_tale(name, sep_text)


def parse_moseltal_full():
    """
    Manages parsing and writes book unterelsass to pickle
    :return: None
    """
    name, titles = initiate.moseltal()
    text = read_text(name)
    sep_text = parse_elsass(text, titles)
    del sep_text[0]
    print_tale(sep_text)
    write_tale(name, sep_text)


def parse_pfalz_1(text: list, titles: list, cat: list, group: list):
    sort_sagen = []
    i = 0
    s = []
    page = 1
    page_memory = []
    add = True
    for sage in text:
        add = True
        if titles[i] + ".\n" in sage:
            # print(sage)
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
            # print(i + 1)
            # print(titles[i])
        if not re.search(r"Page\s?\d+", sage):
            for c in cat:
                if c in sage:
                    add = False
            for g in group:
                if g in sage:
                    add = False
            if not re.search(r"^\d+$", sage):
                if not re.search(r"^$", sage):
                    if add:
                        s.append(sage[:-1])
        else:
            # print("Y")
            s.append("page_marker_ocr" + str(page + 30) + "\n")
            s.append("page_marker_book" + str(page) + "\n")
            page += 1
    # print(sort_sagen)
    return sort_sagen
    # return ["!This is under construction!"]


def parse_pfalz_2(text: list, titles: list, cat: list, group: list):
    sort_sagen = []
    i = 0
    s = []
    page = 1
    page_memory = []
    # print(titles)
    for sage in text:
        if titles[i] + ".\n" in sage:
            # print(sage)
            # print(titles[i])
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
            # print(i + 1)
            # print(titles[i])
        if not re.search(r"^\d\d\d$", sage):
            if not re.search(r"^$", sage):
                s.append(sage[:-1])
        else:
            # print("Y")
            s.append("page_marker_ocr" + str(int(sage) + 31) + "\n")
            s.append("page_marker_book" + str(int(sage) + 1) + "\n")
            page += 1
    # print(sort_sagen)
    return sort_sagen
    # return ["!This is under construction!"]

def parse_pfalz_3(text: list, titles: list, cat: list, group: list):
    sort_sagen = []
    i = 0
    s = []
    page = 283
    page_memory = []
    line = True
    #print(titles)
    for sage in text:
        line = True
        if titles[i] + ".\n" in sage or titles[i] + "\n" in sage:
            #print(sage)
            line = False
            # print(titles[i])
            mem = False
            if i != 0:
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
            # print(i + 1)
            # print(titles[i])
        if not re.search(r"^(-\s?\d\d\d)|^(\d\d\d\s?-)|^(-\s?\d\d\d\s?-)", sage):
            if not re.search(r"^\?", sage):
                if not re.search(r"^$", sage):
                    s.append(sage[:-1])
        else:
            #print(sage)
            #print(page)
            if page == 332:
                page = 335
            s.append("page_marker_ocr" + str(page + 30) + "\n")
            s.append("page_marker_book" + str(page) + "\n")
            t = re.sub(r"^(-\s?\d\d\d)|^(\d\d\d\s?-)|^(-\s?\d\d\d\s?-)", "", sage)
            if t and line:
                s.append(t)
            page += 1
    # print(sort_sagen)
    #print(page)
    return sort_sagen
    # return ["!This is under construction!"]
def parse_pfalz_full():
    name, titles, cat, group, num = initiate.pfalz()
    text = read_text(name[0])
    sep_text_1 = parse_pfalz_1(text, titles, cat, group)
    del sep_text_1[0]
    # print_tale(sep_text_1)
    text = read_text(name[1])
    sep_text_2 = parse_pfalz_2(text, titles[num[0]:], cat, group)
    del sep_text_2[0]
    #print_tale(sep_text_2)
    text = read_text(name[2])
    sep_text_3 = parse_pfalz_3(text, titles[num[1]:], cat, group)
    del sep_text_3[0]
    #print_tale(sep_text_3)
    sep_text = sep_text_1 + sep_text_2 + sep_text_3
    print_tale(sep_text)
    write_tale("pfalz_sagen", sep_text)



def parse_erzählungen_moselthal(text, titles):
    sort_sagen = []
    i = 0
    s = [[]]
    page = 1
    page_memory = []
    for sage in text:
        add = True
        #print(sage)
        if titles[i] in sage:
            print(sage)
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
            # print(i + 1)
            # print(titles[i])
        if not re.search(r"Page \d+", sage):
            if not re.search(r"-*\d+-*", sage):
                if not re.search(r"-+\s\n*", sage):
                    if not re.search(r"―+\s*\n", sage):
                        if not re.search(r"!+", sage):
                            if not re.search(r"^\w\s\n$", sage):
                                if not re.search(r"", sage):
                                    if not re.search(r"\*", sage):
                                        if not re.search(r"•\s*\n", sage):
                                            if not re.search(r"—\s*\n", sage):
                                                if not re.search(r"[-—―\d]+\s*\n", sage):
                                                    if add:
                                                        s.append(sage[:-1])
        else:
            print(page)
            s.append("page_marker_ocr" + str(page + 20) + "\n")
            s.append("page_marker_book" + str(page) + "\n")
            page += 1
    print(len(sort_sagen))
    return sort_sagen
    # return ["!This is under construction!"]

def parse_erzählungen_moseltal_full():
    name, titles = initiate.erzählungen_moseltal()
    text = read_text(name)
    #print(text)
    sep_text = parse_erzählungen_moselthal(text, titles)

def print_tale(book: list):
    """
    Prints list of lists in readable format
    :param book: list of lists of tale book
    :return: None
    """
    for tale in book:
        print(tale)
    print(len(book))


def parse():
    """
    Main function to parse raw data and prepare for XML-creation
    :return: None
    """
    book_names = {1: "Trier und Umgebung", 2: "Lothringen", 3: "Oberelsass", 4: "Unterelsass", 5: "Moseltal",
                  6: "Geschichten Moseltal", 7: "Pfalz", 8: "Erzählungen Moselthal"}
    book = book_names[2]
    if book == "Trier und Umgebung":
        print("Parsing Trier und Umgebung")
        parse_trier_umgebung_full()
    elif book == "Lothringen":
        print("Parsing Lothringen")
        parse_lothringen_full()
    elif book == "Oberelsass":
        print("Parsing Oberelsass")
        parse_oberelsass_full()
    elif book == "Unterelsass":
        print("Parsing Unterelsass")
        parse_unterelsass_full()
    elif book == "Moseltal":
        print("Parsing Moseltal")
        parse_moseltal_full()
    elif book == "Geschichten Moseltal":
        parse_geschichten_moseltal_full()
    elif book == "Pfalz":
        parse_pfalz_full()
    elif book == "Erzählungen Moselthal":
        parse_erzählungen_moseltal_full()

parse()
