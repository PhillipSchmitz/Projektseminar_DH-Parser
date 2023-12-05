from xml.etree import ElementTree as ET
import pickle
import initiate


def retrieve_list(name):
    with open("parsed_sagen/" + name + ".pkl", "rb") as f:
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
    fileDesc = ET.SubElement(tei_header, "fileDesc")
    titleStmt = ET.SubElement(fileDesc, "titleStmt")
    publicationStmt = ET.SubElement(fileDesc, "publicationStmt")
    sourceDesc = ET.SubElement(fileDesc, "sourceDesc")
    text = ET.SubElement(tei, "text")
    body = ET.SubElement(text, "body")

    return tei, body, tree


def create_category(body: ET, cat: str, number: int):
    category = ET.SubElement(body, "div", {"type": cat, "n": str(number)})
    category.text = cat
    return category


def create_sage(category: ET, sage: str, number: int):
    """
    creates an xml TEI body part containing a tale
    :param body: TEI body tag
    :param sage:
    :param number:
    :return:
    """
    title = ET.SubElement(category, "head", {"type": sage, "n": str(number)})
    title.text = sage
    return title


def create_text(tale: ET, text: list):
    content = ET.SubElement(tale, "p")
    for tale_line in text:
        lb = ET.SubElement(content, "lb")
        lb.text = tale_line[:-1]


def create_book(body: ET, book: list, dictionary: dict):
    i_cat = 1
    i_tale = 1
    tale_nodes = []
    cat_memory = ""
    for tale in book:
        print(tale)
        title = tale[0]
        category = dictionary[title]
        if not category == cat_memory:
            tale_cat = create_category(body, category, i_cat)
            i_cat += 1
        tale_nodes.append(create_sage(tale_cat, title, i_tale))
        create_text(tale_cat, tale[1:])
        i_tale += 1


def write_xml(tree: ET, name: str):
    ET.indent(tree, space="\t", level=0)
    with open("xml_sagen/" + name + ".xml", "wb") as f:
        tree.write(f, encoding="utf-8")


def main():
    name, titles, categories, dict = initiate.trier_und_umgebung()
    sagen = retrieve_list(name)
    del sagen[0]
    tei, body, tree = create_xml_tree()
    create_book(body, sagen, dict)
    write_xml(tree, name)


main()
