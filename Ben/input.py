from Ben.trier_und_umgebung_input_parameters import get_sql as tu_sql


def get_trier_und_umgebung_parameters():
    name, book_title, data = tu_sql()
    #print(data)
    return name, book_title, data

get_trier_und_umgebung_parameters()