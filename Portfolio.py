from datetime import date

class Portfolio:
    listPortfolio = []

    def printOverview(self):
        print("""
      #########
      Portfolio
      #############################
      ÜBERSICHT Portfolio
      Datum: {datum}
      #############################
      -----------------------------
      - Wert Portfolio: xxx
      - seit Beginn   : xxx
      - Aktie: xxx
      - Aktie: xxx
      - Aktie: xxx
      -----------------------------""".format(datum=date.today()))