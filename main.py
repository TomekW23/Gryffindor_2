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

# Przykładowe wejście
wejscie = {
    "geleon": [1, 3, 5],
    "sykl": [18, 20, 10],
    "knut": [30, 40, 7]
}

# Wyświetlanie wyniku
print(licz_sume(wejscie))