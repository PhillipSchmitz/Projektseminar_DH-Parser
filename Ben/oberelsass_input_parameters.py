def get_tei_header():
    MainTitle = "Die Sagen des Elsasses"
    SubTitle = "getreu nach der Volksüberlieferung, den Chroniken und andern gedruckten und handschriftlichen Quellen, gesammelt von August Stöber. Neue Ausgabe besorgt von Kurt Mündel. Erster Teil. Die Sagen des Ober-Elsass."
    Author = "August Stöber"
    PublicationYear = "1892"
    PublicationPlace = "Strassburg, German Empire (modern day France)"
    # PublicationCountry="Germany"
    Publisher = "J. H. Ed Heitz (Heitz & Mündel)"
    Edition = "Erster Teil. Die Sagen des Ober-Elsass"

    Copyright = "CC0"
    encoder = "Ben Conrad"

    return MainTitle, SubTitle, Author, PublicationYear, PublicationPlace, Publisher, Edition, Copyright, encoder

def get_pkl():
    pickle_filename = "oberelsass_sagen"
    return pickle_filename

def get_dict():

    dict = {'Die Schlange im Jura': 'Jura', 'St Morands Ruhe': 'Altkirch', 'Der Käpellegeist': 'Heimersdorf',
        'Die Zwerge in der Wolfshöhle': 'Pfirt', 'Des Teufels Recht auf Pfirt': '',
        'Die Todtenprozession zu Luppach': 'Luppach', 'Die Galgenplatte': 'Alt-Pfirt', 'Der Lachgeist im Haag': '',
        'Der Geist Laxi im Biederthaler Schlosse': 'Biederthal', 'Junker Schnabel': 'Hagenthal',
        'Die Here von Köstlach': 'Köstlach', 'Das Herenschloß': 'Dürlinsdorf', 'Der Schmied im Berge': '',
        'Das versunkene Schloß Färis und der alte Graf': 'Mörnach', 'Die Herdwible von Mörnach': '',
        'Die Erbauung von Liebenstein': 'Liebsdorf', 'Der schwarze Vogel von Liebenstein': '',
        'Das Hündlein aus der wilden Jagd': '', 'Der Hausgeist geht zur Kelte': 'Oberlarg',
        'Die drei Spinnerinnen': '', 'Der Hexentanz auf der Kalmiser Weide': '',
        'Das gefundene Silbergeld bei Mörsberg': '', 'Der Mann mit dem Lapphute zu Oberlarg': '',
        'Die weiße Frau am Goldigberg': 'Langizen', 'DasTotenpferd un dd ie Totenprozession zu Moos': 'Moos',
        'Das Bildstöcklein bei Winkel': 'Winkel', 'Das Altschloß bei Winkel': 'Winkel',
        'Der Dornstrauch bei Neun-Eich': 'Lüzel', 'Das Silberloch bei Lüzel': '',
        'Die weiße Frau auf dem Küppele': 'Jufurt', 'Der Brißgyberg': '', 'Versenkte Glocken': 'Brubach, Didenheim',
        'Das Weingeigerlein von Brunstatt': 'Brunstatt', 'Das schwarze Tier am Mühlbach': '',
        'Die Gespensterheere im Nordfeld': 'Mülhausen', 'Kreuzregen': '', 'Himmelschweiß': '',
        'Der Schapgräber am Davidsbrünnlein': '', 'Die weiße Frau in grünen Pantoffeln': '',
        'Der verlorene Bräutigam': '', 'Der Milchsuppenacker': '',
        'Die Henne mit den goldenen Eiern in der St. Marykapelle bei Riedesheim': 'Riedesheim',
        'Das Dorftier zu Hegenheim': 'Hegenheim bei Hüningen', 'Die Geisterkirche auf dem Rhein': 'Kembs, Niffer',
        'Der weiße Mann vom Julzacher Schlosse': 'Julzach', 'Die weiße Jungfrau am Weiher': '',
        'Die weißen Mädchen an der Lindlache': '', 'Der schwarze Mann am Rain': '', 'Die Erscheinung am Rain': '',
        'Das weiße Pferd': '', 'Der Pferdeschatten am Rain': '', 'Der Nachtjäger': '',
        'Das Tucherle am Viertelssteg': '', 'Das Doggele': '', 'Das Fronfastentier': '', 'Der Dorfejel': '',
        'Der Milchbrunnen': '', 'Maria in der Eich': 'Rülisheim', 'Masmünsters Entstehung': 'Masmünster',
        'Der Lachtelweiher': 'Kirchberg bei Masmünster', 'Das Muttergottesbild in Sewen': 'Sewen',
        'Das Dambürle im Masmünsterthale': 'Masmünsterthal',
        'Die weiße Dame von Rothenberg': 'Rothenberg (Rougemont)', 'Die Gründung von Neu-Thann': 'Thann',
        'StTheobaldus rettet Thann im Schwedenkriege': 'Thann', 'Das Ex Voto in der Kirche zu Alt- Thann': '',
        'Die gebannten Kriegsheere': 'Sennheim', 'Kaiser Barbarossa unter dem Bibelstein': '',
        'Der Freier auf Freundstein': 'Weile br ei Thann', 'Die Feldmesser auf dem Belchen': 'Großer Belchen',
        'Gespenstertiere im Belchensee': '', 'Wie Gebweiler gerettet wurde': 'Gebweiler',
        'Des Fürsten zu Murbach jäher Tod': '', 'Der Teufel auf Hugstein': '', 'Kunigunde von Hungerstein': '',
        'Der Schlangenkönig vom Heißenstein': '', 'Die schwarze Frau am Heißenstein': '',
        'Die Alte auf der Barnabasbrücke': '', 'Der wundersame Käfer': 'Bühl bei Gebweiler',
        'Die Glocke von Bühl': '', 'Die singende Jungfrau im Lauchthal': '',
        'Die Erscheinung auf der Melkerei Hofrieth': '', 'Ritter Kurt und die Kapelle von Ungersheim': 'Ungersheim',
        'St Maria im Schäferthal': 'Sulzmatt', 'Der Langenstein bei Sulzmatt': '',
        'DieStiftung des Klosters St. Valentin zu Rufach': 'Rufach', 'St Landolins Gut zu Rufach': '',
        'Die Weiber von Rufach': '', 'Das Hungertuch in der Kirche von Rufach': '', 'Der Rufacher Galgen': '',
        'Dem Teufel zu': '', 'Der Bollenberg': '', 'Die Wallfahrt Schauenberg': 'Geberschweier',
        'Die Greifenklaue des heiligen Imerius': '', 'Bischof Friedrich von Zeringen': '',
        'Stiftung des Klosters Marbach': '', 'Graf Hugos Buße': 'Egisheim', 'Bruno von Egisheim': '',
        'Die Erscheinung in Pfeffels Garten': 'Colmar', 'Die Erscheinung im Waschhause': '',
        'Die gespenstige Milchfrau': '', 'Das Nachtkalb': '', 'Warum die Colmarer Knöpfler heißen': '',
        'Die Kornmutter': 'Heiligkreuz bei Colmar', 'Frau Faste': '',
        'Die wilde Jagd bei Heiligkreuz': 'Heiligkreuz bei Colmar',
        'Der Hexenzug in der Hardt': 'Hettenschlag bei Neubreisach',
        'Das Bruderhäuschen bei Widensolen': 'Widensolen bei Neubreisach', 'Der Riese im Kastenwald': 'Andolsheim',
        'Warum der Logelbach zur Gemeinde Winzenheim gehört': 'Logelbach bei Colmar',
        'Die weiße Frau von Pflixburg': 'Winzenheim',
        'Die Wallfahrt zum Waldbruderkreuz am Grabe des heiligen Ignatius': 'Zimmerbach',
        'Die Entstehung des Bades Sulzbach 84B': 'Sulzbach', 'Die Zwerge auf dem Kerbholz': 'Sulzern',
        'Die Schrägmännel': '', 'Der grüne See im Münsterthale': '', 'Der Soldatenschlatten am Hoheneck': '',
        'Der goldene Wagen': 'Mezeral', 'Der Alte vom Berge': 'Weier im Thale',
        'Die Wallfahrt Dreien Aehren': 'Drei Aehren', 'Das Muttergottesbild zu Dreien Aehren': '',
        'Das Riesengrab auf dem Hohnack': '', 'Das weiße Mädchen an der Fecht': 'Ingersheim',
        'Der Geist im Ingersheimer Schlosse': '', 'Die Wöchnerin': '', 'Der Hungerbrunnen': '',
        'St Deodat': 'Ammerschweier',
        'Die Bilder der Muttergottes und des Evangelisten St. Johannes vergießen Thränen': 'Kienzheim',
        'Kaiser Friedrich Barbarossa in Kaysersberg': 'Kaysersberg',
        'Die riesenmäßigen Holzschuhe auf dem Rathause zu Kaysersberg': '', 'Der Flieger': '',
        'Die Teufelskutsche': '', 'Die Tschäpläre': '', 'Das Pestkreuz bei Kaysersberg': '',
        'Der feurige Kreis im Kaysersberger Wald': '', 'Der Einsiedler von Alspach': 'Alspach bei Kaysersberg',
        'Der weiße See': 'Urbeis (Orbey)', 'Der Zellenberger Burgersmann': 'Reichenweier',
        'Die heilige Huna': 'Hunaweier', 'Das Wappen der Grafen von Rappoltstein': 'Rappoltsweiler',
        'Die Brüder von Rappoltstein': '', 'Die Jungfrau auf St. Ulric h': 'Rappoltsweiler',
        'Die drei Schwestern von Rappoltstein': '', "Herni's Kreuz": '',
        'Das Silberglöcklein und die Schloßhunde': '', 'Die Gespensterkutsche von Hoh- Rappoltstein': '',
        'Der Höllenhaken bei Rappoltsweiler': '', 'Der Hirzsprung': '',
        'Die Gründung von Dreikirchen oder Dusenbach': '', 'Die gespenstige Herde': 'Elsenheim u Jllhäusern',
        'Das Dorf Tannenkirch': 'Lanneukirch', 'Das Dorftier von Tannenkirch': '', 'Die Here von Tannenkirch': '',
        'Das gelbe Fräulein auf der Hohkönigsburg': 'Hohlönigsburg bei Tannenkirch',
        'Die silberne Rose': 'Markirch', 'Warum die Markircher Silberminen Nichts mehr abwerfen': '',
        'Der Jungfrauenplaß bei Markirch': '', 'Die Glocke von Leberau': 'Leberau', 'Der Charlemont': ''}
    
    n_book=1
    n_universal=42  #Start Nummer für universelle Nummer
    num_dict = {}  #ID/Nummern statt Sagennamen als key. Manche Sagen können die gleichen Titel haben, zb. einfach Nummern

     #je nach Werk anpassen {Name der Sage: Kategorie, Gruppe, Ort, Nummer im Werk, universelle Nummer, XML-ID}
    for key, value in dict.items():
        group = "NoGroup"                      
        categorie = "NoCategorie"               #if cat and group already in dict, replace with value[1]. Nested categories split using a symbol(f.ex. @)
        placeID = value
        if value == "":
            placeID = "NoPlace"
        xml_id = "Elsass1." + str(n_book)
        dict[key]=[key, categorie, group, placeID,n_book, n_book + n_universal, xml_id]    
        
        num_dict[xml_id] = dict[key]
        n_book +=1
    
    #print(dict)
    #print(num_dict)

    

    return dict, num_dict

def get_sql():
    name = "oberelsass"
    book_title = "Die Sagen des Elsasses. Erster Teil. Die Sagen des Ober-Elsass"
    dict = get_dict()
    lang = "deutsch"
    return name, book_title, dict, lang


get_dict()



