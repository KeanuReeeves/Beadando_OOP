from datetime import datetime, timedelta

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class Egyagyasszoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(5800, szobaszam)

class Ketagyasszoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(8000, szobaszam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_letrehoz(self, szoba):
        self.szobak.append(szoba)

    def foglalas_felvetel(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                if datum > datetime.now():
                    if len(self.foglalasok) > 0:
                        for foofoglalas in self.foglalasok:
                            if (foofoglalas.datum != foglalas.datum):
                                self.foglalasok.append(foglalas)
                                return szoba.ar
                            else:
                                return "Erre az időpontra már van foglalás"
                    else:
                        self.foglalasok.append(foglalas)
                        return szoba.ar
                else:
                    return "Csak jövőbeli dátumot adhatsz meg"
            else:
                return "Nincs ilyen szoba"

    def foglalas_lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return True
        else:
            return False

    def listaz_foglalasok(self):
        for foglalas in self.foglalasok:
            print(f'Szobaszám: {foglalas.szoba.szobaszam}, Ár: {foglalas.szoba.ar}, Foglalás Dátuma: {foglalas.datum}')

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

def feltolt_szalloda(szalloda):
    szalloda.szoba_letrehoz(Egyagyasszoba(101))
    szalloda.szoba_letrehoz(Ketagyasszoba(102))
    szalloda.szoba_letrehoz(Egyagyasszoba(103))

    szalloda.foglalas_felvetel(101, datetime.now() + timedelta(days=1))
    szalloda.foglalas_felvetel(102, datetime.now() + timedelta(days=2))
    szalloda.foglalas_felvetel(103, datetime.now() + timedelta(days=3))
    szalloda.foglalas_felvetel(101, datetime.now() + timedelta(days=4))
    szalloda.foglalas_felvetel(102, datetime.now() + timedelta(days=5))

def main():
    szalloda = Szalloda("Szalloda")
    feltolt_szalloda(szalloda)

    while True:
        print("\nMit akarsz csinálni?")
        print("1. Szoba foglalás")
        print("2. Foglalás törlés")
        print("3. Foglalások listázája")
        print("4. Kilépés")

        valasztas = input("Választás: ")

        if valasztas == "1":
            szobaszam = int(input("Add meg a szobaszámot: "))
            datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            ar = szalloda.foglalas_felvetel(szobaszam, datum)
            if isinstance(ar, int):
                print(f"A foglalás sikeres, ára: {ar}")
            else:
                print(ar)

        elif valasztas == "2":
            print("Kérem, adja meg a foglalás adatait:")
            szobaszam = int(input("Szobaszám: "))
            datum_str = input("Dátum (YYYY-MM-DD formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            foglalas = None
            for f in szalloda.foglalasok:
                if f.szoba.szobaszam == szobaszam and f.datum == datum:
                    foglalas = f
                    break
            if foglalas:
                szalloda.foglalas_lemondas(foglalas)
                print("A foglalás törölve.")
            else:
                print("Nem található ilyen foglalás.")

        elif valasztas == "3":
            szalloda.listaz_foglalasok()

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()