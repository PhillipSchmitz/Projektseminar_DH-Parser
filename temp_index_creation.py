import re


def elsass():
    with open("elsass_index_speicher.txt", "r", encoding="utf-8") as f:
        index = f.readlines()

    title = []
    ort = []
    combo = []
    for line in index:
        v = re.sub(r"\t+.+\n", "", line)
        if not v == "":
            m = v[0].upper()
            v = m + v[1:]
            v = re.sub(r"\.+", "", v)
            v = re.sub(r"\s+$", "", v)
            ort.append(v)
        t = re.sub(r".+\t+", "", line)
        t = re.sub(r"\n", "", t)
        t = re.sub(r"^\d+\.\s*", "", t)
        t = re.sub(r"•*\s*\d+$", "", t)
        t = re.sub(r"[\.•·]", "", t)
        t = re.sub(r"\s+$", "", t)
        t = re.sub(r"\sst\s", " St. ", t)
        title.append(t)
        combo.append([t, v])
    # print(combo)

    output = "["
    for i in title:
        output += "'" + i + "'" + ","
    output += "]"
    print(output)

    dict_out = "{"
    for i in combo:
        dict_out += "'" + i[0] + "': '" + i[1] + "',"
    dict_out += "}"
    # print(dict_out)


def moseltal():
    with open("moseltal_temp.txt", "r", encoding="utf-8") as f:
        titles = f.readlines()

    clean = []
    for title in titles:
        title = re.sub(r"^\s*\d+\.", "", title)
        title = re.sub(r"\.\n$", "", title)
        title = re.sub(r"^\s+", "", title)
        clean.append(title)

    output = '['
    for c in clean:
        output += '"' + c + '",'
    output += ']'

    print(output)


def geschichten_moseltal():
    with open("geschichten_moseltal_temp.txt", "r", encoding="utf-8") as f:
        titles = f.readlines()

    clean = []
    for title in titles:
        title = re.sub(r"\d+\. ", "", title)
        title = re.sub(r"\.\n$", "", title)
        clean.append(title)

    output = '['
    for c in clean:
        output += '"' + c + '",'
    output += ']'

    print(output)


def pfalz():
    with open("temp_pfalz_index.txt", "r", encoding="utf-8") as f:
        titles = f.readlines()

    clean = []
    cat = -1
    group = -1
    for title in titles:
        # print(title)
        if re.search(r"^[ABCD]\.", title):
            clean.append([title[:-1], []])
            cat += 1
            # print(clean[cat])
            group = -1
        elif re.search(r"^[IV]+\.", title):
            clean[cat][1].append([title[:-1], []])
            # print(clean[cat][1][group])
            group += 1
        else:
            # print(clean[cat][group])
            clean[cat][1][group][1].append(title[:-1])

    solo_titles = []
    solo_group = []
    solo_cat = []
    dict = {}
    i = 1
    for c in clean:
        for g in c[i]:
            for t in g[1]:
                solo_titles.append(t)
                dict[t] = [c[0], g[0]]
            solo_group.append(g[0])
            i += 1
        solo_cat.append(c[0])
        i = 1
    print(solo_cat)
    print(solo_group)
    print(solo_titles)
    t = ['1. Die Geisterschlacht', '2. Die Fahrt der Toten', '3. Die überschiffenden Mönche', '4. Der ewige Jäger',
         '5. Der Jägerpfuhl', '6. Der wilde Jäger von Sponheim', '7. Der wilde Jäger am Donnersberg',
         '8. Der Lindenschmidt', '9. Der Einaug vom Scharfeneck', '10. Der Geist vom Scharfeneck',
         '11. Hans Trapp', '12. Das weiße Reh', '13. Der Geist auf dem Bleifelsen',
         '14. Der blutschwitzende Stein', '15. Der gebannte Geist',
         '16. Der Irrwisch auf dem Klosterberg bei Winterbach', '17. Das Flämmchen',
         '18. Der Schuß auf das Flämmchen', '19. Der Geist auf dem Kieneck', '20. Der falsche Eid',
         '21. Die Sage vom Maulus', '22. Des Beilsteiners Umgang', '23. Der Maire von Meisenheim',
         '24. Das Mädchen vom Pauliner Schlößchen', '25. Die unredliche Wirtin', '26. Der Grenzsteinverrücker',
         '27. Kanzel und Nonne', '28. Das Nonnental bei Neustadt', '29. Der Hund von Auerbach',
         '30. Die Wassernixe zu Eschringen', '31. Die schöne Tanne', '32. Die drei Wiesenfräulein',
         '33. Die drei Jungfrauen', '34. Die drei Schwestern', '35. Das Schloßfräulein',
         '36. Der Schloßgarten auf dem Großen Stiefel', '37. Die Schloßfrau und ihre Wäsche',
         '38. Die weiße Dame vom Pauliner Schlößchen', '39. Die Wildfrau',
         '40. Das Wildfrauloch bei Schweinschied', '41. Das Wildfrauenloch bei Schwarzerden',
         '42. Das Lindenmütterchen', '43. Die guten Zwerge', '44. Das Graumännchensloch', '45. Das graue Männchen',
         '46. Der Ritter vom Huneberg', '47. Das Kehrebacher Knüppchen', '48. Die Erdmännlein',
         '49. Die Schlange und das Kind', '50. Die Schlangenkönigin', '51. Der Drachenfels bei Dürkheim',
         '52. Der Drachenfels bei Busenberg', '53. Das wütende Heer', '54. Die wilde Jagd',
         '55. Vom Rosse des wilden Jägers', '56. Die Riesen des Bliestales', '57. Die Riesen des Wasgenwaldes',
         '58. Das Heidentürmchen zu Speyer', '59. Der Riese Kreuzmann', '60. Das Riesen- oder Hünengrab',
         '61. Vom Gotte Wodan', '62. Kolb von Wartenberg', '63. Die Waldkapelle',
         '64. Gott Donar und sein Gefährt', '65. Der Burgbau auf dem Rheingrafenstein', '66. Der Teufelsstein',
         '67. Der Teufelstisch', '68. Der Teufelsberg', '69. Der Teufelsbrunnen', '70. Der Müller und der Teufel',
         '71. Die Hexe vom Münstertal', '72. Die gebrannte Hexe', '73. Die diebische Hexe',
         '74. Das Hexengewitter', '75. Der Hexenball', '76. Hexentanz und Hexenkraut',
         '77. Der Zauberschüße Punker von Rohrbach', '78. Der Schnittlfelsen', '79. Der Heidenfelsen',
         '80. Der krumme Dallacker', '81. Der Stab des Klausners', '82. Das Marienbild zu Gräfinthal',
         '83. Das Muttergottesbild zu Forst', '84. Das Marienbild zu Ranschbach',
         '85. Das fromme Knäblein zu Speyer', '86. Das Marienbild im Dom zu Speyer',
         '87. Der rauschende Kelch im Speyerer Dom', '88. Die Maria-Hilf-Kapelle auf dem Kolmerberg',
         '89. Die Kapelle und das Glöckchen des hl. Cyriakus', '90. Der hl. Cyriakus und der Wingertsbalken',
         '91. Die Strutelpeters-Kapelle', '92. Die St. Lorenzkapelle', '93. Das goldene Kreuz im Klosterweiher',
         '94. Der Servatiusbrunnen', '95. Der Lorenzenbrunnen', '96. Die Wunder des hl. Philipp von Zell',
         '97. Die Glocken zu Speyer', '98. Die fliegende Glocke', '99. Die große Glocke von Neustadt',
         '100. Die Glocke von Lindesheim', '101. Das versunkene Glöcklein', '102. Die vergrabenen Glocken',
         '103. Die goldene Orgel', '104. Das goldene Kegelspiel', '105. Der Schatz zu Beilstein',
         '106. Das weiße Fräulein an der dicken Eiche', '107. Die Schätze zu Wilenstein',
         '108. Der Stolzenberger Schatz', '109. Der weiße Peter', '110. Der Schatz auf dem Disibodenberg',
         '111. Der Schatz auf Hohenfels', '112. Der Schatz zu Rotenkirchen', '113. Der Schatz auf Scharfeneck',
         '114. Die Juden und der Schatz', '115. Die Heidenburg', '116. Der Krötenstuhl',
         '117. Der Klosterbrunnen bei Pirmasens', '118. Der Bauer und der Schatz',
         '119. Die vergessene Schlüsselblume', '120. Die Schätze im Innern des Kirkeler Bergs',
         '121. Der Birkenbusch auf Kirkel', '122. Die unterirdischen Schätze im Pauliner Schlößchen',
         '123. In Gold verwandelte Porzellanscherben', '124. Das weiße Fräulein auf der Leinbachmühle',
         '125. Der entgangene Schatz', '126. Der gehobene Schatz', '127. Das Glühhäuschen', '128. Die Glut',
         '129. Die blaue Flamme', '130. Die Heidenmauer', '131. Attilas Grab',
         '132. Wie die Heidenburg fiel',
         '133. Kaiser Adolfs Tod', '134. Wie die Bauern Schloß Lindelbrunn nahmen',
         '135. Die Bauern auf Neuleiningen', '136. Das Klösterlein zu Fischbach', '137. Der Hirt von Oggersheim',
         '138. Die Mordkammer', '139. Zerstörung des Klosters St. Medard', '140. Belagerung von Burg Lichtenberg',
         '141. Neustadts Retterin', '142. Der Metallfühler', '143. Jammerhalde und Hahnenfalz',
         '144. Der Trompeter an der dicken Eiche', '145. Der tote Soldat', '146. Der heimgekehrte Krieger',
         '147. Nächtliche Erscheinung zu Speyer', '148. Wie du willt, Melchior', '149. Treuenfels',
         '150. Der Eberkopf', '151. Der Mönchskopf', '152. Die Grafen von Eberstein',
         '153. Die Burgfrau von Berwartstein', '154. Der böse Wolfsberger', '155. Das Grab Noes und die Pest',
         '156. Entstehung von Kaiserslautern', '157. Schloß und Dorf Neidenfels',
         '158. Kehrdichannichts, Murmelnichtviel, Schaudichnichtum', '159. Entstehung von Bad Diedelkopf',
         '160. Gründung Kreuznachs', '161. Gründung des Klosters Difibodenberg',
         '162. Stiftung von Klingenmünster', '163. Limburgs Entstehung', '164. Das Kloster Rosenthal',
         '165. Die Rosentreppe', '166. Der Roßsprung bei Speyer',
         '167. Das Fuchsloch oder Gnadenwasser bei Zeiskam', '168. Die Felsenkirche zu Oberstein',
         '169. Der Abt Jakob von Hornbach', '170. Das Dietrichskirchel', '171. Die verkehrte Kirche',
         '172. Die Wolfskirche bei Bosenbach', '173. Das Kind von der Falkenburg',
         '174. Die Peternell bei Bergzabern', '175. Die Dagobertshecke und die Haingeraiden',
         '176. Des Remigs Teil vom Wafichenwald', '177. Das steinerne Kreuz',
         '178. Das gläserne Kreuz', '179. Das Steinkreuz im Walde', '180. Das weiße Kreuz im Bienwald',
         '181. Sickingens Würfel', '182. Der Abtstein', '183. Der Hohe Stein', '184. Der Gollenstein',
         '185. Ein Grabstein in der St. Johanniskirche zu Dürkheim', '186. Der Reitersprung', '187. Kühner Sprung',
         '188. Der Jungfernsprung bei Battenberg', '189. Der Jungfernsprung bei Dahn', '190. Der Wolfsfels',
         '191. Die Hirschtrabe', '192. Der Nonnenfels', '193. Das Frifraloch bei Offenbach am Glan',
         '194. Die Heidenhöhle', '195. Das Affolterloch', '196. Der Maidenbrunnen', '197. Der Reiterbrunnen',
         '198. Der tiefe Brunnen', '199. Wasserberg und tiefer Brunnen', '200. Von drei Brunnen',
         '201. Der Hungerbrunnen bei Kaiserslautern', '202. Die Silbergrube', '203. Die Erzgrube im Langental',
         '204. Die drei Züge', '205. Ernesti-Glück', '206. Die Geißkammer', '207. Der Kampf am Wasgenstein',
         '208. Keiser Friderich zu Keiserslautern', '209. Des Kaisers Bett', '210. Der Hecht im Kaiserwoog',
         '211. Der Ritter von Beilstein', '212. Das Hufeisen zu Kaiserslautern',
         '213. Warum die Kaiser im Dom zu Speyer bestattet wurden', '214. Kaiser Rudolfs Ritt zum Grabe',
         '215. Kaiser Heinrich IV. zu Böckelheim', '216. Der Lindenplatz auf Hartenburg',
         '217. Die Göllheimer Ulme', '218. Die Tschiffliker Kirschen', '219. Der Pfeil',
         '220. Der Löwe im pfälzischen und bayerischen Wappen', '221. Raugraf Heinrich und Maria von Brabant',
         '222. Franz von Sickingen und der Geist vom Rotenfelsen', '223. Der alte Ruppert vom Ruppertsfelsen',
         '224. Das Kloster Seebach', '225. Das Kloster Marienstein', '226. Die Brautfahrt',
         '227. Weibestreue',
         '228. Das Fräulein mit dem steinernen Herzen', '229. Die Lilie zu Altenbaumberg',
         '230. Die gelben Schlüsselblumen', '231. Hildegard von Hoheneck', '232. Das Fräulein von Wilenstein',
         '233. Schön Elsbeth von der Kästenburg', '234. Richard Löwenherz auf Trifels',
         '235. Das Pfälzer Weberlein', '236. Das ehrliche Weberlein zu Zeiskam', '237. Der Junker von Randeck',
         '238. Der böse Scharfenecker', '239. Die lederne Brücke', '240. Des Spangenbergers Sohn',
         '241. Der Raub der Monstranz', '242. Der Raubritter Wynant', '243. Die Falkensteiner Blutnelken',
         '244. Kaspar von Spangenberg', '245. Das Mordloch', '246. Der Mutter Fluch',
         '247. Der ewige Fuhrmannsweg', '248. Junker Elz von Wecklingen', '249. Die Hand des Toten',
         '250. Die unverwelkliche Hand', '251. Die Edelfräulein zu Altdorf',
         '252. Der böse Bischof und der getreue Hutzmann', '253. Das Balkemännel', '254. Der Mann im Monde',
         '255. Der böse Müller', '256. Der Eremit auf dem Rosenberg', '257. Das versunkene Kloster',
         '258. Woher die Pfalz ihren Namen hat',
         '259. Wie vier ehemals Guttenbergische Dörfer ihre Namen erhielten', '260. Noch zwei andere Ortsnamen',
         '261. Warum die Pfälzer Krischer heißen',
         '262. Die Sausenheimer "Essel"', '263. Die Oppauer "Dampfnudelstürmer"', '264. Die Friesenheimer "Eulen"',
         '265. Annweilers Name und Spottname', '266. Der Sammetärmel von Annweiler', '267. Was der Teufel verlor',
         '268. Der Hofnarr von Münster', '269. Der Pfarrer von Grumbach', '270. Die dicke Landgräfin',
         '271. Der Trunk aus dem Stiefel', '272. Der durstige Abt', '273. Der Weinkampf zu Wachenheim',
         '274. Der Gescheideste', '275. Des Pfalzgrafen Hirschjagd', '276. Der Reiterlud von Iggelheim',
         '277. Die Kugeltaufe zu Ebernburg', '278. Der pfälzische Eulenspiegel', '279. Das Eselsei',
         '280. Das neue Schulhaus', '281. Der englische Schneider', '282. Die Adjunkten-Wahl',
         '283. Wie tief ist der Brunnen?']
    dict = {'1. Die Geisterschlacht': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                       'I. Von Seelen, Geistern und Gespenstern.'],
            '2. Die Fahrt der Toten': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                       'I. Von Seelen, Geistern und Gespenstern.'],
            '3. Die überschiffenden Mönche': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'I. Von Seelen, Geistern und Gespenstern.'],
            '4. Der ewige Jäger': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                   'I. Von Seelen, Geistern und Gespenstern.'],
            '5. Der Jägerpfuhl': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                  'I. Von Seelen, Geistern und Gespenstern.'],
            '6. Der wilde Jäger von Sponheim': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                'I. Von Seelen, Geistern und Gespenstern.'],
            '7. Der wilde Jäger am Donnersberg': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                  'I. Von Seelen, Geistern und Gespenstern.'],
            '8. Der Lindenschmidt': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                     'I. Von Seelen, Geistern und Gespenstern.'],
            '9. Der Einaug von Scharfeneck': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'I. Von Seelen, Geistern und Gespenstern.'],
            '10. Der Geist vom Scharfeneck': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'I. Von Seelen, Geistern und Gespenstern.'],
            '11. Hans Trapp': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                               'I. Von Seelen, Geistern und Gespenstern.'],
            '12. Das weiße Reh': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                  'I. Von Seelen, Geistern und Gespenstern.'],
            '13. Der Geist auf dem Bleifelsen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                 'I. Von Seelen, Geistern und Gespenstern.'],
            '14. Der blutschwitzende Stein': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'I. Von Seelen, Geistern und Gespenstern.'],
            '15. Der gebannte Geist': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                       'I. Von Seelen, Geistern und Gespenstern.'],
            '16. Der Irrwisch auf dem Klosterberg bei Winterbach': [
                'A. Vom alten und neuen Glauben. (Mythische Sagen.)', 'I. Von Seelen, Geistern und Gespenstern.'],
            '17. Das Flämmchen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                  'I. Von Seelen, Geistern und Gespenstern.'],
            '18. Der Schuß auf das Flämmchen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                'I. Von Seelen, Geistern und Gespenstern.'],
            '19. Der Geist auf dem Kieneck': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'I. Von Seelen, Geistern und Gespenstern.'],
            '20. Der falsche Eid': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                    'I. Von Seelen, Geistern und Gespenstern.'],
            '21. Die Sage vom Maulus': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                        'I. Von Seelen, Geistern und Gespenstern.'],
            '22. Des Beilsteiners Umgang': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                            'I. Von Seelen, Geistern und Gespenstern.'],
            '23. Der Maire von Meisenheim': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                             'I. Von Seelen, Geistern und Gespenstern.'],
            '24. Das Mädchen vom Pauliner Schlößchen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                        'I. Von Seelen, Geistern und Gespenstern.'],
            '25. Die unredliche Wirtin': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                          'I. Von Seelen, Geistern und Gespenstern.'],
            '26. Der Grenzsteinverrücker': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                            'I. Von Seelen, Geistern und Gespenstern.'],
            '27. Kanzel und Nonne': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                     'I. Von Seelen, Geistern und Gespenstern.'],
            '28. Das Nonnental bei Neustadt': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                               'I. Von Seelen, Geistern und Gespenstern.'],
            '29. Der Hund von Auerbach': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                          'I. Von Seelen, Geistern und Gespenstern.'],
            '30. Die Wassernixe zu Eschringen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                 'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '31. Die schöne Tanne': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                     'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '32. Die drei Wiesenfräulein': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                            'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '33. Die drei Jungfrauen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                        'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '34. Die drei Schwestern': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                        'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '35. Das Schloßfräulein': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                       'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '36. Der Schloßgarten auf dem Großen Stiefel': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                            'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '37. Die Schloßfrau und ihre Wäsche': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                   'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '38. Die weiße Dame vom Pauliner Schlößchen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                           'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '39. Die Wildfrau': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                 'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '40. Das Wildfrauloch bei Schweinschied': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                       'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '41. Das Wildfrauenloch bei Schwarzerden': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                        'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '42. Das Lindenmütterchen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                         'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '43. Die guten Zwerge': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                     'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '44. Das Graumännchensloch': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                          'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '45. Das graue Männchen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                       'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '46. Der Ritter vom Huneberg': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                            'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '47. Das Kehrebacher Knüppchen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '48. Die Erdmännlein': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                    'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '49. Die Schlange und das Kind': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'II. Von Elfen und Nixen, Zwergen und Wichten.'],
            '50. Die Schlangenkönigin': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                         'III. Von Dämonen und Göttern.'],
            '51. Der Drachenfels bei Dürkheim': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                 'III. Von Dämonen und Göttern.'],
            '52. Der Drachenfels bei Busenberg': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                  'III. Von Dämonen und Göttern.'],
            '53. Das wütende Heer': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                     'III. Von Dämonen und Göttern.'],
            '54. Die wilde Jagd': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                   'III. Von Dämonen und Göttern.'],
            '55. Vom Rosse des wilden Jägers': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                'III. Von Dämonen und Göttern.'],
            '56. Die Riesen des Bliestales': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'III. Von Dämonen und Göttern.'],
            '57. Die Riesen des Wasgenwaldes': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                'III. Von Dämonen und Göttern.'],
            '58. Das Heidentürmchen zu Speyer': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                 'III. Von Dämonen und Göttern.'],
            '59. Der Riese Kreuzmann': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                        'III. Von Dämonen und Göttern.'],
            '60. Das Riesen- oder Hünengrab': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                               'III. Von Dämonen und Göttern.'],
            '61. Vom Gotte Wodan': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                    'III. Von Dämonen und Göttern.'],
            '62. Kolb von Wartenberg': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                        'III. Von Dämonen und Göttern.'],
            '63. Die Waldkapelle': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                    'III. Von Dämonen und Göttern.'],
            '64. Gott Donar und sein Gefährt': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                'III. Von Dämonen und Göttern.'],
            '65. Der Burgbau auf dem Rheingrafenstein': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                         'IV. Von Teufeln, Hexen und Zauberern.'],
            '66. Der Teufelsstein': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                     'IV. Von Teufeln, Hexen und Zauberern.'],
            '67. Der Teufelstisch': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                     'IV. Von Teufeln, Hexen und Zauberern.'],
            '68. Der Teufelsberg': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                    'IV. Von Teufeln, Hexen und Zauberern.'],
            '69. Der Teufelsbrunnen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                       'IV. Von Teufeln, Hexen und Zauberern.'],
            '70. Der Müller und der Teufel': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'IV. Von Teufeln, Hexen und Zauberern.'],
            '71. Die Hexe vom Münstertal': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                            'IV. Von Teufeln, Hexen und Zauberern.'],
            '72. Die gebrannte Hexe': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                       'IV. Von Teufeln, Hexen und Zauberern.'],
            '73. Die diebische Hexe': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                       'IV. Von Teufeln, Hexen und Zauberern.'],
            '74. Das Hexengewitter': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                      'IV. Von Teufeln, Hexen und Zauberern.'],
            '75. Der Hexenball': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                  'IV. Von Teufeln, Hexen und Zauberern.'],
            '76. Hexentanz und Hexenkraut': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                             'IV. Von Teufeln, Hexen und Zauberern.'],
            '77. Der Zauberschüße Punker von Rohrbach': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                         'IV. Von Teufeln, Hexen und Zauberern.'],
            '78. Der Schnittlfelsen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                       'IV. Von Teufeln, Hexen und Zauberern.'],
            '79. Der Heidenfelsen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                     'IV. Von Teufeln, Hexen und Zauberern.'],
            '80. Der krumme Dallacker': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                         'IV. Von Teufeln, Hexen und Zauberern.'],
            '81. Der Stab des Klausners': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                           'V. Von Zeichen und Wundern.'],
            '82. Das Marienbild zu Gräfinthal': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                 'V. Von Zeichen und Wundern.'],
            '83. Das Muttergottesbild zu Forst': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                  'V. Von Zeichen und Wundern.'],
            '84. Das Marienbild zu Ranschbach': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                 'V. Von Zeichen und Wundern.'],
            '85. Das fromme Knäblein zu Speyer': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                  'V. Von Zeichen und Wundern.'],
            '86. Das Marienbild im Dom zu Speyer': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                    'V. Von Zeichen und Wundern.'],
            '87. Der rauschende Kelch im Speyerer Dom': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                         'V. Von Zeichen und Wundern.'],
            '88. Die Maria-Hilf-Kapelle auf dem Kolmerberg': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                              'V. Von Zeichen und Wundern.'],
            '89. Die Kapelle und das Glöcklein des hl. Cyriakus': [
                'A. Vom alten und neuen Glauben. (Mythische Sagen.)', 'V. Von Zeichen und Wundern.'],
            '90. Der hl. Cyriakus und die Wingertsbalken': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                            'V. Von Zeichen und Wundern.'],
            '91. Die Strutelpeters-Kapelle': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'V. Von Zeichen und Wundern.'],
            '92. Die St. Lorenzkapelle': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                          'V. Von Zeichen und Wundern.'],
            '93. Das goldene Kreuz im Klosterweiher': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                       'V. Von Zeichen und Wundern.'],
            '94. Der Servatiusbrunnen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                         'V. Von Zeichen und Wundern.'],
            '95. Der Lorenzenbrunnen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                        'V. Von Zeichen und Wundern.'],
            '96. Die Wunder des hl. Philipp von Zell': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                        'V. Von Zeichen und Wundern.'],
            '97. Die Glocken zu Speyer': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                          'VI. Von Glocken und Schätzen.'],
            '98. Die fliegende Glocke': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                         'VI. Von Glocken und Schätzen.'],
            '99. Die große Glocke von Neustadt': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                  'VI. Von Glocken und Schätzen.'],
            '100. Die Glocke von Lindesheim': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                               'VI. Von Glocken und Schätzen.'],
            '101. Das versunkene Glöcklein': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'VI. Von Glocken und Schätzen.'],
            '102. Die vergrabenen Glocken': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                             'VI. Von Glocken und Schätzen.'],
            '103. Die goldene Orgel': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                       'VI. Von Glocken und Schätzen.'],
            '104. Das goldene Kegelspiel': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                            'VI. Von Glocken und Schätzen.'],
            '105. Der Schatz zu Beilstein': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                             'VI. Von Glocken und Schätzen.'],
            '106. Das weiße Fräulein an der dicken Eiche': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                            'VI. Von Glocken und Schätzen.'],
            '107. Die Schätze zu Wilenstein': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                               'VI. Von Glocken und Schätzen.'],
            '108. Der Stolzenberger Schatz': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'VI. Von Glocken und Schätzen.'],
            '109. Der weiße Peter': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                     'VI. Von Glocken und Schätzen.'],
            '110. Der Schatz auf dem Disibodenberg': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                      'VI. Von Glocken und Schätzen.'],
            '111. Der Schatz auf Hohenfels': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'VI. Von Glocken und Schätzen.'],
            '112. Der Schatz zu Rotenkirchen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                'VI. Von Glocken und Schätzen.'],
            '113. Der Schatz auf Scharfeneck': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                'VI. Von Glocken und Schätzen.'],
            '114. Die Juden und der Schatz': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'VI. Von Glocken und Schätzen.'],
            '115. Die Heidenburg': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                    'VI. Von Glocken und Schätzen.'],
            '116. Der Krötenstuhl': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                     'VI. Von Glocken und Schätzen.'],
            '117. Der Klosterbrunnen bei Pirmasens': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                      'VI. Von Glocken und Schätzen.'],
            '118. Der Bauer und der Schatz': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                              'VI. Von Glocken und Schätzen.'],
            '119. Die vergessene Schlüsselblume': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                   'VI. Von Glocken und Schätzen.'],
            '120. Die Schätze im Innern des Kirkeler Bergs': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                              'VI. Von Glocken und Schätzen.'],
            '121. Der Birkenbusch auf Kirkel.': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                 'VI. Von Glocken und Schätzen.'],
            '122. Die unterirdischen Schätze im Pauliner Schlößchen': [
                'A. Vom alten und neuen Glauben. (Mythische Sagen.)', 'VI. Von Glocken und Schätzen.'],
            '123. In Gold verwandelte Porzellanscherben': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                           'VI. Von Glocken und Schätzen.'],
            '124. Das weiße Fräulein auf der Leinbachmühle': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                                              'VI. Von Glocken und Schätzen.'],
            '125. Der entgangene Schatz': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                           'VI. Von Glocken und Schätzen.'],
            '126. Der gehobene Schatz': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                         'VI. Von Glocken und Schätzen.'],
            '127. Das Glühhäuschen': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                      'VI. Von Glocken und Schätzen.'],
            '128. Die Glut': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)', 'VI. Von Glocken und Schätzen.'],
            '129. Die blaue Flamme': ['A. Vom alten und neuen Glauben. (Mythische Sagen.)',
                                      'VI. Von Glocken und Schätzen.'],
            '130. Die Heidenmauer': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.', 'IVI. Ohne Gruppe'],
            '131. Attilas Grab': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.', 'IVI. Ohne Gruppe'],
            '132. Wie die Heidenburg fiel': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                             'IVI. Ohne Gruppe'],
            '133. Kaiser Adolfs Tod': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                       'IVI. Ohne Gruppe'], '134. Wie die Bauern Schloß Lindelbrunn nahmen': [
            'B. Von pfälzischer Landes-, Orts- und Familiengeschichte.', 'IVI. Ohne Gruppe'],
            '135. Die Bauern auf Neuleiningen': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                 'IVI. Ohne Gruppe'],
            '136. Das Klösterlein zu Fischbach': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                  'IVI. Ohne Gruppe'],
            '137. Der Hirt von Oggersheim': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                             'IVI. Ohne Gruppe'],
            '138. Die Mordkammer': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.', 'IVI. Ohne Gruppe'],
            '139. Zerstörung des Klosters St. Medard': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                        'I. Von Kriegen und Fehden und anderen Nöten.'],
            '140. Belagerung von Burg Lichtenberg': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                     'I. Von Kriegen und Fehden und anderen Nöten.'],
            '141. Neustadts Retterin': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                        'I. Von Kriegen und Fehden und anderen Nöten.'],
            '142. Der Metallfühler': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                      'I. Von Kriegen und Fehden und anderen Nöten.'],
            '143. Jammerhalde und Hahnenfalz': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                'I. Von Kriegen und Fehden und anderen Nöten.'],
            '144. Der Trompeter an der dicken Eiche': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                       'I. Von Kriegen und Fehden und anderen Nöten.'],
            '145. Der tote Soldat': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                     'I. Von Kriegen und Fehden und anderen Nöten.'],
            '146. Der heimgekehrte Krieger': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                              'I. Von Kriegen und Fehden und anderen Nöten.'],
            '147. Nächtliche Erscheinung zu Speyer': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                      'I. Von Kriegen und Fehden und anderen Nöten.'],
            '148. Wie du willt, Melchior': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                            'I. Von Kriegen und Fehden und anderen Nöten.'],
            '149. Treuenfels': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                'I. Von Kriegen und Fehden und anderen Nöten.'],
            '150. Der Eberkopf': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                  'I. Von Kriegen und Fehden und anderen Nöten.'],
            '151. Der Mönchskopf auf Hartenburg': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                   'I. Von Kriegen und Fehden und anderen Nöten.'],
            '152. Die Grafen von Eberstein': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                              'I. Von Kriegen und Fehden und anderen Nöten.'],
            '153. Die Burgfrau von Berwartstein': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                   'I. Von Kriegen und Fehden und anderen Nöten.'],
            '154. Der böse Wolfsberger': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                          'I. Von Kriegen und Fehden und anderen Nöten.'],
            '155. Das Grab Noä und die Best': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                               'I. Von Kriegen und Fehden und anderen Nöten.'],
            '156. Entstehung von Kaiserslautern': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                   'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '157. Schloß und Dorf Neidenfels': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '158. Kehrdichannichts, Murmelnichtviel, Schaudichnichtum': [
                'B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '159. Entstehung von Bad Diedelkopf': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                   'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '160. Gründung Kreuznachs': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                         'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '161. Gründung des Klosters Difibodenberg': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                         'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '162. Stiftung von Klingenmünster': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                 'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '163. Limburgs Entstehung': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                         'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '164. Das Kloster Rosenthal': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                           'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '165. Die Rosentreppe': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                     'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '166. Der Roßsprung bei Speyer': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                              'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '167. Das Fuchsloch oder Gnadenwasser bei Zeiskam': [
                'B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '168. Die Felsenkirche zu Oberstein': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                   'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '169. Der Abt Jakob von Hornbach': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '170. Das Dietrichskirchel': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                          'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '171. Die verkehrte Kirche': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                          'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '172. Die Wolfskirche bei Bosenbach': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                   'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '173. Das Kind von der Falkenburg': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                 'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '174. Die Peternell bei Bergzabern': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                  'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '175. Die Dagobertshecke und die Haingeraiden 219': [
                'B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '176. Des Remigs Teil vom Wafichenwald': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                      'II. Von Gründungen, Stiftungen und Ortsbenennungen.'],
            '177. Das steinerne Kreuz': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                         'III. Von Kreuzen und Steinen, von'],
            '178. Das gläserne Kreuz': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                        'III. Von Kreuzen und Steinen, von'],
            '179. Das Steinkreuz im Walde': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                             'III. Von Kreuzen und Steinen, von'],
            '180. Das weiße Kreuz im Bienwald': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                 'III. Von Kreuzen und Steinen, von'],
            '181. Sickingens Würfel.': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                        'III. Von Kreuzen und Steinen, von'],
            '182. Der Abtstein': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                  'III. Von Kreuzen und Steinen, von'],
            '183. Der Hohe Stein': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                    'III. Von Kreuzen und Steinen, von'],
            '184. Der Gollenstein': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                     'III. Von Kreuzen und Steinen, von'],
            '185. Ein Grabstein in der St. Johanniskirche zu Dürkheim': [
                'B. Von pfälzischer Landes-, Orts- und Familiengeschichte.', 'III. Von Kreuzen und Steinen, von'],
            '186. Der Reitersprung': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                      'III. Von Kreuzen und Steinen, von'],
            '187. Kühner Sprung': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                   'III. Von Kreuzen und Steinen, von'],
            '188. Der Jungfernsprung bei Battenberg': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                       'III. Von Kreuzen und Steinen, von'],
            '189. Der Jungfernsprung bei Dahn': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                 'III. Von Kreuzen und Steinen, von'],
            '190. Der Wolfsfels': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                   'III. Von Kreuzen und Steinen, von'],
            '191. Die Hirschtrabe': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                     'III. Von Kreuzen und Steinen, von'],
            '192. Der Nonnenfels': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                    'III. Von Kreuzen und Steinen, von'],
            '193. Das Frifraloch bei Offenbach am Glan': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                          'III. Von Kreuzen und Steinen, von'],
            '194. Die Heidenhöhle': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                     'III. Von Kreuzen und Steinen, von'],
            '195. Das Affolterloch': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                      'III. Von Kreuzen und Steinen, von'],
            '196. Der Maidenbrunnen': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                       'III. Von Kreuzen und Steinen, von'],
            '197. Der Reiterbrunnen': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                       'III. Von Kreuzen und Steinen, von'],
            '198. Der tiefe Brunnen': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                       'III. Von Kreuzen und Steinen, von'],
            '199. Wasserberg und tiefer Brunnen': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                   'III. Von Kreuzen und Steinen, von'],
            '200. Von drei Brunnen': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                      'III. Von Kreuzen und Steinen, von'],
            '201. Der Hungerbrunnen bei Kaiserslautern': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                          'III. Von Kreuzen und Steinen, von'],
            '202. Die Silbergrube': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                     'IV. Vom heimischen Bergbau.'],
            '203. Die Erzgrube im Langental': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                               'IV. Vom heimischen Bergbau.'],
            '204. Die drei Züge': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                   'IV. Vom heimischen Bergbau.'],
            '205. Ernesti-Glück': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                   'IV. Vom heimischen Bergbau.'],
            '206. Die Geißkammer': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                    'IV. Vom heimischen Bergbau.'],
            '207. Der Kampf am Wasgenstein': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                              'V. Von Helden, Geschlechtern und Wappen.'],
            '208. Keiser Friderich zu Keiserslautern': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                        'V. Von Helden, Geschlechtern und Wappen.'],
            '209. Des Kaisers Bett': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                      'V. Von Helden, Geschlechtern und Wappen.'],
            '210. Der Hecht im Kaiserwoog': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                             'V. Von Helden, Geschlechtern und Wappen.'],
            '211. Der Ritter von Beilstein': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                              'V. Von Helden, Geschlechtern und Wappen.'],
            '212. Das Hufeisen zu Kaiserslautern': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                    'V. Von Helden, Geschlechtern und Wappen.'],
            '213. Warum die Kaiser im Dom zu Speyer bestattet wurden': [
                'B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                'V. Von Helden, Geschlechtern und Wappen.'],
            '214. Kaiser Rudolfs Ritt zum Grabe': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                   'V. Von Helden, Geschlechtern und Wappen.'],
            '215. Kaiser Heinrich IV. zu Böckelheim': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                       'V. Von Helden, Geschlechtern und Wappen.'],
            '216. Der Lindenplatz auf Hartenburg': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                    'V. Von Helden, Geschlechtern und Wappen.'],
            '217. Die Göllheimer Ulme': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                         'V. Von Helden, Geschlechtern und Wappen.'],
            '218. Die Tschiffliker Kirschen': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                               'V. Von Helden, Geschlechtern und Wappen.'],
            '219. Der Pfeil': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                               'V. Von Helden, Geschlechtern und Wappen.'],
            '220. Der Löwe im pfälzischen und bayerischen Wappen': [
                'B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                'V. Von Helden, Geschlechtern und Wappen.'], '221. Raugraf Heinrich und Maria von Brabant': [
            'B. Von pfälzischer Landes-, Orts- und Familiengeschichte.', 'V. Von Helden, Geschlechtern und Wappen.'],
            '222. Franz von Sickingen und der Geist vom Rotenfelsen': [
                'B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                'V. Von Helden, Geschlechtern und Wappen.'],
            '223. Der alte Ruppert vom Ruppertsfelsen': ['B. Von pfälzischer Landes-, Orts- und Familiengeschichte.',
                                                         'V. Von Helden, Geschlechtern und Wappen.'],
            '224. Das Kloster Seebach': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                         'I. Von mancherlei Treue und Verrat.'],
            '225. Das Kloster Marienstein': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                             'I. Von mancherlei Treue und Verrat.'],
            '226. Die Brautfahrt': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                    'I. Von mancherlei Treue und Verrat.'],
            '227. Weibestreue': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                 'I. Von mancherlei Treue und Verrat.'],
            '228. Das Fräulein mit dem steinernen Herzen 287': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                                                'I. Von mancherlei Treue und Verrat.'],
            '229. Die Lilie zu Altenbaumburg': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                                'I. Von mancherlei Treue und Verrat.'],
            '230. Die gelben Schlüsselblumen': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                                'I. Von mancherlei Treue und Verrat.'],
            '231. Hildegard von Hoheneck': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                            'I. Von mancherlei Treue und Verrat.'],
            '232. Das Fräulein von Wilenstein': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                                 'I. Von mancherlei Treue und Verrat.'],
            '233. Schön Elsbeth von der Kästenberg': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                                      'I. Von mancherlei Treue und Verrat.'],
            '234. Richard Löwenherz auf Trifels': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                                   'I. Von mancherlei Treue und Verrat.'],
            '235. Das Pfälzer Weberlein': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                           'I. Von mancherlei Treue und Verrat.'],
            '236. Das ehrliche Weberlein zu Zeiskam': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                                       'I. Von mancherlei Treue und Verrat.'],
            '237. Der Junker von Randeck': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                            'I. Von mancherlei Treue und Verrat.'],
            '238. Der böse Scharfenecker': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                            'I. Von mancherlei Treue und Verrat.'],
            '239. Die lederne Brücke': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                        'I. Von mancherlei Treue und Verrat.'],
            '240. Des Spangenbergers Sohn': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                             'I. Von mancherlei Treue und Verrat.'],
            '241. Der Raub der Monstranz': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                            'II. Von übler Taten Lohn.'],
            '242. Der Raubritter Wynant': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                           'II. Von übler Taten Lohn.'],
            '243. Die Falkensteiner Blutnelken': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                                  'II. Von übler Taten Lohn.'],
            '244. Kaspar von Spangenberg': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                            'II. Von übler Taten Lohn.'],
            '245. Das Mordloch': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)', 'II. Von übler Taten Lohn.'],
            '246. Der Mutter Fluch': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                      'II. Von übler Taten Lohn.'],
            '247. Der ewige Fuhrmannsweg': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                            'II. Von übler Taten Lohn.'],
            '248. Junker Elz von Wecklingen': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                               'II. Von übler Taten Lohn.'],
            '249. Die Hand des Toten': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                        'II. Von übler Taten Lohn.'],
            '250. Die unverwesliche Hand': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                            'II. Von übler Taten Lohn.'],
            '251. Die Edelfräulein zu Altdorf': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                                 'II. Von übler Taten Lohn.'],
            '252. Der böse Bischof und der getreue Hutzmann': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                                               'II. Von übler Taten Lohn.'],
            '253. Das Balkemännel': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                     'II. Von übler Taten Lohn.'],
            '254. Der Mann im Monde': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                       'II. Von übler Taten Lohn.'],
            '255. Der böse Müller': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                     'II. Von übler Taten Lohn.'],
            '256. Der Eremit auf dem Rosenberg.': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                                   'II. Von übler Taten Lohn.'],
            '257. Das versunkene Kloster': ['C. Von allerlei Gutem und Bösem. (Ethische Sagen.)',
                                            'II. Von übler Taten Lohn.'],
            '258. Woher die Pfalz ihren Namen hat': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                     'I. Von Orts- und Spitznamen.'],
            '259. Wie vier ehemals Guttenbergische Dörfer': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                             'I. Von Orts- und Spitznamen.'],
            '260. Noch zwei andere Ortsnamen': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                'I. Von Orts- und Spitznamen.'],
            '261. Warum die Pfälzer Krischer heißen': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                       'I. Von Orts- und Spitznamen.'],
            '262. Die Sausenheimer Essel"': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                             'I. Von Orts- und Spitznamen.'],
            '263. Die Oppauer Dampfnudelstürmer"': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                    'I. Von Orts- und Spitznamen.'],
            '264. Die Friesenheimer Eulen"': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                              'I. Von Orts- und Spitznamen.'],
            '265. Annweilers Name und Spottname': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                   'I. Von Orts- und Spitznamen.'],
            '266. Der Sammetärmel von Annweiler': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                   'I. Von Orts- und Spitznamen.'],
            '267. Was der Teufel verlor.': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                            'I. Von Orts- und Spitznamen.'],
            '268. Der Hofnarr von Münster': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                             'II. Von Streichen und Schwänken.'],
            '269. Der Pfarrer von Grumbach': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                              'II. Von Streichen und Schwänken.'],
            '270. Die dicke Landgräfin': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                          'II. Von Streichen und Schwänken.'],
            '271. Der Trunk aus dem Stiefel': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                               'II. Von Streichen und Schwänken.'],
            '272. Der durstige Abt': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                      'II. Von Streichen und Schwänken.'],
            '273. Der Weinkampf zu Wachenheim': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                 'II. Von Streichen und Schwänken.'],
            '274. Der Gescheideste': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                      'II. Von Streichen und Schwänken.'],
            '275. Des Pfalzgrafen Hirschjagd': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                'II. Von Streichen und Schwänken.'],
            '276. Der Reiterlud von Iggelheim': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                 'II. Von Streichen und Schwänken.'],
            '277. Die Kugeltaufe zu Ebernburg': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                 'II. Von Streichen und Schwänken.'],
            '278. Der pfälzische Eulenspiegel.': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                                  'II. Von Streichen und Schwänken.'],
            '279. Das Eselsei': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                 'III. Vom pfälzischen Schilda.'],
            '280. Das neue Schulhaus': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                        'III. Vom pfälzischen Schilda.'],
            '281. Der englische Schneider': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                             'III. Vom pfälzischen Schilda.'],
            '282. Die Adjunkten-Wahl': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                        'III. Vom pfälzischen Schilda.'],
            '283. Wie tief ist der Brunnen': ['D. Von Schalkheit und Torheit. (Humoristische Sagen.)',
                                              'III. Vom pfälzischen Schilda.']}
    d = {}
    i = 0
    print(len(dict))
    for key in dict:
        if not re.search(r"\d+\. \w+", key):
            print(i)
        d[t[i]] = dict[key]
        i += 1
    print(d)


def locs_pfalz():
    with open("temp_pfalz locs.txt", "r", encoding="utf-8") as f:
        locs_raw = f.readlines()
    locs = []
    for loc in locs_raw:
        loc = re.sub(r"\n", "", loc)
        locs.append(loc)
    loc_names = []
    loc_tale = []
    i = 1
    for loc in locs:
        l = re.search(r"[A-Za-z\s\.äöüß-]+", loc)
        loc_names.append(l.group(0)[:-1])
        t = re.search(r"[\d,\s]+$", loc)
        # if t.group(0) == " ":
        #   print(i)
        #  print(l.group(0))
        n = re.findall(r"\d+", t.group(0))
        nn = []
        for e in n:
            nn.append(int(e))
        loc_tale.append(nn)
        i += 1
    # print(loc_name)
    print(len(loc_tale))
    loc_full = {}
    for i in range(len(loc_tale)):
        j = 0
        tmp = []
        for t in loc_tale:
            for n in t:
                # print(n)
                # print(i)
                if n == i + 1:
                    tmp.append(loc_names[j])
                    # print("y")
            j += 1
        loc_full[i + 1] = tmp

    print(loc_full)


pfalz()
