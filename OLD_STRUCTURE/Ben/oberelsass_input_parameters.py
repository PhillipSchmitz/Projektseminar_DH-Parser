import json


def get_tei_header():
    MainTitle = "Die Sagen des Elsasses"
    SubTitle = "getreu nach der Volksüberlieferung, den Chroniken und andern gedruckten und handschriftlichen Quellen, gesammelt von August Stöber. Neue Ausgabe besorgt von Kurt Mündel. Erster Teil. Die Sagen des Ober-Elsass."
    Author = "August Stöber"
    PublicationYear = "1892"
    PublicationPlace = "Strassburg, German Empire (modern day France)"
    # PublicationCountry="Germany"
    Publisher = "J. H. Ed Heitz (Heitz & Mündel)"
    Edition = "Erster Teil. Die Sagen des Ober-Elsass"
    srcDesc = "Von August Stöber gesammelte Sagen über den Oberelsass"

    Copyright = "CC0"
    encoder = "Ben Conrad, Dennis Binz"

    return [MainTitle, SubTitle, Author, PublicationYear, PublicationPlace, Publisher, Edition, srcDesc, Copyright,
            encoder]


def get_pkl():
    pickle_filename = "oberelsass_sagen"
    return pickle_filename


def get_dict():
    dict = {'Die Schlange im Jura': 'Jura', 'St. Morands Ruhe': 'Altkirch', 'Der Käpellegeist': 'Heimersdorf',
            'Die Zwerge in der Wolfshöhle': 'Pfirt', 'Des Teufels Recht auf Pfirt': 'Pfirt',
            'Die Todtenprozession zu Luppach': 'Luppach', 'Die Galgenplatte': 'Alt-Pfirt',
            'Der Lachgeist im Haag': 'Alt-Pfirt', 'Der Geist "Laxi" im Biederthaler Schlosse': 'Biederthal',
            'Junker Schnabel': 'Hagenthal', 'Die Here von Köstlach': 'Köstlach', 'Das Herenschloß': 'Dürlinsdorf',
            'Der Schmied im Berge': 'Dürlinsdorf', 'Das versunkene Schloß Färis und der alte Graf': 'Mörnach',
            'Die Herdwible von Mörnach': 'Mörnach', 'Die Erbauung von Liebenstein': 'Liebsdorf',
            'Der schwarze Vogel auf Liebenstein': 'Liebsdorf', 'Das Hündlein aus der wilden Jagd': 'Liebsdorf',
            'Der Hausgeist geht zur Kelte': 'Oberlarg', 'Die drei Spinnerinnen': 'Oberlarg',
            'Der Hexentanz auf der Kalmiser Waide': 'Oberlarg', 'Das gefundene Silbergeld bei Mörsperg': 'Oberlarg',
            'Der Mann mit dem Lapphute zu Oberlarg': 'Oberlarg', 'Die weiße Dame vom Goldigberg': 'Langizen',
            'Das Totenpferd und die Totenprozession zu Moos': 'Moos', 'Das Bildstöcklein bei Winkel': 'Winkel',
            'Das Altschloß bei Winkel': 'Winkel', 'Der Dornstrauch bei Neun-Eich': 'Lüzel',
            'Das Silberloch bei Lützel': 'Lüzel', 'Die weiße Frau auf dem Küppele': 'Jufurt',
            'Der Britzgyberg': 'Jufurt', 'Versenkte Glocken': 'Brubach, Didenheim',
            'Das Weingeigerlein auf Brunstatt': 'Brunstatt', 'Das schwarze Tier am Mühlbach': 'Brunstatt',
            'Die Gespensterheere im Nordfeld': 'Mülhausen', 'Kreuzregen': 'Mülhausen', 'Himmelschweiß': 'Mülhausen',
            'Der Schatzgräber am Davidsbrünnlein': 'Mülhausen', 'Die weiße Frau in grünen Pantoffeln': 'Mülhausen',
            'Der verlorene Bräutigam': 'Mülhausen', 'Der Milchsuppen-Acker': 'Mülhausen',
            'Die Henne mit den goldenen Eiern in der Sankt-Marx-Kapelle bei Riedisheim': 'Riedesheim',
            'Das Dorftier zu Hegenheim': 'Hegenheim bei Hüningen', 'Die Geisterkirche auf dem Rhein': 'Kembs, Niffer',
            'Der weiße Mann vom Illzacher Schlosse': 'Julzach', 'Die weiße Jungfrau am Weiher': 'Julzach',
            'Die weißen Mädchen an der Lindlache': 'Julzach', 'Der schwarze Mann am Rain': 'Julzach',
            'Die Erscheinung am Rain': 'Julzach', 'Das weiße Pferd': 'Julzach', 'Der Pferdeschatten am Rain': 'Julzach',
            'Der Nachtjäger': 'Julzach', 'Das Tucherle am Viertelssteg': 'Julzach', 'Das Doggele': 'Julzach',
            'Das Fronfastentier': 'Julzach', 'Der Dorfesel': 'Julzach', 'Der Milchbrunnen': 'Julzach',
            'Maria in der Eich': 'Rülisheim', 'Masmünsters Entstehung': 'Masmünster',
            'Der Lachtelweiher': 'Kirchberg bei Masmünster', 'Das Muttergottesbild in Sewen': 'Sewen',
            'Das Dambürle im Masmünsterthale': 'Masmünsterthal',
            'Die weiße Dame von Rothenberg': 'Rothenberg (Rougemont)', 'Die Gründung von Neu-Thann': 'Thann',
            'St. Theobaldus rettet Thann im Schwedenkriege': 'Thann', 'Das Ex Voto von der Kirche Alt-Thann': 'Thann',
            'Die gebannten Kriegsheere': 'Sennheim', 'Kaiser Barbarossa unter dem Bibelstein': 'Sennheim',
            'Der Freier auf Freundstein': 'Weile br ei Thann', 'Die Feldmesser auf dem Belchen': 'Großer Belchen',
            'Die Gespenstertiere im Belchensee': 'Großer Belchen', 'Wie Gebweiler gerettet ward. 1448': 'Gebweiler',
            'Des Fürsten zu Murbach jäher Tod. 1477': 'Gebweiler', 'Der Teufel auf Hugstein': 'Gebweiler',
            'Kunigunde von Hungerstein. 1487': 'Gebweiler', 'Der Schlangenkönig vom Heißenstein': 'Gebweiler',
            'Die Schwarze Frau am Heißenstein': 'Gebweiler', 'Die Alte auf der Barnabasbrücke': 'Gebweiler',
            'Der wundersame Käfer': 'Bühl bei Gebweiler', 'Die Glocke von Bühl': 'Bühl bei Gebweiler',
            'Die singende Jungfrau im Lauchthal': 'Bühl bei Gebweiler',
            'Die Erscheinung auf der Melkerei Hofrieth': 'Bühl bei Gebweiler',
            'Ritter Kurt und die Kapelle von Ungersheim': 'Ungersheim', 'St. Maria im Schäferthal': 'Sulzmatt',
            'Der Langenstein bei Sulzmatt': 'Sulzmatt', 'Die Stiftung des Klosters St. Valentin zu Rufach': 'Rufach',
            'St. Landolins Gut zu Rufach': 'Rufach', 'Die Weiber von Rufach': 'Rufach',
            'Das Hungertuch in der Kirche von Rufach': 'Rufach', 'Der Rufacher Galgen': 'Rufach',
            'Dem Teufel zu! 1721': 'Rufach', 'Der Bollenberg': 'Rufach', 'Die Wallfahrt Schauenberg': 'Geberschweier',
            'Die Greifenklaue des heiligen Imerius': 'Geberschweier', 'Bischof Friedrich von Zeringen': 'Geberschweier',
            'Die Stiftung des Kloster Marbach': 'Geberschweier', 'Graf Hugos Buße': 'Egisheim',
            'Bruno von Egisheim': 'Egisheim', 'Die Erscheinung in Pfeffels Garten': 'Colmar',
            'Die Erscheinung im Waschhause': 'Colmar', 'Die gespenstische Milchfrau': 'Colmar',
            'Das Nachtkalb': 'Colmar', 'Warum die Colmarer Knöpfler heißen': 'Colmar',
            'Die Kornmutter': 'Heiligkreuz bei Colmar', 'Frau Faste': 'Heiligkreuz bei Colmar',
            'Die wilde Jagd bei Heilig-Kreuz': 'Heiligkreuz bei Colmar',
            'Der Hexenzug in der Hardt': 'Hettenschlag bei Neubreisach',
            'Das Bruderhäuschen bei Widensolen': 'Widensolen bei Neubreisach', 'Der Riese im Kastenwald': 'Andolsheim',
            'Warum der Logelbach zur Gemeinde Winzenheim gehört': 'Logelbach bei Colmar',
            'Die weiße Frau von Pflixburg': 'Winzenheim',
            'Die Wallfahrt zum Waldbruderkreuz am Grabe des heiligen Ignatius': 'Zimmerbach',
            'Die Entstehung des Bades Sulzbach': 'Sulzbach', 'Die Zwerge auf dem Kerbholz': 'Sulzern',
            'Die Schrätzmännel': 'Sulzern', 'Der Grüne See im Münsterthale': 'Sulzern',
            'Der Soldatenschlatten am Hoheneck': 'Sulzern', 'Der goldene Wagen': 'Mezeral',
            'Der Alte vom Berge': 'Weier im Thale', 'Die Wallfahrt Dreien-Aehren': 'Drei Aehren',
            'Das Muttergottesbild zu Dreien-Aehren': 'Drei Aehren', 'Das Riesengrab auf dem Hohnack': 'Drei Aehren',
            'Das weiße Mädchen an der Fecht': 'Ingersheim', 'Der Geist im Ingersheimer Schlosse': 'Ingersheim',
            'Die Wöchnerin': 'Ingersheim', 'Der Hungerbrunnen': 'Ingersheim', 'St. Deodat': 'Ammerschweier',
            'Die Bilder der Muttergottes und des Evangelisten St. Johannes vergießen Thränen': 'Kienzheim',
            'Kaiser Friedrich Barbarossa in Kaysersberg': 'Kaysersberg',
            'Die riesenmäßigen Holzschuhe auf dem Rathause zu Kaysersberg': 'Kaysersberg', 'Der Flieger': 'Kaysersberg',
            'Die Teufelskutsche': 'Kaysersberg', 'Die Tschäpläre': 'Kaysersberg',
            'Das Pestkreuz bei Kaysersberg': 'Kaysersberg', 'Der feurige Kreis bei Rappoltsweiler': 'Kaysersberg',
            'Der Einsiedler von Alspach': 'Alspach bei Kaysersberg', 'Der weiße See': 'Urbeis (Orbey)',
            'Der Zellenberger Burgersmann': 'Reichenweier', 'Die heilige Hunna': 'Hunaweier',
            'Das Wappen des Grafen von Rappoltstein': 'Rappoltsweiler', 'Die Brüder von Rappoltstein': 'Rappoltsweiler',
            'Die Jungfrau auf St. Ulrich': 'Rappoltsweiler', 'Die drei Schwestern von Rappoltstein': 'Rappoltsweiler',
            "Herni's Kreuz": 'Rappoltsweiler', 'Das Silberglöcklein und die Schloßhunde': 'Rappoltsweiler',
            'Die Gespensterkutsche von Hoh-Rappoltstein': 'Rappoltsweiler',
            'Der Höllenhaken bei Rappoltsweiler': 'Rappoltsweiler', 'Der Hirzsprung': 'Rappoltsweiler',
            'Die Gründung von Dreikirchen oder Dusenbach': 'Rappoltsweiler',
            'Die gespenstige Herde': 'Elsenheim u Jllhäusern', 'Das Dorf Tannenkirch': 'Lanneukirch',
            'Das Dorftier von Tannenkirch': 'Lanneukirch', 'Die Here von Tannenkirch': 'Lanneukirch',
            'Das gelbe Fräulein auf der Hohkönigsburg': 'Hohlönigsburg bei Tannenkirch',
            'Die silberne Rose': 'Markirch', 'Warum die Markircher Silberminen Nichts mehr abwerfen': 'Markirch',
            'Der Jungfrauenplatz bei Markirch': 'Markirch', 'Die Glocke von Leberau': 'Leberau',
            'Der Charlemont': 'Leberau'}

    loc = [[], ['Altkirch', 47.6210336538, 7.24484329622], ['Heimersdorf', 47.563206505, 7.23667862006],
           ['Pfirt', 47.4935597154, 7.3158338091], ['Pfirt', 47.4935597154, 7.3158338091], [], [], [],
           ['Biederthal', 47.4709691234, 7.43560956506], ['Hagenthal', 47.5308980609, 7.48185417828],
           ['Köstlach', 47.5117644426, 7.2711596241], [], [], ['Mörnach', 47.5098929884, 7.24557465368],
           ['Mörnach', 47.5098929884, 7.24557465368], ['Liebsdorf', 47.4789687972, 7.2231472766],
           ['Liebsdorf', 47.4789687972, 7.2231472766], ['Liebsdorf', 47.4789687972, 7.2231472766],
           ['Oberlarg', 47.4511026465, 7.23130338788], ['Oberlarg', 47.4511026465, 7.23130338788],
           ['Oberlarg', 47.4511026465, 7.23130338788], ['Oberlarg', 47.4511026465, 7.23130338788],
           ['Oberlarg', 47.4511026465, 7.23130338788], [], ['Moos', 47.5112217629, 7.21307892037],
           ['Winkel', 47.4588691493, 7.26354708265], ['Winkel', 47.4588691493, 7.26354708265], [], [], [], [], [], [],
           [], ['Mülhausen', 47.749163303, 7.32570047509], ['Mülhausen', 47.749163303, 7.32570047509],
           ['Mülhausen', 47.749163303, 7.32570047509], ['Mülhausen', 47.749163303, 7.32570047509],
           ['Mülhausen', 47.749163303, 7.32570047509], ['Mülhausen', 47.749163303, 7.32570047509],
           ['Mülhausen', 47.749163303, 7.32570047509], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
           ['Rülisheim', 47.8223744559, 7.35273202444], [], [], ['Sewen', 47.8075577891, 6.88027043152], [], [],
           ['Thann', 48.3253039558, 7.34853223079], ['Thann', 48.3253039558, 7.34853223079],
           ['Thann', 48.3253039558, 7.34853223079], ['Sennheim', 49.0163802116, 0.323907540392],
           ['Sennheim', 49.0163802116, 0.323907540392], [], [], [], ['Gebweiler', 47.9096692207, 7.21013500007],
           ['Gebweiler', 47.9096692207, 7.21013500007], ['Gebweiler', 47.9096692207, 7.21013500007],
           ['Gebweiler', 47.9096692207, 7.21013500007], ['Gebweiler', 47.9096692207, 7.21013500007],
           ['Gebweiler', 47.9096692207, 7.21013500007], ['Gebweiler', 47.9096692207, 7.21013500007], [], [], [], [],
           ['Ungersheim', 47.8739838916, 7.30532668717], ['Sulzmatt', 47.9701032152, 7.21175482373],
           ['Sulzmatt', 47.9701032152, 7.21175482373], ['Rufach', 47.9688422434, 7.27338874141],
           ['Rufach', 47.9688422434, 7.27338874141], ['Rufach', 47.9688422434, 7.27338874141],
           ['Rufach', 47.9688422434, 7.27338874141], ['Rufach', 47.9688422434, 7.27338874141],
           ['Rufach', 47.9688422434, 7.27338874141], ['Rufach', 47.9688422434, 7.27338874141],
           ['Geberschweier', 48.0068225604, 7.25975546236], ['Geberschweier', 48.0068225604, 7.25975546236],
           ['Geberschweier', 48.0068225604, 7.25975546236], ['Geberschweier', 48.0068225604, 7.25975546236],
           ['Egisheim', 48.0371183049, 7.30052876111], ['Egisheim', 48.0371183049, 7.30052876111],
           ['Colmar', 48.1099405789, 7.38468690323], ['Colmar', 48.1099405789, 7.38468690323],
           ['Colmar', 48.1099405789, 7.38468690323], ['Colmar', 48.1099405789, 7.38468690323],
           ['Colmar', 48.1099405789, 7.38468690323], [], [], [], [], [], ['Andolsheim', 48.0652206217, 7.43654259206],
           [], ['Winzenheim', 48.6578223701, 7.50786446733], ['Zimmerbach', 48.0745599556, 7.23005041952],
           ['Sulzbach', 48.0284078615, 7.20442898654], ['Sulzern', 48.0828918874, 7.09256896947],
           ['Sulzern', 48.0828918874, 7.09256896947], ['Sulzern', 48.0828918874, 7.09256896947],
           ['Sulzern', 48.0828918874, 7.09256896947], [], [], [], [], [], ['Ingersheim', 48.1014572023, 7.31053680908],
           ['Ingersheim', 48.1014572023, 7.31053680908], ['Ingersheim', 48.1014572023, 7.31053680908],
           ['Ingersheim', 48.1014572023, 7.31053680908], ['Ammerschweier', 48.119478992, 7.25998332176], [],
           ['Kaysersberg', 48.1836015307, 7.18808543159], ['Kaysersberg', 48.1836015307, 7.18808543159],
           ['Kaysersberg', 48.1836015307, 7.18808543159], ['Kaysersberg', 48.1836015307, 7.18808543159],
           ['Kaysersberg', 48.1836015307, 7.18808543159], ['Kaysersberg', 48.1836015307, 7.18808543159],
           ['Kaysersberg', 48.1836015307, 7.18808543159], [], [], ['Reichenweier', 48.1787804995, 7.27259187393],
           ['Hunaweier', 48.1824285926, 7.30403809307], ['Rappoltsweiler', 48.2065139236, 7.28672468283],
           ['Rappoltsweiler', 48.2065139236, 7.28672468283], ['Rappoltsweiler', 48.2065139236, 7.28672468283],
           ['Rappoltsweiler', 48.2065139236, 7.28672468283], ['Rappoltsweiler', 48.2065139236, 7.28672468283],
           ['Rappoltsweiler', 48.2065139236, 7.28672468283], ['Rappoltsweiler', 48.2065139236, 7.28672468283],
           ['Rappoltsweiler', 48.2065139236, 7.28672468283], ['Rappoltsweiler', 48.2065139236, 7.28672468283],
           ['Rappoltsweiler', 48.2065139236, 7.28672468283], [], [], [], [], [],
           ['Markirch', 48.2285762223, 7.16926143657], ['Markirch', 48.2285762223, 7.16926143657],
           ['Markirch', 48.2285762223, 7.16926143657], ['Leberau', 48.2678392398, 7.27599094644],
           ['Leberau', 48.2678392398, 7.27599094644]]

    n_book = 1
    n_universal = 42  # Start Nummer für universelle Nummer
    num_dict = {}  # ID/Nummern statt Sagennamen als key. Manche Sagen können die gleichen Titel haben, zb. einfach Nummern
    i = 0
    uid = 533
    werkID = 4

    # je nach Werk anpassen {Name der Sage: Kategorie, Gruppe, Ort, Nummer im Werk, universelle Nummer, XML-ID}
    for key, value in dict.items():
        group = "NaN"
        categorie = "NaN"  # if cat and group already in dict, replace with value[1]. Nested categories split using a symbol(f.ex. @)
        placeID = value
        if loc[i]:
            longitude = loc[i][2]
            latitude = loc[i][1]
        else:
            longitude = 0
            latitude = 0
        xml_id = "Elsass1." + str(n_book)
        dict[key] = {"id": uid,
                     "werk_id": werkID,
                     "n_book": n_book,
                     "title": key,
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

    with open("oberelsass_sagen.json", "w", encoding="UTF-8") as f:
        json.dump(dict, f, ensure_ascii=False, indent=2)

    return dict

get_dict()

def get_front():
    with open("vorwort/oberelsass_vorwort.txt", "r", encoding="utf-8") as f:
        return " ".join(
            [
                word.strip()
                for word in f.read().split()
            ]
        )


def get_back():
    with open("nachwort/oberelsass_nachwort.txt", "r", encoding="utf-8") as f:
        return " ".join(
            [
                word.strip()
                for word in f.read().split()
            ]
        )


def get_sql():
    name = "oberelsass_sagen"
    book_title = "Die Sagen des Elsasses. Erster Teil. Die Sagen des Ober-Elsass"
    dict = get_dict()
    # lang = "deutsch"
    return name, book_title, dict


# get_dict()


def fill_dict(dict: dict):
    mem = ""
    for title in dict:
        if dict[title] != "":
            mem = dict[title]
        else:
            dict[title] = mem
    return dict


DICT = {'Die Schlange im Jura': 'Jura', 'St. Morands Ruhe': 'Altkirch', 'Der Käpellegeist': 'Heimersdorf',
        'Die Zwerge in der Wolfshöhle': 'Pfirt', 'Des Teufels Recht auf Pfirt': '',
        'Die Todtenprozession zu Luppach': 'Luppach', 'Die Galgenplatte': 'Alt-Pfirt', 'Der Lachgeist im Haag': '',
        'Der Geist "Laxi" im Biederthaler Schlosse': 'Biederthal', 'Junker Schnabel': 'Hagenthal',
        'Die Here von Köstlach': 'Köstlach', 'Das Herenschloß': 'Dürlinsdorf', 'Der Schmied im Berge': '',
        'Das versunkene Schloß Färis und der alte Graf': 'Mörnach', 'Die Herdwible von Mörnach': '',
        'Die Erbauung von Liebenstein': 'Liebsdorf', 'Der schwarze Vogel auf Liebenstein': '',
        'Das Hündlein aus der wilden Jagd': '', 'Der Hausgeist geht zur Kelte': 'Oberlarg', 'Die drei Spinnerinnen': '',
        'Der Hexentanz auf der Kalmiser Waide': '', 'Das gefundene Silbergeld bei Mörsperg': '',
        'Der Mann mit dem Lapphute zu Oberlarg': '', 'Die weiße Dame vom Goldigberg': 'Langizen',
        'Das Totenpferd und die Totenprozession zu Moos': 'Moos', 'Das Bildstöcklein bei Winkel': 'Winkel',
        'Das Altschloß bei Winkel': 'Winkel', 'Der Dornstrauch bei Neun-Eich': 'Lüzel', 'Das Silberloch bei Lützel': '',
        'Die weiße Frau auf dem Küppele': 'Jufurt', 'Der Britzgyberg': '', 'Versenkte Glocken': 'Brubach, Didenheim',
        'Das Weingeigerlein auf Brunstatt': 'Brunstatt', 'Das schwarze Tier am Mühlbach': '',
        'Die Gespensterheere im Nordfeld': 'Mülhausen', 'Kreuzregen': '', 'Himmelschweiß': '',
        'Der Schatzgräber am Davidsbrünnlein': '', 'Die weiße Frau in grünen Pantoffeln': '',
        'Der verlorene Bräutigam': '', 'Der Milchsuppen-Acker': '',
        'Die Henne mit den goldenen Eiern in der Sankt-Marx-Kapelle bei Riedisheim': 'Riedesheim',
        'Das Dorftier zu Hegenheim': 'Hegenheim bei Hüningen', 'Die Geisterkirche auf dem Rhein': 'Kembs, Niffer',
        'Der weiße Mann vom Illzacher Schlosse': 'Julzach', 'Die weiße Jungfrau am Weiher': '',
        'Die weißen Mädchen an der Lindlache': '', 'Der schwarze Mann am Rain': '', 'Die Erscheinung am Rain': '',
        'Das weiße Pferd': '', 'Der Pferdeschatten am Rain': '', 'Der Nachtjäger': '',
        'Das Tucherle am Viertelssteg': '', 'Das Doggele': '', 'Das Fronfastentier': '', 'Der Dorfesel': '',
        'Der Milchbrunnen': '', 'Maria in der Eich': 'Rülisheim', 'Masmünsters Entstehung': 'Masmünster',
        'Der Lachtelweiher': 'Kirchberg bei Masmünster', 'Das Muttergottesbild in Sewen': 'Sewen',
        'Das Dambürle im Masmünsterthale': 'Masmünsterthal', 'Die weiße Dame von Rothenberg': 'Rothenberg (Rougemont)',
        'Die Gründung von Neu-Thann': 'Thann', 'St. Theobaldus rettet Thann im Schwedenkriege': 'Thann',
        'Das Ex Voto von der Kirche Alt-Thann': '', 'Die gebannten Kriegsheere': 'Sennheim',
        'Kaiser Barbarossa unter dem Bibelstein': '', 'Der Freier auf Freundstein': 'Weile br ei Thann',
        'Die Feldmesser auf dem Belchen': 'Großer Belchen', 'Die Gespenstertiere im Belchensee': '',
        'Wie Gebweiler gerettet ward. 1448': 'Gebweiler', 'Des Fürsten zu Murbach jäher Tod. 1477': '',
        'Der Teufel auf Hugstein': '', 'Kunigunde von Hungerstein. 1487': '', 'Der Schlangenkönig vom Heißenstein': '',
        'Die Schwarze Frau am Heißenstein': '', 'Die Alte auf der Barnabasbrücke': '',
        'Der wundersame Käfer': 'Bühl bei Gebweiler', 'Die Glocke von Bühl': '',
        'Die singende Jungfrau im Lauchthal': '', 'Die Erscheinung auf der Melkerei Hofrieth': '',
        'Ritter Kurt und die Kapelle von Ungersheim': 'Ungersheim', 'St. Maria im Schäferthal': 'Sulzmatt',
        'Der Langenstein bei Sulzmatt': '', 'Die Stiftung des Klosters St. Valentin zu Rufach': 'Rufach',
        'St. Landolins Gut zu Rufach': '', 'Die Weiber von Rufach': '', 'Das Hungertuch in der Kirche von Rufach': '',
        'Der Rufacher Galgen': '', 'Dem Teufel zu! 1721': '', 'Der Bollenberg': '',
        'Die Wallfahrt Schauenberg': 'Geberschweier', 'Die Greifenklaue des heiligen Imerius': '',
        'Bischof Friedrich von Zeringen': '', 'Die Stiftung des Kloster Marbach': '', 'Graf Hugos Buße': 'Egisheim',
        'Bruno von Egisheim': '', 'Die Erscheinung in Pfeffels Garten': 'Colmar', 'Die Erscheinung im Waschhause': '',
        'Die gespenstische Milchfrau': '', 'Das Nachtkalb': '', 'Warum die Colmarer Knöpfler heißen': '',
        'Die Kornmutter': 'Heiligkreuz bei Colmar', 'Frau Faste': '',
        'Die wilde Jagd bei Heilig-Kreuz': 'Heiligkreuz bei Colmar',
        'Der Hexenzug in der Hardt': 'Hettenschlag bei Neubreisach',
        'Das Bruderhäuschen bei Widensolen': 'Widensolen bei Neubreisach', 'Der Riese im Kastenwald': 'Andolsheim',
        'Warum der Logelbach zur Gemeinde Winzenheim gehört': 'Logelbach bei Colmar',
        'Die weiße Frau von Pflixburg': 'Winzenheim',
        'Die Wallfahrt zum Waldbruderkreuz am Grabe des heiligen Ignatius': 'Zimmerbach',
        'Die Entstehung des Bades Sulzbach': 'Sulzbach', 'Die Zwerge auf dem Kerbholz': 'Sulzern',
        'Die Schrätzmännel': '', 'Der Grüne See im Münsterthale': '', 'Der Soldatenschlatten am Hoheneck': '',
        'Der goldene Wagen': 'Mezeral', 'Der Alte vom Berge': 'Weier im Thale',
        'Die Wallfahrt Dreien-Aehren': 'Drei Aehren', 'Das Muttergottesbild zu Dreien-Aehren': '',
        'Das Riesengrab auf dem Hohnack': '', 'Das weiße Mädchen an der Fecht': 'Ingersheim',
        'Der Geist im Ingersheimer Schlosse': '', 'Die Wöchnerin': '', 'Der Hungerbrunnen': '',
        'St. Deodat': 'Ammerschweier',
        'Die Bilder der Muttergottes und des Evangelisten St. Johannes vergießen Thränen': 'Kienzheim',
        'Kaiser Friedrich Barbarossa in Kaysersberg': 'Kaysersberg',
        'Die riesenmäßigen Holzschuhe auf dem Rathause zu Kaysersberg': '', 'Der Flieger': '', 'Die Teufelskutsche': '',
        'Die Tschäpläre': '', 'Das Pestkreuz bei Kaysersberg': '', 'Der feurige Kreis bei Rappoltsweiler': '',
        'Der Einsiedler von Alspach': 'Alspach bei Kaysersberg', 'Der weiße See': 'Urbeis (Orbey)',
        'Der Zellenberger Burgersmann': 'Reichenweier', 'Die heilige Hunna': 'Hunaweier',
        'Das Wappen des Grafen von Rappoltstein': 'Rappoltsweiler', 'Die Brüder von Rappoltstein': '',
        'Die Jungfrau auf St. Ulrich': 'Rappoltsweiler', 'Die drei Schwestern von Rappoltstein': '',
        "Herni's Kreuz": '', 'Das Silberglöcklein und die Schloßhunde': '',
        'Die Gespensterkutsche von Hoh-Rappoltstein': '', 'Der Höllenhaken bei Rappoltsweiler': '',
        'Der Hirzsprung': '', 'Die Gründung von Dreikirchen oder Dusenbach': '',
        'Die gespenstige Herde': 'Elsenheim u Jllhäusern', 'Das Dorf Tannenkirch': 'Lanneukirch',
        'Das Dorftier von Tannenkirch': '', 'Die Here von Tannenkirch': '',
        'Das gelbe Fräulein auf der Hohkönigsburg': 'Hohlönigsburg bei Tannenkirch', 'Die silberne Rose': 'Markirch',
        'Warum die Markircher Silberminen Nichts mehr abwerfen': '', 'Der Jungfrauenplatz bei Markirch': '',
        'Die Glocke von Leberau': 'Leberau', 'Der Charlemont': ''}

# d = fill_dict(DICT)
