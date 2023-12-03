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


def create_sage(body: ET, sage: str, number: int, cat: str):
    """
    creates an xml TEI body part containing a tale
    :param body: TEI body tag
    :param sage:
    :param number:
    :return:
    """
    sage = ET.SubElement(body, "div", {"sage": sage, "category": cat, "n": str(number)})
    return sage


def create_text(tale: ET, text: list):
    content = ET.SubElement(tale, "p")
    for tale_line in text:
        line = ET.SubElement(content, "line")
        line.text = tale_line


def create_book(body: ET, book: list, dictionary: dict):
    i = 1
    tale_nodes = []
    for tale in book:
        print(tale)
        title = tale[0][:-2]
        category = dictionary[title]
        tale_nodes.append(create_sage(body, title, i, category))
        create_text(tale_nodes[-1], tale[1:])
        i += 1


def write_xml(tree: ET, name: str):
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
