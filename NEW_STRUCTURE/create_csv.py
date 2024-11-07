"""Hier entstehen die SQL Dateien der Sagen, mit denen die Datenbank gefüttert wird"""
import glob

import pandas as pd
import pickle
import re
import json
from OLD_STRUCTURE.Ben import input


def retrieve_list(name: str):
    with open("parsed_sagen/" + name + ".pkl", "rb") as f:
        tale_list = pickle.load(f)
    return tale_list


def create_dataframe_input(tales: list, tale_dict: dict, tale_list: list):
    df_input = []
    #print(len(tales))
    i = 0
    for tale in tales:
        df_tale = []
        tale_str = ""
        for line in tale[1:]:
            if "page_marker" in line:
                continue
            line = re.sub(r"\n", " ", line)
            tale_str += line
            # print(tale_str)
        df_tale.append(tale_dict[tale_list[i]]["id"])
        df_tale.append(tale_dict[tale_list[i]]["werk_id"])
        df_tale.append(tale_dict[tale_list[i]]["n_book"])
        df_tale.append(tale_dict[tale_list[i]]["n_book"])
        df_tale.append(tale_dict[tale_list[i]]["title"])
        df_tale.append(tale_dict[tale_list[i]]["division_1"])
        df_tale.append(tale_dict[tale_list[i]]["division_2"])
        df_tale.append(tale_dict[tale_list[i]]["place_id"])
        df_tale.append(tale_dict[tale_list[i]]["longitude"])
        df_tale.append(tale_dict[tale_list[i]]["latitude"])
        df_tale.append(tale_str)
        df_tale.append(tale_dict["name"])
        df_input.append(df_tale)

        i += 1
    return df_input


def create_dataframe_output(df_input: list):
    df = pd.DataFrame(df_input, columns=["sagenid", "werkid", "sagenidautor", "sagenidimwerk", "titel", "sagenkategorie",
                                         "sagengruppe", "ortschaft", "longitude", "latitude", "volltext", "buchtitel"])
    return df


def write_csv(df_output: pd.DataFrame, name: str):
    df_output.to_csv("sql_sagen/csv/" + name + ".csv", ";", encoding="utf-8", index=False)


def main():
    # f_list = [input.get_trier_und_umgebung_parameters, input.get_moseltal_parameters, input.get_pfalz_parameters, input.get_oberelsass_parameter, input.get_unterelsass_parameters, input.get_lothringen_parameters]

    json_list = glob.glob("metadata/Database/*")

    for file in json_list:
        with open(file, "r", encoding="utf-8") as f:
            meta = json.load(f)
        file = re.sub(r"^[\w/\\]{18}", "", file)
        name = re.sub(r"\.json", "", file)


    # for func in f_list:
        # name, book_title, data = func()
        # print(data)
        tale_list = retrieve_list(name)

        title_list = list(meta.keys())[1:]

        df_input = create_dataframe_input(tale_list, meta, title_list)
        df_output = create_dataframe_output(df_input)
        print(df_output)
        write_csv(df_output, name)
        """df_output = df_output.copy().assign()
        columns = ", ".join(df_output.columns)
        tuples = map(str, df_output.itertuples(index=False, name=None))
        values = re.sub(r"(?<=\W)(nan|None)(?=\W)", "NULL", (",\n" + " " * 7).join(tuples))
        print(f"INSERT INTO {test_schema} ({columns})\nVALUES {values};")"""


main()
