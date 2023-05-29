class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickless, {self.knuts} knuts"

    def __add__(self, other):  # Metodo que permite Overload operator
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 20, 25)
print(potter)
wesley = Vault(25, 20, 100)
print(potter)
total = potter + wesley
print(total)
