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


def most_frequent(List: list):
    return max(set(List), key=List.count)


def locify(locs: list):
    loc_out_fr = []
    loc_out_first = []
    for loc in locs:
        if loc:
            loc_out_fr.append(most_frequent(loc))
            loc_out_first.append(loc[0])
        else:
            loc_out_fr.append("")
            loc_out_first.append("")
    return loc_out_fr, loc_out_first


def matching(loc: list, coord: list):
    loco = []
    for l in loc:
        loc_mem = []
        for co in coord:
            if l in co[0]:
                # print(l)
                loc_mem = [l, co[1], float(co[2])]
                break
        if not loc_mem:
            loc_mem = [l, "NaN"]
        if l == "":
            #print("Yay")
            loc_mem = ["NaN", "NaN"]
        loco.append(loc_mem)
    return loco


def match_el(locs: list, coord: list):
    loco = []
    for loc in locs:
        loc_mem = []
        for co in coord:
            if loc in co[0]:
                # print(l)
                loc_mem = [loc, co[1], co[2]]
                break
        loco.append(loc_mem)
    return loco


def main_de():
    name = "moseltal_sagen"
    locs = retrieve_list(name)
    print(locs)
    freq, first = locify(locs)
    print(freq)
    print(first)
    coord = retrieve_coordinates("DE-txt.csv")
    # print(coord)
    t = matching(first, coord)
    i = 0
    for l in t:
        if l[1] == ("NaN"):
            i += 1
    print(i)
    print(t)
    print(len(t))


def main_el():
    name = "unterelsass_sagen"
    locs = retrieve_list(name)
    print(locs)
    coord = retrieve_coordinates("elsass-orte.csv")
    # print(coord)
    # coord = floatify(coord)
    print(coord)
    t = match_el(locs, coord)
    print(t)
    print(len(t))
    c = 0
    for i in t:
        if i:
            c += 1
    print(c)


main_de()
