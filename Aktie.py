class Aktie:
    name = ""
    aktuellerWert = 0

    def getName(self):
        return self.name

    def setAktuellerWert(self, value):
        self.aktuellerWert = value
    def getAktuellerWert(self):
        return self.aktuellerWert

    def __int__(self, name, aktuellerWert):
        self.name = name
        self.aktuellerWert = aktuellerWert
