# -*- coding: utf-8 -*-
inkøbsliste = ['Juice', 'Tomater', 'Kartofler',
		'Bannaner']

print('Den første vare er:', inkøbsliste[0])

inkøbsliste[0] = "Æble juice"
print('Den første vare er:', inkøbsliste[0])

print(inkøbsliste[1:3])

andre_begivenhedder = ['Vask bil', 'Hent børne fra skole', 'Gå i banken']

to_do_liste = [andre_begivenhedder, inkøbsliste,]

print(to_do_liste)

print((to_do_liste[1][1]))

inkøbsliste.append('Løg')

print(to_do_liste)

inkøbsliste.insert(1,'Agurk')

print(inkøbsliste)

inkøbsliste.remove('Agurk')

print(inkøbsliste)

inkøbsliste.sort()

print(inkøbsliste)

inkøbsliste.reverse()

print(inkøbsliste)

del inkøbsliste[4]

print(to_do_liste)

to_do_liste2 = andre_begivenhedder + inkøbsliste

print(len(to_do_liste2))
print(max(to_do_liste2))
print(min(to_do_liste2))
