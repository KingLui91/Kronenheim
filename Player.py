import terminaltables

class Player:

    name = "Gregor Eisenhand"
    sigmari = 10
    inventar = []

    def __str__(self):
        data = [
            ["CHARACTERBESCHREIBUNG", " "],
            ["Name: ", self.name],
            ["Sigmarit: ", self.sigmari],
            ["Inventar: ", str(len(self.inventar))+"/10"],
            ]
        table = terminaltables.AsciiTable(data, title="SPIELER")
        print(table.table)