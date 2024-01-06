"""Hier entsteht die Zuordnung der Orte"""
import initiate
import flair
import pickle


def retrieve_list(name: str):
    """
    Retrieves book content from pickle file
    :param name: name of tale book
    :return: list of lists of tale text
    """
    with open("parsed_sagen/" + name + ".pkl", "rb") as f:
        tale_list = pickle.load(f)
    return tale_list


def ner_with_flair(text: str):
    """
    Performs Named Entity Recognition on a tale to identify locations
    :param text: tale in string form
    :return: Not sure yet
    """
    from flair.data import Sentence
    from flair.models import SequenceTagger

    # Load the German language model
    # optional: flair/ner-german-large (F1 score: 0.92), flair/ner-german-legal, flair/ner-german
    tagger = SequenceTagger.load("flair/ner-german-large")
    sentence = Sentence(text)
    tagger.predict(sentence)
    print(sentence)

    print('The following NER tags are found:')
    # optional: PER, LOC, ORG, MISC
    for entity in sentence.get_spans('ner'):
        print(entity)


def stringify_book(tale_book: list):
    """
    Converts list of list format of tale book into list of strings
    :param tale_book: list of lists containing a tale book
    :return: list of strings of tale book
    """
    book = []
    for tale in tale_book:
        tale_str = stringify_tale(tale)
        book.append(tale_str)
    return book


def stringify_tale(tale: list):
    """
    Converts list format of a tale into a string
    :param tale: list of tale
    :return: string of tale
    """
    tale_str = ""
    for line in tale:
        tale_str += line[:-1]
    return tale_str


def main():
    """
    Main function to handle NER on a tale book
    :return: None
    """
    name = "trier_umgebung_sagen"
    tale_book = retrieve_list(name)
    str_book = stringify_book(tale_book)
    print(str_book)


main()
