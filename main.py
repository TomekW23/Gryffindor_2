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


# Przykładowe wywołanie funkcji z opcją specjalną wyjec
koszt = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec')
print(koszt)

# Przykładowe wywołanie funkcji bez opcji specjalnej
koszt_bez_specjalnej = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list')
print(koszt_bez_specjalnej)
