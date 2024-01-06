"""
!!!IMPORTANT!!!

This script is only used to clean the Google OCR files from white spaces and new lines. The output file from this
script can't be used by the ocr-parser because of naming differences of the output file and the parser input file.
This is to prevent accidental replacement of the parser input file. The input file may be manually adjusted for
proper parser support (e.g. minor title differences).
To use the output of this script in the ocr parser you need to manually add '_sagen' between filename and '.txt'
and remove everything before the first tale.
Do not change this script to automate the naming!
"""
import re


def read_book(name: str):
    """
    Reads book from Google OCR file
    :param name: name of the book
    :return: list with all lines of the book
    """
    with open("google_ocr_raw/" + name + ".txt", "r", encoding="utf-8") as f:
        sagen_raw = f.readlines()
    return sagen_raw


def clean_book(book_raw: list):
    """
    Removes unnecessary spaces and empty lines
    :param book_raw: list of all booklines
    :return: list of all lines but cleaned
    """
    sagen = []
    for s in book_raw:
        sa = re.sub(r"\n", "", s)
        if sa == "":
            continue
        sb = re.sub(r"\s{2}\s*", " ", sa)
        sc = re.sub(r"\t+", "", sb)
        sd = re.sub(r"^\s", "", sc)
        sagen.append(sd + "\n")
    print(sagen)
    return sagen


def write_cleaned_book(book: list, name: str):
    """
    Writes the cleaned book to txt-file
    :param book: list of lines of cleaned book
    :param name: name of the book
    :return: None
    """
    with open("ocr_sagen/" + name + ".txt", "w", encoding="utf-8") as f:
        f.writelines(book)


def main():
    """
    Main function for handling Google OCR cleaning
    :return: None
    """
    name_list = ["Deutsche_Sagen_im_Elsass", "Die_Sagen_des_(Unter-)Elsasses", "Die_Sagen_des_Elsasses",
                 "Sagen_und_Bilder_aus_Lothringens_Vorzeit", "sagen_geschichten_moseltal"]
    output_list = ["None", "unterelsass", "oberelsass", "lothringen", "moseltal"]
    book_number = 4
    name = name_list[book_number]
    output = output_list[book_number]
    book_list = read_book(name)
    cleaned = clean_book(book_list)
    write_cleaned_book(cleaned, output)


main()
