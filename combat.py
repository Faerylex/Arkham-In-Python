#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A short combat module for Arkham Horror. Battle begins with combat_prompt, which asks users 
to select 'run'or 'fight.' If a user selects 'run', a sneak check is made against the monster's
evasiveness.
"""




def combat_prompt(hero, monster):
    combat_round = 0
    while (hero.health > 0 and hero.sanity > 0):
        print("""You are in combat. What would you like to do? 'run' or 'fight'?""")
        choice = input()
        if (choice == "run"):
            if (hero.sneak_check(monster)):
                print("Successfully escaped!")
                break
            else:
                print("You could not escape. The monster delivers %s damage." % str(monster.combat_dmg))
                
                hero.health -= monster.combat_dmg
                if (hero.health<=0):
                    print("You have been knocked unconcious.")
                    break
        elif (choice == "fight"):
            if (combat_round==0):
                sanity_check(hero, monster)
                if (hero.sanity<=0):
                    print("You have gone insane.")
                    break
            rolls = hero.fight + monster.combat_mod
            sucs = hero.roll_dice(rolls)
            print("You rolled %s successes during the fight check." % str(sucs))
            if (sucs >= monster.toughness):
                print("You have defeated the monster!")
                del monster
                break
            else:
                print("The monster attacks for %s damage!" % str(monster.combat_dmg))
                print("%s has %s health left." % hero.name, str(hero.health))
                hero.health -= monster.combat_dmg
        else:
            print("Select another option. You must select 'run' or 'fight'.")
            
        
def sanity_check(hero, monster):
    if (hero.will_check(monster)):
        print("The sanity check was passed.")
    else:
        print("The sanity check was as much a failure as you are. The monster hits for %s sanity damage." % str(monster.horror_dmg))
        hero.sanity -= monster.horror_dmg
        

def combat(hero, monster):
    if (hero.combat_check(monster)):
        print("The monster is defeated.")
    else:
        print("The monster strikes.")
        hero.health -= monster.combat_dmg























