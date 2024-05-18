def waluta_str_na_dict(waluta_str: str) -> dict:
    ciag = waluta_str.split(" ")
    
    galeon = 0
    sykl = 0
    knut = 0

    for element_index in range(len(ciag)):
        # Sprawdź czy element to galeon jesli tak to poprzedni element jest wartością galeonu
        if ciag[element_index].startswith("g"):
            galeon = int(ciag[element_index-1])
            continue
        # Sprawdź czy element to sykl jesli tak to poprzedni element jest wartością sykla
        if ciag[element_index].startswith("s"):
            sykl = int(ciag[element_index-1])
            continue
        # Sprawdź czy element to knut jesli tak to poprzedni element jest wartością knuta
        if ciag[element_index].startswith("k"):
            knut = int(ciag[element_index-1])
            continue

    return {"galeon": galeon, "sykl": sykl, "knut": knut}

# Przykład wywołania z samymi knutami
print(waluta_str_na_dict("13 knut"))

# Przykład wywołania z wszystkimi monetami
print(waluta_str_na_dict("17 galeon 2 sykl 13 knut"))
