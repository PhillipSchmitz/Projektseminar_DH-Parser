import pickle
import pandas as pd


def retrieve_list(name: str):
    with open("ner_sagen/" + name + ".pkl", "rb") as f:
        tale_list = pickle.load(f)
    return tale_list


def setify_tale(locations: list):
    uni_loc = []
    for loc in locations:
        uni_loc.append(list(set(loc)))
    return uni_loc


def setify_all(locations: list):
    uni_loc = []
    for loc in locations:
        for l in loc:
            uni_loc.append(l)
    uni_loc = list(set(uni_loc))
    return uni_loc


def reconcile_data(locations: list):
    rec_output = []
    for loc in locations:
        rec_output.append([loc, "None"])
    # print(rec_output)
    df = pd.DataFrame(rec_output, columns=["Ort", "None"])
    # print(df)
    df.to_csv("location_test.csv", "\t", encoding="utf-8")


def retrieve_coordinates(name: str):
    data = pd.read_csv(name, sep="\t")
    # print(data)
    return data.values.tolist()


def matching(uni_loc: list, coord: list):
    loco = []
    for loc in uni_loc:
        loc_mem = []
        for l in loc:
            for co in coord:
                if l in co[0]:
                    loc_mem = [l, co[1], co[2]]
                    break
        loco.append(loc_mem)
    return loco


def main():
    name = "trier_umgebung_sagen"
    locs = retrieve_list(name)
    # print(locs)
    uni_loc = setify_tale(locs)
    # print(uni_loc)
    # reconcile_data(uni_loc)
    coord = retrieve_coordinates("DE-txt.csv")
    # print(coord)
    t = matching(uni_loc, coord)
    print(t)
    print(len(t))


main()
