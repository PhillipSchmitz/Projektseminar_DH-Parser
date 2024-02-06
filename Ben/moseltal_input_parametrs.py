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

    loc = [['Trier', 49.75179, '6.6237'], ['Gallien', 51.83845, '12.75766'], ['Trier', 49.75179, '6.6237'],
           ['Olewig', 49.74107, '6.67274'], ['Ruwerbache', 'NaN'], ['Trier', 49.75179, '6.6237'],
           ['Mosel', 49.91252, '7.01949'], ['Trier', 49.75179, '6.6237'], ['Trier', 49.75179, '6.6237'],
           ['Trier', 49.75179, '6.6237'], ['Trier', 49.75179, '6.6237'], ['Porta nigra', 'NaN'],
           ['Trier', 49.75179, '6.6237'], ['Rom', 48.33136, '8.29324'], ['Moselbrücke', 'NaN'],
           ['Trier', 49.75179, '6.6237'], ['Trier', 49.75179, '6.6237'], ['Andernach', 50.44574, '7.36055'],
           ['Trier', 49.75179, '6.6237'], ['Trier', 49.75179, '6.6237'], ['Trier', 49.75179, '6.6237'],
           ['Trier', 49.75179, '6.6237'], ['Trier', 49.75179, '6.6237'], ['Elz', 51.54245, '7.72393'],
           ['Trier', 49.75179, '6.6237'], ['Rhein', 49.04888, '8.25959'], ['Trier', 49.75179, '6.6237'], ['NaN', 'NaN'],
           ['Trierer Domes', 'NaN'], ['Trierlandes', 'NaN'], ['Meilenwald', 'NaN'], ['Pfalzel', 49.78104, '6.69411'],
           ['Ruwer', 49.78489, '6.7061'], ['Kyll', 50.25272, '6.67983'], ['Quint', 49.83013, '6.70752'],
           ['Mosel', 49.91252, '7.01949'], ['Neuß', 51.21667, '6.65'], ['Meilenwald', 'NaN'],
           ['Trier', 49.75179, '6.6237'], ['Mainz', 49.98625, '8.25318'], ['Spinnerkreuz', 'NaN'], ['Himmerode', 'NaN'],
           ['Himmelrat', 'NaN'], ['Lyva', 'NaN'], ['Sponheim', 49.84496, '7.72665'], ['Kreuznach', 49.82389, '7.69833'],
           ['Märterkirche', 'NaN'], ['Trier', 49.75179, '6.6237'], ['Neumagen', 47.94895, '7.67318'],
           ['Thron', 51.27513, '12.20761'], ['Neumagen', 47.94895, '7.67318'], ['Piesports', 'NaN'],
           ['Trier', 49.75179, '6.6237'], ['NaN', 'NaN'], ['Straßburg', 49.55239, '8.85112'],
           ['Minheim', 49.86493, '6.93692'], ['Winterich', 'NaN'], ['Brauneberg', 49.9, '6.98333'],
           ['Veldenz', 49.87001, '7.03051'], ['NaN', 'NaN'], ['Mainz', 49.98625, '8.25318'],
           ['Bernkastel', 49.91602, '7.07664'], ['Berns', 51.36131, '14.05225'], ['Bernkastel', 49.91602, '7.07664'],
           ['Ehrenbreitstein', 50.36012, '7.62013'], ['Rom', 48.33136, '8.29324'], ['Traben', 49.95076, '7.11562'],
           ['Cues', 49.91602, '7.07664'], ['Graach', 49.93333, '7.08333'], ['Rosenburg', 54.42884, '9.02007'],
           ['Wehlen', 49.68135, '7.12699'], ['Bachthales', 'NaN'], ['Trier', 49.75179, '6.6237'],
           ['Trier', 49.75179, '6.6237'], ['Sponheim', 49.84496, '7.72665'], ['Trier', 49.75179, '6.6237'],
           ['Wolf', 50.8, '11.98333'], ['Riesbach', 52.29208, '9.35199'], ['Traben', 49.95076, '7.11562'],
           ['Gräfenburg', 'NaN'], ['Trarbach', 49.95076, '7.11562'], ['Traben', 49.95076, '7.11562'],
           ['Sponheim', 49.84496, '7.72665'], ['Mosel', 49.91252, '7.01949'], ['Koblenz', 50.33333, '7.58333'],
           ['Obermosel', 'NaN'], ['Trarbach', 49.95076, '7.11562'], ['Trarbach', 49.95076, '7.11562'],
           ['Montroyal', 'NaN'], ['Trarbach', 49.95076, '7.11562'], ['Starkenburg', 49.64604, '8.64783'],
           ['Enkirch', 49.98434, '7.12997'], ['Burg', 48.22053, '8.71928'], ['Daun', 50.16667, '6.66667'],
           ['Cröferreich', 'NaN'], ['Reil', 49.35048, '8.77258'], ['Marienkrone', 'NaN'], ['Mose', 50.45515, '9.35918'],
           ['Zell', 47.8, '11.46667'], ['NaN', 'NaN'], ['Marienbur', 52.12667, '9.965'],
           ['Marienbur', 52.12667, '9.965'], ['Marienburg', 52.12667, '9.965'], ['Arras', 51.05601, '12.90432'],
           ['Bertrich', 50.06667, '7.03333'], ['Entersburg', 'NaN'], ['Neef', 53.51829, '9.79828'],
           ['Stubben', 53.53333, '10.65'], ['Stubben', 53.53333, '10.65'], ['Eller', 51.55, '10.36667'],
           ['Udos', 'NaN'], ['Senheim', 50.08333, '7.21667'], ['Beilstein', 50.74796, '8.35069'],
           ['Beilstein', 50.74796, '8.35069'], ['Leipzig', 51.5, '12.33333'], ['Oberwörth', 48.46667, '8.91667'],
           ['Mosel', 49.91252, '7.01949'], ['Kochem', 50.16854, '7.12267'], ['Kochem', 50.16854, '7.12267'],
           ['Kochems', 'NaN'], ['Baden', 49.30637, '8.64236'], ['Kochem', 50.16854, '7.12267'],
           ['Winneburg', 50.15595, '7.14287'], ['Winneburg', 50.15595, '7.14287'], ['Endertbach', 50.14892, '7.16124'],
           ['Antoniuskreuz', 'NaN'], ['Clotten', 'NaN'], ['Pommern', 50.16667, '7.28333'],
           ['Treis', 50.17174, '7.30218'], ['Treis', 50.17174, '7.30218'], ['Carden', 'NaN'],
           ['Carde', 52.01667, '12.7'], ['Maifeld', 50.29479, '7.34725'], ['Elz', 51.54245, '7.72393'],
           ['Elz', 51.54245, '7.72393'], ['Maienstadt', 'NaN'], ['Elz', 51.54245, '7.72393'], ['Bischofsstein', 'NaN'],
           ['Münster', 51.66667, '8'], ['Brodenbach', 50.23333, '7.45'], ['Mosel', 49.91252, '7.01949'],
           ['Alken', 47.59893, '8.38499'], ['Bleidenberg', 50.25, '7.45'], ['Trier', 49.75179, '6.6237'],
           ['Aswaldo', 'NaN'], ['Gondorf', 50.29512, '7.46141'], ['Gondorf', 50.29512, '7.46141'],
           ['Kobern', 50.33333, '7.46667'], ['Diebelicher Berg', 'NaN'], ['Kobern', 50.33333, '7.46667'],
           ['Untermosel', 'NaN'], ['Winningen', 51.82297, '11.45028'], ['Mosel', 49.91252, '7.01949'],
           ['Koblenz', 50.33333, '7.58333'], ['Koblenz', 50.33333, '7.58333'], ['Rhein', 49.04888, '8.25959'],
           ['Koblenz', 50.33333, '7.58333'], ['Remüs', 'NaN'], ['Moselbrücke', 'NaN'], ['Koblenz', 50.33333, '7.58333'],
           ['Klemensplat', 'NaN'], ['Koblenz', 50.33333, '7.58333'], ['Austerlig', 'NaN'], ['Kastorhof', 'NaN'],
           ['Koblenz', 50.33333, '7.58333'], ['Koblenz', 50.33333, '7.58333'], ['Koblenz', 50.33333, '7.58333']]

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
        #xml_id = "Elsass1." + str(n_book)
        dict[title] = [uid, werkID, n_book, title, categorie, group, placeID, longitude,
                       latitude]
        # num_dict[xml_id] = dict[key]
        n_book += 1
        i += 1
        uid += 1
    #print(dict)
    #print(len(titles))
    print(c)
    # print(num_dict)

    return dict


def get_sql():
    name = "moseltal_sagen"
    book_title = "Geschichten und Erzählungen des Moseltals"
    dict = get_dict()
    # lang = "deutsch"
    return name, book_title, dict
