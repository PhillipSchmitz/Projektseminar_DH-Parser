"""Hier entstehen die SQL Dateien der Sagen, mit denen die Datenbank gefüttert wird"""
import pandas as pd
from pandas.io.sql import get_schema
import initiate
import pickle
from random import randint
import re
from Ben import input


def retrieve_list(name: str):
    with open("parsed_sagen/" + name + ".pkl", "rb") as f:
        tale_list = pickle.load(f)
    return tale_list


def create_dataframe_input(tales: list, tale_dict: dict):
    df_input = []
    i = 1
    for tale in tales:
        # print(tale_dict[tale[0]][10])
        df_tale = []
        tale_str = ""
        for line in tale[1:]:
            if "page_marker" in line:
                continue
            tale_str += line
            # print(tale_str)
        df_tale.append(tale_dict[tale[0]][0])
        df_tale.append(tale_dict[tale[0]][1])
        df_tale.append(tale_dict[tale[0]][2])
        df_tale.append(tale_dict[tale[0]][3])
        df_tale.append(tale_dict[tale[0]][4])
        df_tale.append(tale_dict[tale[0]][5])
        df_tale.append(tale_dict[tale[0]][6])
        df_tale.append(tale_dict[tale[0]][7])
        df_tale.append(tale_dict[tale[0]][8])
        df_tale.append(tale_dict[tale[0]][9])
        df_tale.append(tale_dict[tale[0]][10])
        df_tale.append(tale_str)
        df_input.append(df_tale)
    return df_input


def create_dataframe_output(df_input: list):
    df = pd.DataFrame(df_input, columns=["uid", "pid", "sagenid", "werkid", "sagennummerimwerk", "titel", "kategorie",
                                         "sagengruppe", "ortschaft", "longitude", "latitude", "volltext"])
    return df


def write_csv(df_output: pd.DataFrame, name: str):
    df_output.to_csv("sql_sagen/" + name + ".csv", ";", encoding="utf-8", index=False)


def main():
    name, booktitle, data = input.get_trier_und_umgebung_parameters()
    # print(data)
    tale_list = retrieve_list(name)
    df_input = create_dataframe_input(tale_list, data)
    df_output = create_dataframe_output(df_input)
    print(df_output)
    write_csv(df_output, name)
    """df_output = df_output.copy().assign()
    columns = ", ".join(df_output.columns)
    tuples = map(str, df_output.itertuples(index=False, name=None))
    values = re.sub(r"(?<=\W)(nan|None)(?=\W)", "NULL", (",\n" + " " * 7).join(tuples))
    print(f"INSERT INTO {test_schema} ({columns})\nVALUES {values};")"""


main()
