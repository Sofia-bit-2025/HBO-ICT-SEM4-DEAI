# Analyse van de BikeToDrive databronnen

## Doel van deze analyse

In deze stap analyseer ik de vijf operationele databronnen van BikeToDrive.

Het doel is nog niet om meteen een sterschema te tekenen.  
Het doel is eerst om goed te begrijpen:

- welk proces elke database beschrijft
- welke tabel het hoofdproces bevat
- welke tabellen extra context geven
- welke gegevens later belangrijk zijn voor feiten en dimensies in het datawarehouse

Deze analyse is gebaseerd op:

- de structuur van de databases op de screenshots
- de tabelnamen in de bronnen
- mijn SDM SQL-script waarin de tabellen al zijn samengebracht

---

# 1. Accessoireverkoop

## Proces

Deze databron beschrijft het proces van de verkoop van accessoires aan klanten.

Het gaat om verkooptransacties waarbij een klant een of meer accessoires koopt.  
De verkoop is gekoppeld aan een monteur.  
Via de monteur is ook het filiaal bekend.

## Tabellen in deze bron

- Accessoire_Verkoop
- Accessoire
- Klant
- Monteur
- Filiaal
- Leverancier

## Hoofdgebeurtenis

De echte gebeurtenis in deze bron is:

- Accessoire_Verkoop

Dit is de transactietabel.  
Hier wordt de verkoopactie vastgelegd die later gemeten kan worden.

## Waarom is Accessoire_Verkoop het hoofdproces?

Deze tabel bevat gegevens die typisch horen bij een verkoopgebeurtenis, zoals:

- datum
- aantal
- verkoopprijs
- klant
- accessoire
- monteur

Dit zijn kenmerken van een feitelijke transactie.

## Rol van de andere tabellen

### Accessoire

Deze tabel beschrijft het verkochte product.

Waarschijnlijke gegevens:
- naam
- soort
- standaardprijs
- inkoopprijs
- leverancier

Betekenis:
- Accessoire is geen gebeurtenis
- Accessoire is productcontext bij de verkoop
- Accessoire wordt later waarschijnlijk een dimensie

### Klant

Deze tabel beschrijft wie koopt.

Waarschijnlijke gegevens:
- naam
- adres
- woonplaats
- geslacht
- geboortedatum

Betekenis:
- Klant is context
- Klant is geen feit
- Klant wordt later waarschijnlijk een dimensie

### Monteur

Deze tabel beschrijft welke medewerker betrokken is bij de verkoop.

Waarschijnlijke gegevens:
- naam
- woonplaats
- uurloon
- filiaal

Betekenis:
- Monteur is context
- Monteur is geen gebeurtenis

Belangrijk:
via Monteur krijg je ook toegang tot Filiaal.

### Filiaal

Deze tabel beschrijft de locatie.

Waarschijnlijke gegevens:
- naam
- adres
- provincie

Betekenis:
- Filiaal is context
- Filiaal is indirect gekoppeld via Monteur

Dat is belangrijk, want filiaal zit niet direct in Accessoire_Verkoop.

### Leverancier

Deze tabel beschrijft van wie het accessoire afkomstig is.

Waarschijnlijke gegevens:
- naam
- adres
- woonplaats

Betekenis:
- Leverancier hoort niet direct bij de verkooptransactie
- Leverancier hoort wel bij het product Accessoire

Dit kan later nuttig zijn voor analyses zoals:
- verkoop per leverancier
- omzet per leverancier
- best verkochte leveranciers

## Samenvatting van deze bron

Deze bron gaat over accessoireverkoop.

- Event: Accessoire_Verkoop
- Productcontext: Accessoire
- Klantcontext: Klant
- Medewerkercontext: Monteur
- Locatiecontext: Filiaal via Monteur
- Herkomst product: Leverancier via Accessoire

## Belangrijk inzicht voor week 4

Deze bron levert heel waarschijnlijk:

- een feit voor accessoireverkoop
- dimensies zoals klant, accessoire, monteur, filiaal en datum

Leverancier kan direct of indirect onderdeel worden van een dimensie.

---

# 2. Fietsverkoop

## Proces

Deze databron beschrijft het proces van de verkoop van fietsen aan klanten.

Het gaat om verkooptransacties waarbij een klant een fiets koopt.  
De transactie is gekoppeld aan een monteur.  
Via de monteur is ook het filiaal bekend.

## Tabellen in deze bron

- Fiets_Verkoop
- Fiets
- Klant
- Monteur
- Filiaal
- Fabrikant

## Hoofdgebeurtenis

De echte gebeurtenis in deze bron is:

- Fiets_Verkoop

Dit is de transactietabel.

## Waarom is Fiets_Verkoop het hoofdproces?

Deze tabel bevat de meetbare verkoopactie.

Waarschijnlijke gegevens:
- datum
- aantal
- verkoopprijs
- klant
- fiets
- monteur

Dit zijn typische kenmerken van een verkoopfeit.

## Rol van de andere tabellen

### Fiets

Deze tabel beschrijft het verkochte product.

Waarschijnlijke gegevens:
- soort
- merk
- type
- standaardprijs
- inkoopprijs
- kleur
- fabrikant

Betekenis:
- Fiets is context
- Fiets is geen gebeurtenis
- Fiets wordt later waarschijnlijk een dimensie

### Klant

Deze tabel beschrijft wie koopt.

Betekenis:
- Klant is context
- Klant is geen feit
- Klant wordt later waarschijnlijk een dimensie

### Monteur

Deze tabel beschrijft welke medewerker betrokken is.

Betekenis:
- Monteur is context
- Monteur is geen feit

Belangrijk:
via Monteur krijg je het filiaal.

### Filiaal

Deze tabel beschrijft de vestiging.

Betekenis:
- Filiaal is locatiecontext
- Filiaal is indirect gekoppeld via Monteur

### Fabrikant

Deze tabel beschrijft de producent van de fiets.

Betekenis:
- Fabrikant is geen event
- Fabrikant is context bij de fiets

Dit kan later nuttig zijn voor analyses zoals:
- omzet per fabrikant
- verkoop per merk of fabrikant
- aantal verkochte fietsen per fabrikant

## Samenvatting van deze bron

Deze bron gaat over fietsverkoop.

- Event: Fiets_Verkoop
- Productcontext: Fiets
- Klantcontext: Klant
- Medewerkercontext: Monteur
- Locatiecontext: Filiaal via Monteur
- Herkomst product: Fabrikant via Fiets

## Belangrijk inzicht voor week 4

Deze bron levert heel waarschijnlijk:

- een feit voor fietsverkoop
- dimensies zoals klant, fiets, monteur, filiaal en datum

Fabrikant kan onderdeel worden van de fietsdimensie of een aparte dimensie, afhankelijk van de ontwerpkeuze.

---

# 3. Onderhoud

## Proces

Deze databron beschrijft het proces van onderhoud aan fietsen.

Het gaat om onderhoudsbeurten die op een bepaalde datum en tijd plaatsvinden.  
Een onderhoudsbeurt is gekoppeld aan een fiets en een monteur.  
Via de monteur is ook het filiaal bekend.

## Tabellen in deze bron

- Onderhoud
- Fiets
- Monteur
- Filiaal
- Fabrikant

## Hoofdgebeurtenis

De echte gebeurtenis in deze bron is:

- Onderhoud

Dit is het onderhoudsevent dat later geanalyseerd kan worden.

## Waarom is Onderhoud het hoofdproces?

Deze tabel bevat het onderhoudsmoment zelf.

Waarschijnlijke gegevens:
- datum
- starttijd
- eindtijd
- fiets
- monteur

Dit is een echte procesregistratie.

## Rol van de andere tabellen

### Fiets

Deze tabel beschrijft welke fiets onderhoud krijgt.

Betekenis:
- Fiets is context
- Fiets is geen event

### Monteur

Deze tabel beschrijft wie het onderhoud uitvoert.

Betekenis:
- Monteur is context
- Monteur is geen event

### Filiaal

Deze tabel beschrijft de locatie.

Belangrijk:
filiaal is ook hier indirect gekoppeld via Monteur.

### Fabrikant

Deze tabel beschrijft de fabrikant van de fiets.

Betekenis:
- Fabrikant is context via Fiets

Dit kan later nuttig zijn voor analyses zoals:
- onderhoud per merk
- onderhoud per fabrikant
- onderhoud per type fiets

## Extra belangrijk bij onderhoud

Deze bron is anders dan verkoop en inkoop.

Waarom?

Omdat onderhoud niet direct een verkoopbedrag bevat.  
De meetwaarden zullen hier waarschijnlijk deels afgeleid moeten worden.

Voorbeelden van afgeleide meetwaarden:
- onderhoudsduur = eindtijd - starttijd
- arbeidskosten = onderhoudsduur × uurloon
- aantal onderhoudsbeurten = 1 per onderhoudsrecord

Dus onderhoud is heel waarschijnlijk een feit, maar met afgeleide meetwaarden.

## Samenvatting van deze bron

Deze bron gaat over onderhoud aan fietsen.

- Event: Onderhoud
- Productcontext: Fiets
- Medewerkercontext: Monteur
- Locatiecontext: Filiaal via Monteur
- Productherkomst: Fabrikant via Fiets

## Belangrijk inzicht voor week 4

Deze bron levert heel waarschijnlijk:

- een feit voor onderhoud
- dimensies zoals fiets, monteur, filiaal en datum

Bij onderhoud zijn afgeleide meetwaarden extra belangrijk.

---

# 4. Accessoire Inkoop

## Proces

Deze databron beschrijft het proces van de inkoop van accessoires.

Het gaat hier niet om verkoop aan klanten, maar om het inkopen van voorraad.

## Tabellen in deze bron

- Accessoire_Inkoop
- Accessoire
- Leverancier

## Hoofdgebeurtenis

De echte gebeurtenis in deze bron is:

- Accessoire_Inkoop

Dit is de inkooptransactie.

## Waarom is Accessoire_Inkoop het hoofdproces?

Deze tabel laat zien dat een accessoire is ingekocht.

Waarschijnlijke gegevens:
- inkoopnr
- inkoopmaand
- inkoopjaar
- aantal
- accessoire

Dit zijn procesgegevens van een inkoopmoment.

## Rol van de andere tabellen

### Accessoire

Deze tabel beschrijft welk accessoire is ingekocht.

Waarschijnlijke gegevens:
- naam
- standaardprijs
- inkoopprijs
- soort
- leverancier

Betekenis:
- Accessoire is context
- Accessoire is geen event

### Leverancier

Deze tabel beschrijft van wie het accessoire afkomstig is.

Betekenis:
- Leverancier is context
- Leverancier is geen event

## Belangrijk verschil met verkoop

Deze bron heeft geen:
- klant
- monteur
- filiaal

Dus dit proces heeft een ander detailniveau en andere context dan verkoop.

Ook opvallend:
de tijd is hier niet als exacte datum opgeslagen, maar als:
- inkoopmaand
- inkoopjaar

Dat betekent dat deze bron waarschijnlijk een andere granulariteit heeft dan verkoop en onderhoud.

Dat is belangrijk voor het datawarehouseontwerp.

## Samenvatting van deze bron

Deze bron gaat over accessoire-inkoop.

- Event: Accessoire_Inkoop
- Productcontext: Accessoire
- Leverancierscontext: Leverancier
- Tijdcontext: maand en jaar, niet volledige datum

## Belangrijk inzicht voor week 4

Deze bron zou een feit kunnen zijn, maar de opdracht vraagt drie feiten in totaal.  
Meestal liggen verkoop en onderhoud meer voor de hand als kernfeiten.

Toch is deze bron wel belangrijk:
- als extra proces
- als bron voor inkoopanalyse
- als bron voor afgeleide meetwaarden zoals inkoopwaarde

---

# 5. Fiets Inkoop

## Proces

Deze databron beschrijft het proces van de inkoop van fietsen.

Het gaat om het inkopen van fietsen voor voorraad.

## Tabellen in deze bron

- Fiets_Inkoop
- Fiets
- Fabrikant

## Hoofdgebeurtenis

De echte gebeurtenis in deze bron is:

- Fiets_Inkoop

Dit is de inkooptransactie.

## Waarom is Fiets_Inkoop het hoofdproces?

Deze tabel beschrijft de inkoopactie.

Waarschijnlijke gegevens:
- inkoopnr
- inkoopmaand
- inkoopjaar
- aantal
- fiets

Dit zijn procesgegevens.

## Rol van de andere tabellen

### Fiets

Deze tabel beschrijft welk product is ingekocht.

Betekenis:
- Fiets is context
- Fiets is geen event

### Fabrikant

Deze tabel beschrijft van welke fabrikant de fiets komt.

Betekenis:
- Fabrikant is context
- Fabrikant is geen event

## Belangrijk verschil met verkoop

Ook hier zie je:
- geen klant
- geen monteur
- geen filiaal
- tijd op maand- en jaarniveau

Dus ook deze bron heeft een andere structuur en granulariteit dan verkoop en onderhoud.

## Samenvatting van deze bron

Deze bron gaat over fietsinkoop.

- Event: Fiets_Inkoop
- Productcontext: Fiets
- Herkomstcontext: Fabrikant
- Tijdcontext: maand en jaar

## Belangrijk inzicht voor week 4

Deze bron is belangrijk voor:
- inkoopanalyse
- vergelijking tussen verkoop en inkoop
- berekening van marges of winst

Maar als er precies drie feiten gekozen moeten worden, moet later bewust beslist worden of inkoop wel of niet een hoofdfeit wordt.

---

# Overkoepelende analyse van alle databronnen

## Welke soorten processen zitten in het geheel?

Als je alle vijf bronnen samen bekijkt, zie je vier soorten bedrijfsprocessen:

1. Accessoireverkoop
2. Fietsverkoop
3. Onderhoud
4. Inkoop van accessoires en fietsen

Dus inhoudelijk zijn er meerdere events aanwezig.

## Welke tabellen zijn duidelijke proces-tabellen?

Dit zijn de tabellen die echte gebeurtenissen registreren:

- Accessoire_Verkoop
- Fiets_Verkoop
- Onderhoud
- Accessoire_Inkoop
- Fiets_Inkoop

Dit zijn de sterkste kandidaten voor feiten.

## Welke tabellen zijn duidelijke context-tabellen?

Dit zijn tabellen die beschrijven wie, wat, waar of van wie:

- Klant
- Monteur
- Filiaal
- Accessoire
- Fiets
- Leverancier
- Fabrikant

Dit zijn duidelijke kandidaten voor dimensies.

---

# Belangrijke patronen die nu al zichtbaar zijn

## 1. Filiaal zit niet altijd direct aan het proces

Bij verkoop en onderhoud komt filiaal niet rechtstreeks uit de procestabel.

Je krijgt filiaal via:
- procestabel
- monteur
- filiaal

Dus filiaal is een indirecte contextdimensie.

## 2. Leverancier en fabrikant zitten aan het product vast

Je krijgt leverancier of fabrikant via:
- procestabel
- product
- leverancier of fabrikant

Dus die context komt niet altijd direct uit de eventtabel.

## 3. Tijd zit niet overal op hetzelfde niveau

Verkoop en onderhoud gebruiken:
- datum

Inkoop gebruikt:
- maand
- jaar

Dus:
- er is een granulariteitsverschil

Dat is een belangrijk inzicht voor het datawarehouseontwerp.

## 4. Product bestaat in twee varianten

Je hebt:
- Accessoire
- Fiets

Dus later moet een keuze gemaakt worden:
- aparte productdimensies houden
- of op hoger niveau slim modelleren

## 5. Verkoop heeft klantcontext, inkoop niet

Dat betekent dat verkoop en inkoop inhoudelijk andere processen zijn.

Dus je mag ze niet zomaar behandelen alsof ze hetzelfde feit zijn.

---

# Voorlopige conclusie

De analyse laat zien dat BikeToDrive meerdere operationele processen bevat met verschillende soorten context en verschillende detailniveaus.

De duidelijkste proces-tabellen zijn:

- Accessoire_Verkoop
- Fiets_Verkoop
- Onderhoud
- Accessoire_Inkoop
- Fiets_Inkoop

De duidelijkste context-tabellen zijn:

- Klant
- Monteur
- Filiaal
- Accessoire
- Fiets
- Leverancier
- Fabrikant

Voor week 4 is vooral belangrijk dat:

- verkoop, onderhoud en inkoop verschillende soorten processen zijn
- sommige context indirect gekoppeld is
- tijd niet in alle bronnen op hetzelfde niveau is opgeslagen
- niet elke procestabel automatisch een hoofdfeit hoeft te worden

Deze analyse vormt de basis voor de volgende stap: het kiezen van de drie feiten en de omliggende dimensies voor het sterschema.