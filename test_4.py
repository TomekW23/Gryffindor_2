print("hello")
from main import wybierz_sowe_zwroc_koszt
from main import wybierz_sowe_zwroc_koszt
from main import wybierz_sowe_zwroc_koszt
def test_wybierz_sowe_zwroc_koszt():
    # Testowanie przypadku gdy odległość jest lokalna, typ to list, potwierdzenie_odbioru jest True, a nie ma opcji specjalnej
    wynik_1 = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list')
    oczekiwany_wynik_1 = {'galeon': 0, 'sykl': 0, 'knut': 9}  # Oczekiwany koszt: 9 knutów (7 za potwierdzenie odbioru + 2 za list lokalny)
    assert wynik_1 == oczekiwany_wynik_1

    # Testowanie przypadku gdy odległość jest krajowa, typ to paczka, potwierdzenie_odbioru jest False, a nie ma opcji specjalnej
    wynik_2 = wybierz_sowe_zwroc_koszt(False, 'krajowa', 'paczka')
    oczekiwany_wynik_2 = {'galeon': 0, 'sykl': 2, 'knut': 1}  # Oczekiwany koszt: 2 sykle + 1 knut (dla paczki krajowej)
    assert wynik_2 == oczekiwany_wynik_2

    # Testowanie przypadku gdy odległość jest dalekobieżna, typ to list, potwierdzenie_odbioru jest True, a opcja specjalna to 'wyjec'
    wynik_3 = wybierz_sowe_zwroc_koszt(True, 'dalekobiezna', 'list', 'wyjec')
    oczekiwany_wynik_3 = {'galeon': 0, 'sykl': 2, 'knut': 11}  # Oczekiwany koszt: 2 sykle + 11 knutów (7 za potwierdzenie odbioru + 4 za opcję specjalną 'wyjec')
    assert wynik_3 == oczekiwany_wynik_3

    # Dodatkowy test na podstawie Twojego przykładowego wywołania funkcji
    wynik_4 = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'list gończy')
    oczekiwany_wynik_4 = {'galeon': 0, 'sykl': 0, 'knut': 16}  # Oczekiwany koszt: 16 knutów (7 za potwierdzenie odbioru + 2 za list lokalny + 1 za opcję specjalną 'list gończy')
    print("Otrzymany wynik:", wynik_4)
    print("Oczekiwany wynik:", oczekiwany_wynik_4)
    assert wynik_4 == oczekiwany_wynik_4

if __name__ == "__main__":
    test_wybierz_sowe_zwroc_koszt()


