# Feitselectie en dimensies

## Gekozen feiten

1. Accessoire_Verkoop  
2. Fiets_Verkoop  
3. Onderhoud  

## Motivatie

Deze drie feiten zijn gekozen omdat:

- ze de belangrijkste bedrijfsprocessen vertegenwoordigen  
- ze echte gebeurtenissen bevatten (transacties of acties)  
- ze meetbare of afleidbare waarden hebben  
- ze samen inzicht geven in verkoop en gebruik  

Inkoop is niet gekozen omdat:

- het minder detail bevat (maand/jaar i.p.v. datum)  
- belangrijke context ontbreekt (klant, monteur, filiaal)  
- het minder centraal is voor analyse  

---

## Feit: Accessoire_Verkoop

### Meetwaarden
- aantal  
- verkoopprijs  
- totale omzet  

### Dimensies
- Klant  
- Accessoire  
- Monteur  
- Filiaal (via Monteur)  
- Datum  

### Extra
- Leverancier (via Accessoire)

---

## Feit: Fiets_Verkoop

### Meetwaarden
- aantal  
- verkoopprijs  
- totale omzet  

### Dimensies
- Klant  
- Fiets  
- Monteur  
- Filiaal (via Monteur)  
- Datum  

### Extra
- Fabrikant (via Fiets)

---

## Feit: Onderhoud

### Meetwaarden
- aantal onderhoudsbeurten  
- onderhoudsduur  
- arbeidskosten  

### Dimensies
- Fiets  
- Monteur  
- Filiaal (via Monteur)  
- Datum  

### Extra
- Fabrikant (via Fiets)

---

## Samenvatting

Feiten:
- Accessoire_Verkoop  
- Fiets_Verkoop  
- Onderhoud  

Belangrijke dimensies:
- Datum  
- Product (Accessoire, Fiets)  
- Klant  
- Monteur  
- Filiaal  
- Leverancier / Fabrikant  

