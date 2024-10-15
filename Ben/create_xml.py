from xml.etree import ElementTree as ET
import pickle
from os.path import join
# import initiate

# ====Parameters====
import trier_und_umgebung_input_parameters as input1  # change to desired input file
import oberelsass_input_parameters as input2
import unterelsass_input_parameters as input3
import moseltal_input_parametrs as input4
import lothringen_input_parametrs as input5
import pfalz_input_parameters as input6

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


def create_tei_header(tei_header: ET, meta: list):
    fileDesc = ET.SubElement(tei_header, "fileDesc")
    titleStmt = ET.SubElement(fileDesc, "titleStmt")
    publicationStmt = ET.SubElement(fileDesc, "publicationStmt")
    sourceDesc = ET.SubElement(fileDesc, "sourceDesc")
    title_full = ET.SubElement(titleStmt, "title", {"type": "full"})
    title_main = ET.SubElement(title_full, "title", {"type": "main"})
    title_main.text = meta[0]
    title_sub = ET.SubElement(title_full, "title", {"type": "sub"})
    title_sub.text = meta[1]
    if meta[6]:
        title_sub_2 = ET.SubElement(title_main, "title", {"type": "sub"})
        title_sub_2.text = meta[6]
    author = ET.SubElement(titleStmt, "author")
    author.text = meta[2]
    publisher = ET.SubElement(publicationStmt, "publisher")
    publisher.text = meta[5]
    address = ET.SubElement(publicationStmt, "address")
    placeName = ET.SubElement(address, "placeName")
    placeName.text = meta[4]
    date = ET.SubElement(publicationStmt, "date", {"when": meta[3]})
    date.text = meta[3]
    src = ET.SubElement(sourceDesc, "p")
    src.text = meta[7]


def create_front(front: ET.Element, front_text: str):
    ab = ET.SubElement(front, "ab")
    ab.text = front_text


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


def create_book(body: ET, book: list, dictionary: dict):
    i_cat = 1
    i_group = 1
    i_tale = 1
    book_tale = i_tale - 1
    tale_nodes = []
    cat_memory = ""
    group_memory = ""
    # dictionary = dictionary[0]
    # print(dictionary)
    for tale in book:
        # for index in dictionary:
        # print(tale[0])
        title = tale[0]
        # print(title)
        print(dictionary)
        category = dictionary[title][4]
        # print(category)
        group = dictionary[title][5]
        # print(group)
        if not category == cat_memory:
            tale_cat = create_category(body, category, i_cat)
            i_cat += 1
            cat_memory = category
        if not group == group_memory:
            tale_group = create_group(tale_cat, group, i_group)
            i_group += 1
            group_memory = group
        sage = create_sage(tale_group, title, i_tale)
        create_text(sage, tale[1:])
        i_tale += 1


def create_back(back: ET.Element, back_text: str):
    ab = ET.SubElement(back, "ab")
    ab.text = back_text


def write_xml(tree: ET, name: str):
    ET.indent(tree, space="\t", level=0)
    with open(name + ".xml", "wb") as f:
        tree.write(f, encoding="utf-8")


def main():
    func_list = [input1, input2, input3, input4, input5, input6]
    for input in func_list:
        global PAGE
        print(input)
        PAGE = 1
        dict = input.get_dict()
        name = input.get_pkl()
        meta = input.get_tei_header()
        front_text = input.get_front()
        back_text = input.get_back()
        # print(meta)
        sagen = retrieve_list(name)
        # print(sagen)
        tei_header, body, tree, front, back = create_xml_tree()
        create_tei_header(tei_header, meta)
        create_front(front, front_text)
        create_book(body, sagen, dict)
        create_back(back, back_text)
        write_xml(tree, name)


main()
