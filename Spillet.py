import random as rd

tilstander = { #en ordbok med tilstander som kan endres til "True" basert på hva spilleren gjør
#bruker en ordbok for disse tilstandene fordi det gjør det lettere å endre de nødvendige variablene på en generell måte i med klassene
    "ekkorn": False, #variabel som endres hvis spilleren får et ekkorn som en venn
    "høy": False, #variabel som skal endres hvis spilleren spiser fleinsopp
    "høyre":False, #denne variabelen og den under sjekker hvilken retning spilleren går i
    "venstre":False,
    "snudd": False,
    "kvalm": False,
    "rickern": False
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


spiller["Navn"] = input("Hva heter du?: ") #lar spilleren velge sitt eget navn, som kommer til å ha en effekt på introen ol.

print(f""">Hei, {spiller['Navn']}!

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

    >La oss begynne...

        
    >INITIALISERER...
    >HENTER INN EVENTS...
    >GIR LAKS TIL BJØRNENE...
    >FINNER FLEINSOPP...
    >SPILLER AV GODE, GAMLE PLATER...
    >GIR EIKENØTTER TIL DYRELIVET...
    >MØTER GAMLE KJENNINGER PÅ STIEN

    >INITIALISERING FULLFØRT



>Du står på kanten av en stor, mørk skog
>Trærne virker høyere enn de vanligvis gjør
>Du vet at på andre siden av skogen venter det en artig tur og mye tobakk
>Selv om skoge virker større og mørkere nå enn den har gjort før, begynner du å gå inn
>Du har jo tross alt gått gjennom den tusen ganger før. Hvorfor skal denne gangen skille seg ut?
>Så snart du setter foten din på stien, vet du at det ikke er noen veg tilbake nå
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
        resultat = input("    >") #henter inn hvilken index resultatet skal komme fra og trekker fra 1 pga måten python bruker indekser på
        if resultat == "Rick Astley": #lite Easter Egg for alle singleEvents ;)
            print("Rick Astley hører ditt skrik om hjelp, og kommer for å redde deg")
            endreTilstand("rickern")
        else:
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
        ">Det er et ekorn! Hva vil du gjøre?: \n>1: gi ekornet en eikenøtt \n>2: ignorer", 
        [
            (">Gratulerer! Du har fått en ny venn!", "ekkorn"), 
            ">Du ignorerte ekkornet. Du føler at det ikke var det lureste valget"
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
            ">Du fortsetter videre på stien... \n>Plutselig, ser du en stor, brun bjørn på stien deg! Hva skal du gjøre nå? \n>1:Klatre opp i det nærmeste treet og håpe at bjørnen ikke klatrer etter deg. \n>2: LØP! \n>3: Vel, du har alltid hatt lyst til å ha en slåsskamp med en bjørn..."
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
    valg = rd.randint(0, len(liste))-1 #velger eventet tilfeldig fordi det ville vært kjedelig hvis det alltid hadde kommet i en bestemt rekkefølge
    liste[valg].spillEvent()
    hvaHarSkjeddEvents.append(liste[valg])
    liste.pop(valg)

while (len(hoyreEvents)!= 0 and len(venstreEvents) !=0 and spiller["HP"] > 0 and tilstander["snudd"] == False and tilstander["rickern"] == False):
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
elif tilstander["ekkorn"]==True and tilstander["kvalm"]==True:
    print(f"""
        >Etter en lang, og slitsom, tur er du endelig kommet gjennom skogen!
        >Du ser at rett ned stien sitter bestemoren din i hagen sin i en god gammal gyngestol
        >"Du e så treig {spiller['Navn']}
        >Plutselig kjenner du at det surrer i magen
        >Det er den rare ekle soppen du spiste!
        >Du kjenner at det kommer opp å whooooosshshhssh
        >Du spyr en stråle mot bakken
        >Så ute av ingenting hopper ekorn kameraten din av skulderen å begynner å spise oppkastet ditt?
        >Du og bestemor synes dette er veldig ekkelt. Dere prøver å skynde dere inn i bilen
        \n
        >GOOD ENDING
        >TRY AGAIN? 
        """)
elif tilstander["ekkorn"]==True:
    print(f"""
        >Etter en lang lang tur gjennom den skumle skogen, har du endelig kommet gjennom!
        >Du ser at lengre ned stien ut av skogen, sitter bestemoren din i en gammel gyngestol i hagen hennes.
        >"Du brukt jævli lang tid {spiller['Navn']}..."
        >Bestemoren din ser på skulderen din.
        >"E d ei rotte? Ta åsså sætt fra dæ den så fær vi"
        >Du merker at ditt ekorn-venn ikke var veldig glad i den kommentaren...
        >Plutselig! 
        >Ekornet angriper bestemoren din! Det er så blodig! 
        >Du klarer ikke se på. Du snur deg. 
        >Det blir stille igjen... 
        >Du snur deg tilbake, men du ser ikke bestemoren din lengre? Det er blod overalt og alt du ser....
        >er ekornet som står på den blodige strikket-genseren til din avdøde bestemor...\n
        >GAME OVER
        >TRY AGAIN?"
        """)    
elif tilstander["høy"]==True:
    print("Kjør rehab ending")
elif tilstander["snudd"] == True:
    print("Kjør 'Bestemor dør av abstinenser' ending")
elif tilstander["kvalm"]==True:
    print("kjør spy-ending :)")
elif tilstander["rickern"] == True:
    print("Kjør rick astley-ending")
else:
    print("vanlig ending")