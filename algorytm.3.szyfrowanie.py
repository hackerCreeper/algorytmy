def szyfruj_XOR(klucz, tekst_jawny, kierunek):
    klucz_liczba = ord(klucz)

    if (kierunek > 0):
        x = 33

        tekst_jawny_liczba = ord(tekst_jawny)
        wynik =  (klucz_liczba ^ tekst_jawny_liczba) + x
    else:
        x = -33
        tekst_jawny_liczba = ord(tekst_jawny) + x
        wynik = (klucz_liczba ^ tekst_jawny_liczba)

    wynik = chr(wynik)
    return wynik

def szyfruj_tekst_jawny(klucz, tekst_jawny ,kierunek):
    i=0
    j=0
    wynik = ""

    while i < len(tekst_jawny):
        wynik += szyfruj_XOR(klucz[j], tekst_jawny[i], kierunek)
        j += 1
        i += 1

        if(j >= len(klucz)):
            j=0

    return wynik

klucz = input("Podaj klucz: ")
tekst_jawny = input("Podaj tekst jawny: ")
kierunek = input("Podaj kierunek: ")
print(szyfruj_tekst_jawny(klucz, tekst_jawny, int(kierunek)))