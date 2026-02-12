def sprawdz_czy_pierwsza(x):
    if (x == 1):
        return False
    else:
        if (x == 2):
            return True
        else:
            for i in range(2, x):
                if x % i == 0:
                    return False
                    break
            else:
                return True


def liczby_pierwsze(zakres):
    for i in range(1, zakres):
        if sprawdz_czy_pierwsza(i):
            print(i)


def szyfr_cezara (tekst_jawny, liczba):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    wynik = ""


    for i in range(0, len(tekst_jawny)):
        litera = tekst_jawny[i]
        pozycja_litery = alfabet.index(litera)
        pozycja = pozycja_litery + liczba

        if pozycja >= len(alfabet):
            pozycja = pozycja - len(alfabet)
        wynik = wynik + alfabet[pozycja]

    return wynik

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















































