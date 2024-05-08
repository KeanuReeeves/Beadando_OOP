class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class Egyagyasszoba(Szoba):
    def __init__(self):
        self.ar = 10
        self.szobaszam = 1

