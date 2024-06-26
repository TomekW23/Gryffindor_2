
import pandas as pd
import math
import csv
import time
import random



def wyslij_sowe(adresat, tresc_listu):
    print(f"Wysyłam sowe do {adresat} z treścią: {tresc_listu}")
    time.sleep(1)
    return random.choices([True, False], weights=(90, 10), k=1)[0]


def nadaj_sowe(adresat, tresc_wiadomosci, potwierdzenie_odbioru, odleglosc, typ, specjalna):
    # Funkcja do obliczenia kosztu sowy na podstawie danych wejściowych
    def wybierz_sowe_zwroc_koszt(odleglosc, typ, specjalna):
        # Tutaj należy zaimplementować logikę do obliczenia kosztu przesyłki na podstawie danych wejściowych
        # Zakładam, że masz już funkcję wybierz_sowe_zwroc_koszt z zadania 5
        
        # Placeholder - zakładamy, że koszt przesyłki wynosi 10
        koszt = 10
        return koszt


    # Funkcja do konwersji słownika na ciąg znaków
    def waluta_dict_na_str(waluta_dict):
        # Tutaj należy zaimplementować logikę konwersji słownika na ciąg znaków
        # Zakładam, że masz już funkcję waluta_dict_na_str z zadania 5
        
        # Placeholder - zakładamy, że zwracamy wartość z klucza "PLN"
        return waluta_dict["PLN"]


    # Obliczanie kosztu przesyłki
    koszt_przesylki = wybierz_sowe_zwroc_koszt(odleglosc, typ, specjalna)
    
    # Konwersja kosztu przesyłki na ciąg znaków
    koszt_przesylki_str = waluta_dict_na_str({"PLN": koszt_przesylki})
    
    # Konwersja potwierdzenia odbioru na odpowiedni format
    potwierdzenie_odbioru_str = "TAK" if potwierdzenie_odbioru else "NIE"
    
    # Dopisanie nowego wiersza do pliku poczta_nadania_lista.csv
    with open('poczta_nadania_lista.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([adresat, tresc_wiadomosci, koszt_przesylki_str, potwierdzenie_odbioru_str])


def wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna=""):
    koszt = {
        "galeon": 0,
        "sykl": 0,
        "knut": 0
    }

    # Koszty bazowe w zależności od odległości i typu
    if odleglosc == "lokalna":
        if typ == "list":
            koszt["knut"] += 2
        elif typ == "paczka":
            koszt["knut"] += 7
    elif odleglosc == "krajowa":
        if typ == "list":
            koszt["sykl"] += 1
            koszt["knut"] += 2
        elif typ == "paczka":
            koszt["sykl"] += 2
            koszt["knut"] += 1
    elif odleglosc == "dalekobiezna":
        if typ == "list":
            koszt["sykl"] += 2
        elif typ == "paczka":
            koszt["sykl"] += 4

    # Dodatkowe koszty za potwierdzenie odbioru
    if potwierdzenie_odbioru:
        koszt["knut"] += 7

    # Dodatkowe koszty za opcję specjalną, jeśli została wybrana
    if specjalna == "wyjec":
        koszt["knut"] += 4
    elif specjalna == "list gończy":
        koszt["sykl"] += 1

    return koszt



def licz_sume(monety):
    # Wartości nominalne
    nom_geleon = 17
    nom_sykl = 21
    nom_knut = 1

    # Obliczanie sumy dla każdego rodzaju monety
    suma_geleon = sum(monety.get("geleon", [])) * nom_geleon
    suma_sykl = sum(monety.get("sykl", [])) * nom_sykl
    suma_knut = sum(monety.get("knut", [])) * nom_knut

    # Zamiana na monety o największym nominale
    while suma_geleon >= nom_sykl:
        suma_geleon -= nom_sykl
        suma_sykl += 1

    while suma_sykl >= nom_knut:
        suma_sykl -= nom_knut
        suma_knut += 1

    return {
        "geleon": suma_geleon,
        "sykl": suma_sykl,
        "knut": suma_knut
    }




def waluta_str_na_dict(waluta_str: str) -> dict:
    ciag = waluta_str.split(" ")

    galeon = 0
    sykl = 0
    knut = 0

    for element_index in range(len(ciag)):
        # Sprawdź czy element to galeon jesli tak to poprzedni element jest wartością galeonu
        if ciag[element_index].startswith("g"):
            galeon = int(ciag[element_index - 1])
            continue
        # Sprawdź czy element to sykl jesli tak to poprzedni element jest wartością sykla
        if ciag[element_index].startswith("s"):
            sykl = int(ciag[element_index - 1])
            continue
        # Sprawdź czy element to knut jesli tak to poprzedni element jest wartością knuta
        if ciag[element_index].startswith("k"):
            knut = int(ciag[element_index - 1])
            continue

    return {"galeon": galeon, "sykl": sykl, "knut": knut}


def waluta_dict_na_str(waluta_dict: dict) -> str:
    # Ilość knutów
    knut_raw = waluta_dict["knut"]
    # Ilość knutów po odjęciu pełnych sykli
    knut = knut_raw % 21
    # Ilość sykli
    sykl_raw = waluta_dict["sykl"] + math.floor(knut_raw / 21)
    # Ilość sykli po odjęciu pełnych galeonów
    sykl = sykl_raw % 17
    # Ilość galeonów
    galeon = waluta_dict["galeon"] + math.floor(sykl_raw / 17)

    response_list = []

    # Wypisz galeony jeśli istnieją
    if galeon != 0:
        response_list.append(f"{galeon} galeon")
    # Wypisz sykle jeśli istnieją
    if sykl != 0:
        response_list.append(f"{sykl} sykl")
    # Wypisz knuty jeśli istnieją
    if knut != 0:
        response_list.append(f"{knut} knut")
    # Zamień listę wiadomości na tekst z spacjami
    response = ' '.join(response_list)

    return response


def wyslij_sowy(adresat, tresc_wiadomosci):
    # Implementacja funkcji wysyłającej sowy
    pass


def poczta_wyslij_sowy(sciezka_csv):
    # Wczytanie danych z pliku CSV
    df = pd.read_csv(sciezka_csv)

    # Iteracja po każdym wierszu w ramce danych
    for index, row in df.iterrows():
        adresat = row['adresat']
        tresc_wiadomosci = row['treść wiadomości']
        koszt_przesylki = row['koszt przesyłki']
        potwierdzenie_odbioru = row['potwierdzenie odbioru']

        # Wysyłanie sowy
        sowa_doleciala = wyslij_sowy(adresat, tresc_wiadomosci)

        # Obliczanie rzeczywistego kosztu
        if sowa_doleciala:
            rzeczywisty_koszt = koszt_przesylki
        else:
            if potwierdzenie_odbioru == 'TAK':
                rzeczywisty_koszt = 0
            else:
                rzeczywisty_koszt = koszt_przesylki

        # Aktualizacja danych w ramce danych
        df.at[index, 'rzeczywisty koszt'] = rzeczywisty_koszt

    # Zapisanie danych do nowego pliku CSV
    output_filename = f"output_sowy_z_poczty_{pd.Timestamp.now().strftime('%d_%m_%Y')}.csv"
    df.to_csv(output_filename, index=False)


