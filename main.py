import time
import random

adresat = input("Podaj adresata listu:")
tresc = input("Podaj treść listu:")
def wyslij_sowe(adresat, tresc_listu):

    print(f"Wysyłam sowe do {adresat} z treścią: {tresc_listu}")
    time.sleep(1)
    return random.choices([True, False], weights=(90, 10), k=1)[0]

wysylam_list = wyslij_sowe(adresat, tresc)

if wysylam_list:
    print("Sowa została pomyślnie wysłana!")
else:
    print("Wysłanie sowy nie powiodło się.")
