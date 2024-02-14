"""Hier entstehen die SQL Dateien der Sagen, mit denen die Datenbank gefüttert wird"""
import pandas as pd
import pickle
import re
from Ben import input


def retrieve_list(name: str):
    with open("parsed_sagen/" + name + ".pkl", "rb") as f:
        tale_list = pickle.load(f)
    return tale_list


def create_dataframe_input(tales: list, tale_dict: dict, book_title: str):
    df_input = []
    print(len(tales))
    i = 1
    for tale in tales:
        df_tale = []
        tale_str = ""
        for line in tale[1:]:
            if "page_marker" in line:
                continue
            line = re.sub(r"\n", " ", line)
            tale_str += line
            # print(tale_str)
        df_tale.append(tale_dict[tale[0]][0])
        df_tale.append(tale_dict[tale[0]][1])
        df_tale.append(tale_dict[tale[0]][2])
        df_tale.append(tale_dict[tale[0]][2])
        df_tale.append(tale_dict[tale[0]][3])
        df_tale.append(tale_dict[tale[0]][4])
        df_tale.append(tale_dict[tale[0]][5])
        df_tale.append(tale_dict[tale[0]][6])
        df_tale.append(tale_dict[tale[0]][7])
        df_tale.append(tale_dict[tale[0]][8])
        df_tale.append(tale_str)
        df_tale.append(book_title)
        df_input.append(df_tale)
    return df_input


def create_dataframe_output(df_input: list):
    df = pd.DataFrame(df_input, columns=["sagenid", "werkid", "sagenidautor", "sagenidimwerk", "titel", "sagenkategorie",
                                         "sagengruppe", "ortschaft", "longitude", "latitude", "volltext", "buchtitel"])
    return df


def write_csv(df_output: pd.DataFrame, name: str):
    df_output.to_csv("sql_sagen/csv/" + name + ".csv", ";", encoding="utf-8", index=False)


def main():
    f_list = [input.get_trier_und_umgebung_parameters, input.get_moseltal_parameters, input.get_pfalz_parameters, input.get_oberelsass_parameter, input.get_unterelsass_parameters, input.get_lothringen_parameters]
    for func in f_list:
        name, book_title, data = func()
        # print(data)
        tale_list = retrieve_list(name)
        df_input = create_dataframe_input(tale_list, data, book_title)
        df_output = create_dataframe_output(df_input)
        print(df_output)
        write_csv(df_output, name)
        """df_output = df_output.copy().assign()
        columns = ", ".join(df_output.columns)
        tuples = map(str, df_output.itertuples(index=False, name=None))
        values = re.sub(r"(?<=\W)(nan|None)(?=\W)", "NULL", (",\n" + " " * 7).join(tuples))
        print(f"INSERT INTO {test_schema} ({columns})\nVALUES {values};")"""


main()
