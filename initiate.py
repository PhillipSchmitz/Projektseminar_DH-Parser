import title_cat_storage as tcs


def trier_und_umgebung():
    """
    initiates variables for tale book "Trier und seine Umgebung in Sagen und Liedern"
    :return:names, titles, categories of tales plus dictionary containing titles with their corresponding category
    """
    name = "trier_umgebung_sagen"
    titles = tcs.get_titles_trier_umgebung()
    categories = tcs.get_categories_trier_umgebung()
    dict = tcs.get_dict_trier_umgebung()
    return name, titles, categories, dict


def trier_und_umgebung_tei_header():
    MainTitle = "Trier und seine Umgebung in Sagen und Liedern."
    SubTitle = "Mit Bemerkungen über die Quellen dieser Sagen."
    Author = "Ph. Laven"
    PublicationYear = "1851"
    PublicationPlace = "Trier, Germany"
    # PublicationCountry="Germany"
    Publisher = "Verlag der Fr. Lintz'schen Buchhandlung"
    Edition = "first"

    Copyright = "CC0"
    encoder = "Ben Conrad"

    return MainTitle, SubTitle, Author, PublicationYear, PublicationPlace, Publisher, Edition, Copyright, encoder


def trier_und_umgebungen_sql():
    name = "trier_umgebung_sagen"
    book_title = "Trier und seine Umgebung in Sagen und Liedern"
    dict = tcs.get_dict_trier_umgebung()
    lang = "deutsch"
    return name, book_title, dict, lang


def lothringen():
    name = "lothringen_sagen"
    titles = tcs.get_titles_lothringen()
    return name, titles


def oberelsass():
    name = "oberelsass_sagen"
    titles = tcs.get_titles_oberelsass()
    return name, titles


def unterelsass():
    name = "unterelsass_sagen"
    titles = tcs.get_titles_unterelsass()
    return name, titles


def moseltal():
    name = "moseltal_sagen"
    titles = tcs.get_titles_moseltal()
    return name, titles


def geschichten_moseltal():
    name = "geschichten_moseltal_sagen"
    titles = tcs.get_titles_geschichten_moseltal()
    return name, titles


def pfalz():
    name = ["pfalz_1_sagen", "pfalz_2_sagen", "pfalz_3_sagen"]
    titles = tcs.get_pfalz_titles()
    cat = tcs.get_pfalz_cat()
    group = tcs.get_pfalz_group()
    num = [130, 225]
    return name, titles, cat, group, num

def erzählungen_moseltal():
    name = "erzählungen_moseltal"
    titles = tcs.get_erzählungen_moseltal_titles()
    return name, titles