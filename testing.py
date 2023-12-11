"""Hier entstehen Funktionen mit denen der Output einer Pythondatei auf strukturelle Richtigkeit geprüft
werden kann"""
import initiate


def test_trier_umgebung(tales: list):
    name, titles, categories, dict = initiate.trier_und_umgebung()
    test = True
    for tale in tales:
        if not tale[0] in titles:
            test = False
            break
    return test
