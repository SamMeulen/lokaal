class Lokaal:
    cursistlist = []

    def __init__(self, nummer, trainer):
        self.nummer = nummer
        self.trainer = trainer

    def cusist_toevoegen(self, cursist):
        self.cursistlist.append(cursist)

    def print_info(self):
        print(str(self.nummer) + " " + self.trainer.voornaam + " " + self.trainer.familienaam)
        print(str(len(self.cursistlist)) + " cursisten:")

        for cursist in self.cursistlist:
            print(cursist.voornaam + " " + cursist.familienaam + " volgt " + cursist.trajekt.naam)
