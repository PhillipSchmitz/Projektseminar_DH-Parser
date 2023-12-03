def get_titles_trier_umgebung():
    titles = ["Das Bild der Stärke",
              "Arimaspes und Eptes",
              "Die Teufelskirche",
              "St. Simeon",
              "Betrachtung",
              "Das goldene Kalb",
              "Die Arena",
              "Der Frankenfürst",
              "Bestrafte Untreue",
              "Katholdis",
              "Der gespenstige Kaiser",
              "Das Ungeheuer",
              "St. Nicolas",
              "Das Verließ",
              "Constantius",
              "Helena",
              "Die Schwalben",
              "Der Krummelstuhl",
              "Das alte Trier",
              "Der Stadtgeist",
              "Trier's Wahrzeichen",
              "Das Trebeta-Bild auf dem Stadthause",
              "Der Engelberg",
              "Die Blume der Mägde",
              "Der mit der Elle gemessene Wein",
              "Das Marktkreuz",
              "Die Inschrift auf der Steipe",
              "Die Steine des Gymnasiums",
              "Coder aureus",
              "Sendung Rictiovar's nach Trier",
              "Einzug der Thebaischen Legion",
              "Das Kreuz",
              "Die vier Steine",
              "Das Deckengemälde der St. Paulinskirche",
              "Der Engel mit dem hölzernen Beine",
              "Cunnet's Tod",
              "Der Mohr",
              "Die Zauberstiefel",
              "Unverhoffte Rettung",
              "Die Hieronymus-Höhle",
              "Friedrich Spee",
              "Der eingemauerte Mönch",
              "Heiteres Leben",
              "Die Blume des Thales",
              "Najaden-Tänze",
              "Der Krondiamant",
              "Hommerspläßchen",
              "Ansicht",
              "Der Fremde und das Sandmädchen",
              "Das Mühlenthal",
              "Das Heinzemännchen",
              "Schlürfen",
              "Das Metzgerskreuzchen",
              "Sonnenaufgang",
              "Die Octave",
              "Das Glöcklein",
              "Der Wassersalamander",
              "In nomine domini",
              "Der letzte Stuart",
              "Der Helenabrunnen",
              "Der Steinbruch der Liebfrauenkirche",
              "Das Abschiedsdenkmal",
              "Der Todtenkopf-Mantel",
              "Der verborgene Keller",
              "Das gerettete Kind",
              "Medardin von Rottenfelt",
              "Alte Inschrift",
              "Der Matheiser Sauerbrunnen",
              "Die Forsthütte",
              "Siko",
              "Spaziergang",
              "Der Name Olewig",
              "Ländliche Bilder",
              "Sauere Milch",
              "Trebeta's Grab",
              "Sickingens Kanonenkugel",
              "Der Erdhügel",
              "Die Kreuzkapelle",
              "Das Marmorbett",
              "Der Hirtenknabe",
              "Der gekreuzigte Amor",
              "Die drei Helden",
              "Glimpf und Schimpf des Moselweins",
              "Betheuerungen eines Liebhabers",
              "Bemerkungen",
              "qwertz"
              ]

    return titles


def get_categories_trier_umgebung():
    categories = ["Die Porta nigra",
                  "Die Römischen Bäder",
                  "Römische Bäder",
                  "Das Amphitheater",
                  "Der Constantinische Palast",
                  "Das Neuthor",
                  "Die Moselbrücke",
                  "Der Dom",
                  "Der Domkreuzgang",
                  "Die Stadt Trier",
                  "Die Stadt Crier",
                  "Einzelheiten der Stadt Trier",
                  "St. Paulin",
                  "Nell's Ländchen",
                  "Pfalzel",
                  "Biewer",
                  "St. Marien",
                  "Zurlauben",
                  "Pallien",
                  "Das Weißhaus",
                  "Der Kockelsberg",
                  "Der Wasserfall",
                  "Kaffe Wettendorf",
                  "Der Pulsberg",
                  "Der Markusberg",
                  "Balduinshäuschen",
                  "Euren",
                  "Zewen",
                  "Igel",
                  "Conz",
                  "Karthause",  # og Index: Karthaufe
                  "St. Medard",
                  "St. Matheis",
                  "Heiligkreuz",
                  "Die Seufzerallee",
                  "Die Olewig",
                  "Das Franzenknöppchen",
                  "Castell an der Saar",
                  "Fliessem",  # og Index: Fließem
                  "Verschiedenes"
                  ]
    return categories


def get_dict_trier_umgebung():
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
    return dict