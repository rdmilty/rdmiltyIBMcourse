#first attempt at an RNG-based game. Only two options atm-- fight or flight.
import random
enemy = ["Warlock", "Bandit", "Skeleton"]
boss = ["Bandit Leader", "Head Warlock", "Skeleton King"]
print("Hello there!")
name = input("What is your name? ")
gender = input("Are you (M)ale or (F)emale? ").upper()
#dice1 = random.randint(0,25)
#escape = random.randint(0,10)
while gender != str("M") and gender != str("F"):
    gender = input("Are you (M)ale or (F)emale? ").upper()
c = input("Are you a (W)arrior, (M)age, (D)efender? ").upper()
while c != str("W") and c != str("M") and c != str("D"):
    c = input("Are you a (W)arrior, (M)age, (D)efender? ").upper()
if c == str("W"):
    hp = 1000
    atk = 10
elif c == str("M"):
    hp = 750
    atk = 18
else:
    hp = 1500
    atk = 5
print(name,", it's time for your journey to begin.")
input("Press Enter")
e1 = random.choice(enemy)
e1_hp = 250
e1_atk = 10
#edice1 = random.randint(0, 15)
player_damage = random.randint(0, 15) + e1_atk #Damage player takes from enemy
damage = random.randint(0, 25) + atk #Damage player does to enemy
#hp = hp - player_damage; e1_hp = e1_hp - damage
e2 = random.choice(enemy)
e2_hp = 325
e2_atk = 12
player_damage2 = random.randint(0, 15) + e2_atk
e3 = random.choice(enemy)
e3_hp = 400
e3_atk = 14
player_damage3 = random.randint(0, 15) + e3_atk
print("An angry",e1,"appears!")
option = input("(A)ttack or (R)un? ").upper()
while hp >= 0 and e1_hp >= 0:
    while option != str("A") and option != str("R"):
        print("You're under attack! You took",player_damage,"damage.")
        print("HP:", hp - player_damage)
        hp = hp - player_damage
        option = input("(A)ttack or (R)un? ").upper()
        if option == str("A"):
            break
        if hp <= 0: exit("YOU DIED.")
    while option == str("A"):
        if e1_hp >= 0 and hp >= 0:
            damage = random.randint(0, 25) + atk
            player_damage = random.randint(0, 13) + e1_atk
            hp = hp - player_damage
            e1_hp = e1_hp - damage
            print("You attacked! ",e1," took",damage,"damage.")
            if e1_hp <= 0:
                print("You defeated the", e1,"!")
                h = input("Heal? Y/N ").upper()
                while h != str("Y") and h != str("N"):
                    h = input("Heal? Y/N ").upper()
                if h == str("Y"):
                    u = random.randint(20, 100)
                    hp = hp + u
                    print("You used a potion dropped by the",e1,", and gained ", u, "health.")
                    print("HP:", hp)
                break
            print(e1, "HP:", e1_hp)
            print("The", e1,"retaliated! You took", player_damage,"damage.")
            if hp <= 0:
                exit("YOU DIED.")
            print("HP:", hp)
            option = input("(A)ttack or (R)un? ").upper()
    if option == str("R"):
        if random.randint(0, 10) > 2:
            print("You escaped!")
            input("Press Enter")
            break
        else:
            player_damage = random.randint(0, 15) + e1_atk
            hp = hp - player_damage
            if hp <= 0:
                exit("YOU DIED.")
            else:
                print("Your path is blocked! You're under attack. You took",player_damage," damage.")
                print("HP:", hp - player_damage)
            option = input("(A)ttack or (R)un)? ").upper()
z = input("Do you wish to continue? Y/N ").upper()
while z != str("Y") and z != str("N"):
    z = input("Do you wish to continue? Y/N ").upper()
if z == str("N"):
    exit("You retired.")
if z == str("Y"):
    input("You continued on your path.")

print("An angry",e2,"appears!")
option = input("(A)ttack or (R)un? ").upper()
while hp >= 0 and e2_hp >= 0:
    while option != str("A") and option != str("R"):
        print("You're under attack! You took",player_damage2,"damage.")
        print("HP:", hp - player_damage2)
        hp = hp - player_damage2
        option = input("(A)ttack or (R)un? ").upper()
        if option == str("A"):
            break
        if hp <= 0: exit("YOU DIED.")
    while option == str("A"):
        if e2_hp >= 0 and hp >= 0:
            damage = random.randint(0, 25) + atk
            player_damage2 = random.randint(0, 13) + e2_atk
            hp = hp - player_damage2
            e2_hp = e2_hp - damage
            print("You attacked! ",e2," took",damage,"damage.")
            if e2_hp <= 0:
                print("You defeated the", e2,"!")
                h = input("Heal? Y/N ").upper()
                while h != str("Y") and h != str("N"):
                    h = input("Heal? Y/N ").upper()
                if h == str("Y"):
                    u = random.randint(75, 150)
                    hp = hp + u
                    print("You used a potion dropped by the",e2,", and gained ", u, "health.")
                    print("HP:", hp)
                break
            print(e2, "HP:", e2_hp)
            print("The", e2,"retaliated! You took", player_damage2,"damage.")
            if hp <= 0:
                exit("YOU DIED.")
            print("HP:", hp)
            option = input("(A)ttack or (R)un? ").upper()
    if option == str("R"):
        if random.randint(0, 10) > 3:
            print("You escaped!")
            input("Press Enter")
            break
        else:
            player_damage2 = random.randint(0, 15) + e2_atk
            hp = hp - player_damage2
            if hp <= 0:
                exit("YOU DIED.")
            else:
                print("Your path is blocked! You're under attack. You took",player_damage2," damage.")
                print("HP:", hp - player_damage2)
            option = input("(A)ttack or (R)un)? ").upper()
#print("You've gained more power from your travels! Well done,", name,".")
z = input("Do you wish to continue? Y/N ").upper()
while z != str("Y") and z != str("N"):
    z = input("Do you wish to continue? Y/N ").upper()
if z == str("N"):
    exit("You retired.")
if z == str("Y"):
    input("You continued on your path.")
print("You've gained more power from your travels! Well done,", name,".")
input("Press ENTER")
atk = atk + 25
print("An angry",e3,"appears!")
option = input("(A)ttack or (R)un? ").upper()
while hp >= 0 and e3_hp >= 0:
    while option != str("A") and option != str("R"):
        print("You're under attack! You took",player_damage3,"damage.")
        print("HP:", hp - player_damage3)
        hp = hp - player_damage3
        option = input("(A)ttack or (R)un? ").upper()
        if option == str("A"):
            break
        if hp <= 0: exit("YOU DIED.")
    while option == str("A"):
        if e3_hp >= 0 and hp >= 0:
            damage = random.randint(5, 30) + atk
            player_damage = random.randint(0, 13) + e3_atk
            hp = hp - player_damage3
            e3_hp = e3_hp - damage
            print("You attacked! ",e3," took",damage,"damage.")
            if e3_hp <= 0:
                print("You defeated the", e3,"!")
                h = input("Heal? Y/N ").upper()
                while h != str("Y") and h != str("N"):
                    h = input("Heal? Y/N ").upper()
                if h == str("Y"):
                    u = random.randint(450, 750)
                    hp = hp + u
                    print("You used a large potion dropped by the",e3,", and gained ", u, "health.")
                    print("HP:", hp)
                break
            print(e3, "HP:", e3_hp)
            print("The", e3,"retaliated! You took", player_damage3,"damage.")
            if hp <= 0:
                exit("YOU DIED.")
            print("HP:", hp)
            option = input("(A)ttack or (R)un? ").upper()
    if option == str("R"):
        if random.randint(0, 10) > 4:
            print("You escaped!")
            input("Press Enter")
            break
        else:
            player_damage3 = random.randint(0, 15) + e3_atk
            hp = hp - player_damage3
            if hp <= 0:
                exit("YOU DIED.")
            else:
                print("Your path is blocked! You're under attack. You took",player_damage3," damage.")
                print("HP:", hp - player_damage3)
            option = input("(A)ttack or (R)un)? ").upper()
z = input("Do you wish to continue? Y/N ").upper()
while z != str("Y") and z != str("N"):
    z = input("Do you wish to continue? Y/N").upper()
if z == str("N"):
    exit("You retired.")
if z == str("Y"):
    print("You continued on your path. ")
input("There's something up ahead...")
if c == str("W"):
    input("You've found a magic sword! You can feel its power radiating.")
elif c == str("M"):
    input("You've found magic staff! You can feel its power radiating.")
else:
    input("You've found a magic shield! You can feel its power radiating.")
print("Your attack increased!")

b1 = random.choice(boss)
b1_hp = 25000
b1_atk = 25
player_damage4 = random.randint(0, 30) + b1_atk
print("An angry",b1,"appears!")
print(b1,": I've heard you're causing problems for my men. Now I'll deal with you.")
option = input("(A)ttack or (R)un? ").upper()
while hp >= 0 and b1_hp >= 0:
    while option != str("A") and option != str("R"):
        print("You're under attack! You took",player_damage4,"damage.")
        print("HP:", hp - player_damage4)
        hp = hp - player_damage4
        option = input("(A)ttack or (R)un? ").upper()
        if option == str("A"):
            break
        if hp <= 0: exit("YOU DIED.")
    while option == str("A"):
        if b1_hp >= 0 and hp >= 0:
            damage = random.randint(350, 675) + atk
            player_damage4 = random.randint(0, 30) + b1_atk
            hp = hp - player_damage4
            b1_hp = b1_hp - damage
            print("You attacked! ",b1," took",damage,"damage.")
            if b1_hp <= 0:
                print("You defeated the", b1,"!")
                h = input("Heal? Y/N ").upper()
                while h != str("Y") and h != str("N"):
                    h = input("Heal? Y/N ").upper()
                if h == str("Y"):
                    u = random.randint(500, 1000)
                    hp = hp + u
                    print("You used an extra-large potion dropped by the",b1,", and gained ", u, "health.")
                    print("HP:", hp)
                break
            print(b1, "HP:", b1_hp)
            print("The",b1,"retaliated! You took", player_damage4,"damage.")
            if hp <= 0:
                exit("YOU DIED.")
            print("HP:", hp)
            option = input("(A)ttack or (R)un? ").upper()
    if option == str("R"):
        if random.randint(0, 10) > 8:
            print("You escaped!")
            input("Press Enter")
            break
        else:
            player_damage4 = random.randint(17, 30) + b1_atk
            hp = hp - player_damage4
            if hp <= 0:
                exit("YOU DIED.")
            else:
                print("Your path is blocked! You're under attack. You took",player_damage4," damage.")
                print("HP:", hp - player_damage4)
            option = input("(A)ttack or (R)un)? ").upper()
z = input("Do you wish to continue? Y/N ").upper()
while z != str("Y") and z != str("N"):
    z = input("Do you wish to continue? Y/N ").upper()
if z == str("N"):
    exit("You retired.")
if z == str("Y"):
    print("You continued on your path.")