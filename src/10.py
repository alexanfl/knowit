rogue = 1
priest = 1
wizard = 1
warrior = 1

def num_adventurers():
    adv = 0
    if rogue == 1:
        adv += 1
    if wizard == 1:
        adv += 1
    if warrior == 1:
        adv += 1
    if priest == 1:
        adv += 1
    return adv

def fight_rules():
    if rogue:
        goblins += 1

remaining_goblins = 0

for room in range(1,101):
    print("\nEntering room number %d\n" % room)
    goblins = room
    healed = 0
    if rogue == 0:
        rogue = -1
        print("""The rogue died in the last room and was left behind.""")
    if priest == 0:
        priest = -1
        print("""The priest died in the last room and was left behind.""")
    if wizard == 0:
        wizard = -1
        print("""The wizard died in the last room and was left behind.""")
    if warrior == 0:
        warrior = -1
        print("""The warrior died in the last room and was left behind.""")

    while goblins > 0:
        # Rule 1
        if rogue and rogue != -1 and goblins > 0:
            goblins -= 1
            print("""The rogue kills 1 goblin. There are %d goblins
                    left in the room.""" % goblins)

        # Rule 2
        if wizard and wizard != -1 and goblins > 0:
            tmp = 10 if goblins >= 10 else goblins
            goblins -= tmp
            print("""The wizard kills %d goblin. There are %d goblins
                    left in the room.""" % (tmp, goblins))

        # Rule 3
        if warrior and warrior != -1 and goblins > 0:
            goblins -= 1
            print("""The warrior kills 1 goblin. There are %d goblins
                    left in the room.""" % goblins)

        # Rule 4
        if priest and priest != -1 and num_adventurers() < 4 and not healed and goblins > 0:
            if not warrior:
                warrior = 1
                healed = 1
                print("""The dead warrior has been revived!""")
            elif not wizard:
                wizard = 1
                healed = 1
                print("""The dead wizard has been revived!""")

        # Rule 5
        if priest != 1 and wizard != 1 and warrior != 1 and goblins > 0:
            remaining_goblins += goblins
            print("""Every one of the adventurers are dead except the rogue.
            He sneaks into the next room. The remaining %d goblins wander of
            and start a better life.""" % goblins)
            goblins = 0

        # Rule 6
        if goblins >= 10*num_adventurers() and goblins > 0:
            if warrior and warrior != -1:
                warrior = 0
                print("""The goblins overun the party and kills the warrior.""")
            elif wizard and wizard != -1:
                wizard = 0
                print("""The goblins overun the party and kills the wizard.""")
            elif priest and priest != -1:
                priest = 0
                print("""The goblins overun the party and kills the priest.""")
        
    input("\nPress Enter to continue to the next room …")
    print("___________________________________")

print("All 17 prisoners have been released.")
print("%d creatures survived." % (17 + num_adventurers() + remaining_goblins))
