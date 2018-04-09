# -*- coding: utf-8 -*-

super_skurke = {'Fiddler' : 'Isaac Bowin',
		'Captain Cold' : 'Leonard Snart',
		'Weather Wizard' : 'Mark Mardon',
		'Mirror Master' : 'Sam Scudder',
		'Pied Piper' : 'Thomas Peterson'}

print(super_skurke['Captain Cold'])

del super_skurke['Fiddler']

super_skurke['Pied Piper'] = 'Hartley Rathaway'

print(super_skurke)

print(len(super_skurke))

print(super_skurke.get('Pied Piper'))

print(super_skurke.keys())

print(super_skurke.values())
