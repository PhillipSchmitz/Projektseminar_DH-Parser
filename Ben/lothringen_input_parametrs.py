def get_tei_header():
    MainTitle = "Trier und seine Umgebung in Sagen und Liedern."
    SubTitle = "Mit Bemerkungen über die Quellen dieser Sagen."
    Author = "Ph. Laven"
    PublicationYear = "1851"
    PublicationPlace = "Trier, Germany"
    # PublicationCountry="Germany"
    Publisher = "Verlag der Fr. Lintz'schen Buchhandlung"
    #Edition = "first"
    Edition = None
    source = "Sagen, die aus Trier selbst stammen oder dem nahen Umfeld"

    Copyright = "CC0"
    encoder = "Ben Conrad"

    return MainTitle, SubTitle, Author, PublicationYear, PublicationPlace, Publisher, Edition,source, Copyright, encoder


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
            ['Metz', 49.119722, 6.176944], "Verdun", 49.159722, 5.382778]

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
        group = "NoGroup"
        categorie = "NoCategory"  # if cat and group already in dict, replace with value[1]. Nested categories split using a symbol(f.ex. @)
        placeID = locs[i][0]
        longitude = locs[i][2]
        latitude = locs[i][1]
        # xml_id = "Elsass2" + str(n_book)
        dict[title] = [uid, werkID, n_book, title, categorie, group, placeID, longitude,
                       latitude]
        # num_dict[xml_id] = dict[key]
        n_book += 1
        i += 1
        uid += 1
    print(dict)
    # print(num_dict)

    return dict


def get_sql():
    name = "lothringen_sagen"
    book_title = "Sagen und Bilder aus Lothringens Vorzeit"
    dict = get_dict()
    # lang = "deutsch"
    return name, book_title, dict
