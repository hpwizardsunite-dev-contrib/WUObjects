#!/usr/bin/env python

# Example extraction script

class Spell:
    def __init__(self):
        self.name = ''
        self.id = ''
        self.image = ''

    def __str__(self):
        # format can be anything you want
        return self.name + ' - ' + self.id + ' - ' + self.image

class Spells:
    def __init__(self, gdc, gdw, s):
        self.gdc = gdc
        self.gdw = gdw
        self.s = s
        self.spells = []

    def extract(self):
        for message in self.gdc['messages']:
            if 'spell' in message:
                spell = Spell()
                spell.name = message['spell']['name']
                spell.id = message['spell']['id']
                spell.image = message['spell']['glyphImage']

                #print(message['spell']['name'])
                #print(message['spell']['id'] + '\n')
                self.spells.append(spell)

        for spell in self.spells:
            for message in self.gdw['messages']:
                if 'spell' in message and message['spell']['id'] == spell.id:
                    #print(message['spell'])
                    # There's literally nothing useful here...
                    pass
            print(spell) # write to file or something later?
