

def ner_with_spacy(text):
    import spacy

    # Load the English language model (F1 score: 0.85)
    nlp = spacy.load('de_core_news_lg')
    doc = nlp(text)

    # Print the named entities identified by the model
    # optional: PERSON, NORP, FAC, ORG, GPE, LOC, EVENT, DATA, ...
    for ent in doc.ents:
        print(ent.text, ent.label_)

    '''
    Franken LOC
    Rheinufer LOC
    Reich LOC
    Mettis PER
    Brunhilde PER
    Andernach LOC
    Metz LOC
    Andernach LOC
    christliche MISC
    Fortunatus PER
    lateinischen MISC
    Meß LOC
    Orne LOC
    Sauer LOC
    Saar LOC
    Trier LOC
    Moselthal LOC
    Wein-bau MISC
    Seht PER
    Weinberg LOC
    Etirne LOC
    Bergs LOC
    Schiefergeröll LOC
    Wo LOC
    Augenweide mir gabst du genug und Weide den Lippen MISC
    Kahn PER
    '''

def ner_with_nltk(text):
    import nltk
    #nltk.download('averaged_perceptron_tagger')
    #nltk.download('maxent_ne_chunker')
    #nltk.download('words')

    tokens = nltk.word_tokenize(text, language='german')
    tagged = nltk.pos_tag(tokens)
    entities = nltk.ne_chunk(tagged)

    # optional: ORGANIZATION, PERSON, LOCATION, DATE, TIME, MONEY, PERCENT, FACILITY, GPE (more general than LOCATION)
    for entity in entities:
        if hasattr(entity, 'label') and entity.label() == 'GPE':
            print(entity)

    '''
    (GPE Um/NNP)
    (GPE Franken/NNP)
    (GPE Frankenreichs/NNP)
    (GPE Andernach/NNP)
    (GPE Meß/NNP)
    (GPE Sauer/NNP)
    (GPE Moselthal/NNP)
    (GPE Bringt/NNP)
    (GPE Weinberg/NNP)
    (GPE Sorgsam/NNP)
    (GPE Zeilen/NNP)
    (GPE Wo/NNP)
    (GPE Liest/NNP)
    (GPE Weide/NNP)
    (GPE Da/NNP)
    (GPE Moselgefild/NNP)
    (GPE Uebung/NNP)
    (GPE Urkunden/NNP)
    '''


def ner_with_flair(text):
    from flair.data import Sentence
    from flair.models import SequenceTagger
    import re

    # Load the German language model
    # optional: flair/ner-german-large (F1 score: 0.92), flair/ner-german-legal, flair/ner-german
    tagger = SequenceTagger.load("flair/ner-german-large")
    sentence = Sentence(text)
    tagger.predict(sentence)
    print(sentence)

    print('The following NER tags are found:')
    locations = []
    # optional: PER, LOC, ORG, MISC
    for entity in sentence.get_spans("ner"):
        #print(entity.tokens)
        ent = str(entity.get_labels()[0])
        #print(ent)
        if re.search(r"LOC", ent):
            #print(ent)
            loc = re.search(r'"\w+"', ent).group(0)
            loc = re.sub(r'"',"", loc)
            locations.append(loc)
    '''
    The following NER tags are found:
    Span[9:10]: "Franken" → ORG (0.9207)
    Span[31:32]: "Frankenreichs" → LOC (1.0)
    Span[33:34]: "Austrasien" → LOC (1.0)
    Span[38:39]: "Mettis" → LOC (1.0)
    Span[40:41]: "Meß" → LOC (1.0)
    Span[46:47]: "Siegebert" → PER (1.0)
    Span[51:52]: "Brunhilde" → PER (1.0)
    Span[57:58]: "Andernach" → LOC (1.0)
    Span[68:69]: "Metz" → LOC (1.0)
    Span[70:71]: "Andernach" → LOC (1.0)
    Span[80:81]: "Fortunatus" → PER (1.0)
    Span[99:100]: "Meß" → LOC (1.0)
    Span[116:117]: "Orne" → LOC (0.9996)
    Span[118:119]: "Sauer" → LOC (0.9997)
    Span[120:121]: "Saar" → LOC (0.9999)
    Span[123:124]: "Trier" → LOC (1.0)
    '''


def main():
    paragraph_from = "Sagen und Geschichten des Moseltals Pages 1-194_OCR, 18. Moselreise des Frankenkönigs Siegebert, 570 n. Chr"
    toy_paragraph = "Um die Mitte des 6. Jahrhunderts hatten die Franken den Schwerpunkt ihrer Herrschaft auf das linke Rheinufer verlegt und ihr Reich in mehrere Königsherrschaften geteilt. Der östliche Teil des Frankenreichs hieß Austrasien, desſen Hauptstadt war Mettis oder Meß, dort herrschte um 570 Siegebert, seine Gemahlin war Brunhilde. Er hatte auch in Andernach einen Königshof, und wie er einmal zu Schiffe von Metz nach Andernach gereist ist, begleitete ihn der gefeierte christliche Dichter Fortunatus. Dieser hat in wohlklingenden lateinischen Versen diese Moselfahrt be- schrieben. Er traf die Fürsten in Meß, dort bestiegen sie einen Kahn, der sie nicht ohne Fährlichkeit an den Münd-ungen der Orne, Sauer und Saar vorüber nach Trier trug. Da treten sie ins enge Moselthal ein, das aber freundlich wird durch den überall hier herrschenden Wein-bau. Gerade diese Schilderung mutet uns ganz modern Es heißt daselbst ſo: an. Seht, wie die steile Wand zu dem höchsten Gipfel hinanklimmt, Bis zu den Sternen zu gehn scheint sie uns, schauerlich wild. Aber nicht nußlos ist das steinige Schiefergebröckel, Bringt es doch üppige Frucht, trieft doch der Felsen von Wein. Sichtbar durch Marken begrenzt, zieht aufwärts Weinberg an Weinberg, Sorgsam in Zeilen gepflanzt, bis zu der Etirne des Bergs: Zwischen dem starrenden Fels des Winzers liebliche Pflanzung, Rötlicher Trauben Pracht zwischen dem grauen Gestein. Und wo die Honigfrüchte dem trockenen Felsen entſprießen, Wo in dem Schiefergeröll lachende Trauben gedeihn, Wo der rankende Wein an den kahlen Bergen hinanklimmt, Und sein schattendes Laub trockene Halden umzieht, Schneidet die farbigen Beeren in fröhlicher Ernte der Winzer, Liest sie, während er hängt hoch an dem hängenden Fels. Augenweide mir gabst du genug und Weide den Lippen, Da ich dich schaute vom Kahn, liebliches Moselgefild! Die sichtbare Abgrenzung der Weinberge von einander durch Marken blieb das Mittelalter hindurch in Uebung, in Urkunden wenigstens werden die einzelnen Weinbergs- parzellen stets Picturen genannt, zu deutsch Bemalung."
    test_paragraph = "Um die Mitte des 6. Jahrhunderts hatten die Franken den Schwerpunkt ihrer Herrschaft auf das linke Rheinufer verlegt und ihr Reich in mehrere Königsherrschaften geteilt. Der östliche Teil des Frankenreichs hieß Austrasien, desſen Hauptstadt war Mettis oder Meß, dort herrschte um 570 Siegebert, seine Gemahlin war Brunhilde."
    #ner_with_spacy(toy_paragraph)
    #ner_with_nltk(toy_paragraph)
    ner_with_flair(test_paragraph)


if __name__ == "__main__":
    main()