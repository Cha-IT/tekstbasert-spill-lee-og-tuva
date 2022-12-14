import random as rd
import time

for i in range(100): #skriver ut 100 tomme linjer for å "rengjøre" terminalen før spilleren enten spiller for første gang eller spiller på nytt
    print()

tilstander = { #en ordbok med tilstander som kan endres til "True" basert på hva spilleren gjør
#bruker en ordbok for disse tilstandene fordi det gjør det lettere å endre de nødvendige variablene på en generell måte i med klassene
    "rickern": False,
    "snudd": False,
    "høyre":False, 
    "forlovet": False,
    "morder": False,
    "høy": False, 
    "venstre":False,
    "ekkorn": False,
    "kvalm": False
}

spiller = { #lager en liten ordbok for informasjon om spilleren, ettersom det kun er to viktige ting man trenger å lagre om spilleren: navn og HP
    "Navn": "Bob Kåre", #middlertidig navn som endres i neste linje
#bruker en placeholder fremfor å legge den inn senere kun fordi det ser bedre ut. Jeg vet at det kommer til å legges til autmoatisk i linjen som tar inn input, dette er kun for estetisk skyld
    "HP": 20 #lagrer HP-en til spilleren, som kun skal endres basert på events senere i spillet
}

def endreHP(val:int): #en funksjon som tar inn en verdi og endrer HP-en til spilleren med den verdien, slik at vi kan lage standard-metoder for alle eventene og fortsatt endre på spillerens HP
    """
    En funksjon som tar inn en verdi og endrer spillerens HP med den verdien

    Parameter:
    val (int) = et positivt eller negativt tall spillerens HP sakl endres med
    """
    newHP = spiller["HP"] + val
    spiller["HP"] = newHP

def endreTilstand(type:str): #en funksjon som tar inn en type tilstand som skal endres og endrer den til True, slik at vi kan lage standard-metoder for alle eventene og fortsatt endre på tilstander
    """
    En funksjon som tar inn typen tilstand som skal endres og endrer den tilstanden slik at den er True

    Parameter:
    type (str) = hvilken nøkkel i ordboken "tilstander" som skal endre verdien sin til True
    """
    tilstander[type] = True

def trengerHjelp():
    """
    En funksjon som kan gi spilleren informasjon om deres hp-tistand og deres andre tilstander
    Denne funksjonen tar ikke inn noen parametere
    """
    print(""" 

        Du spørr om hjelp!
            Om spillet:
                Du får et spørsmål der du får noen valgmuligheter, og skriver tallet
                som korrensponderer med det valget du vil ta
        Du kan også sjekke HP-tilstanden din ved å skrive:
            HP
        Du kan også sjekke om du har noen andre tilstander/virkninger på deg ved å skrive:
            Tilstander
        Du kan fortsette spillet ved å skrive inn:
            Cont
        
        Håper du fikk nytte av dette! :)
                
    """)
    brukerSvar = input("    >")#gir brukeren muligheten til å skrive inn et input som vil la dem enten sjekke tilstander, HP, eller fortsette spillet
    while brukerSvar.lower()!="cont": #så lenge brukeren sier at hen IKKE vil fortsette spillet, skal hen få muligheten til å fortsette å skrive inn inputs som lar hen sjekke HP/tilstander
        if brukerSvar.lower() == "hp": #printer ut spillers HP hvis input=hp
            print(f"    >Du har {spiller['HP']}HP!")
        elif brukerSvar.lower() == "tilstander":
            brukertilstander = [] #lager en liste som skal ha alle tilstandene til brukeren og kan da brukes til å sjekke om spilleren ikke har noen tilstander
            for i in tilstander.keys(): #går gjennom alle mulige tilstander brukeren kan ha
                if tilstander[i]== True: #må først sjekke om brukeren faktisk har tilstanden
                    if  i=="høyre" or i=="venstre": #sjekker så om tilstanden er et retning, ettersom man ikke bare kan si "du er høyre/venstre"
                        print(f"    >Du gikk til {i}")
                    elif i == "ekkorn": #siden tilstanden "ekkorn" er den eneste tilstanden man bare ikke kan si "du er [tilstand]" når man har et ekorn, lager vi et spesialunntak for denne. "Du er ekkorn" er ikke ordentlig norsk, lizzom .
                        print("    >Du har et ekorn på skulderen!")
                    else: #hvis det er alle andre tilstanden enn ekorn-tilstanden, skriver vi ut et generelt output
                        print(f"    >Du er {i}")
                    brukertilstander.append(i) #legger til alle tilstandene til brukeren i listen
            if len(brukertilstander)==0: #sjekker om listen er tom, og sier ifra til brukeren hvis hen ikke har noen tilstander
                print("    >Du har ingen tilstander")
        else: #hvis brukeren ikke skriver inn et godkjent svar, skrives dette ut
            print("    >Husk å skrive 'cont' for å fortsette")
        brukerSvar = input("    >") #gir så brukeren muligheten til å sjekke et annen verdi eller avslutte hjelpemenyen og avslutte spillet
        


class singleEvents:

    """
    Klasse som lager interaksjoner der man får kun ett prompt
    """
    def __init__(self, beskrivelse:str, hvaSkjer:str, resultat:list) -> None:

        """
        Konstruktører:
        beskrivelse (str) = en beskrivelse av scenen
        hvaSkjer (str) = sier hva som skjer til spilleren og gir de ulike handlingene spilleren kan gjøre
        resultat (list) = en liste med de ulike resultatene basert på hva spilleren velger å gjøre
        """
        self.beskrivelse = beskrivelse
        self.hvaSkjer = hvaSkjer
        self.resultat = resultat
    
    def spillEvent(self):

        """
        En funksjon som iverksetter eventet som skal kjøres
        Tar automatisk inn variabelen "self", ettersom funksjonen er spesifikk for en klasse
        """
        print(self.beskrivelse) #printer først ut beskrivelsen for å forklare hva som skjer
        fortsett = True
        while fortsett:#bruker en while-løkke som slutter når spilleren skrier inn et gyldig input
            try: #bruker try- og except-blokker for å være sikker på at det ikke oppstår en error hvis spilleren ikke skriver inn et gyldig input
                print(self.hvaSkjer) #printer ut hva som skjer og hva spilleren har muligheten til å gjøre
                resultat = input("    >") #henter inn hvilken index resultatet skal komme fra og trekker fra 1 pga måten python bruker indekser på
                if resultat.lower() == "rick astley": #lite Easter Egg for alle events ;)
                    endreTilstand("rickern")
                else:
                    if resultat.lower() == "hjelp":
                        trengerHjelp()
                        print(self.hvaSkjer)
                        resultat = input("    >")
                    resultat = int(resultat)-1
                    if type(self.resultat[resultat]) == tuple: #sjekker om resultatet vi har fått er lagret i en tuple, ettersom dette betyr at noe skal endres
#grunnen til at vi skal bruke tupler på den måten vi gjør det på er fordi hvis funksjonen som skal endre på HP/en tilstand bare deklareres inni en tuple med resultatet, vil variabelen endres uansett om det er det valget spilleren tar.
#å sette enkle str eller int verdier som siste variabel i en tuple gjør det lettere å bare sjekke om resultatet først er en tuple, og så sjekke hva slags verdi som ligger sist i tuplen og endre det som skal endres
#hvis vi hadde trengt et event der både HP og en tilstand skal endres, kunne man løst dette ved å ha det siste elementet i tuplen være en tuple, og gjort det som en standard at tilstand ligger først og HP ligger sist (dette er også kjent som en "tutupplele")
                        if type(self.resultat[resultat][1]) == int: #sjekker om den siste verdien i tuplen er et tall, ettersom dette betyr at HP-en til spilleren skal endres
                            endreHP(self.resultat[resultat][1]) #endrer HP-en til spilleren med verdien som ligger sist i tuplen med en funksjon som ligger lengre oppe i koden
                        elif type(self.resultat[resultat][1]) == str: #sjekker om den siste verdien er en str, ettersom dette betyr at en tilstand på endres
                            endreTilstand(self.resultat[resultat][1])#endrer tilstanden som står bakerst i tuplen slik at den for den boolske verdien True
                        print(self.resultat[resultat][0])#printer ut teksten som står først i tuplen, som er det skriftlige resultatet spilleren skal få
                    else: #hvis resultatet ikke er en tuple, printer vi bare ut resultatet
                        print(self.resultat[resultat])
                    print()
                fortsett = False
            except:
                print(">Du kan kun skrive inn et gyldig tall... \n>La oss ta det fra toppen igjen...")



class multiEvents(singleEvents):
    """
    Klasse som lager interaksjoner der man får flere prompts
    """
    def __init__(self, beskrivelse: str, hvaSkjer: str, hvaSkjerTo: list, resultat: list) -> None:

        """
        Konstruktører:
        beskrivelse (str) = en beskrivelse av scenen
        hvaSkjer (str) = et prompt som presenterer den første valgmuligheten for spilleren og hva spilleren kan gjøre
        hvaSkjerTo (list) = en liste med hva som skjer videre etter valget spilleren tar i den første valgmuligheten
        resultat (list) = En dobbel liste som gir et resultat basert på hva spilleren velger å gjøre i de to ulike valgmulighetene
        """
        super().__init__(beskrivelse, hvaSkjer, resultat) #henter disse inn fra super-klassen
        self.hvaSkjerTo = hvaSkjerTo #deklarerer et atributt vi kun trenger for denne sub-klassen
    
    def spillEvent(self):

        """
        En funksjon som iverksetter eventet som skal kjøres
        Tar automatisk inn variabelen "self", ettersom funksjonen er spesifikk for en klasse
        """
        #denne metoden gjør egentlig mye av de samme som metoden i superklassen, men den har bare noen par ekstra ledd
        print(self.beskrivelse)
        fortsett = True
        while fortsett:
            try:  
                print(self.hvaSkjer)  
                forsteResultat = input("    >")
                if forsteResultat.lower() == "rick astley": #lite Easter Egg for alle events ;)
                    endreTilstand("rickern")
                    
                else:
                    if forsteResultat.lower() == "hjelp":
                        trengerHjelp()
                        print(self.hvaSkjer)
                        forsteResultat = input("    >")
                    forsteResultat = int(forsteResultat)-1
                    print(self.hvaSkjerTo[forsteResultat]) #siden vi ikke skal gi et resultat enda, printer vi nå ut hva som skjer basert på den forrige handlingen og gir spilleren nye valgmuligheter
                    andreResultat = input("    >")
                    if andreResultat.lower() == "rick astley": #lite Easter Egg for alle events ;)
                        endreTilstand("rickern")
                    else:
                        if andreResultat.lower() == "hjelp":
                            trengerHjelp()
                            print(self.hvaSkjer)
                            andreResultat = input("    >")
                        andreResultat = int(andreResultat)-1
                        if type(self.resultat[forsteResultat][andreResultat]) == tuple: 
                #tar samme skjekken for verdier som skal endres på samme måte som i super-klassen, men nå skjekker vi listen som ligger inni listen
                            if type(self.resultat[forsteResultat][andreResultat][1]) == int:
                                endreHP(self.resultat[forsteResultat][andreResultat][1])
                            elif type(self.resultat[forsteResultat][andreResultat][1]) == str:
                                endreTilstand(self.resultat[forsteResultat][andreResultat][1])
                            print(self.resultat[forsteResultat][andreResultat][0])
                        else:
                            print(self.resultat[forsteResultat][andreResultat])
                        print()
                fortsett = False
            except:
                print(">Du kan kun skrive inn et gyldig tall... \n>La oss ta det fra toppen igjen...")
 

#vil anbefale å ha Wordwrap på for dette med mindre du har lyst til å scrolle veldig langt bort for å lese all teksten
mainPathEvents = [
    singleEvents(
        ">Når du går videre inn i skogen, ser du at stien deler seg i to...", 
        ">Hva vil du gjøre? \n>1: Gå til venstre \n>2: Gå til høyre", 
        [
            (">Du fortsetter å gå inn i skogen, denne gangen til venstre...", "venstre"), 
            (">Du fortsetter inn i skogen, denne gangen til høyre...", "høyre")
        ]
    ),
    singleEvents(
        ">Du fortsetter inn i skogen \n>Å nei! Hva er dette?! \n>Et tre har falt ned på stien. Bak det falne treet er det en stor kampestein", 
        ">Det virker som noe stress å komme seg rundt alt dette. \n>Hva vil du gjøre?: \n>1: Gå rundt \n>2: Snu", 
        [
            ">Du gikk rundt hindringene. Du må være veldig glad i tobakk eller hva?", 
            (">Du snudde. Bestemora di er veldig skuffet over at dere ikke fikk dratt på harrytur til Sverige", "snudd")
        ]
    )
]

venstreEvents = [
    singleEvents(
        ">Du fortsetter ned den vakre stien. Du hører fuglesang og livet kjennes ganske herlig.", 
        ">Plutselig hører du noen merkelige lyder av stien... Hva vil du gjøre?\n>1: Fortsette nedover stien \n>2: Utforske den merkelige lyden...", 
        [
            ">Du fortsetter nedover stien, ingenting skjer...", 
            (">Gratulerer! Du fant en kake!\n>Du tar en bit av kaken. \n>Nam! \n>Du får 2hp", 2)
        ]
    ), 
    singleEvents(
        ">Du går gjennom skogen. Du hører små fotskritt i treet nært deg", 
        ">Det er et ekorn! Hva vil du gjøre?: \n>1: gi ekornet en eikenøtt \n>2: ignorere ekornet", 
        [
            (">Gratulerer! Du har fått en ny venn! \n>Du kaller han Todd :)", "ekkorn"), 
            (">Du ignorerte ekornet \n>Du ser at ekornet begynner å bli sur på deg \n>Kanskje du bare burde gitt det den eikenøtta... \n>Å nei! \n>Ekornet ble surt nok til å gå til angrep! \n>Du blir klort opp av ekornet og mister 5HP", -5)
        ]
    ),
    singleEvents(
        ">Du går nedover stien. Du begynner å se deg litt rundt og merker noen litt merkelige sopper.",
        ">Du kjenner du er litt sulten, kanskje de ikke er farlige? \n>Vil du spise soppen? \n>1: Ja \n>2: Nei",
        [
            (">Du spiser soppen. \n>Det var helt vanlig sopp, men den smakte litt muggen... \n>Du blir kvalm :(", "kvalm"),
            ">Du valgte å ikke spise soppen. Det var kanskje lurt, den luktet veldig vondt.... \n>Du fortsetter nedover den fine stien"
        ]
    ),
    multiEvents(
        ">Fuglene kvitrer rundt deg imens du fortsetter ned stien. \n>Solen glimter gjennom trærne og du føler deg varm på innsiden",
        ">Trærne fletter seg tettere sammen, og før du vet ordet av det, ser du en liten bjørn. Hva vil du gjøre? \n>1: Gå rundt babybjørnen og håpe at moren ikke ser deg \n>2: Se rundt deg og gå bort til bjørnen hvis moren ikke er her",
        [
            ">Du går forbi babybjørnen i en stor bue, slik at du ikke terger moren hvis den er i nærheten... \n>Det ser ut til å fungere! Babybjørnen ser rart på deg, men ingen moderbjørn kommer for å angripe. \n>Men å nei! Du gikk for langt ut fra stien og datt ned i en grop! \n>Hva vil du gjøre? \n>1: Prøve å klatre ut av den gjørmete gropen \n>2: Akseptere din skjebne og bare bli liggende", 
            ">Du ser deg godt om og klarer ikke å se mammabjørnen. \n>Sakte men sikkert går du opp til den og strekker ut hånden din... \n>BRØL! \n>Du så deg ikke godt nok for! Mammabjørnen kommer løpende mot deg! \n>Hva gjør du nå? \n>1: Legge deg ned i fosterstilling og begynn å sug på tomellen \n>2: Begynn å be \n>3: LØP!"
        ],
        [
            [
                ">Med gjørme under fingerneglene, klorer du deg opp fra hullet. \n>Så snart du er ute av hullet, tar du deg en liten pust i bakken, før du fortsetter videre på stien",
                (">Du legger deg ned i gjørma og godtar din skjebne... \n>Det begynner å regne... \n>Gjørma begynner å utvide seg, men du flytter deg ikke \n>Den er nesten høy nok til å dekke hele ansiktet ditt nå... \n>Nesen og munnen din er helt dekket av gjørme. Du klarer ikke å puste \n>Du kveles... sakte men sikkert... \n>Du slutter å puste", -20)
            ],
            [
                (">Du legger deg ned i fosterstilling og begynner å sutte på tommelen sin \n>Mammabjørnen stopper opp, hun synes at du ligner på ungen sin! \n>Hun gir deg noen blåbær hun egentlig hadde spart opp til å gå i dvale til vinteren. \n>Du spiser blåbærene, de smaker fantastisk! \n>Du får 2HP!", 2),
                (">Du legger deg ned på stien og begynner å be til hva enn du tror er der oppe \n>Mammabjørnen kommer rasende mot deg, dritsur fordi du våget å gå bort til ungen hennes. \n>Du klores opp, lem fra lem. \n>Men det ser ut til at det å be før du døde var en god idé! Du havner i himmelen! \n>I himmelen møter du bestemora di. Hun sier at du tok for lang tid til å kommer deg til huset hennes og at hun døde av abstinenser",-20),
                ">Kanskje det er adrenalinet, kanskje mammabjørnen har spist for mye i forbredelse til dvalen, men du klarer å løpe unna \n>Du slutter ikke å løpe før du er helt sikker på at mammabjørnen har sluttet å jage deg \n>Du fortsetter nedover stien, anpusten"
            ]
        ]
    )
]

hoyreEvents = [
    singleEvents(
        ">Du går nedover stien. \n>Trærne pakker seg tettere og tettere sammen, og du begynner å føle at noe er Galt. \n>Du kunne trengt litt glede akkurat nå...", 
        ">Mellom trærne kan du se noe metall som glimter. \n>Det er en gramofon! Det er en plate i den allerede.... \n>Spill av? \n>1: Ja \n>2: Nei", 
        [
            ("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⠀⠀
>En fantastisk lyd kommer ut av gramofonen. Det er Rick Astley! \n>Du får 2HP""", 2), 
        (">Du ignorerer gramfonen. \n>Å nei! Hva skjer? \n>Gramofonen ble for overopphetet og ekslpoderte! Du mister 5HP!", -5)
        ]
    ), 

    multiEvents(
        ">Imens du går gjennom skogen, begynner du å føle deg sulten. \n>Selv om du vet at det er god mat i Sverige, trenger du noe nå \n>Du fortsetter på stien, men holder et åpent øye for noe spiselig...", 
        ">Men hva er dette?\n>Litt borte fra stien ser du litt sopp. \n>Du mener å huske at du har sett noe lignende i en bok bestemoren din har om spiselig sopp. \n>Hva gjør du? \n>1: Går bort og spiser soppen \n>2: Fortsetter videre på stien", 
        [
            ">Etter du har spist soppen, innser du at synet ditt begynner å gå litt bananas. \n>Du har nettopp spist fleinsopp! Hva skal du gjøre? \n>1: Svelge soppen og bare la alt dette skje \n>2: Få deg selv til å kaste opp soppen", 
            ">Du fortsetter videre på stien... \n>Plutselig, ser du en stor, brun bjørn på stien foran deg! Hva skal du gjøre nå? \n>1:Klatre opp i det nærmeste treet og håpe at bjørnen ikke klatrer etter deg. \n>2: LØP! \n>3: Vel, du har alltid hatt lyst til å ha en slåsskamp med en bjørn..."
        ],
        [
            [
                (">Du svelger soppen og føler at den virkelig kicker inn. \n>Disse fargene er skikkkelig morsomme, ass...", "høy"),
                (">Du sliter litt i starten, men så snart du får fingeren langt nok bak i halsen kommer all soppen opp igjen \n>Synet ditt begynner sakte men sikkert å bli normalt igjen, men bare for å være sikker setter du deg inntil et tre og hviler litt. \n>Magesyren brenner i munnen din. Du mister 2HP", -2)
            ],
            [
                (">Du klatrer så høyt du klarer, men bjørnen følger like etter! \n>Heldigvis har bjørnen spist seg feit på laks fra en lokal elv, så den kommer seg ikke langt opp i treet, og gir seg etter en liten stund \n>Uheldigvis klarer den å komme seg høyt nok opp til å klore deg på beinet. Du mister 8HP", -8),
                ">Du vet ikke hvordan, men du klarer å løpe fra bjørnen! \n>Den feite bjørnen slutter å jage deg etterhvert, og når du er helt sikker på at den ikke følger etter deg, fortsetter du å gå nedover stien",
                (">Hverken du selv eller Gud vet hvorfor du slår til bjørnen, men du løper bort til den og slår den på snuten så hardt du kan \n>Den blir selvfølgelig sur, og biter deg så hardt den kan \n>Du faller ned, og lurer på hvor i livet det gikk så galt at du endte opp med å bli spist levende av en bjørn. \n>Etter den har fått med seg store deler av magen og armene dine, fortsetter bjørnen fornøyd videre i stien. \n>Du mister 19HP", -19)
            ]
        ]
    ),

    multiEvents(
        ">Fuglene kvitrer rundt deg, og solen skinner varmt på ditt kinn",
        ">Plutselig ser du en vakker dame gå på stien foran deg. \n>Hun snur seg og ser deg \n>Hun sakker ned, som om hun venter på deg. \n>Hva vil du gjøre? \n>1: Introduser deg selv (hølig), \n>2: Introduser deg selv (uhøflig) \n>3: Løfte en nærtliggende stein og kaste den på henne",
        [
            ">Hun hilser tilbake \n>Dere har en hyggelig samtale, og du føler virkelig at dere har en connection. \n>Du har aldri ledd like mye som du har med henne \n>Du har aldri følt deg like fortsått, like sett som du har med henne \n>Du vet at hvis du ikke sier noe, kommer du alltid til å tenke på hva du kunne gjort anderledes hvis du bare hadde sagt noe \n>Du har ikke lyst til å miste henne når stiene dere er på (i livet) deler seg \n>Hva vil du gjøre?\n>1: Kysse henne \n>2: Fri til henne \n>3: Ingenting.",
            ">Du går bort til henne og drar frem alle banneordene bestemora di noen gang har lært deg \n>Agnes, som du lærer at hun heter, finner sine ord og skjeller deg ut \n>Du har aldri møtt noen som henne \n>Hva vil du gjøre? \n>1: Fri til henne \n>2: Gå videre, \n>3:Equal rights, equal fights",
            ">Du holder øyekontakt imens du plukker opp steinen \n>Hun ser forvirret på deg imens du sikter \n>Du kaster den. \n>Hun faller ned på bakken \n>Hjernen tyter ut av en diger sprekk \n>Begge øya spretter ut \n>'Å nei' tenker Agnes \n>'Jeg ser ikke ut!' \n Blodet spruter på deg! \n\n>Hva gjør du nå? \n>1: Begrav kroppen \n>2: Spis henne \n>3: Forlat åstedet"
        ],
        [
            [
                (">Du jobber opp motet og kysser henne \n>Hun ser forskrekket på deg \n>Hun slår deg på kinnet, hardt \n>Du mister 12HP", -12),
                (">Selv om du ikke har noen ring, faller du ned på (ett) kne \n>Agnes, som du har lært at du heter, begynner å gråte \n>Hun sier 'Ja'", "forlovet"),
                ">Det begynner å bli sent, du vet at du må komme deg videre \n>Motvillig, sier dere hade \n>Du vet at du alltid kommer til å tenkte på hva som kunne vært \n>Men noen må dra først. Dette er en veldig gammel historie. Det finnes ingen annen versjon av denne historien \n>Du fortsetter å gå, du kan ikke se tilbake nå. \n>Ikke se tilbake \n>Aldri se tilbake \n\n>Du ser ikke tilbake\n\n>Hun er borte nå, du kan ikke gjøre noe med det\n>Du faller ned på stien, tårene nekter å komme \n>Du vet ikke hvor lenge du ligger der \n>Det føles ut som... \n>Du vet ikke hva det føles ut som... \n\n>Du reiser deg opp og fortsetter på stien"
            ],
            [
                (">Du er imponert av sarkasmen og kunnskapen hennes. \n>Du faller ned på kne \n>Agnes er ikke imponert, og slår til deg, hardt \n>Du mister 10HP", -10),
                ">Du innser at har bedre ting bruke tiden din på, og fortsetter nedover stien \n>Du slettet nettopp Twitter fordi du var lei av å argumentere med 14-åringer med minecraft-youtubere som profilbilde, så hvorfor skal du fortsette denne samtalen?",
                (">Du slår til Angnes, hun slår tilbake \n>Dere har en slåsskamp midt på stien. \n>Agnes er sterkere enn hun ser ut \n>Hun vinner, og river av et av ørene dine. \n>Du mister 14HP", -14)
            ],
            [
                ">Du begynner å grave et hull med hendene dine. \n>Jorden samler seg under fingerneglene dine \n>Det gjør vondt, men du fortsetter å grave. \n>Så snart hullet er dypt nok, dytter du kvinnen inn i hullet. \n>Du tetter hullet med jorden, og legger mose på toppen slik at ingen skal se Hva Som Er Der. \n>Du håper at ingen begynner å lete her \n>Du fortsetter nedover stien",
                (">Du begynner å spise de mest gjenkjennelige delene av kroppen hennes, så begynner du å spise lårene hennes. \n>På et tidspunkt klarer du ikke å spise mere, både fordi det er menneskekjøtt, og fordi du har spist for mye \n>Du gjemmer det du ikke klarer å spise i en lyng, og håper at dyrene i skogen finner henne før politiet gjør det", "morder"),
                (">Du forlater åstedet, alltid hjemsøkt av hva du har gjort. \n>Hvorfor gjorde du dette? \n>Hvorfor gjorde du dette?\n>Hvorfor gjorde du dette?\n>Hvorfor gjorde du dette?\n>Hvorfor gjorde du dette? \n\n>...\n>Du fortsetter nedover stien","morder")
            ]
        ]
    )
]

def velgerEvent(liste:list): #en felles funksjon for å velge inn ulike events
    """
    En funksjon som velger et tilfeldig event fra en liste

    Parameter:
    liste (list) = listen som et event skal hentes ut fra
    """
    valg = rd.randint(0, len(liste))-1 #velger eventet tilfeldig fordi det ville vært kjedelig hvis det alltid hadde kommet i en bestemt rekkefølge
    liste[valg].spillEvent()
    liste.pop(valg)

def spillIkkeOver():
    if len(hoyreEvents)!=0 and len(venstreEvents)!=0 and spiller["HP"]>0 and tilstander["snudd"] != True and tilstander["rickern"]== False: #skjekker om de ulike kriteriene for at spillet skal fortsette er oppfylt
        return True #hvis kriteriene er oppfylt, returnerer funksjonen "True" og spillet kommer til å fortsette
    else:
        return False #hvis alle kriteriene ikke er oppfylt, returnerer funksjonen "False", og spillet avsluttes, og man for den passende endingen

spiller["Navn"] = input("Hva heter du?: ") #lar spilleren velge sitt eget navn, som kommer til å ha en effekt på introen ol.

#printer ut introduksjonen til spilleren
print(f"""    >Hei, {spiller['Navn']}!

    >Velkommen til spillet vårt! 
    >Dette er et tekstbasert spill der du får noen valg. 
    >Du skriver inn tallet som passer til valget du vil ta
    >Det tror jeg du får til... 
    >Lykke til!
        
    >Du og din bestemor har planlagt en harrytur i lang tid.
    >Hun er desverre for gammel til å kjøre selv, men du har ikke en egen bil.
    >Du skal gjennom skogen for å komme til bestemoren din og kjøre hennes volvo 240 til Storlien
    >Desverre bor du på den andre siden av en skummel skog :(
    >Du må komme deg gjennom skogen og til bestemors hus
    >Du vil vel ikke gå glipp av en harrytur til Sverige, vil du det?

                    HVIS DU TRENGER HJELP
                        SKRIV "hjelp"

    >La oss begynne...

""")
time.sleep(10)#legger inn pauser i printingen slik at det blir mer brukervennlig og lettere å lese
print("""
    >INITIALISERER...
    
    >HENTER INN EVENTS...
    >GIR LAKS TIL BJØRNENE...
    >FINNER FLEINSOPP...
    >SPILLER AV GODE, GAMLE PLATER...
    >GIR EIKENØTTER TIL DYRELIVET...
    >MØTER GAMLE KJENNINGER PÅ STIEN""")
time.sleep(2)
print("""
    >INITIALISERING FULLFØRT""")
time.sleep(2)

print("""
>Du står på kanten av en stor, mørk skog
>Trærne virker høyere enn de vanligvis gjør
>Du vet at på andre siden av skogen venter det en artig tur og mye tobakk
>Selv om skogen virker større og mørkere nå enn den har gjort før, begynner du å gå inn
>Du har jo tross alt gått gjennom den tusen ganger før. Hvorfor skal denne gangen skille seg ut?
>Så snart du setter foten din på stien, vet du at det ikke er noen veg tilbake nå
""")
time.sleep(7)

while spillIkkeOver():
    #sjekker hvilken retning spilleren går i og gir et event fra den tilhørende listen
    if tilstander["høyre"] == True:
        velgerEvent(hoyreEvents)
    elif tilstander["venstre"] == True:
        velgerEvent(venstreEvents)
    else:
        velgerEvent(mainPathEvents)

#sjekker de ulike tilstandene spilleren muligens har endret på i løpet av spillet, og ser hvilken ending spilleren da får
if spiller["HP"]<=0:
    print(">GAME OVER \n>TRY AGAIN?")
elif tilstander["morder"] == True:
    print(f"""
    >Du kommer deg ut av skogen, men til hvilken pris?
    >Du har blod på hendene, på klærne dine. Du lukter helt forferdelig
    >Du hører sirener i bakgrunnen
    >Du møter blikket til bestemoren din
    >Hun vet
    >Hun vet hva du har gjort
    >Hun klarer ikke møte blikket ditt
    >Du faller ned på knærne dine og bare detter sammen
    >Hva har du gjort?
    >Politiet kommer og setter deg i håndjern
    >Du setter deg i bilden og ser ut vinduet
    >Bestemoren møter blikket ditt med tårer i fjeset
    >Du vil aldri kunne dra på en harrytur igjen...

    >GAME OVER
    >DU FIKK ENDING "MORDER"
    >10/11
    """)
elif tilstander["forlovet"] == True and tilstander["høy"] == True:
    print(f"""
    >Du og din kjære Agnes kommer dere endelig gjennom skogen!
    >Du går med litt ustødige skritt, kanskje den soppen ble for mye, men uansett!
    >Dere går nedover mot bestemoren din
    >Hun ser litt rart på Agnes, men dere tenker ikke noe over det...
    >Du er så lykkelig, men vet ikke om det er fleinen sin feil eller fordi du nettop er blitt forlovet?
    >Det har kanskje ikke noe å si
    >Agnes, du og bestemoren din setter dere i bilen og gjør dere klar for å kjøre
    >Du sitter selvfølgelig IKKE bak rattet
    >Det går noen timer
    >Og noen fler
    >Enda fler?
    >Bestemoren din er så fokusert på strikkingen hennes,
    >men du har lagt merke til at dette IKKE er veien til Storlien!
    >Du ser til Agnes
    >Hva?
    >Er det den samme personen?
    >Har jeg blitt lurt?
    >Du hadde kanskje glemt av din nåværende påvirkning...
    >Det er sikkert ikke noe farlig uansett
    >Du sovner
        ,men våkner aldri opp igjen...

    >GAME OVER
    >DU FIKK ENDING "HJERTESORG"
    >8/11
    """)

elif tilstander["ekkorn"]==True and tilstander["kvalm"]==True:
    print(f"""
    >Etter en lang, og slitsom, tur er du endelig kommet gjennom skogen!
    >Du ser at rett ned stien sitter bestemoren din i hagen sin i en god gammal gyngestol
    >"Du e så treig {spiller['Navn']}"
    >Plutselig kjenner du at det surrer i magen
    >Det er den rare ekle soppen du spiste!
    >Du kjenner at det kommer opp å whooooosshshhssh
    >Du spyr en stråle mot bakken
    >Så ute av ingenting hopper ekorn kameraten din av skulderen å begynner å spise oppkastetditt?
    >Du og bestemor synes dette er veldig ekkelt. Dere prøver å skynde dere inn i bilen
    
    >GAME OVER
    >DU FIKK ENDING "SKREKK OG GRU"
    >7/11
    """)
elif tilstander['forlovet'] == True:
    print(f"""
    >Du, og Agnes, kommer dere nedelig ut av skogen!
    >"Ka om vi bare gifte oss no?"
    >Agnes ser dypt inne i øynene dine
    >Du driter litt i bestemor nå!
    >Dere springer ned til bilen hennes og kjører av sted
    >Du vet om en liten kirke som kan vie dere IDAG
    >På veien dit tenker du litt på bestemoren din, hun sitter alene
    >Dere skulle jo egentlig til Storlien sammen?
    >Du velger å ikke tenke noe mer på det
    >Agnes går først ut av bilen, hun børster litt på håret
    >og rister av litt jord og møkk fra turen
    >Dette er drømmedama, tenker du
    >Dere er nå gift!
    >Du har en kone!
    >Dette hadde du ikke forventet
    >På veien hjem er hodet ditt helt tomt for tanker
    >Noen blikk sendes frem og tilbake mellom dere
    >Du kjører bilen inn til bestemoren din igjen
    >Det kommer en litt ekkel følelse i magen
    >Skyldfølelse?
    >Du er egentlig mer spent på å fortelle bestemoren din om alt som har hent,
        men
    >Dere ringer på, ikke noe svar
    >Agnes går rundt for å sjekke i hagen på andre siden
    >Du går inn
    >Plutselig!
    >Du hører et skrik fra Agnes og springer for å se hva som skjer
    >Der ligger bestemoren din død
    >Død på bakken
    >Senere blir det fastslått av legen at hun døde av abstinenser og hjertesorg
    >Hun hadde gledet seg så mye til å dra med barnebarnet hennes på tur
    >Bestemoren din har vært enke i mange år
    >Hun er mye alene, og hennes egne barn snakker nesten ikke med henne
    >Du er knust, Agnes prøver å trøste deg i flere uker, men det hjelper ikke mye
    >Din bestemor er nå dø.

    >GAME OVER
    >DU FIKK ENDING "FORLOVET"
    >6/11
    """)
elif tilstander["ekkorn"]==True:
    print(f"""
    >Etter en lang lang tur gjennom den skumle skogen, har du endelig kommet gjennom!
    >Du ser at lengre ned stien ut av skogen, sitter bestemoren din i en gammel gyngestol ihagen hennes.
    >"Du brukt jævli lang tid {spiller['Navn']}..."
    >Bestemoren din ser på skulderen din.
    >"E d ei rotte? Ta åsså sætt fra dæ den så fær vi"
    >Du merker at ditt ekorn-venn ikke var veldig glad i den kommentaren...
    >Plutselig! 
    >Ekornet angriper bestemoren din! Det er så blodig! 
    >Du klarer ikke se på. Du snur deg. 
    >Det blir stille igjen... 
    >Du snur deg tilbake, men du ser ikke bestemoren din lengre? Det er blod overalt og alt duser....
    >er ekornet som står på den blodige strikket-genseren til din avdøde bestemor...

    >GAME OVER
    >DU FIKK ENDING "EKORN"
    >5/11
    """)    
elif tilstander["høy"]==True:
    print(f"""
    >Etter en lang, og veldig merkelig tur...., kommer du endelig deg gjennom skogen!
    >Du ser deg rundt og finner bestemoren din
    >Hun sitter i en gammel gyngestol og holder på å sovne...
    >"Du brukt no ganske lang tid no da {spiller['Navn']}!"
    >Bestemoren stirrer deg opp og ned, hun merker det er noe rart ved deg?
    >"Kom no så går vi te bila"
    >Du er klar for å kjøre, noe som du virkelig ikke burde gjøre i din påvirkede tilstand, men
    >plutselig setter bestemoren din seg bak rattet?
    >Du setter deg i passasjer-setet og dovner litt bort..
    >Når du våkner sitter du fast?
    >Du ser deg rundt og kjenner igjen at du har havnet på st. olavs?
    >"D e for ditt eget bøeste..."
    >En tåre rinner ned det kalde kinnet til bestemoren din mens du blir trillet inn til
    >Rehab for rusmisbruk...
    
    >GAME OVER
    >DU FIKK ENDING "HØY"
    >4/11
    """)
elif tilstander["snudd"] == True:
    print(f"""
    >Du snudde
    >Du ORKER ikke å prøve å komme deg rundt alt dette
    >Du går tilbake stien du NETTOP startet på
    >Du drar hjem og legger deg ned og sover, som en lat fis
    >Neste dag våkner du til en telefon som ringer
    >Det er moren din, hun er på gråten?
    >Det viser seg at bestemoren din døde denne natten av tobakk abstinenser!
    
    >Om du bare hadde ORKET å dra rundt den kampesteinen og det treet
    >Da hadde hun kanskje overlevd...
    
    >GAME OVER 
    >DU FIKK ENDING "SNUR"
    >1/11
    """)
elif tilstander["kvalm"]==True:
    print(f"""
    >Endelig, etter mange timer, er du kommet gjennom skogen!
    >Du ser deg rundt og ser bestemoren din, hun gynger i den samme stolen som hun alltid gjør
    >Du kjenner noe uggent i magen?
    >Du ignorer det for nå og går til bestemoren din
    >Hun er glad for å se deg, selv om det ikke virker slik
    >"Prøv å bruk litt lenger tid neste gang da!"
    >Hun går rett til bilen og setter seg i passasjer-setet
    >Hun setter på p7 klem på radioen og finner fram strikketøyet sitt
    >Du setter deg i bilen og kjører ut innkjørselen
    >Dere kommer et stykke før du kjenner den uggne følelsen i magen din igjen..
    >Du kjenner at noe du spiste tidligere, virkelig har laget trøbbel i magen
    >Du blir kvalmere og kvalmerer mens dere kjører, men dere er på E6'n og kan ikke kjøre til side
    >Du prøver å holde kvalmen nede, men det finnes grenser!
    >Du klarer ikke holde det lengre, og det kommer overalt
    >På deg, på bestemoren din og på vinduet
    >Du klarer ikke se veien lengre og i en pannikk tilstand snurr du bare på rattet
    >Dere krasjer i en fjellvegg langs veien og det var det siste dere gjorde...
    
    >GAME OVER
    >DU FIKK ENDING "KVALM"
    >3/11
    """)
elif tilstander["rickern"] == True:
    print(f"""
    >Du roper ut etter Rick Astley
    >DU FÅR SVAR?
    >Du hører en fjern melodi som kommer nærmere og nærmere...
    >Rick flyr over deg!
    >Han svever ned og plukker deg opp
    >Han flyr deg over skogen og du ser alt det fæle som kunne ha skjedd
    >Etter bare noen minutter er du kommet over hele skogen
    >Rick setter deg forsiktig ned på bakken
    >I det dere lander får han og bestemoren din øyekontakt med en gang
    >Du kan nesten se hjertene i øynene deres...
    >Noen uker senere
    >Du er invitert til din bestemor og Rick Astleys bryllup
    >Du sitter på første rad, du ser venner og familie med tårer i øynene
    >"Do you , Rick Astley god amongst men, take Brunhilde as your lawfully wedded wife?"
    >"I do"
    >"And do you, Brunhilde Eriksen, take Rick Astley as your lawfully wedded husband?"
    >"I do"
    >"You may kiss the bride!"
    >Kirken dere er i bryter ut i sang!
    >For en lykkelig dag <3
    >Du hører en orgel versjon av "Never gonna' give you up" spiller mens de går ut av kirken
    >Dere levde lykkelig resten av deres dager
        
    >GAME OVER
    >DU FIKK ENDING "RICK ASTLEY"
    >11/11
    """)
else:
    print(f"""
    >Etter en relativt trygg tur gjennom skogen
    >kommer du deg gjennom!
    >Du er i god form og kjenner det ikke er noe galt som kan skje nå
    >Du går nedover stien videre til bestemoren din
    >"Du brukt lang tid"
    >Hun ser litt gretten ut mens dere går til bilen, men ingenting skjer
    >Dere kommer dere til storlien og ser en stor plakat som leser:
        "Erbjudande på snusförpackningar!"   
            (Tilbud på snuspakker!)
    >Dere kjøper masse snus og godteri og kjører trygt hjem
    >Du og bestemoren din sovner på soffaen mens Jon Almaas "praktisk info" går i bakgrunnen

    >GAME OVER
    >DU FIKK "VANLIG ENDING" 
    >2/11
    """)