def get_pkl():
    pickle_filename = "oberelsass_sagen"
    return pickle_filename


def get_dict():
    titles = ["Das rote Haus zu Trier und die Sage von Triers Gründung",
              "Wie das Trierer Land unter Römerherrschaft kam", "Trier als römische Stadt", "Das Amphitheater zu Trier",
              "Zwei Sagen vom Kaskeller", "Sagen von der römischen Wasserleitung",
              "Die Kultur des Mosellandes zur Römerzeit", "Arimaspes und Eptes",
              "Legende von der Einführung des Christentums in Trier", "Glaubenseifer der ersten Christen zu Trier",
              "Die heilige Helena", "Die Porta nigra oder das Römerthor zu Trier", "Der heilige Einsiedler Simeon",
              "Die Teufelskirche zu Trier", "Die Moselbrücke zu Trier", "St. Maximin und St. Paulin",
              "Das Ende des römischen Triers", "Moselreise des Frankenkönigs Siegebert, 570 n. Chr",
              "Adalbero und Poppo", "Der heilige Rock zu Trier", "König Orendel und der graue ungenähte Rock Christi",
              "22. Der Stadtgeist zu Trier", "Die Vorstadt Löwenbrücken bei Trier", "Erzbischof Balduin von Trier",
              "Moselreise des Kaisers Maximilian 1512 n. Chr", "Markgraf Albrecht von Brandenburg in Trier",
              "Erzbischof Philipp Christoph von Sötern", "More Trevirensi", "Der Krummelstuhl im Trierer Dom",
              "Ein seltsames Volksfest zu Trier", "Das Kesselstattische Majorat", "Pfalzel", "Ruwer",
              "Die drei Schwestern zu Aum an der Kyll", "Die Quint. Zwei Eberjagden im Meilenwalde",
              "Etwas von der Weisheit des Schöffengerichts zu Schweich", "Der heilige Born bei Schweich",
              "Riktiovar im Meilenwalde bei Schweich", "Die Schlacht bei Rigodulum (Riol)",
              "Peter von Aspelt, genannt Aichspalter", "Das Spinnerkreuz bei Mehring",
              "Das Kloster Himmerode im Salmbachthal", "Die Nachtigallen im Kloster Himmelrath", "Leiwen",
              "Trittenheim", "Der Abt Tritheim als Zauberer",
              "Die Märterkirche bei Neumagen und die thebaische Legion", "Die Konstantinsburg zu Neumagen",
              "Konstantins Kreuz auf Kron", "Thron", "Die Burg des Bischofs Nicetius", "Piesport",
              "Das Kloster Klausen", "Ein Wunder durch das Gnadenbild zu Klausen",
              "Noch ein Wunder durch das Klausener Gnadenbild", "Minheim. Die Marienrosen",
              "Ohligsberg, Winterich und Filzen", "Der Brauneberg", "Die Grafschaft Veldenz",
              "Der Treuring. Eine Sage aus Veldenz", "Johannes von Liefer", "Bernkastel",
              "Der Bernkasteler Doktor", "Der Kellermeister von Bernkastel",
              "Noch eine Geschichte vom Kurfürsten Franz Georg", "Nikolaus von Cues", "Das Hospital zu Cues",
              "Der böse Maurus zu Cues", "Graach und Zeltingen", "Der letzte Burgherr von Zeltingen", "Wehlen",
              "Kloster Machern", "Die Urley bei Uerzig", "Das Cröferreich", "Die hintere Grafschaft Sponheim",
              "Reformation und Gegenreformation an der Mosel", "Wolf und das Wolfer Kloster", "Riesbach", "Traben",
              "Die Gräfenburg bei Trarbach", "Trarbach",
              "Etwas vom Weinbau und Weinverkauf an der Mosel vor 200 Jahren",
              "Geldarmut der Moselbauern in früheren Jahrhunderten", "Weinbau an der Mosel heutzutage", "Das Mosellied",
              "Die Moselweine", "Bergbau zwischen Bernkastel und Trarbach. Der Wildstein", "Bad Wildstein",
              "Die Festung Montroyal auf dem Trabener Berg", "Göthes Moselreise",
              "Die Gräfin Lauretta von Sponheim- Starkenburg und Erzbischof Balduin", "Enkirch",
              "Der Burger Wein als Fastentrunk", "Das Kloster Springirsbach",
              "Sage von der Kaiserherberge im Condelwald", "Der Reilerhals", "Die Marienkrone zu Pünderich",
              "Rottwirtschaft an der Mosel", "Ferme wie ein Zeller", "Was ein Zeller Arzt vom Moselwein hält",
              "Kloster Marienburg", "Der Schatz im Kloster Marienburg", "Die drei Zecher zu Bullay",
              "Die Burg Arras im Alfthal", "Zwei Sagen von Bertrich", "Das Mannethal an der Entersburg bei Bertrich",
              "Legende von dem Bau der Neefer Kapelle", "Kloster Stubben", "Das Beutestück des Kreuzritters zu Stubben",
              "Eller und Ediger", "Die Einsiedelei bei Leimen", "Senheim und Senhals", "Poltersdorf",
              "Beilstein und die Familie Metternich", "Peter Schade aus Bruttig",
              "Ober- und Niederernst. Pfarr- und Klosterweine", "Ein Ebernacher Rezept gegen Sonnenfinsternis",
              "Kochem", "Pfalzgraf Heinrich der Tolle von Kochem", "Zerstörung Kochems 1689",
              "Der Pater Martin von Kochem", "Der Kochemer Weisheit", "Die eingemauerte Jungfrau in der Winneburg",
              "Noch eine Sage von der Winneburg", "Das Kreuz auf der Kniebrech bei Kochem",
              "Das Antoniuskreuz zwischen Uelmen und Kochem", "Clotten, die Residenz einer Königin von Polen",
              "Pommern und Kloster Rosenthal", "Treis und Kloster Engelport",
              "Wie Albero von Monsterol die Burg Treis genommen hat", "Carden und der heilige Castor",
              "Die Sonntagsmühle bei Carden", "Die Schwanenkirche auf dem Maifelde unweit Carden",
              "Schloß Eltz bei Moselkern", "Die Grafen von Eltz", "Frevel eines eltzischen Jägers",
              "Der durchlöcherte Harnisch zu Eltz", "Bischofsstein", "Münstermaifeld", "Die Ehrenburg bei Brodenbach",
              "Die Sternburg oder der Tempelhof bei Löf", "Alken und die Burg Thurant", "Der gewippte Vogt",
              "Die Stiftung zu Lehmen", "Nickel Aswaldo", "Gondorf und die Familie von der Leyen",
              "Der rote Aermel zu Gondorf", "Kobern und seine zwei Burgen", "Lutter, der letzte Ritter von Kobern",
              "Das Koberner Wahrzeichen", "Hexenprozesse an der Untermosel, besonders in Winningen",
              "Volksfeste zu Winningen", "Die Miseräbelchen", "Koblenz als römische Stadt",
              "Koblenz als erzbischöfliche Stadt", "Die St. Kastorkirche zu Koblenz", "Die selige Ritza",
              "Die St. Florinskirche zu Koblenz", "Die Moselbrücke", "Adelshöfe in Koblenz",
              "Altertümliche Häuser in Koblenz", "Koblenz als französische Stadt", "Der Korporal Spohn",
              "Zwei Wahrzeichen von Koblenz", "Koblenz als preußische Stadt", "Berühmte Koblenzer",
              "Göthe in Koblenz"]

    loc = [['Trier', 49.75565, 6.63935], ['Gallien', 'NaN'], ['Trier', 49.75565, 6.63935],
           ['Olewig', 49.74107, 6.67274], ['Ruwerbache', 'NaN'], ['Köln', 50.22725, 7.02453],
           ['Mosel', 49.91602, 7.07664], ['Trier', 49.75565, 6.63935], ['Trier', 49.75565, 6.63935],
           ['Trier', 49.75565, 6.63935], ['Trier', 49.75565, 6.63935], ['Porta nigra', 'NaN'],
           ['Trier', 49.75565, 6.63935], ['Trier', 49.75565, 6.63935], ['Mosel', 49.91602, 7.07664],
           ['Trier', 49.75565, 6.63935], ['Trier', 49.75565, 6.63935], ['Andernach', 50.43109, 7.40425],
           ['Trier', 49.75565, 6.63935], ['Trier', 49.75565, 6.63935], ['Trier', 49.75565, 6.63935],
           ['Trier', 49.75565, 6.63935], ['Trier', 49.75565, 6.63935], ['Elz', 49.83544, 7.07571],
           ['Trier', 49.75565, 6.63935], ['Kulmbach', 'NaN'], ['Trier', 49.75565, 6.63935], ['NaN', 'NaN'],
           ['Trierer Do', 'NaN'], ['Trierlandes', 'NaN'], ['Meilenwald', 'NaN'], ['Pfalzel', 49.78104, 6.69411],
           ['Ruwer', 49.7867, 6.71044], ['Kyll', 49.87009, 6.59057], ['Quint', 49.82436, 6.7063],
           ['Mosel', 49.91602, 7.07664], ['Meilenwald', 'NaN'], ['Meilenwald', 'NaN'], ['Trier', 49.75565, 6.63935],
           ['Mainz', 49.98419, 8.2791], ['Mehrin', 49.8, 6.83333], ['Himmerode', 'NaN'], ['Himmelrat', 'NaN'],
           ['Livania', 'NaN'], ['Sponheim', 49.84496, 7.72665], ['Kreuznach', 49.8414, 7.86713],
           ['Märterkirche', 'NaN'], ['Trier', 49.75565, 6.63935], ['Neumagen', 49.85, 6.9], ['Neumagen', 49.85, 6.9],
           ['Neumagen', 49.85, 6.9], ['Piesport', 49.8864, 6.91649], ['Trier', 49.75565, 6.63935], ['NaN', 'NaN'],
           ['Nanzig', 'NaN'], ['Minheim', 49.86493, 6.93692], ['Winterich', 'NaN'], ['Brauneberg', 49.90583, 6.98127],
           ['Veldenz', 49.88867, 7.02206], ['NaN', 'NaN'], ['Mainz', 49.98419, 8.2791],
           ['Bernkastel', 49.91602, 7.07664], ['Bernkastel', 49.91602, 7.07664], ['Bernkastel', 49.91602, 7.07664],
           ['Ehrenbreitstein', 50.36012, 7.62013], ['Deutschland', 'NaN'], ['Hazenport', 'NaN'],
           ['Cues', 49.91602, 7.07664], ['St. Martin', 'NaN'], ['Rosenburg', 'NaN'], ['Wehlen', 49.94117, 7.04202],
           ['Niederlahnstein', 50.31268, 7.60328], ['Trier', 49.75565, 6.63935], ['Trier', 49.75565, 6.63935],
           ['Sponheim', 49.84496, 7.72665], ['Trier', 49.75565, 6.63935], ['Wolf', 49.97908, 7.10345],
           ['Riesbach', 'NaN'], ['Traben', 49.95076, 7.11562], ['Gräfenburg', 'NaN'], ['Trarbach', 49.95076, 7.11562],
           ['Mosel', 49.91602, 7.07664], ['Sponheim', 49.84496, 7.72665], ['Mosel', 49.91602, 7.07664],
           ['Dresden', 'NaN'], ['Obermosel', 'NaN'], ['Bernkastel', 49.91602, 7.07664], ['Trarbach', 49.95076, 7.11562],
           ['Montroyal', 'NaN'], ['Trarbach', 49.95076, 7.11562], ['Starkenburg', 49.95535, 7.13994],
           ['Enkirch', 49.98434, 7.12997], ['Burg', 50.00784, 7.12243], ['Springirsbac Von Reil', 'NaN'],
           ['Springirsbach', 'NaN'], ['Bertrich', 50.06667, 7.03333], ['Eifelland', 'NaN'],
           ['Mosel', 49.91602, 7.07664], ['Zell', 50.02918, 7.18232], ['NaN', 'NaN'],
           ['Springiersbach', 50.02572, 7.06875], ['Marienburg', 'NaN'], ['Limburg an der Lahn', 'NaN'],
           ['Arras', 50.05264, 7.10583], ['Bertrich', 50.06667, 7.03333], ['Entersburg', 'NaN'],
           ['Neef', 50.1, 7.13333], ['Bremm', 50.1, 7.11667], ['Stubben', 'NaN'], ['Eller', 50.11667, 7.15],
           ['Ediger', 50.1, 7.16667], ['Senheim', 50.08333, 7.21667], ['Poltersdorf', 50.1, 7.23333],
           ['Beilstein', 50.11667, 7.25], ['Leipzig', 'NaN'], ['Kochem', 50.14511, 7.16379],
           ['Mosel', 49.91602, 7.07664], ['Kochem', 50.14511, 7.16379], ['Kochem', 50.14511, 7.16379],
           ['Kochems', 'NaN'], ['Baden', 49.90691, 6.52262], ['Kochem', 50.14511, 7.16379],
           ['Kochem', 50.14511, 7.16379], ['Winneburg', 'NaN'], ['Endertbach', 'NaN'], ['Antoniuskreuz', 'NaN'],
           ['Clotten', 'NaN'], ['Pommern', 50.16667, 7.28333], ['Treis', 50.18333, 7.3], ['Treis', 50.18333, 7.3],
           ['Carden', 'NaN'], ['Engelport', 50.13333, 7.28333], ['Schwanenkirche', 'NaN'], ['Elz', 49.83544, 7.07571],
           ['Elz', 49.83544, 7.07571], ['Kempenicher Hauses', 'NaN'], ['Elz', 49.83544, 7.07571],
           ['Bischofsstein', 'NaN'], ['Münster', 49.81159, 7.84523], ['Brodenbach', 50.23333, 7.45],
           ['Mosel', 49.91602, 7.07664], ['Alken', 50.25, 7.45], ['Alken', 50.25, 7.45], ['Trier', 49.75565, 6.63935],
           ['Aswaldo', 'NaN'], ['Gondorf', 50.29512, 7.46141], ['Gondorf', 50.29512, 7.46141],
           ['Kobern', 50.30856, 7.45917], ['Kochem', 50.14511, 7.16379], ['Kobern', 50.30856, 7.45917],
           ['Trier', 49.75565, 6.63935], ['Winningen', 50.31667, 7.51667], ['Mosel', 49.91602, 7.07664],
           ['Koblenz', 50.35357, 7.57883], ['Koblenz', 50.35357, 7.57883], ['Rhein', 49.96675, 7.8992],
           ['St. Kastor', 'NaN'], ['Remüs', 'NaN'], ['Koblenz', 50.35357, 7.57883], ['Koblenz', 50.35357, 7.57883],
           ['Koblen', 50.35357, 7.57883], ['Koblenz', 50.35357, 7.57883], ['Austerlig', 'NaN'],
           ['Koblen', 50.35357, 7.57883], ['Koblenz', 50.35357, 7.57883], ['Koblenz', 50.35357, 7.57883],
           ['Koblenz', 50.35357, 7.57883]]

    dict = {}
    n_book = 1
    n_universal = 42  # Start Nummer für universelle Nummer
    num_dict = {}  # ID/Nummern statt Sagennamen als key. Manche Sagen können die gleichen Titel haben, zb. einfach Nummern
    i = 0
    uid = 83
    pid = 84
    werkID = 2
    c = 0

    # je nach Werk anpassen {Name der Sage: Kategorie, Gruppe, Ort, Nummer im Werk, universelle Nummer, XML-ID}
    for title in titles:
        group = "NoGroup"
        categorie = "NoCategory"  # if cat and group already in dict, replace with value[1]. Nested categories split using a symbol(f.ex. @)
        placeID = loc[i][0]
        if loc[i][1] != "NaN":
            c += 1
            longitude = loc[i][2]
            latitude = loc[i][1]
        else:
            longitude = 0
            latitude = 0
        # xml_id = "Elsass1." + str(n_book)
        dict[title] = [uid, werkID, n_book, title, categorie, group, placeID, longitude,
                       latitude]
        # num_dict[xml_id] = dict[key]
        n_book += 1
        i += 1
        uid += 1
    # print(dict)
    # print(len(titles))
    print(c)
    # print(num_dict)

    return dict


def get_sql():
    name = "moseltal_sagen"
    book_title = "Geschichten und Erzählungen des Moseltals"
    dict = get_dict()
    # lang = "deutsch"
    return name, book_title, dict
