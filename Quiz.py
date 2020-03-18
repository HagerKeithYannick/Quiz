from random import randint as rand
from os import system as cmd

mc1 = {
    'frage':'Soll man gerade nach unten graben?',
    'a':'Nein',
    'b':'Nein',
    'c':'Ja',
    'd':'Nein',
    'res':'c',
}
mc2 = {
    'frage':'Wie hoch ist das grösste Level welches ein Verzauberungstrank-Effekt erreichen kann?',
    'a':'100',
    'b':'255',
    'c':'64',
    'd':'10',
    'res':'b',
}
mc3 = {
    'frage':'Seit welchem Jahr gibt es Minecraft?',
    'a':'2021',
    'b':'2013',
    'c':'2009',
    'd':'1997',
    'res':'c',
}

mc_fragen = [mc1,mc2,mc3,]

trash1 = {
    'frage':'Seit wann gibt es fortnite?',
    'a':'21. Juli 2017',
    'b':'23. Oktober 2017',
    'c':'11. April 2017',
    'd':'24. Dezember 2018',
    'res':'a',
}

trash2 = {
    'frage':'Wie viele registrierte Nutzer hatte Fortnite im März 2019?',
    'a':'3.1415',
    'b':'300 Mio',
    'c':'50 Mia.',
    'd':'250 Mio.',
    'res':'d',
}

trash3 = {
    'frage':'Was für 3 Materialien gibt es in Fortnite, mit denen man bauen kann?',
    'a':'Erde, Gummi und Ziegel',
    'b':'Holz, Stein und Metall',
    'c':'Plastik, Sand und Glas',
    'd':'REE, Fisch und Orangen',
    'res':'b',
}

trash_fragen = [trash1,trash2,trash3,]

sv1 = {
    'frage':'Aus wie vielen Mitarbeitern besteht das Entwicklerteam fur Stardew Valley?',
    'a':'1',
    'b':'50',
    'c':'1.5 Mio.',
    'd':'200',
    'res':'a',
}

sv2 = {
    'frage':'Existiert Fleisch (mit ausnahme von Fisch) in Stardew Valley?',
    'a':'Ja',
    'b':'Nein',
    'c':'Es exisistieren nur dessen IDs und Sprites',
    'd':'Keine Ahnung',
    'res':'c',
}

sv3 = {
    'frage':'Wie heisst das Pseudonym des Entwicklers von Stardew Valley?',
    'a':'Notch',
    'b':'Epicgames',
    'c':'Cucklefisch',
    'd':'Concernedape',
    'res':'d',
}

sv_fragen = [sv1,sv2,sv3,]

pkmn1 = {
    'frage':'Kann man Yoshi aus Super Mario in Pokemon Blau fangen?',
    'a':'Ja',
    'b':'Nein',
    'c':'Nur mit Glitches',
    'd':'Keine Ahnung',
    'res':'b',
}

pkmn2 = {
    'frage':'Welche Nummer trägt Pikachu im Nationalen Pokedex?',
    'a':'#025',
    'b':'#054',
    'c':'#016',
    'd':'#030',
    'res':'a',
}

pkmn3 = {
    'frage':'Wie heisst der legendäre Titan von Hoenn welches aus Eis besteht?',
    'a':'Regiice',
    'b':'Regice',
    'c':'Regieis',
    'd':'Regyice',
    'res':'b',
}

pkmn_fragen = [pkmn1,pkmn2,pkmn3,]

fragen = {
    'minecraft':mc_fragen,
    'fortnite':trash_fragen,
    'stardewvalley':sv_fragen,
    'pokemon':pkmn_fragen,
}     

themen = []

for i in fragen.keys():
    themen.append(i)

lifes = 3
score = 0

#----------Quiz----------
main = True
while main:
    #cmd('cls') # Im Falle eines ERRORS auskommentieren
    rng = rand(0,2)
    
    print(f'''
    leben:  {lifes}
    Punkte: {score}

    Themen:
    ''')

    for inhalt in themen:
        print(inhalt)

    t_auswahl = input('\nWähle ein Thema aus: ').lower()
    if t_auswahl in themen:
        print(f"{fragen[t_auswahl][rng]['frage']}\n")
        print(f"a) {fragen[t_auswahl][rng]['a']}")
        print(f"b) {fragen[t_auswahl][rng]['b']}")
        print(f"c) {fragen[t_auswahl][rng]['c']}")
        print(f"d) {fragen[t_auswahl][rng]['d']}")
        antwort = input('Antwort: ')
        if antwort == fragen[t_auswahl][rng]['res']:
            print('Deine Antwort ist Richtig!')
            score += 1
        else:
            print(f'Deine Antwort ist Falsch! Die Richtige Antwort ist {fragen[t_auswahl][rng]["res"]}')
            lifes -= 1

        input('Drücke Enter: ')
        themen.remove(t_auswahl)

    if lifes == 0:
        print(f'''
        Game Over

        Deine Punktzahl beträgt: {score}
        ''')
        input('Drücke Enter: ')
        main = False
    
    if len(themen) == 0:
        print(f'''
        Glückwunsch, du hast gewonnen.

        Übriges Leben: {lifes}
        ''')
        input('Drücke Enter: ')
        main = False