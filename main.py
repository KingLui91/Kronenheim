from Aktie import Aktie
from Börse import Börse
from Player import Player
from Portfolio import Portfolio
from Story import Story
import time

aktie = Aktie()
börse = Börse()
player = Player()
portfolio = Portfolio()
story = Story()

class Game:

    capital = 10000
    portfolio = 0
    roundLimit = 10
    roundCounter = 0
    title = "Kronenheim"
    user = ""
    zielvermögen = 1000000

    def userOrder(self):

        user = input(": ")

        if user == "__help":
            print("""
      #############################
      LISTE ALLER BEFHLE
      #############################
      -----------------------------
      - __help: Aufruf der Befehlsliste
      - __setCap: Festlegen des Kapitalwerts
      -----------------------------
      """)

        if user == "__setCap":
            print("Kapital: ")

        input("[ENTER]")

    def settings(self):
        print("""
  #############################
  SETTINGS
  #############################
  ----------------------------------
  - Startkapital: {STARTCAPITAL} Sig
  - Zielvermögen: {ZIELVERMÖGEN} Sig
  - Anzahl der Runden: {ROUNDLIMIT}
  -----------------------------------
  """.format(STARTCAPITAL=self.capital, ROUNDLIMIT=self.roundLimit, ZIELVERMÖGEN=self.zielvermögen))

    def showBörse(self):
        börse.printDailyOverview()

    def showGameTitle(self):
        print("""
        ██╗  ██╗██████╗  ██████╗ ███╗   ██╗███████╗███╗   ██╗██╗  ██╗███████╗██╗███╗   ███╗
        ██║ ██╔╝██╔══██╗██╔═══██╗████╗  ██║██╔════╝████╗  ██║██║  ██║██╔════╝██║████╗ ████║
        █████╔╝ ██████╔╝██║   ██║██╔██╗ ██║█████╗  ██╔██╗ ██║███████║█████╗  ██║██╔████╔██║
        ██╔═██╗ ██╔══██╗██║   ██║██║╚██╗██║██╔══╝  ██║╚██╗██║██╔══██║██╔══╝  ██║██║╚██╔╝██║
        ██║  ██╗██║  ██║╚██████╔╝██║ ╚████║███████╗██║ ╚████║██║  ██║███████╗██║██║ ╚═╝ ██║
        ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝     ╚═╝
        """)

    def startGame(self):

        self.showGameTitle()

        time.sleep(3)

        story.textDiscripWorld()
        story.choose_3option("aaa","awd","wwww")

        input("[ENTER]")

        story.tellLegend()

        player.__str__()

        input("[ENTER]")

        story.textDiscripCity()

        input("[ENTER]")

        print("")

##################################
game = Game()
game.startGame()
input("[ENTER]")
