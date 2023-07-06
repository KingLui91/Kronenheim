class Story:
    def choose_3option(self, text1, text2, text3):
        print("""
    CHOOSE A: {option_a}
    CHOOSE B: {option_b}
    CHOOSE C: {option_c}
    """.format(option_a=text1, option_b=text2, option_c=text3))

        user = input("ENTER: ")
        print(" ")
        if user == "A":
            print("Story for option A")
        elif user == "B":
            print("Story for option B")
        elif user == "C":
            print("Story for option C")
        else:
            print("input was not correct")
            self.choose_3option(text1, text2, text3)

    def choose_2option(self, text1, text2):
        print("""
    CHOOSE A: {option_a}
    CHOOSE B: {option_b}
    """.format(option_a=text1, option_b=text2))

        user = input("ENTER: ")
        print(" ")
        if user == "A":
            print("Story for option A")
        elif user == "B":
            print("Story for option B")
        else:
            print("input was not correct")
            self.choose_2option(text1, text2)

    def textDiscripWorld(self):
        print(
            """In der fantastischen Welt von Warhammer Age of Sigmar, fernab von den Schlachtfeldern und epischen Kriegen, gibt es auch Platz für Unternehmer und Geschäftsleute, die nach Erfolg und Reichtum streben. Einer dieser ehrgeizigen Unternehmer ist Gregor Eisenhand, ein zwergischer Kaufmann und Tüftler.""")
    def textDiscripCity(self):
        print("""
In den Ländern der Sterblichen gibt es eine prächtige Reichsstadt namens Kronenheim. Kronenheim liegt im Herzen des Reiches der Sterne und ist ein pulsierendes Zentrum des Handels, der Kultur und des Wohlstands.
Als Gregor nach langer Reise über den Kamm eines Hügels vor der Stadt schreitet, breitet sich vor ihm dieses Juwel von einer Stadt aus.
Sie erstreckt sich entlang der Ufer eines majestätischen Flusses, der von kristallklarem Wasser gespeist wird. Die Architektur von Kronenheim ist eine harmonische Verschmelzung aus verschiedenen Kulturen und Rassen. Hohe, elegante Türme der Aelfen erheben sich neben massiven, von Duardin errichteten Steinmauern, während prachtvolle Gärten der Sylvaneth die Straßen der Stadt schmücken. Magie durchzieht die Luft und lässt Laternen in den Straßen schweben und bunte Leuchten über den Kanälen tanzen.
Die Straßen von Kronenheim sind belebt und voller geschäftiger Menschen. Hier, so sagte man ihm schon als kleiner Zwergenbengel, treffen Händler aus allen Ecken der Reiche aufeinander, um ihre Waren zu präsentieren. Marktplätze sind gefüllt mit exotischen Gewürzen, kostbaren Edelsteinen, kunstvollen Waffen und feinsten Stoffen. In den Werkstätten und Manufakturen der Stadt werden kunstvolle Rüstungen geschmiedet, Zauberstäbe geschnitzt und prächtige Gemälde gemalt.
Das Zentrum der Stadt bildet der prächtige Handelspalast, in dem die wohlhabendsten Kaufleute, darunter auch Gregor Eisenhand, ihre Geschäfte tätigen. Hier finden Verhandlungen statt, Handelsabkommen werden geschlossen und neue Partnerschaften werden geschmiedet. Der Handelspalast selbst ist ein architektonisches Meisterwerk, mit mächtigen Säulen, kunstvollen Schnitzereien und riesigen gläsernen Kuppeln, die den Himmel über Kronenheim enthüllen.
Die Stadtwache von Kronenheim sorgt für Recht und Ordnung, um den friedlichen Handel zu gewährleisten. Die Wachen tragen prächtige Rüstungen und sind bekannt für ihre Loyalität und Tapferkeit. Sie patrouillieren durch die Straßen und überwachen den sicheren Transport von Waren und Reisenden.
Kronenheim ist auch ein Zentrum der Bildung und des Wissens. Die Große Bibliothek beherbergt eine unermessliche Sammlung von alten Schriften, magischen Grimoires und historischen Aufzeichnungen. Hier kommen Gelehrte, Magier und Geschichtenerzähler zusammen, um ihr Wissen zu teilen und neue Erkenntnisse zu erlangen.
Inmitten dieses prachtvollen Umfelds von Handel, Kultur und Wissen möchte Gregor Eisenhand leben und seine Zukunft gestalten.

"Ahhh, Kronenheim.", sagt er laut zu sich selbst. "Hier werde ich mein Ziel verfolgen einer der angesehensten Kaufleute in den Reichen der Steblichen zu werden. Mit scharfen Verstand, Geschäftstüchtigkeit und unbändigen Unternehmergeist wird mir das gelingen." sagte Georg aus tiefster Überzeugung. "...Oder mich soll der Blitz beim Scheisen treffen", murmelt er und begibt sich auf den Pfad den Hügel hinab in Richtung Stadt.

""")

    def tellLegend(self):
        print("""
Mit einem bescheidenen Startkapital von 10 Sigmarit hatte Gregor Eisenhand ein ehrgeiziges Ziel vor Augen: den Aufbau eines blühenden Handelsimperiums, das in der gesamten Reichsstadt verbreitet ist. Mit geschicktem Geschäftssinn und einem Auge für profitables Wachstum begab er sich auf seine Reise, um sein Vermögen zu vermehren.
In den ersten Jahren investierte Gregor klug in verschiedene Handelsunternehmen und Werkstätten. Er erkannte das Potenzial der aufstrebenden Rassen und beteiligte sich an den Produktionen der Aelfen, die filigrane Kunstgegenstände herstellten, sowie an den gewaltigen Schmieden der Duardin(Zwerge), die mächtige Waffen und Rüstungen produzierten. Durch geschickte Verhandlungen und Beziehungen mit den verschiedenen Fraktionen gelang es Gregor, sich Zugang zu exklusiven Märkten und lukrativen Handelsverträgen zu verschaffen.
Mit dem Fortschreiten der Jahre diversifizierte Gregor seine Investitionen. Er eröffnete Gasthäuser, in denen sich tapfere Krieger nach ihren Schlachten erholen konnten, und gründete eine Reederei, um Handelsrouten auf den mystischen Flüssen und Kanälen der Reiche zu erschließen. Zudem unterstützte er talentierte Magier und Alchemisten, die seltene Zaubertränke und magische Artefakte herstellten.
Jede Runde brachte neue Herausforderungen und Chancen. Gregor musste kluge Entscheidungen treffen, um sein Vermögen zu schützen und zu vermehren. Er investierte in Verteidigungsmaßnahmen, um seine Geschäfte vor rivalisierenden Unternehmern und feindlichen Überfällen zu schützen. Zudem schloss er Bündnisse und Handelsabkommen, um seine Marktstellung zu festigen und neue Absatzmärkte zu erschließen.
Nach 10 langen Runden hatte Gregor Eisenhand sein Zielvermögen erreicht. Sein Handelsimperium erstreckte sich über mehrere Städte, und sein Name war in der gesamten Welt von Warhammer Age of Sigmar bekannt. Er hatte nicht nur Reichtum erlangt, sondern auch Anerkennung und Respekt für seine geschäftlichen Fähigkeiten.
Gregor Eisenhand wurde zu einer Legende in der Unternehmerwelt von Age of Sigmar, eine inspirierende Figur für aufstrebende Geschäftsleute und ein Beweis für die Macht von Vision, Durchhaltevermögen und klugem Investieren. Seine Geschichte erinnert daran, dass selbst inmitten von Kriegen und epischen Schlachten Raum für Wachstum und Erfolg besteht, und dass wahre Helden nicht nur auf dem Schlachtfeld zu finden sind, sondern auch in den Hand

Dies ist sine Geschichte.
""")
