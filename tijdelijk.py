# definieer dictionary 
prijzen = {
    "aardbei"   : 3,
    "vanille"   : 3, #was oorspronkelijk 4, maar volgens opdracht 5 is het 3 * 0.8
    "chocolade" : 5
}

# aanbieding
aanbieding = prijzen["vanille"] * 0.8

# reclametekst 2 decimalen
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding:.2f}" #2 decimalen
reclame_tekst2 = reclame_tekst #compatible met opdracht 5 en 6
reclame_tekst3 = reclame_tekst2.upper() #omzetten in kleine letters
reclame_tekst4 = reclame_tekst3.split() #splitsen in list

# afdrukken
for e1 in reclame_tekst4:
    if len(e1) >=5:
        print(e1.lower()) #5 letters en meer in kleine letters
    else:
        print(e1) #1 t/m 4 letters in hoofdletters - staat het al