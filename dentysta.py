import json
import math
import os

DANE_SCIEZKA = "dane/rejestrowanie.txt"

def wczytaj(sciezka:str) ->dict:
    dane = {}
    if os.path.exists(sciezka):
        with open(sciezka) as plik:
            dane = json.load(plik)
    return dane

def zapis(dane:dict, sciezka:str):
    with open(sciezka, "w") as plik:
        json.dump(dane, plik, indent=4)

def wyswietl():
    return wczytaj(DANE_SCIEZKA)

def dodaj(nowe_dane):
    dane = wczytaj(DANE_SCIEZKA)
    dane.update(nowe_dane)
    zapis(dane, DANE_SCIEZKA)


def main():
    if not os.path.exists(DANE_SCIEZKA):
        zapis({}, DANE_SCIEZKA)
    indeks = 1 
    while True:
        opcja = input("Podaj co chcesz zrobic: ")
        match opcja:
            case "wyswietl":
                print(wyswietl())
            case "dodaj":
                imie = input("Podaj imie: ")
                nazwisko = input("Podaj nazwisko: ")
                lata = input("Podaj wiek: ")
                nowe_dane = {
                    indeks: {
                            "imie":imie,
                            "nazwisko":nazwisko,
                            "lata":lata
                        }
                    }
                dodaj(nowe_dane)
                indeks = indeks+1
            case "exit":
                break

main()