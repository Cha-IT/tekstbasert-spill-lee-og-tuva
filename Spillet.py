#Lee og Tuvas superkule IT-prosjekt
#hvem gjør hva:
#Lee: lager multi-events(X), organiserer og rydder opp i kode
#Tuva: lager ulike events og resultater, introparagraf til spiller
import random as rd

tilstander = { #en ordbok med tilstander som kan endres til "True" basert på hva spilleren gjør
#bruker en ordbok for disse tilstandene fordi det gjør det lettere å endre de nødvendige variablene på en generell måte i med klassene
    "ekkorn": False, #variabel som endres hvis spilleren får et ekkorn som en venn
    "høy": False, #variabel som skal endres hvis spilleren spiser fleinsopp
    "Høyre":False, #denne variabelen og den under sjekker hvilken retning spilleren går i
    "Venstre":False,
    "Snudd": False
}

spiller = { #lager en liten ordbok for informasjon om spilleren, ettersom det kun er to viktige ting man trenger å lagre om spilleren: navn og HP
    "Navn": "Bob Kåre", #middlertidig navn som endres i neste linje
#bruker en placeholder fremfor å legge den inn senere kun fordi det ser bedre ut. Jeg vet at det kommer til å legges til autmoatisk i linjen som tar inn input, dette er kun for estetisk skyld
    "HP": 20 #lagrer HP-en til spilleren, som kun skal endres basert på events senere i spillet
}
spiller["Navn"] = input("Hva heter du?: ") #lar spilleren velge sitt eget navn, som kommer til å ha en effekt på introen ol.

def endreHP(val:int): #en funksjon som tar inn en verdi og endrer HP-en til spilleren med den verdien
    """
    En funksjon som tar inn en verdi og endrer spillerens HP med den verdien

    Parameter:
    val (int) = et positivt eller negativt tall spillerens HP sakl endres med
    """
    newHP = spiller["HP"] + val
    spiller["HP"] = newHP

def endreTilstand(type:str): #en funksjon som tar inn en type tilstand som skal endres og endrer den til True
    """
    En funksjon som tar inn typen tilstand som skal endres og endrer den tilstanden slik at den er True

    Parameter:
    type (str) = hvilken nøkkel i ordboken "tilstander" som skal endre verdien sin til True
    """
    tilstander[type] = True


#intro
print(f""">Hei, {spiller['Navn']}!

        >Velkommen til spillet vårt! 
        >Dette er et tekstbasert spill der du får to valg. 
        >Enten velger du 1 eller 2 
        >Det tror jeg du får til... 
        >Lykke til!
        
        >Du og din bestemor har planlagt en harrytur i lang tid og.
        >Hun er desverre for gammel til å kjøre selv, men du har ikke en egen bil.
        >Du skal gjennom skogen for å komme til bestemoren din og kjøre hennes volvo 240 til Storlien
        >Desverre bor du på den andre siden av en skummel skog :( \n
         """)

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
        print(self.beskrivelse) #printer først ut beskrivelsen for å sette ~stemmningen~
        print(self.hvaSkjer) #printer ut hva som skjer og hva spilleren har muligheten til å gjøre
        resultat = int(input("    >"))-1 #henter inn hvilken index resultatet skal komme fra og trekker fra 1 pga måten python bruker indekser på
        if type(self.resultat[resultat]) == tuple: #sjekker om resultatet vi har fått er lagret i en tuple, ettersom dette betyr at noe skal endres
#grunnen til at vi skal bruke tupler på den måten vi gjør det på er fordi hvis funksjonen som skal endre på HP/en tilstand bare deklareres inni en tuple med resultatet, vil variabelen endres uansett om det er det valget spilleren tar.
#å sette enkle str eller int verdier som siste variabel i en tuple gjør det lettere å bare sjekke om resultatet først er en tuple, og så sjekke hva slags verdi som ligger sist i tuplen og endre det som skal endres
#ikke spør meg (Lee) hva som skjer hvis et event krever at både en tilstand og HP skal endres. men siden ingen events SKAL ha det (jeg ser på deg, Tuva), trenger jeg(Lee) ikke å bekymre meg om det
#men hvis det nå skulle skje, kan man vel bruke en tuple inni en tuple (en "tuptuplele", hvis du vil)
            if type(self.resultat[resultat][1]) == int: #sjekker om den siste verdien i tuplen er et tall, ettersom dette betyr at HP-en til spilleren skal endres
                endreHP(self.resultat[resultat][1]) #endrer HP-en til spilleren med verdien som ligger sist i tuplen med en funksjon som ligger lengre oppe i koden
            elif type(self.resultat[resultat][1]) == str: #sjekker om den siste verdien er en str, ettersom dette betyr at en tilstand på endres
                endreTilstand(self.resultat[resultat][1])#endrer tilstanden som står bakerst i tuplen slik at den for den boolske verdien True
            print(self.resultat[resultat][0])#printer ut teksten som står først i tuplen, som er det skriftlige resultatet spilleren skal få
        else: #hvis resultatet ikke er en tuple, printer vi bare ut resultatet
            print(self.resultat[resultat])
        print()



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
        self.hvaSkjerTo = hvaSkjerTo #lager en egen variabel vi kun trenger for denne
    
    def spillEvent(self):
        """
        En funksjon som iverksetter eventet som skal kjøres
        Tar automatisk inn variabelen "self", ettersom funksjonen er spesifikk for en klasse
        """
        print(self.beskrivelse)
        print(self.hvaSkjer)
        forsteResultat = int(input("    >"))-1
        print(self.hvaSkjerTo[forsteResultat]) #siden vi ikke skal gi et resultat enda, printer vi nå ut hva som skjer basert på den forrige handlingen og gir spilleren nye valgmuligheter
        andreResultat = int(input("    >"))-1
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
 


mainPathEvents = [
    singleEvents(
        ">Når du går videre inn i skogen, ser du at stien deler seg i to...", 
        ">Hva vil du gjøre? \n>1: Gå til venstre \n>2: Gå til høyre", 
        [
            (">Du fortsetter å gå inn i skogen, denne gangen til venstre...", "Venstre"), 
            (">Du fortsetter inn i skogen, denne gangen til høyre...", "Høyre")
        ]
    ),
    singleEvents(
        ">Du fortsetter inn i skogen \n>Å nei! Hva er dette?! \n>Et tre har falt ned på stien. Bak det falne treet er det en stor kampestein", 
        ">Det virker som noe stress å komme seg rundt alt dette. \n>Hva vil du gjøre?: \n>1: Gå rundt \n>2: Snu", 
        [
            ">Du gikk rundt hindringene. Du må være veldig glad i tobakk eller hva?", 
            (">Du snudde. Bestemora di er veldig skuffet over at dere ikke fikk dratt på harrytur til Sverige", "Snudd")
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
        ">Det er et ekorn! Hva vil du gjøre?: \n>1: gi ekkornet en eikenøtt \n>2: ignorer", 
        [
            (">Gratulerer! Du har fått en ny venn!", "ekkorn"), 
            ">Du ignorerte ekkornet. Du føler at det ikke var det lureste valget"
        ]
    )
]

hoyreEvents = [
    singleEvents(
        ">Du fortsetter gjennom skogen. Mellom trærne kan du se noe metall som glimter.", 
        ">Det er en gramofon! Det er en plate i den allerede.... \n>Spill av? \n>1: Ja \n>2: Nei", 
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
    singleEvents(
        ">Du går nedover stien. Du begynner å se deg litt rundt og merker noen litt merkelige sopper."
        ">Du kjenner du er litt sulten, kanskje de ikke er farlige? \n Vil du spise soppen? \n >1: Ja \n>2: Nei",
        [
            
        ]   

    ),
    multiEvents(
        ">Imens du går gjennom skogen, begynner du å føle deg sulten. \n>Selv om du vet at det er god mat i Sverige, trenger du noe nå \n>Du fortsetter på stien, men holder et åpent øye for noe spiselig...", 
        ">Men hva er dette?\n>Litt borte fra stien ser du litt sopp. \n>Du mener å huske at du har sett noe lignende i en bok bestemoren din har om spiselig sopp. \n>Hva gjør du? \n>1: Går bort og spiser soppen \n>2: Fortsetter videre på stien", 
        [
            ">Etter du har spist soppen, innser du at synet ditt begynner å gå litt bananas. \n>Du har nettopp spist fleinsopp! Hva skal du gjøre? \n>1: Svelge soppen og bare la alt dette skje \n>2: Få deg selv til å kaste opp soppen", 
            ">Du fortsetter videre på stien... \n>Plutselig, ser du en stor, brun bjørn på stien deg! Hva skal du gjøre nå? \n>1:Klarte opp i det nærmeste treet og håpe at bjørnen ikke klatrer etter deg. \n>2: LØP! \n>3: Vel, du har alltid hatt lyst til å ha en slosskamp med en bjørn..."
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
]
hvaHarSkjeddEvents = []

def velgerEvent(liste:list): #en felles funksjon for å velge inn ulike events
    """
    En funksjon som velger et tilfeldig event fra en liste

    Parameter:
    liste (list) = listen som et event skal hentes ut fra
    """
    valg = rd.randint(0, len(liste))-1
    liste[valg].spillEvent()
    hvaHarSkjeddEvents.append(liste[valg])
    liste.pop(valg)

while (len(hoyreEvents)!= 0 and len(venstreEvents) !=0 and spiller["HP"] >= 0 and tilstander["Snudd"] == False):
    if tilstander["Høyre"] == True:
        velgerEvent(hoyreEvents)
    elif tilstander["Venstre"] == True:
        velgerEvent(venstreEvents)
    else: #hvis man går rett fram på stien
        velgerEvent(mainPathEvents)

#sjekker de ulike tilstandene spilleren muligens har endret på i løpet av spillet, og ser hvilken ending spilleren da får
if spiller["HP"]<=0:
    print(">GAME OVER \n>TRY AGAIN?")
elif tilstander["ekkorn"]==True:
    print("Kjør ekkorn-ending")    
elif tilstander["høy"]==True:
    print("Kjør rehab ending")
elif tilstander["Snudd"] == True:
    print("Kjør 'Bestemor dør av abstinenser' ending")
else:
    print("vanlig ending")