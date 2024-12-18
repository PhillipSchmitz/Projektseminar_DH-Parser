from OLD_STRUCTURE.Ben.trier_und_umgebung_input_parameters import get_sql as tu_sql
from OLD_STRUCTURE.Ben.oberelsass_input_parameters import get_sql as oe_sql
from OLD_STRUCTURE.Ben.unterelsass_input_parameters import get_sql as ue_sql
from OLD_STRUCTURE.Ben.moseltal_input_parametrs import get_sql as mo_sql
from OLD_STRUCTURE.Ben.pfalz_input_parameters import get_sql as pf_sql
from OLD_STRUCTURE.Ben.lothringen_input_parametrs import get_sql as lo_sql


def get_trier_und_umgebung_parameters():
    name, book_title, data = tu_sql()
    # print(data)
    return name, book_title, data


def get_oberelsass_parameter():
    name, book_title, data = oe_sql()
    return name, book_title, data


def get_unterelsass_parameters():
    name, book_title, data = ue_sql()
    return name, book_title, data


def get_moseltal_parameters():
    name, book_title, data = mo_sql()
    return name, book_title, data


def get_pfalz_parameters():
    name, book_title, data = pf_sql()
    return name, book_title, data


def get_lothringen_parameters():
    name, book_title, data = lo_sql()
    return name, book_title, data
