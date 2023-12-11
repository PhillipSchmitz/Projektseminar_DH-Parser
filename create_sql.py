"""Hier entstehen die SQL Dateien der Sagen, mit denen die Datenbank gefüttert wird"""
import pandas as pd
import initiate
import pickle
from random import randint


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
        df_tale.append(randint(1,2))
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
    print(df_output)
    df_output.to_csv("sql_sagen/test.csv", "\t", encoding="utf_8")
    ort_output = create_locations()
    print(ort_output)
    ort_output.to_csv("sql_sagen/ort_test.csv", "\t", encoding="utf_8")
    book_output = create_book()
    print(book_output)
    book_output.to_csv("sql_sagen/werk_test.csv", "\t", encoding="utf_8")


main()
