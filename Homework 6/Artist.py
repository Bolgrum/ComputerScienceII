class Artist:

    def __init__(self, name='None', birthYear=0, deathYear=0):
        self.name = name
        self.birthYear = birthYear
        self.deathYear = deathYear

    def printInfo(self):
        if self.deathYear == -1:
            print(f'Artist: {self.name}, born {self.birthYear}')
        else:
            print(f'Artist: {self.name} ({self.birthYear}-{self.deathYear})')