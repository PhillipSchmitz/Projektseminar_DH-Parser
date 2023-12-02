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
    tei_header = ET.SubElement(tei, "teiHeader")
    fileDesc = ET.SubElement(tei_header, "fileDesc")
    titleStmt = ET.SubElement(fileDesc, "titleStmt")
    publicationStmt = ET.SubElement(fileDesc, "publicationStmt")
    sourceDesc = ET.SubElement(fileDesc, "sourceDesc")
    text = ET.SubElement(tei, "text")
    body = ET.SubElement(text, "body")

    return tei, body


def create_sage(body: ET, sage: str, number: str):
    """
    creates an xml TEI body part containing a tale
    :param body: TEI body tag
    :param sage:
    :param number:
    :return:
    """
    sage = ET.SubElement(body, "div", {"sage": sage, "n": number})
    return sage


def main():
    name, titles, categories, dict = initiate.trier_und_umgebung()
    sagen = retrieve_list(name)
    tei, body = create_xml_tree()
    sage = create_sage(body, "Trierer Sage", "1")
    ET.dump(tei)


main()
