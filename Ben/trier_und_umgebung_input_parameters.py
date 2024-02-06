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
    uid = 1716
    pid = 84
    werkID = "Trier1"

    for title, value in dict.items():
        group = value
        categorie = "noCategorie"  # if cat and group already in dict, replace with value[1]. Nested categories split using a symbol(f.ex. @)
        for o in ort:
            if value in o:
                placeID = value
                longitude = o[2]
                latitude = o[1]
            else:
                placeID = "Trier"
                latitude = 49.76917
                longitude = 6.675
        # xml_id = "Trier1." + str(n_book)
        dict[title] = [uid, pid, uid, werkID, n_book, title, categorie, group, placeID, longitude,
                       latitude, 3]  # je nach Werk anpassen {Name der Sage: Kategorie, Gruppe, Nummer im Werk, universelle Nummer, XML-ID}

        # num_dict[xml_id] = dict[title]
        n_book += 1
        uid += 1
    #print(dict)
    return dict


def get_sql():
    name = "trier_umgebung_sagen"
    book_title = "Trier und seine Umgebung in Sagen und Liedern"
    dict = get_dict()
    return name, book_title, dict

#get_dict()
