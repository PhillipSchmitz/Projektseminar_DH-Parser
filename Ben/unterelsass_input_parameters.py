def get_tei_header():
    MainTitle = "Trier und seine Umgebung in Sagen und Liedern."
    SubTitle = "Mit Bemerkungen über die Quellen dieser Sagen."
    Author = "Ph. Laven"
    PublicationYear = "1851"
    PublicationPlace = "Trier, Germany"
    # PublicationCountry="Germany"
    Publisher = "Verlag der Fr. Lintz'schen Buchhandlung"
    Edition = "first"

    Copyright = "CC0"
    encoder = "Ben Conrad"

    return MainTitle, SubTitle, Author, PublicationYear, PublicationPlace, Publisher, Edition, Copyright, encoder

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
    
    n_book=1
    n_universal=42  #Start Nummer für universelle Nummer
    num_dict = {}  #ID/Nummern statt Sagennamen als key. Manche Sagen können die gleichen Titel haben, zb. einfach Nummern

    for key, value in dict.items():
        group = value                       
        categorie = "noCategorie"               #if cat and group already in dict, replace with value[1]. Nested categories split using a symbol(f.ex. @)
        placeID="noPlace"
        xml_id = "Trier1." + str(n_book)
        dict[key]=[key, categorie, group, placeID,n_book, n_book + n_universal, xml_id]     #je nach Werk anpassen {Name der Sage: Kategorie, Gruppe, Nummer im Werk, universelle Nummer, XML-ID}
        
        num_dict[xml_id] = dict[key]
        n_book +=1
    
    print(dict)
    print(num_dict)

    

    return dict

def get_sql():
    name = "trier_umgebung_sagen"
    book_title = "Trier und seine Umgebung in Sagen und Liedern"
    dict = get_dict()
    lang = "deutsch"
    return name, book_title, dict, lang


get_dict()



