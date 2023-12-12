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


def trier_und_umgebungen_sql():
    name = "trier_umgebung_sagen"
    book_title = "Trier und seine Umgebung in Sagen und Liedern"
    dict = tcs.get_dict_trier_umgebung()
    lang = "deutsch"
    return name, book_title, dict, lang