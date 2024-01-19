"""Hier entstehen die SQL Dateien der Sagen, mit denen die Datenbank gefüttert wird"""
import pandas as pd
from pandas.io.sql import get_schema
import initiate
import pickle
from random import randint
import re
import sqlalchemy
from sqlalchemy import create_engine
import sqlite3


def retrieve_list(name: str):
    with open("parsed_sagen/" + name + ".pkl", "rb") as f:
        tale_list = pickle.load(f)
    return tale_list


def create_dataframe_input(tales: list, tale_dict: dict, lang: str):
    df_input = []
    i = 1
    for tale in tales:
        df_tale = []
        tale_str = ""
        for line in tale[1:]:
            tale_str += line
        df_tale.append(i)
        df_tale.append(tale[0])
        df_tale.append(tale_str)
        df_tale.append(lang)
        df_tale.append(tale_dict[tale[0]])
        df_tale.append(randint(1, 5))
        df_tale.append(randint(1, 2))
        i += 1
        df_input.append(df_tale)
    return df_input


def create_dataframe_output(df_input: list):
    df = pd.DataFrame(df_input, columns=["SagenID", "Titel", "Volltext", "Sprache", "Kategorie", "OrtID", "WerkID"])
    return df


def create_locations():
    df = pd.DataFrame([[1, "Trier", "5566"], [2, "Paris", "1234"], [3, "Tokyo", "3743"], [4, "Nairobi", "3468"],
                       [5, "Manila", "2345"]], columns=["OrtID", "Name", "Koordinaten"])
    return df


def create_book():
    df = pd.DataFrame([[1, "Sagen aus Trier", "Cornelia Funke"], [2, "Sagen von woanders", "Rick Riordan"]],
                      columns=["WerkID", "Name", "Autor"])
    return df


def main():
    name, book_title, dict, lang = initiate.trier_und_umgebungen_sql()
    tale_list = retrieve_list(name)
    df_input = create_dataframe_input(tale_list, dict, lang)
    df_output = create_dataframe_output(df_input)
    test_schema = get_schema(df_output, "Sage")
    #print(test_schema)
    df_output = df_output.copy().assign()
    columns = ", ".join(df_output.columns)
    tuples = map(str, df_output.itertuples(index=False, name=None))
    values = re.sub(r"(?<=\W)(nan|None)(?=\W)", "NULL", (",\n" + " " * 7).join(tuples))
    print(f"INSERT INTO {test_schema} ({columns})\nVALUES {values};")
    """conn = sqlite3.connect("sql_sagen/sagen.sql")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS Sage (SagenID number, Titel text, Volltext text, Sprache text, Kategorie text, OrtID number, WerkID number)")
    c.execute("CREATE TABLE IF NOT EXISTS Ort (OrtID number, Name text, Koordinaten number)")
    c.execute("CREATE TABLE IF NOT EXISTS Werk (WerkID number, Name text, Koordinaten number)")
    conn.commit()
    df_output.to_csv("sql_sagen/sagen_test.csv", "\t", encoding="utf-8")
    df_output.to_sql("Sage", conn, if_exists="replace", index=False)
    ort_output = create_locations()
    #print(ort_output)
    ort_output.to_csv("sql_sagen/ort_test.csv", "\t", encoding="utf-8")
    ort_output.to_sql("Ort", conn, if_exists="replace", index=False)
    book_output = create_book()
    #print(book_output)
    book_output.to_csv("sql_sagen/werk_test.csv", "\t", encoding="utf-8")
    book_output.to_sql("Werk", conn, if_exists="replace", index=False)
    c.execute('''  
        SELECT * FROM Sage
                  ''')
    for row in c.fetchall():
        print(row)
    c.execute('''  
            SELECT * FROM Ort
                      ''')
    for row in c.fetchall():
        print(row)
    c.execute('''  
        SELECT * FROM Werk
                  ''')
    for row in c.fetchall():
        print(row)"""

main()
