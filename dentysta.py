import json
import os

DANE_SCIEZKA = "dane/rejestrowanie.txt"

def wczytaj(sciezka):
    dane = {}
    if os.path.exists(sciezka):
        with open(sciezka, encoding=4) as plik:
            dane = json.load(plik)
    return dane

def zapis(dane, sciezka):
    with open(sciezka, "w" ,encoding=4) as plik:
        json.dump(dane, plik)
