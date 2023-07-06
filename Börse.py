import terminaltables
class Börse:
    
    gelisteteAktien = []

    def addAktie(self, object):
        self.gelisteteAktien.append(object.__str__())

    def __str__(self):
        data = [
            ["Heading 1 ", "Heading 2"],
            ["Data", "Data"],
            ["Data", "Data"],
            ["Data", "Data"],
            ]
        table = terminaltables.AsciiTable(data,title="BÖRSE AKTUELL")
        print(table.table)
