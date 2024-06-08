"""Hier entstehen Funktionen mit denen der Output einer Pythondatei auf strukturelle Richtigkeit geprüft
werden kann"""
import initiate
import pickle

def test_trier_umgebung(tales: list):
    name, titles, categories, dict = initiate.trier_und_umgebung()
    test = True
    for tale in tales:
        if not tale[0] in titles:
            test = False
            break
    return test


def retrieve_list():
    with open("parsed_sagen/oberelsass_sagen.pkl", "rb") as f:
        tale_list = pickle.load(f)
    print(tale_list)

#retrieve_list()