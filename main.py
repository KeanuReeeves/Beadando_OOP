class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class Egyagyasszoba(Szoba):
    def __init__(self):
        self.ar = 10
        self.szobaszam = 1

class Ketagyasszoba(Szoba):
    def __init__(self):
        self.ar = 20
        self.szobaszam = 2

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

class Foglalas:
    def __init__(self):
