# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:29:47 2020

@author: Jeffrey Folz
"""

##################################
#First draft of arkham databse. Will hold information on characters, monsters, items, and cards

#06132020: Monsers table added with function to retrieve random monster information, which is returned as a tuple.

##################################

import sqlite3
import random

con = sqlite3.connect('arkham.db')
c = con.cursor()


c.execute('DROP TABLE monsters') #drops monsters table; useful in debugging

c.execute('''CREATE TABLE monsters
(id int PRIMARY KEY,
name TEXT,
color text,
symbol text,
sneak_mod int,
horror_mod int,
combat_mod int,
horror_dmg int,
combat_dmg int,
toughness int
endless int,
undead int,
ambush int,
mag_res int,
phys_res int,
mag_imm int,
phys_imm int,
weapon_imm int,
overwhelming int,
nightmarish int,
elusive int
)''')

c.execute("INSERT INTO monsters VALUES (1,'Byakhee','Blue','circle',-2,-1,0,1,2,1,0,0,0,0,0,0,0,0,0,0)")
c.execute("INSERT INTO monsters VALUES (2,'Zombie','Black','moon', 1,-1,-1,1,2,1,0,1,0,0,0,0,0,0,0,0)")
c.execute("INSERT INTO monsters VALUES (3,'Ghoul','Black','hexagon',-3,0,-1,1,1,1,0,0,1,0,0,0,0,0,0,0)")

con.commit()
con.close()



#Retrieves a random onster from the database and returns it as a tupble.
def get_random_monster():
    connection = sqlite3.connect('arkham.db')
    cursor = connection.cursor()
    cursor.execute('SELECT MAX(id) FROM monsters')
    mons = (random.randint(1,cursor.fetchone()[0]),)
    cursor.execute('SELECT * FROM monsters WHERE id = ?', mons)
    return(cursor.fetchone())
    connection.close()
    

    

