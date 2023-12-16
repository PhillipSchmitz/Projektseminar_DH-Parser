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
    with open("ocr_sagen/" + name + "_bereinigt.txt", "w", encoding="utf-8") as f:
        f.writelines(book)


def main():
    """
    Main function for handling Google OCR cleaning
    :return: None
    """
    name_list = ["Deutsche_Sagen_im_Elsass", "Die_Sagen_des_(Unter-)Elsasses", "Die_Sagen_des_Elsasses",
                 "Sagen_und_Bilder_aus_Lothringens_Vorzeit"]
    name = name_list[3]
    book_list = read_book(name)
    cleaned = clean_book(book_list)
    write_cleaned_book(cleaned, name)


main()
