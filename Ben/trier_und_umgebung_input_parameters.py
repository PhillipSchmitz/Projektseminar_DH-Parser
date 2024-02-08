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

def get_pkl():
    pickle_filename = "trier_umgebung_sagen"
    return pickle_filename

def get_dict():
    dict = {"Das Bild der Stärke": "Die Porta nigra",
            "Arimaspes und Eptes": "Die Porta nigra",
            "Die Teufelskirche": "Die Porta nigra",
            "St. Simeon": "Die Porta nigra",
            "Betrachtung": "Die Römischen Bäder",
            "Das goldene Kalb": "Die Römischen Bäder",
            "Die Arena": "Das Amphitheater",
            "Der Frankenfürst": "Das Amphitheater",
            "Bestrafte Untreue": "Das Amphitheater",
            "Katholdis": "Das Amphitheater",
            "Der gespenstige Kaiser": "Der Constantinische Palast",
            "Das Ungeheuer": "Das Neuthor",
            "St. Nicolas": "Die Moselbrücke",
            "Das Verließ": "Die Moselbrücke",
            "Constantius": "Der Dom",
            "Helena": "Der Dom",
            "Die Schwalben": "Der Dom",
            "Der Krummelstuhl": "Der Domkreuzgang",
            "Das alte Trier": "Die Stadt Trier",
            "Der Stadtgeist": "Die Stadt Trier",
            "Trier's Wahrzeichen": "Die Stadt Trier",
            "Das Trebeta-Bild auf dem Stadthause": "Einzelheiten der Stadt Trier",
            "Der Engelberg": "Einzelheiten der Stadt Trier",
            "Die Blume der Mägde": "Einzelheiten der Stadt Trier",
            "Der mit der Elle gemessene Wein": "Einzelheiten der Stadt Trier",
            "Das Marktkreuz": "Einzelheiten der Stadt Trier",
            "Die Inschrift auf der Steipe": "Einzelheiten der Stadt Trier",
            "Die Steine des Gymnasiums": "Einzelheiten der Stadt Trier",
            "Coder aureus": "Einzelheiten der Stadt Trier",
            "Sendung Rictiovar's nach Trier": "St. Paulin",
            "Einzug der Thebaischen Legion": "St. Paulin",
            "Das Kreuz": "St. Paulin",
            "Die vier Steine": "St. Paulin",
            "Das Deckengemälde der St. Paulinskirche": "St. Paulin",
            "Der Engel mit dem hölzernen Beine": "St. Paulin",
            "Cunnet's Tod": "St. Paulin",
            "Der Mohr": "Nells Ländchen",
            "Die Zauberstiefel": "Pfalzel",
            "Unverhoffte Rettung": "Biewer",
            "Die Hieronymus-Höhle": "St. Marien",
            "Friedrich Spee": "St. Marien",
            "Der eingemauerte Mönch": "St. Marien",
            "Heiteres Leben": "Zurlauben",
            "Die Blume des Thales": "Pallien",
            "Najaden-Tänze": "Pallien",
            "Der Krondiamant": "Das Weißhaus",
            "Hommerspläßchen": "Der Kockelsberg",
            "Ansicht": "Der Wasserfall",
            "Der Fremde und das Sandmädchen": "Der Wasserfall",
            "Das Mühlenthal": "Der Wasserfall",
            "Das Heinzemännchen": "Der Wasserfall",
            "Schlürfen": "Kaffee Wettendorf",
            "Das Metzgerskreuzchen": "Der Pulsberg",
            "Sonnenaufgang": "Der Markusberg",
            "Die Octave": "Der Markusberg",
            "Das Glöcklein": "Der Markusberg",
            "Der Wassersalamander": "Balduinshäuschen",  # Wasserfalamandar im OCR
            "In nomine domini": "Balduinshäuschen",
            "Der letzte Stuart": "Balduinshäuschen",
            "Der Helenabrunnen": "Euren",
            "Der Steinbruch der Liebfrauenkirche": "Zewen",
            "Das Abschiedsdenkmal": "Igel",
            "Der Todtenkopf-Mantel": "Konz",
            "Der verborgene Keller": "Karthaufe",
            "Das gerettete Kind": "St. Medard",
            "Medardin von Rottenfelt": "St. Matheis",
            "Alte Inschrift": "St. Matheis",
            "Der Matheiser Sauerbrunnen": "St. Matheis",
            "Die Forsthütte": "St. Matheis",
            "Siko": "Heiligkreuz",
            "Spaziergang": "Die Seufzerallee",  # spazirgang im.txt verbessert
            "Der Name Olewig": "Die Olewig",
            "Ländliche Bilder": "Die Olewig",
            "Sauere Milch": "Die Olewig",
            "Trebeta's Grab": "Das Franzenknöppchen",
            "Sickingens Kanonenkugel": "Das Franzenknöppchen",
            "Der Erdhügel": "Das Franzenknöppchen",
            "Die Kreuzkapelle": "Das Franzenknöppchen",
            "Das Marmorbett": "Castell an der Saar",
            "Der Hirtenknabe": "Fließem",
            "Der gekreuzigte Amor": "Verschiedenes",
            "Die drei Helden": "Verschiedenes",
            "Glimpf und Schimpf des Moselweins": "Verschiedenes",
            "Betheuerungen eines Liebhabers": "Verschiedenes",
            "Bemerkungen": "Verschiedenes"
            }

    ort = [["Euren", 49.74023, 6.60896], ["Zewen", 49.71985, 6.57681], ["Igel", 49.71033, 6.55498],
           ["Konz", 49.69539, 6.57329], ["Castell an der Saar", 49.56513, 6.55942]]

    n_book = 1
    n_universal = 42  # Start Nummer für universelle Nummer
    num_dict = {}  # ID/Nummern statt Sagennamen als key. Manche Sagen können die gleichen Titel haben, zb. einfach Nummern
    uid = 1
    pid = 84
    werkID = 1

    for title, value in dict.items():
        group = value
        categorie = "NoCategory"  # if cat and group already in dict, replace with value[1]. Nested categories split using a symbol(f.ex. @)
        for o in ort:
            if value in o:
                print(value)
                placeID = value
                longitude = o[2]
                latitude = o[1]
                break
            else:
                placeID = "Trier"
                latitude = 49.76917
                longitude = 6.675
        # xml_id = "Trier1." + str(n_book)
        dict[title] = [uid, werkID, n_book, title, categorie, group, placeID, longitude,
                       latitude]  # je nach Werk anpassen {Name der Sage: Kategorie, Gruppe, Nummer im Werk, universelle Nummer, XML-ID}

        # num_dict[xml_id] = dict[title]
        n_book += 1
        uid += 1
    print(dict)
    return dict


def get_sql():
    name = "trier_umgebung_sagen"
    book_title = "Trier und seine Umgebung in Sagen und Liedern"
    dict = get_dict()
    return name, book_title, dict

get_dict()
{'Das Bild der Stärke': [1, 1, 1, 'Das Bild der Stärke', 'NoCategory', 'Die Porta nigra', 'Trier', 6.675, 49.76917], 'Arimaspes und Eptes': [2, 1, 2, 'Arimaspes und Eptes', 'NoCategory', 'Die Porta nigra', 'Trier', 6.675, 49.76917], 'Die Teufelskirche': [3, 1, 3, 'Die Teufelskirche', 'NoCategory', 'Die Porta nigra', 'Trier', 6.675, 49.76917], 'St. Simeon': [4, 1, 4, 'St. Simeon', 'NoCategory', 'Die Porta nigra', 'Trier', 6.675, 49.76917], 'Betrachtung': [5, 1, 5, 'Betrachtung', 'NoCategory', 'Die Römischen Bäder', 'Trier', 6.675, 49.76917], 'Das goldene Kalb': [6, 1, 6, 'Das goldene Kalb', 'NoCategory', 'Die Römischen Bäder', 'Trier', 6.675, 49.76917], 'Die Arena': [7, 1, 7, 'Die Arena', 'NoCategory', 'Das Amphitheater', 'Trier', 6.675, 49.76917], 'Der Frankenfürst': [8, 1, 8, 'Der Frankenfürst', 'NoCategory', 'Das Amphitheater', 'Trier', 6.675, 49.76917], 'Bestrafte Untreue': [9, 1, 9, 'Bestrafte Untreue', 'NoCategory', 'Das Amphitheater', 'Trier', 6.675, 49.76917], 'Katholdis': [10, 1, 10, 'Katholdis', 'NoCategory', 'Das Amphitheater', 'Trier', 6.675, 49.76917], 'Der gespenstige Kaiser': [11, 1, 11, 'Der gespenstige Kaiser', 'NoCategory', 'Der Constantinische Palast', 'Trier', 6.675, 49.76917], 'Das Ungeheuer': [12, 1, 12, 'Das Ungeheuer', 'NoCategory', 'Das Neuthor', 'Trier', 6.675, 49.76917], 'St. Nicolas': [13, 1, 13, 'St. Nicolas', 'NoCategory', 'Die Moselbrücke', 'Trier', 6.675, 49.76917], 'Das Verließ': [14, 1, 14, 'Das Verließ', 'NoCategory', 'Die Moselbrücke', 'Trier', 6.675, 49.76917], 'Constantius': [15, 1, 15, 'Constantius', 'NoCategory', 'Der Dom', 'Trier', 6.675, 49.76917], 'Helena': [16, 1, 16, 'Helena', 'NoCategory', 'Der Dom', 'Trier', 6.675, 49.76917], 'Die Schwalben': [17, 1, 17, 'Die Schwalben', 'NoCategory', 'Der Dom', 'Trier', 6.675, 49.76917], 'Der Krummelstuhl': [18, 1, 18, 'Der Krummelstuhl', 'NoCategory', 'Der Domkreuzgang', 'Trier', 6.675, 49.76917], 'Das alte Trier': [19, 1, 19, 'Das alte Trier', 'NoCategory', 'Die Stadt Trier', 'Trier', 6.675, 49.76917], 'Der Stadtgeist': [20, 1, 20, 'Der Stadtgeist', 'NoCategory', 'Die Stadt Trier', 'Trier', 6.675, 49.76917], "Trier's Wahrzeichen": [21, 1, 21, "Trier's Wahrzeichen", 'NoCategory', 'Die Stadt Trier', 'Trier', 6.675, 49.76917], 'Das Trebeta-Bild auf dem Stadthause': [22, 1, 22, 'Das Trebeta-Bild auf dem Stadthause', 'NoCategory', 'Einzelheiten der Stadt Trier', 'Trier', 6.675, 49.76917], 'Der Engelberg': [23, 1, 23, 'Der Engelberg', 'NoCategory', 'Einzelheiten der Stadt Trier', 'Trier', 6.675, 49.76917], 'Die Blume der Mägde': [24, 1, 24, 'Die Blume der Mägde', 'NoCategory', 'Einzelheiten der Stadt Trier', 'Trier', 6.675, 49.76917], 'Der mit der Elle gemessene Wein': [25, 1, 25, 'Der mit der Elle gemessene Wein', 'NoCategory', 'Einzelheiten der Stadt Trier', 'Trier', 6.675, 49.76917], 'Das Marktkreuz': [26, 1, 26, 'Das Marktkreuz', 'NoCategory', 'Einzelheiten der Stadt Trier', 'Trier', 6.675, 49.76917], 'Die Inschrift auf der Steipe': [27, 1, 27, 'Die Inschrift auf der Steipe', 'NoCategory', 'Einzelheiten der Stadt Trier', 'Trier', 6.675, 49.76917], 'Die Steine des Gymnasiums': [28, 1, 28, 'Die Steine des Gymnasiums', 'NoCategory', 'Einzelheiten der Stadt Trier', 'Trier', 6.675, 49.76917], 'Coder aureus': [29, 1, 29, 'Coder aureus', 'NoCategory', 'Einzelheiten der Stadt Trier', 'Trier', 6.675, 49.76917], "Sendung Rictiovar's nach Trier": [30, 1, 30, "Sendung Rictiovar's nach Trier", 'NoCategory', 'St. Paulin', 'Trier', 6.675, 49.76917], 'Einzug der Thebaischen Legion': [31, 1, 31, 'Einzug der Thebaischen Legion', 'NoCategory', 'St. Paulin', 'Trier', 6.675, 49.76917], 'Das Kreuz': [32, 1, 32, 'Das Kreuz', 'NoCategory', 'St. Paulin', 'Trier', 6.675, 49.76917], 'Die vier Steine': [33, 1, 33, 'Die vier Steine', 'NoCategory', 'St. Paulin', 'Trier', 6.675, 49.76917], 'Das Deckengemälde der St. Paulinskirche': [34, 1, 34, 'Das Deckengemälde der St. Paulinskirche', 'NoCategory', 'St. Paulin', 'Trier', 6.675, 49.76917], 'Der Engel mit dem hölzernen Beine': [35, 1, 35, 'Der Engel mit dem hölzernen Beine', 'NoCategory', 'St. Paulin', 'Trier', 6.675, 49.76917], "Cunnet's Tod": [36, 1, 36, "Cunnet's Tod", 'NoCategory', 'St. Paulin', 'Trier', 6.675, 49.76917], 'Der Mohr': [37, 1, 37, 'Der Mohr', 'NoCategory', 'Nells Ländchen', 'Trier', 6.675, 49.76917], 'Die Zauberstiefel': [38, 1, 38, 'Die Zauberstiefel', 'NoCategory', 'Pfalzel', 'Trier', 6.675, 49.76917], 'Unverhoffte Rettung': [39, 1, 39, 'Unverhoffte Rettung', 'NoCategory', 'Biewer', 'Trier', 6.675, 49.76917], 'Die Hieronymus-Höhle': [40, 1, 40, 'Die Hieronymus-Höhle', 'NoCategory', 'St. Marien', 'Trier', 6.675, 49.76917], 'Friedrich Spee': [41, 1, 41, 'Friedrich Spee', 'NoCategory', 'St. Marien', 'Trier', 6.675, 49.76917], 'Der eingemauerte Mönch': [42, 1, 42, 'Der eingemauerte Mönch', 'NoCategory', 'St. Marien', 'Trier', 6.675, 49.76917], 'Heiteres Leben': [43, 1, 43, 'Heiteres Leben', 'NoCategory', 'Zurlauben', 'Trier', 6.675, 49.76917], 'Die Blume des Thales': [44, 1, 44, 'Die Blume des Thales', 'NoCategory', 'Pallien', 'Trier', 6.675, 49.76917], 'Najaden-Tänze': [45, 1, 45, 'Najaden-Tänze', 'NoCategory', 'Pallien', 'Trier', 6.675, 49.76917], 'Der Krondiamant': [46, 1, 46, 'Der Krondiamant', 'NoCategory', 'Das Weißhaus', 'Trier', 6.675, 49.76917], 'Hommerspläßchen': [47, 1, 47, 'Hommerspläßchen', 'NoCategory', 'Der Kockelsberg', 'Trier', 6.675, 49.76917], 'Ansicht': [48, 1, 48, 'Ansicht', 'NoCategory', 'Der Wasserfall', 'Trier', 6.675, 49.76917], 'Der Fremde und das Sandmädchen': [49, 1, 49, 'Der Fremde und das Sandmädchen', 'NoCategory', 'Der Wasserfall', 'Trier', 6.675, 49.76917], 'Das Mühlenthal': [50, 1, 50, 'Das Mühlenthal', 'NoCategory', 'Der Wasserfall', 'Trier', 6.675, 49.76917], 'Das Heinzemännchen': [51, 1, 51, 'Das Heinzemännchen', 'NoCategory', 'Der Wasserfall', 'Trier', 6.675, 49.76917], 'Schlürfen': [52, 1, 52, 'Schlürfen', 'NoCategory', 'Kaffee Wettendorf', 'Trier', 6.675, 49.76917], 'Das Metzgerskreuzchen': [53, 1, 53, 'Das Metzgerskreuzchen', 'NoCategory', 'Der Pulsberg', 'Trier', 6.675, 49.76917], 'Sonnenaufgang': [54, 1, 54, 'Sonnenaufgang', 'NoCategory', 'Der Markusberg', 'Trier', 6.675, 49.76917], 'Die Octave': [55, 1, 55, 'Die Octave', 'NoCategory', 'Der Markusberg', 'Trier', 6.675, 49.76917], 'Das Glöcklein': [56, 1, 56, 'Das Glöcklein', 'NoCategory', 'Der Markusberg', 'Trier', 6.675, 49.76917], 'Der Wassersalamander': [57, 1, 57, 'Der Wassersalamander', 'NoCategory', 'Balduinshäuschen', 'Trier', 6.675, 49.76917], 'In nomine domini': [58, 1, 58, 'In nomine domini', 'NoCategory', 'Balduinshäuschen', 'Trier', 6.675, 49.76917], 'Der letzte Stuart': [59, 1, 59, 'Der letzte Stuart', 'NoCategory', 'Balduinshäuschen', 'Trier', 6.675, 49.76917], 'Der Helenabrunnen': [60, 1, 60, 'Der Helenabrunnen', 'NoCategory', 'Euren', 'Euren', 6.60896, 49.74023], 'Der Steinbruch der Liebfrauenkirche': [61, 1, 61, 'Der Steinbruch der Liebfrauenkirche', 'NoCategory', 'Zewen', 'Zewen', 6.57681, 49.71985], 'Das Abschiedsdenkmal': [62, 1, 62, 'Das Abschiedsdenkmal', 'NoCategory', 'Igel', 'Igel', 6.55498, 49.71033], 'Der Todtenkopf-Mantel': [63, 1, 63, 'Der Todtenkopf-Mantel', 'NoCategory', 'Konz', 'Konz', 6.57329, 49.69539], 'Der verborgene Keller': [64, 1, 64, 'Der verborgene Keller', 'NoCategory', 'Karthaufe', 'Trier', 6.675, 49.76917], 'Das gerettete Kind': [65, 1, 65, 'Das gerettete Kind', 'NoCategory', 'St. Medard', 'Trier', 6.675, 49.76917], 'Medardin von Rottenfelt': [66, 1, 66, 'Medardin von Rottenfelt', 'NoCategory', 'St. Matheis', 'Trier', 6.675, 49.76917], 'Alte Inschrift': [67, 1, 67, 'Alte Inschrift', 'NoCategory', 'St. Matheis', 'Trier', 6.675, 49.76917], 'Der Matheiser Sauerbrunnen': [68, 1, 68, 'Der Matheiser Sauerbrunnen', 'NoCategory', 'St. Matheis', 'Trier', 6.675, 49.76917], 'Die Forsthütte': [69, 1, 69, 'Die Forsthütte', 'NoCategory', 'St. Matheis', 'Trier', 6.675, 49.76917], 'Siko': [70, 1, 70, 'Siko', 'NoCategory', 'Heiligkreuz', 'Trier', 6.675, 49.76917], 'Spaziergang': [71, 1, 71, 'Spaziergang', 'NoCategory', 'Die Seufzerallee', 'Trier', 6.675, 49.76917], 'Der Name Olewig': [72, 1, 72, 'Der Name Olewig', 'NoCategory', 'Die Olewig', 'Trier', 6.675, 49.76917], 'Ländliche Bilder': [73, 1, 73, 'Ländliche Bilder', 'NoCategory', 'Die Olewig', 'Trier', 6.675, 49.76917], 'Sauere Milch': [74, 1, 74, 'Sauere Milch', 'NoCategory', 'Die Olewig', 'Trier', 6.675, 49.76917], "Trebeta's Grab": [75, 1, 75, "Trebeta's Grab", 'NoCategory', 'Das Franzenknöppchen', 'Trier', 6.675, 49.76917], 'Sickingens Kanonenkugel': [76, 1, 76, 'Sickingens Kanonenkugel', 'NoCategory', 'Das Franzenknöppchen', 'Trier', 6.675, 49.76917], 'Der Erdhügel': [77, 1, 77, 'Der Erdhügel', 'NoCategory', 'Das Franzenknöppchen', 'Trier', 6.675, 49.76917], 'Die Kreuzkapelle': [78, 1, 78, 'Die Kreuzkapelle', 'NoCategory', 'Das Franzenknöppchen', 'Trier', 6.675, 49.76917], 'Das Marmorbett': [79, 1, 79, 'Das Marmorbett', 'NoCategory', 'Castell an der Saar', 'Castell an der Saar', 6.55942, 49.56513], 'Der Hirtenknabe': [80, 1, 80, 'Der Hirtenknabe', 'NoCategory', 'Fließem', 'Trier', 6.675, 49.76917], 'Der gekreuzigte Amor': [81, 1, 81, 'Der gekreuzigte Amor', 'NoCategory', 'Verschiedenes', 'Trier', 6.675, 49.76917], 'Die drei Helden': [82, 1, 82, 'Die drei Helden', 'NoCategory', 'Verschiedenes', 'Trier', 6.675, 49.76917], 'Glimpf und Schimpf des Moselweins': [83, 1, 83, 'Glimpf und Schimpf des Moselweins', 'NoCategory', 'Verschiedenes', 'Trier', 6.675, 49.76917], 'Betheuerungen eines Liebhabers': [84, 1, 84, 'Betheuerungen eines Liebhabers', 'NoCategory', 'Verschiedenes', 'Trier', 6.675, 49.76917], 'Bemerkungen': [85, 1, 85, 'Bemerkungen', 'NoCategory', 'Verschiedenes', 'Trier', 6.675, 49.76917]}
