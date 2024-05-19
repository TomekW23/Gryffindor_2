import csv

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

# Przykładowe użycie funkcji nadaj_sowe
nadaj_sowe("Jan Kowalski", "Przykładowa wiadomość", True, "krajowa", "paczka", "nie dotyczy")