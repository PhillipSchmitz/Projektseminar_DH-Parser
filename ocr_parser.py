import re

with open("ocr_sagen/trier_umgebung_sagen.txt", "r", encoding="utf-8") as f:
    sagen = f.readlines()

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
              "Karthaufe",
              "St. Medard",
              "St. Matheis",
              "Heiligkreuz",
              "Die Seufzerallee",
              "Die Olewig",
              "Das Franzenknöppchen",
              "Castell an der Saar",
              "Fließem",
              "Verschiedenes"
              ]

sort_sagen = []
i = 0
j = 0
s = []
b = True
for sage in sagen:
    add = True
    if titles[i] in sage:
        # print(titles[i])
        i += 1
        b = True
        sort_sagen.append(s)
        #print(s)
        s = []
    if not re.search(r"----- \d+ / \d+ -----", sage):
        if not re.search(r"\d+", sage):
            for cat in categories:
                cat = cat + ".\n"
                #print(cat)
                if sage == cat:
                    add = False
                    print(sage)
                    break
                cat = cat[4:]
                if sage == cat:
                    add = False
                    print(sage)
                    break
            if add:
                s.append(sage)
    # print(s)
    j += 1
    if b:
        # print(j)
        b = False

del sort_sagen[0]
i = 0
for sage in sort_sagen:
    print(sage)
    sage[0] = re.sub(r"\*", "", sage[0])
    with open("trier_umgebung_sagen/" + str(i) + " " + sage[0][0:-2] + ".txt", "w", encoding="utf-8") as f:
        f.writelines(sage)
    i += 1

#print(len(titles))