import json


def get_tei_header():
    MainTitle = "Sagen und Bilder aus Lothringens Vorzeit"
    SubTitle = None
    Author = "Oskar Schwebel"
    PublicationYear = "1886"
    PublicationPlace = "Lorbach, Germany"
    # PublicationCountry="Germany"
    Publisher = "Verlag von Robert Hupfer"
    # Edition = "first"
    Edition = None
    source = "Sagen aus dem Gebiet Lothringen"

    Copyright = "CC0"
    encoder = "Ben Conrad, Dennis Binz"

    return MainTitle, SubTitle, Author, PublicationYear, PublicationPlace, Publisher, Edition, source, Copyright, encoder


def get_pkl():
    pickle_filename = "lothringen_sagen"
    return pickle_filename


def get_dict():
    titles = ["Frau Florentina die Getreue",
              "Die Bischöfe von Metz und ihre Legenden",
              "Im Königspalaste zu Metz",
              "Sankta Glossindis von Metz",
              "Im Schatten des Hirtenstabes von Gorze",
              "Die Kaiserin Hildegard",
              "Lohengrin",
              "Papst Leo IX.",
              "Der hlg. Richard und Kaiser Heinrich II.",
              "Die Sagen der Herzöge von Lothringen",
              "Wappen, Fahnen, Schlachtrufe u. Devisen der Herzöge von Lothringen",
              "Templer- und Adelssagen",
              "Der Graf von Engelweiler und die Waldfrau",
              "Auf Feld und Flur",
              "Geflügelte Worte aus dem alten Metz",
              "Der reiche Bürger von Verdun"]

    locs = [['Metz', 49.119722, 6.176944], ['Metz', 49.119722, 6.176944], ['Pfalz', 0, 0],
            ['Troyes', 48.298889, 4.078056],
            ['Gorze', 49.053889, 5.998889], ['Metz', 49.119722, 6.176944], ['Bouillon', 49.795556, 5.068111],
            ['Clugny', 46.434444, 4.659167], ['Verdun', 49.159722, 5.382778], ['Maréville', 49.452778, 5.456667],
            ['Lothringen', 0, 0], ['Lothringen', 0, 0], ['Engelweiler', 0, 0], ['Lothringen', 0, 0],
            ['Metz', 49.119722, 6.176944], ["Verdun", 49.159722, 5.382778]]

    n_book = 1
    n_universal = 42  # Start Nummer für universelle Nummer
    num_dict = {}  # ID/Nummern statt Sagennamen als key. Manche Sagen können die gleichen Titel haben, zb. einfach Nummern
    i = 0
    uid = 1010
    pid = 84
    werkID = 6
    dict = {}

    for title in titles:
        # print(i)
        group = "NaN"
        categorie = "NaN"  # if cat and group already in dict, replace with value[1]. Nested categories split using a symbol(f.ex. @)
        placeID = locs[i][0]
        longitude = locs[i][2]
        latitude = locs[i][1]
        # xml_id = "Elsass2" + str(n_book)
        dict[title] = {"id": uid,
                       "werk_id": werkID,
                       "n_book": n_book,
                       "title": title,
                       "division_1": categorie,
                       "division_2": group,
                       "place_id": placeID,
                       "longitude": longitude,
                       "latitude": latitude}
        # num_dict[xml_id] = dict[key]
        n_book += 1
        i += 1
        uid += 1
    print(dict)
    # print(num_dict)

    with open("lothringen_sagen.json", "w", encoding="UTF-8") as f:
        json.dump(dict, f, ensure_ascii=False, indent=2)

    return dict

get_dict()


def get_front():
    with open("vorwort/lothringen_vorwort.txt", "r", encoding="utf-8") as f:
        return " ".join(
            [
                word.strip()
                for word in f.read().split()
            ]
        )


def get_back():
    with open("nachwort/lothringen_nachwort.txt", "r", encoding="utf-8") as f:
        return " ".join(
            [
                word.strip()
                for word in f.read().split()
            ]
        )


def get_sql():
    name = "lothringen_sagen"
    book_title = "Sagen und Bilder aus Lothringens Vorzeit"
    dict = get_dict()
    # lang = "deutsch"
    return name, book_title, dict
