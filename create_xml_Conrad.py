#===imports===
from xml.etree import ElementTree as ET
import pickle
import initiate
import re

#===Parameters===
MainTitle="Trier und seine Umgebung in Sagen und Liedern."
SubTitle="Mit Bemerkungen über die Quellen dieser Sagen."
Author="Ph. Laven"
PublicationYear="1851"
PublicationPlace="Trier, Germany"
#PublicationCountry="Germany"
Publisher="Verlag der Fr. Lintz'schen Buchhandlung"
Edition="first"

Copyright="CC0"
encoder="Ben Conrad"
#IDStart = 0                #Start for UniversalID, check with Parser

#===Functions===
def retrieve_list(name):
    with open("parsed_sagen/" + name + ".pkl", "rb") as f:
        tale_list = pickle.load(f)
    return tale_list


def create_xml_tree():
    """
    creates TEI root element and TEI header
    :return:
    """
    tei = ET.Element("TEI", {"version": "3.3.0", "xmlns": "http://www.tei-c.org/ns/1.0"})
    tree = ET.ElementTree(tei) 
    tei_header = ET.SubElement(tei, "teiHeader")
    text = ET.SubElement(tei, "text")
    front = ET.SubElement(text, "front")
    body = ET.SubElement(text, "body")
    back = ET.SubElement(text, "back")

    return tei, body, tree, tei_header


def create_group(body: ET, cat: str, number: int):
    group = ET.SubElement(body, "div", {"type": "Sagengruppe", "n": str(number)})
    group_Header = ET.SubElement (group, "head")
    group_Header.text = cat
    #category.text = cat
    return group


def create_sage(category: ET, sage: str, number: int):
    """
    creates an xml TEI body part containing a tale
    :param body: TEI body tag
    :param sage:
    :param number:
    :return:
    """
    sage_div = ET.SubElement(category, "div", {"type": "Sage", "n": str(number)})
    sage_head = ET.SubElement(sage_div, "head")
    sage_head.text = sage
    
    return sage_div


def create_text(tale: ET, text: list):
    content = ET.SubElement(tale, "p")
    for tale_line in text:
        if re.search(r"page_marker_ocr\d+", tale_line):
            pb_number_ocr = re.sub(r"page_marker_ocr(\d+)\n", r"\1", tale_line)
            #print (pb_number_ocr)
            pb = ET.SubElement (content, "pb", {"type": "ocr", "n": pb_number_ocr})
            
        elif re.search(r"page_marker_book\d+", tale_line):
            pb_number_book = re.sub(r"page_marker_book(\d+)\n", r"\1", tale_line)
            pb = ET.SubElement (content, "pb", {"type": "book", "n": pb_number_book})
    
        else:
            l = ET.SubElement(content, "l")
            l.text = tale_line[:-1]
    


def create_header (tei_header):
    fileDesc = ET.SubElement(tei_header, "fileDesc")
    titleStmt = ET.SubElement(fileDesc, "titleStmt")
    full_title = ET.SubElement(titleStmt, "title", {"type": "full"})
    ET.SubElement(full_title, "title", {"type": "main"}).text = MainTitle
    ET.SubElement(full_title, "title", {"type": "sub"}).text = SubTitle
    ET.SubElement(titleStmt, "author").text = Author
    respStmt = ET.SubElement(titleStmt, "respStmt")
    resp = ET.SubElement(respStmt, "resp")
    resp.text = "Encoded by"
    encoder_name = ET.SubElement(respStmt, "name")
    encoder_name.text = encoder

    publicationStmt = ET.SubElement(fileDesc, "publicationStmt")
    ET.SubElement(publicationStmt, "publisher").text = "Projektseminar Praxis der Digital Humanities"
    ET.SubElement(publicationStmt, "pubPlace").text = "University of Trier, Germany"
    availabilty = ET.SubElement(publicationStmt, "availability")
    ET.SubElement(availabilty, "p").text = Copyright


    sourceDesc = ET.SubElement(fileDesc, "sourceDesc")
    bibl = ET.SubElement(sourceDesc, "bibl")
    ET.SubElement(bibl, "author").text = Author
    full_title = ET.SubElement(bibl, "title", {"type": "full"})
    ET.SubElement(full_title, "title", {"type": "main"}).text = MainTitle
    ET.SubElement(full_title, "title", {"type": "sub"}).text = SubTitle
    ET.SubElement(bibl, "edition").text = Edition
    ET.SubElement(bibl, "pubPlace").text = PublicationPlace
    ET.SubElement(bibl, "publisher").text = Publisher
    ET.SubElement(bibl, "date").text = PublicationYear

    encodingDesc = ET.SubElement(tei_header, "encodingDesc")
    projectDesc = ET.SubElement(encodingDesc, "projectDesc")
    ET.SubElement(projectDesc, "p").text = "Erfassung von Sagensammlungen des 19. Jahrhunderts entlang Mosel. OCRisierung. Modelierung. Lokalisierung."
    editorialDecl = ET.SubElement(encodingDesc, "editorialDecl")
    ET.SubElement(editorialDecl, "p").text = "Typographic Lines encoded as line elements"
    ET.SubElement(encodingDesc, "geoDecl").text = "Flat Earth Coordinate System"
    
    


def create_body(body: ET, book: list, dictionary: dict):
    i_group = 1
    i_tale = 1
    tale_nodes = []
    group_memory = ""
    for tale in book:
        #print(tale)
        title = tale[0]
        group = dictionary[title]
        if not group == group_memory:
            tale_group = create_group(body, group, i_group)
            i_group += 1
        group_memory = group 
        tale_nodes.append(create_sage(tale_group, title, i_tale))
        create_text(tale_nodes[-1], tale[1:])
        i_tale += 1


def write_xml(tree: ET, name: str):
    ET.indent(tree, space="\t", level=0)
    #StringXML = ET.tostring(tree, encoding="utf-8")
    #print(StringXML)
    #ADD to beginning of string:
    #<?xml version="1.0" encoding="utf-8"?>
    #<?xml-model href="https://tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>


    with open("xml_sagen/" + name + ".xml", "wb") as f:
        tree.write(f, encoding="utf-8")


def main():
    name, titles, categories, dict = initiate.trier_und_umgebung()
    sagen = retrieve_list(name)
    tei, body, tree, tei_header = create_xml_tree()
    create_header(tei_header)
    create_body(body, sagen, dict)
    write_xml(tree, name)
    print("\nDone!\n")


main()