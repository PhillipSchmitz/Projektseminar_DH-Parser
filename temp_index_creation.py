import re


def elsass():
    with open("elsass_index_speicher.txt", "r", encoding="utf-8") as f:
        index = f.readlines()

    title = []
    ort = []
    combo = []
    for line in index:
        v = re.sub(r"\t+.+\n", "", line)
        if not v == "":
            m = v[0].upper()
            v = m + v[1:]
            v = re.sub(r"\.+", "", v)
            v = re.sub(r"\s+$", "", v)
            ort.append(v)
        t = re.sub(r".+\t+", "", line)
        t = re.sub(r"\n", "", t)
        t = re.sub(r"^\d+\.\s*", "", t)
        t = re.sub(r"•*\s*\d+$", "", t)
        t = re.sub(r"[\.•·]", "", t)
        t = re.sub(r"\s+$", "", t)
        t = re.sub(r"\sst\s", " St. ", t)
        title.append(t)
        combo.append([t, v])
    # print(combo)

    output = "["
    for i in title:
        output += "'" + i + "'" + ","
    output += "]"
    print(output)

    dict_out = "{"
    for i in combo:
        dict_out += "'" + i[0] + "': '" + i[1] + "',"
    dict_out += "}"
    # print(dict_out)


def moseltal():
    with open("moseltal_temp.txt", "r", encoding="utf-8") as f:
        titles = f.readlines()

    clean = []
    for title in titles:
        title = re.sub(r"^\s*\d+\.", "", title)
        title = re.sub(r"\.\n$", "", title)
        title = re.sub(r"^\s+", "", title)
        clean.append(title)

    output = '['
    for c in clean:
        output += '"' + c + '",'
    output += ']'

    print(output)


def geschichten_moseltal():
    with open("geschichten_moseltal_temp.txt", "r", encoding="utf-8") as f:
        titles = f.readlines()

    clean = []
    for title in titles:
        title = re.sub(r"\d+\. ", "", title)
        title = re.sub(r"\.\n$", "", title)
        clean.append(title)

    output = '['
    for c in clean:
        output += '"' + c + '",'
    output += ']'

    print(output)


geschichten_moseltal()
