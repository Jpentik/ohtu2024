class IntJoukko:
    oletuskapasiteetti = 5
    oletuskasvatus = 5

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if isinstance(kapasiteetti, int) and kapasiteetti > 0:
            self.kapasiteetti = kapasiteetti
        else: self.kapasiteetti = self.oletuskapasiteetti
        if isinstance(kasvatuskoko, int) and kasvatuskoko > 0:
            self.kasvatuskoko = kasvatuskoko 
        else: self.kasvatuskoko = self.oletuskasvatus
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def _kasvatus(self):
        uusi_kapasiteetti = len(self.lukujono) + self.kasvatuskoko
        uusi_lukujono = [0] * uusi_kapasiteetti
        for i in range(self.alkioiden_lkm):
            uusi_lukujono[i] = self.lukujono[i]
        self.lukujono = uusi_lukujono

    def kuuluu(self, luku):
        return luku in self.lukujono[:self.alkioiden_lkm]

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            if self.alkioiden_lkm >= len(self.lukujono):
                self._kasvatus()
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1
            return True
        return False

    def poista(self, luku):
        for i in range(self.alkioiden_lkm):
            if self.lukujono[i] == luku:
                self._siirra_alkiot(i)
                self.alkioiden_lkm -= 1
                return True
        return False

    def _siirra_alkiot(self, kohta):
        for i in range(kohta, self.alkioiden_lkm - 1):
            self.lukujono[i] = self.lukujono[i + 1]
        self.lukujono[self.alkioiden_lkm - 1] = 0

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm]
    
    def mahtavuus(self):
        return self.alkioiden_lkm

    def __str__(self):
        return "{" + ", ".join(str(self.lukujono[i]) for i in range(self.alkioiden_lkm)) + "}"

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        for luku in a.to_int_list() + b.to_int_list():
            yhdiste.lisaa(luku)
        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        for luku in a.to_int_list():
            if luku in b.to_int_list():
                leikkaus.lisaa(luku)
        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        for luku in a.to_int_list():
            if luku not in b.to_int_list():
                erotus.lisaa(luku)
        return erotus