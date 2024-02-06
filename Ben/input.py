from Ben.trier_und_umgebung_input_parameters import get_sql as tu_sql
from Ben.oberelsass_input_parameters import get_sql as oe_sql
from Ben.unterelsass_input_parameters import get_sql as ue_sql
from Ben.moseltal_input_parametrs import get_sql as mo_sql
from Ben.pfalz_input_parameters import get_sql as pf_sql

def get_trier_und_umgebung_parameters():
    name, book_title, data = tu_sql()
    # print(data)
    return name, book_title, data


def get_oberelsass_parameter():
    name, data = oe_sql()
    return name, data


def get_unterelsass_parameters():
    name, data = ue_sql()
    return name, data


def get_moseltal_parameters():
    name, data = mo_sql()
    return name, data


def get_pfalz_parameters():
    name, data = pf_sql()
    return name, data