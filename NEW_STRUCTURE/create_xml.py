from xml.etree import ElementTree as ET
import pickle
import json
from os.path import join
import glob

# import initiate

# ====Parameters====
"""
import trier_und_umgebung_input_parameters as input1  # change to desired input file
import oberelsass_input_parameters as input2
import unterelsass_input_parameters as input3
import moseltal_input_parametrs as input4
import lothringen_input_parametrs as input5
import pfalz_input_parameters as input6
"""

# NAME = "moseltal"
# NAME = "oberelsass"
# NAME = "unterelsass"
# NAME = "lothringen"
# NAME = "pfalz"
# NAME = "trier"

PAGE = 1


def retrieve_list(name):
    # with open("/parsed_sagen/" + name + ".pkl", "rb") as f:
    with open(
            r"C:\Users\binz3\Dokumente\Uni\STeM\Semester 4\Projektseminar\Projektseminar_DH-Parser\parsed_sagen" + "\\" + name + ".pkl",
            "rb") as f:
        tale_list = pickle.load(f)
    return tale_list


def create_xml_tree():
    """
    creates TEI root element and TEI header
    :return:
    """
    tei = ET.Element("TEI", {"xmlns": "http://www.tei-c.org/ns/1.0"})
    tree = ET.ElementTree(tei)
    tei_header = ET.SubElement(tei, "teiHeader")
    text = ET.SubElement(tei, "text")
    front = ET.SubElement(text, "front")
    body = ET.SubElement(text, "body")
    back = ET.SubElement(text, "back")

    return tei_header, body, tree, front, back


def create_tei_header(tei_header: ET, meta: dict):
    fileDesc = ET.SubElement(tei_header, "fileDesc")
    titleStmt = ET.SubElement(fileDesc, "titleStmt")
    publicationStmt = ET.SubElement(fileDesc, "publicationStmt")
    sourceDesc = ET.SubElement(fileDesc, "sourceDesc")
    title_full = ET.SubElement(titleStmt, "title", {"type": "full"})
    title_main = ET.SubElement(title_full, "title", {"type": "main"})
    title_main.text = meta["fileDesc"]["title"]
    title_sub = ET.SubElement(title_full, "title", {"type": "sub"})
    title_sub.text = meta["fileDesc"]["subtitle"]
    author = ET.SubElement(titleStmt, "author")
    author.text = meta["fileDesc"]["author"]
    publisher = ET.SubElement(publicationStmt, "publisher")
    publisher.text = meta["fileDesc"]["publisher"]
    address = ET.SubElement(publicationStmt, "address")
    placeName = ET.SubElement(address, "placeName")
    placeName.text = meta["fileDesc"]["address"]
    date = ET.SubElement(publicationStmt, "date", {"when": meta["fileDesc"]["date"]})
    date.text = meta["fileDesc"]["date"]
    src = ET.SubElement(sourceDesc, "p")
    src.text = meta["fileDesc"]["sourceDesc"]

    encodingDesc = ET.SubElement(tei_header, "encodingDesc")
    projectDesc = ET.SubElement(encodingDesc, "projectDesc")
    p = ET.SubElement(projectDesc, "p")
    p.text = meta["encodingDesc"]["projectDesc"]
    editorialDecl = ET.SubElement(encodingDesc, "editorialDecl")
    correction = ET.SubElement(editorialDecl, "correction")
    p = ET.SubElement(correction, "p")
    p.text = meta["encodingDesc"]["editorialDecl"]["correction"]
    normalization = ET.SubElement(editorialDecl, "normalization")
    p = ET.SubElement(normalization, "p")
    p.text = meta["encodingDesc"]["editorialDecl"]["normalization"]
    segmentation = ET.SubElement(editorialDecl, "segmentation")
    p = ET.SubElement(segmentation, "p")
    p.text = meta["encodingDesc"]["editorialDecl"]["segmentation"]

    profileDesc = ET.SubElement(tei_header, "profileDesc")
    abstract = ET.SubElement(profileDesc, "abstract")
    p = ET.SubElement(abstract, "p")
    p.text = meta["profileDesc"]["abstract"]
    langUsage = ET.SubElement(profileDesc, "langUsage")
    for lang in meta["profileDesc"]["langUsage"]:
        language = ET.SubElement(langUsage, "language", {"ident": lang["ident"]})
        language.text = lang["name"]
    textClass = ET.SubElement(profileDesc, "textClass")
    classCode = ET.SubElement(textClass, "classCode", {"scheme": meta["profileDesc"]["classCode"]})


def create_front(front: ET.Element, front_text: list):
    if len(front_text) == 3:
        grimm = ET.SubElement(front, "ab")
        grimm.text = front_text[2]
    ab = ET.SubElement(front, "ab", {"type": "foreword"})
    ab.text = front_text[0]
    index = ET.SubElement(front, "ab", {"type": "index"})
    index.text = front_text[1]


def create_category(body: ET, cat: str, number: int):
    category = ET.SubElement(body, "div", {"type": "category", "n": str(number)})
    cat_head = create_head(category, cat)
    return category


def create_group(body: ET, group_name: str, number: int):
    group = ET.SubElement(body, "div", {"type": "group", "n": str(number)})
    gr_head = create_head(group, group_name)
    return group


def create_head(div: ET, name: str):
    head = ET.SubElement(div, "head")
    head.text = name
    return head


def create_sage(category: ET, sage: str, number: int):
    """
    creates an xml TEI body part containing a tale
    :param body: TEI body tag
    :param sage:
    :param number:
    :return:
    """
    div3 = ET.SubElement(category, "div", {"type": "tale"})
    title = ET.SubElement(div3, "head", {"n": str(number)})
    title.text = sage
    return div3


def create_text(tale: ET, text: list):
    global PAGE
    content = ET.SubElement(tale, "p")
    for tale_line in text:
        if "page_marker_book" in tale_line:
            p = ET.SubElement(content, "pb", {"n": str(PAGE)})
            PAGE += 1
        elif "page_marker_ocr" in tale_line:
            continue
        else:
            l = ET.SubElement(content, "l")
            l.text = tale_line[:-1]


def create_book(body: ET, book: list, dictionary: dict, division: list):
    i_cat = 1
    i_group = 1
    i_tale = 1
    book_tale = i_tale - 1
    tale_nodes = []
    if len(division) == 2:
        if division[0] == "cat":
            if division[1] == "cat":
                cat_1_memory = ""
                cat_2_memory = ""

                for tale in book:
                    title = tale[0]
                    category_1 = dictionary[title][4]
                    category_2 = dictionary[title][5]
                    if not category_1 == cat_1_memory:
                        tale_cat_1 = create_category(body, category_1, i_cat)
                        i_cat += 1
                        cat_1_memory = category_1
                    if not category_2 == cat_2_memory:
                        tale_cat_2 = create_category(tale_cat_1, category_2, i_group)
                        i_group += 1
                        cat_2_memory = category_2
                    sage = create_sage(tale_cat_2, title, i_tale)
                    create_text(sage, tale[1:])
                    i_tale += 1

            if division[1] == "group":
                cat_memory = ""
                group_memory = ""

                for tale in book:
                    title = tale[0]
                    category_1 = dictionary[title][4]
                    category_2 = dictionary[title][5]
                    if not category_1 == cat_memory:
                        tale_cat = create_category(body, category_1, i_cat)
                        i_cat += 1
                        cat_memory = category_1
                    if not category_2 == group_memory:
                        tale_group = create_group(tale_cat, category_2, i_group)
                        i_group += 1
                        group_memory = category_2
                    sage = create_sage(tale_group, title, i_tale)
                    create_text(sage, tale[1:])
                    i_tale += 1

    elif len(division) == 1:
        if division[0] == "group":
            group_memory = ""

            for tale in book:
                title = tale[0]
                group = dictionary[title][5]
                if not group == group_memory:
                    tale_group = create_group(body, group, i_group)
                    i_group += 1
                    group_memory = group
                sage = create_sage(tale_group, title, i_tale)
                create_text(sage, tale[1:])
                i_tale += 1

        elif division[0] == "NaN":
            for tale in book:
                title = tale[0]
                sage = create_sage(body, title, i_tale)
                create_text(sage, tale[1:])
                i_tale += 1


def create_back(back: ET.Element, back_text: dict[int: dict[str: str]]):
    for i in range(len(back_text)):
        key = list(back_text[i].keys())[0]
        ab = ET.SubElement(back, "ab", {"type": key})
        ab.text = back_text[i][key]


def write_xml(tree: ET, name: str):
    ET.indent(tree, space="\t", level=0)
    with open(f"xml_sagen/{name}.xml", "wb") as f:
        tree.write(f, encoding="utf-8")


def main():
    with open(f"metadata/TEI/{NAME}_sagen.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)

    with open(f"metadata/Database/{NAME}_sagen.json", "r", encoding="utf-8") as f:
        database = json.load(f)

    with open(f"vorwort/{NAME}/{NAME}_vorwort.txt", "r", encoding="utf-8") as f:
        front_text = f.read()

    with open(f"vorwort/{NAME}/{NAME}_index.txt", "r", encoding="utf-8") as f:
        index = f.read()

    front_list = [front_text, index]

    if NAME == "oberelsass":
        with open(f"vorwort/oberelsass/oberelsass_grimm.txt", "r", encoding="utf-8") as f:
            front_list.append(f.read())

    if NAME == "oberelsass" or NAME == "unterelsass" or NAME == "trier":
        with open(f"nachwort/{NAME}/{NAME}_quellen.txt", "r", encoding="utf-8") as f:
            back_sources = f.read()

        back_list = {0: {"sources": back_sources}}

    elif NAME == "lothringen" or NAME == "moseltal":
        with open(f"nachwort/{NAME}/{NAME}_quellen.txt", "r", encoding="utf-8") as f:
            back_sources = f.read()

        with open(f"nachwort/{NAME}/{NAME}_nachwort.txt", "r", encoding="utf-8") as f:
            back_text = f.read()

        if NAME == "moseltal":
            back_list = {0: {"sources": back_sources}, 1: {"postscript": back_text}}
        elif NAME == "lothringen":
            back_list = {1: {"sources": back_sources}, 0: {"postscript": back_text}}

    elif NAME == "pfalz":
        with open(f"nachwort/{NAME}/{NAME}_quellen.txt", "r", encoding="utf-8") as f:
            back_sources = f.read()

        with open(f"nachwort/{NAME}/{NAME}_orte.txt", "r", encoding="utf-8") as f:
            back_locs = f.read()

        back_list = {0: {"sources": back_sources}, 1: {"locations": back_locs}}

    else:
        back_list = []

    with open(f"parsed_sagen/{NAME}_sagen.pkl", "rb") as f:
        sagen = pickle.load(f)

    global PAGE
    PAGE = 1
    tei_header, body, tree, front, back = create_xml_tree()
    create_tei_header(tei_header, metadata)
    create_front(front, front_list)
    create_book(body, sagen, database, metadata["division"])
    create_back(back, back_list)
    write_xml(tree, f"{NAME}_sagen")


main()
