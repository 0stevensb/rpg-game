import random
import time
class enemystats():
    def __init__(self,name,eatk,edef,emaxhp,goldrp,expdrp,especial1,especial2,itemdrop,emag):
        self.name =name
        self.type=1
        self.eatk=eatk
        self.edef=edef
        self.emaxhp=emaxhp
        self.goldrp=goldrp
        self.expdrp = expdrp
        self.especial1=especial1
        self.especial2=especial2
        self.itemdrop=itemdrop
        self.emag=emag
class itemstats():
  def __init__(self,name,iatk,idef,goldcst,ispecial,imag,equippable,manacstmod,iheal,itype):
    self.name=name
    self.type =2
    self.iatk=iatk
    self.idef=idef
    self.goldcst=goldcst
    self.ispecial=ispecial
    self.imag = imag
    self.equippable=equippable
    self.manacostmod=manacstmod
    self.iheal=iheal
    self.itype = itype
class spellstats():
  def __init__(self,name,spdamage,spheal,spmanacost,spspecial):
    self.name=name
    self.spdamage=spdamage
    self.spheal=spheal
    self.spmanacost = spmanacost
    self.spspecial=spspecial
def search(y):
   if y=="bees":
    thing=bees
   elif y =="skeleton":
    thing=skeleton
   elif y=="iron sword":
    thing = ironswrd
   if thing.type ==1:
    print(thing.name, thing.eatk,thing.edef,thing.ehp,thing.goldrp)
   elif thing.type ==2:
    print(thing.name, thing.iatk,thing.idef,thing.goldcst)
def hpcheck():
  global alive
  if php<=0:
    alive = False
def damage(atk,defence):
    global pdamagemult
    d=  (atk - defence)
    return d
def phit():
    global ehp, pdamagemult,crit,ctpdef,cteatk,pstatus
    ctpatk=patk+citem.iatk+patkmod
    ctpdef=pdef+citem.idef+pdefmod
    cteatk=cenemy.eatk+eatkmod
    ctedef=cenemy.edef + edefmod
    attacks=1
    if citem.ispecial==1:
      attacks+=1
    for i in range(attacks):
     if (random.randint(1,25)==10 and citem.ispecial!=7) or (random.randint(1,5)==5 and citem.ispecial==7):
      pdamagemult*=3
      crit=True
      print("Critical hit!")
     damagedealt =round((damage(ctpatk*pdamagemult,ctedef)))
     if crit:
      pdamagemult/=3
      crit=False
    
     if damagedealt<0 or cenemy.especial1==8:
      damagedealt =0
     print(f"You dealt {damagedealt} damage!")
     ehp-=damagedealt
     if cenemy.especial1==6 and random.randint(1,4) and pstatus==0 and citem.ispecial!=5:
      print("You were poisoned!")
      pstatus = 1
     print(f"The {cenemy.name} now has {ehp} hp")
     if ehp<=0:
       break
def ehit():
  global php,edamagemult,crit,ctpatk,ctedef,frozen,efrozen,ehp,eatkmod,edefmod,pstatus
  ctpatk=patk+citem.iatk+patkmod+carmour.iatk
  ctpdef=pdef+citem.idef+pdefmod+carmour.idef
  cteatk=cenemy.eatk+eatkmod
  ctedef=cenemy.edef + edefmod
  if (cenemy.especial1!=1 or turncount%2==0) and not efrozen:
   if (random.randint(1,25)==10 and cenemy.especial1!=9) or (random.randint(1,5)==5 and cenemy.especial1==9):
      crit=True
      edamagemult*=3
      print("Critical hit!")
   if cenemy.especial1==2 or (cenemy.especial1==4 and random.randint(1,3)==3): 
    damagedealt=round(damage(cenemy.emag*edamagemult,pmag+citem.imag+carmour.imag))
   else:
     damagedealt =round(damage(cteatk*edamagemult,ctpdef))
   if crit:
    edamagemult/=3
    crit=False
   if damagedealt<0:
      damagedealt =0
   print(f"You took {damagedealt} damage!")
   if cenemy.especial1==5:
     ehp+=round(damagedealt/2)
     if ehp>cenemy.emaxhp:
       ehp=cenemy.emaxhp
     if round(damagedealt/2)>0:
      eatkmod+=1
      print(f"The {cenemy.name} healed {round(damagedealt/2)} hp!")
   php-=(damagedealt)
   print(f"You now have {php} hp")
   if cenemy.especial1==6 and random.randint(1,4)==1 and pstatus==0:
     print("You were poisoned!")
     pstatus = 1
   if cenemy.especial1==3:
    edamagemult+=0.5
   if cenemy.especial2==1 and random.randint(1,3)==3:
     frozen=True
     print("You were frozen!")
   if cenemy.especial1 == 7:
     ehp=0
     print(f"The {cenemy.name} exploded!")
     hpcheck()
  
  else:
    print(f"The {cenemy.name} did nothing....")
    efrozen=False
  hpcheck()
def chest():
  global gold,citem,cenemy,ehp,turncount,alive,enemy,php
  choice=""
  while choice != "y" and choice!="n":
   choice = input("You found a chest! Open it? (y/n) ")
   if choice =="y":
     x=random.randint(1,5)
     if x  ==1:
       gold+=50
       print("It contained 50 gold!")
       newencounter()
     elif x==2:
       x=random.randint(1,7)
       if x ==1:
         y=ironswrd
       elif x==2:
         y=shield
       elif x==3:
         y=slimeball
       elif x== 4:
         y=bomb
       elif x == 5:
         y=bow
       elif x ==6:
         y=scythe
       elif x ==7:
         y=cloak
       print(f"It contained a {y.name}!")
       if y.equippable:
         valid = False
         while not valid:
          choice = input("Equip it? (y/n) ")
          if choice=="y":
           if y.itype==1:
             if citem!=nothing:
              inventory.append(citem)
             citem=y
           elif y.itype==2:
            if carmour!= nothing:
             inventory.append(carmour)
            carmour=y
           print(f"You equipped the {(y).name}")
           valid = True
          elif choice =="n":
            print("You put it in your inventory")
            inventory.append(y)
            valid = True
       inventory.append(y)
       newencounter() 
     elif x==3:
       print("It's a mimic!")
       cenemy=mimic
       ehp=cenemy.emaxhp
       turncount=0
       enemy=True
     elif x==4:
       print("It's a trap!")
       php-= 10 
       print("You took 10 damage")
       hpcheck()
       if alive ==False:
         break
       newencounter()
     elif x==5:
       print("It's empty...")
       newencounter()
   elif choice =="n":
     print("Better safe than sorry...")
     newencounter()
def fishinghole():
  global gold,citem,carmour
  choice =""
  while choice !="y" and choice!="n":
   choice=input("You spotted a pond with a fishing rod on it's banks. Take a look? (y/n) ")
  if choice =="y":
   exit = False
   while not exit:
    choice = input(f"You spot a bait dispenser for 50 gold. You have {gold}. Buy some? (y/n) ")
    if choice =="y":
      if gold>=50:
        gold-=50
        y=random.randint(1,4)
        if y==1:
          print("You caught a fish!")
          inventory.append(fish)
        elif y==2:
          print("You caught nothing...")
        elif y==3:
          print("You fished up 60 gold!")
          gold+=60
        elif y==4:
          x=random.randint(1,7)
          if x ==1:
            y=ironswrd
          elif x==2:
            y=shield
          elif x==3:
             y=slimeball
          elif x== 4:
             y=bomb
          elif x == 5:
             y=bow
          elif x ==6:
             y=scythe
          elif x ==7:
            y=cloak
          print(f"You fished up a {y.name}!")
          if y.equippable:
            valid = False
            while not valid:
              choice = input("Equip it? (y/n) ")
              if choice=="y":
               if y.itype==1:
                 if citem!=nothing:
                  inventory.append(citem)
                 citem=y
               elif y.itype==2:
                if carmour!= nothing:
                 inventory.append(carmour)
                carmour=y
               print(f"You equipped the {(y).name}")
               valid = True
              elif choice =="n":
                print("You put it in your inventory")
                inventory.append(y)
                valid = True
          else:
           inventory.append(y)
    elif choice =="n":
      exit =True
  newencounter()
def newencounter():
  global gold,xp,ehp,cenemy,php,level,patk,pdef,pmaxhp,enemy,edamagemult,turncount,citem,pmag,pmaxmana,pmana,patkmod,pdefmod,eatkmod,edefmod,atkgrwth,defgrwth,maggrwth,managrwth,hpgrwth,efrozen,carmour,emaxhp
  efrozen=False
  if enemy:
   if citem.ispecial==6:
    php+=round(cenemy.emaxhp/4)
    print(f"You healed {round(cenemy.emaxhp/4)} hp! You now have {php} hp")
   edamagemult=1
   eatkmod=0
   edefmod=0
   pdefmod=0
   patkmod=0
   gold+=cenemy.goldrp
   print(f"The {cenemy.name} dropped {cenemy.goldrp} gold! You now have {gold} gold")
   if cenemy.itemdrop!=0 and random.randint(1,5)==5:
      print(f"The {cenemy.name} dropped a {(cenemy.itemdrop).name}!")
      if (cenemy.itemdrop).equippable:
        valid = False
        while not valid:
          choice = input("Equip it? (y/n) ")
          if choice=="y":
           if (cenemy.itemdrop).itype ==1:
            if citem!=nothing:
              inventory.append(citem)
            citem=cenemy.itemdrop
           elif (cenemy.itemdrop).itype ==2:
            if carmour!=nothing:
              inventory.append(carmour)
            carmour=cenemy.itemdrop
           print(f"You equipped the {(cenemy.itemdrop).name}")
           valid = True
          elif choice =="n":
            print("You put it in your inventory")
            inventory.append(cenemy.itemdrop)
            valid = True
      else:
        inventory.append(cenemy.itemdrop)     
   xp+=cenemy.expdrp
   print(f"You gained {cenemy.goldrp} xp! You now have {xp} xp")
   while xp>=75+(25*level):
    xp-=75+(25*level)
    level+=1
    print(f"Level up! You are now level {level}")
    patk+=random.randint(0,atkgrwth)
    pdef+=random.randint(0,defgrwth)
    pmaxhp+=random.randint(0,hpgrwth)
    pmag+=random.randint(0,maggrwth)
    pmaxmana+=random.randint(0,managrwth)
    if pmana<pmaxmana:
     pmana=pmaxmana
    print(f"Your attack is now {patk}")
    print(f"Your defence is now {pdef}")
    print(f"Your magic is now {pmag}")
    print(f"Your max mana is now {pmaxmana}")
    print(f"Your max hp is now {pmaxhp}")
    if php<pmaxhp:
     php=pmaxhp
  enemy=False
  y= random.randint(1,6)
  if y==1:
    y=random.randint(1,6)
    if y<=2:
     shop()
    elif y==3:
     gamble()
    elif y==4:
      chest()
    elif y==5:
      bombshop()
    elif y==6:
      fishinghole()
  else:
   enemy=True
   z=random.randint(1,16)
   if z ==1:
    cenemy= bees
   elif z==2:
    cenemy= skeleton
   elif z == 3:
    cenemy = dragon
   elif z==4:
    cenemy = slime
   elif z == 5:
    cenemy=bandit
   elif z ==6:
     cenemy=troll
   elif z==7:
     cenemy=thingy
   elif z ==8:
     cenemy=mage
   elif z ==9:
     cenemy=golem
   elif z ==10:
     cenemy=icewitch
   elif z ==11:
     cenemy=vampire
   elif z ==12:
     cenemy=mech
   elif z== 13:
     cenemy=bomber
   elif z ==14:
     cenemy=ghost
   elif z == 15:
     cenemy=icegolem
   elif z == 16:
     cenemy=assassin
   ehp=cenemy.emaxhp
   print(f"You encountered a {cenemy.name}!")
   turncount=0
def bombshop():
  global gold
  choice=""
  while choice != "y" and choice != "n":
    choice=input("You spot a shady figure who appears to be selling items. Approach her? (y/n) ")
    if choice=="y":
      bought=0
      exit=False
      while not exit and bought<5:
        choice2 = input(f"She seems to be selling bombs for 60 gold. You have {gold} gold. Buy one? (y/n) ")
        if choice2 =="y":
          if gold>=60:
            inventory.append(bomb)
            gold-=60
            bought+=1
          else:
            print("Insufficent gold")
        elif choice2 =="n":
          exit = True    
      newencounter()  
    if choice =="n":
     print("You have enough issues as is")  
     newencounter()
def shop():
  global gold,xp,patk,php,pmaxhp,citem,pstatus,carmour
  print("You found a shop!")
  exit = False
  while not exit:
    print(f"You have {gold} gold and {php}/{pmaxhp} hp. Your current equipped weapon is {citem.name} and armour is {carmour.name}")
    choice = int(input("1: Strength Potion (70 Gold) 2: XP Potion (60 Gold) 3: Health Potion (50 Gold) 4: Iron Sword (100 Gold) 5: Gun (200 Gold) 6: Shield (100 Gold)\n7: Swift Dagger (200 Gold) 8: Staff (150 Gold) 9: Leather Armour (80 Gold) 10: Plate Armour (200 Gold)\n11: Sell 12: Leave "))
    if   choice == 1:
      if gold >= 70:
        patk+=2
        gold-=70
        print(f"Your attack is now {patk}")
      else:
        print("Insuffient Gold")
    elif choice == 2:
      if gold >=60:
        gold-=60
        xp+=100
        print(f"You now have {xp} xp")
      else:
        print("Insufficient gold")
    elif choice == 3:
      if gold >= 50:
        gold-=50
        php=pmaxhp
        print("You were healed to full")
        if pstatus!=0:
          pstatus=0
          print("Your status was cured!")
      else:
        print("Insufficient gold")
    elif choice == 4:
      if gold >=100:
       if citem!=nothing:
          inventory.append(citem)
       citem=ironswrd
       gold-=100
       print("You equipped the Iron Sword!")
      else:
        print("Insufficient gold")  
    elif choice == 5:
      if gold >=200:
         if citem!=nothing:
          inventory.append(citem)
         gold-=200
         citem=gun
         print("You equipped the Gun!")
      else:
        print("Insufficient gold")  
    elif choice == 6:
      if gold >=100:
         if citem!=nothing:
          inventory.append(citem)
         gold-=100
         citem=shield
         print("You equipped the Shield!")
      else:
        print("Insufficient gold")  
    elif choice == 7:
      if gold >=200:
         if citem!=nothing:
          inventory.append(citem)
         gold-=200
         citem=swiftdagger
         print("You equipped the Swift Dagger!")
      else:
        print("Insufficient gold")  
    elif choice == 8:
      if gold >=150:
         if citem!=nothing:
          inventory.append(citem)
         gold-=150
         citem=staff
         print("You equipped the Staff!")
      else:
        print("Insufficient gold") 
    elif choice == 9:
      if gold >=80:
         if carmour!=nothing:
          inventory.append(carmour)
         gold-=80
         carmour=lthrarmr
         print("You equipped the Leather Armour!")
      else:
        print("Insufficient gold")   
    elif choice == 10:
      if gold >=200:
         if carmour!=nothing:
          inventory.append(carmour)
         gold-=200
         carmour=platearmour
         print("You equipped the Plate Armour!")
      else:
        print("Insufficient gold") 
    elif choice == 11:
      print(f"Equipped weapon: {citem.name} Equipped armour: {carmour.name}")
      print("Inventory:")
      for x in range(len(inventory)):
        print(f"{x+1}: {inventory[x].name} ({inventory[x].goldcst} gold)")
      choice = int(input("Which item would you like to sell? 0 for equipped weapon, -1 for equipped armour, -2 to exit "))-1
      if choice == -1:
       print(f"You sold your {citem.name} for {citem.goldcst} gold!")
       gold+=citem.goldcst
       citem=nothing
      elif choice==-2:
        print(f"You sold your {carmour.name} for {carmour.goldcst} gold!")
        gold+=carmour.goldcst
        carmour=nothing
      elif choice>= 0 and choice <= len(inventory):
        print(f"You sold your {inventory[choice].name} for {inventory[choice].goldcst} gold!")
        gold+=inventory[choice].goldcst
        inventory.pop(choice)
    elif choice ==12:
      exit = True
      newencounter()#
def spellchoice():
  global cspell, magic
  valid = False
  while not valid:
    choice = input(f"What spell will you use? You have {pmana} mana. 1: Magic Missile ({magicmissile.spmanacost+citem.manacostmod+carmour.manacostmod} Mana) 2: Heal ({heal.spmanacost+citem.manacostmod+carmour.manacostmod} Mana) 3: Meteor Strike ({meteorstrike.spmanacost+citem.manacostmod+carmour.manacostmod} Mana) 4: Life Drain ({lifedrain.spmanacost+citem.manacostmod+carmour.manacostmod} Mana) 5: None ")
    if choice == "1":
      if pmana >=magicmissile.spmanacost+citem.manacostmod+carmour.manacostmod:
       cspell =magicmissile
       magic = True
       valid = True
      else:
        print("Insuffient mana")
    elif choice == "2":
      if pmana >=heal.spmanacost+citem.manacostmod+carmour.manacostmod:
       cspell =heal
       magic = True
       valid = True
      else:
        print("Insuffient mana")
    elif choice == "3":
      if pmana >=meteorstrike.spmanacost+citem.manacostmod+carmour.manacostmod:
       cspell =meteorstrike
       magic = True
       valid = True
      else:
        print("Insuffient mana")
    elif choice == "4":
      if pmana >=lifedrain.spmanacost+citem.manacostmod+carmour.manacostmod:
       cspell =lifedrain
       magic = True
       valid = True
      else:
        print("Insuffient mana")
    elif choice == "5":
      valid = True
      movechoice()
    if magic == True:
      pmaghit()
def pmaghit():
    global ehp, pdamagemult,crit,ctpdef,cteatk,pmag,emag,magic,pmana,citem,php,efrozen,pstatus,carmour
    attacks=1
    print(f"You used {cspell.name}!")
    if cspell.spdamage>0:
     for i in range(attacks):
      if random.randint(1,25)==10:
       pdamagemult*=3
       crit=True
       print("Critical hit!")
      damagedealt =round((damage((pmag+cspell.spdamage+citem.imag+carmour.imag)*pdamagemult,cenemy.emag)))
      if damagedealt<0:
        damagedealt=0
      print(f"You dealt {damagedealt} damage!")
      ehp-=damagedealt
      if cspell.spspecial==1:
        php+=round(damagedealt/2)
        print(f"You healed {round(damagedealt/2)} hp!")
        if php>pmaxhp:
          php=pmaxhp
      print(f"The {cenemy.name} now has {ehp} hp")
      if citem.ispecial==3 and random.randint(1,3)==3:
       efrozen=True
       print(f"The {cenemy.name} was frozen!")
      if crit:
       pdamagemult/=3
       crit=False
      if damagedealt<0:
       damagedealt =0
    pmana-=cspell.spmanacost+citem.manacostmod+carmour.manacostmod
    if cspell.spheal>0:
       php+=cspell.spheal
       if php>pmaxhp:
         php=pmaxhp
       print(f"You healed {cspell.spheal} hp!")
    if cspell.spspecial==2:
      if pstatus!=0:
       pstatus=0
       print("Your status was cured!")
    magic =False
def movechoice():
  global enemy,pdefmod,run,citem,pmana,pdamagemult,ctedef,ehp,php,crit,carmour
  valid = False
  while not valid:
   choice = input("What will you do? 1: Attack 2: Defend 3: Magic 4: Run 5: Inventory ")
   if choice =="1":
     valid = True
     phit()
   elif choice == "2":
     valid=True
     pdefmod +=5
     print("You defended!")
   elif choice =="3":
     valid=True
     spellchoice()
   elif choice =="4": 
     valid=True
     if random.randint(1,2)==2:
       print("You escaped!")
       run=True
       enemy=False
       newencounter()
     else:
       print("You couldn't escape!")
   elif choice =="5":
     print(f"Equipped weapon: {citem.name} Equipped armour: {carmour.name}")
     for x in range(len(inventory)):
          
          print(f"{x+1}: {inventory[x].name}")
     choice = int(input("Which item? 0 to exit "))-1
     if choice> -1 and choice <= len(inventory):
       if inventory[choice].equippable:
        if inventory[choice].itype==1:
          inventory.append(citem)
          citem=inventory[choice]
          print(f"You equipped the {citem.name}")
        elif inventory[choice].itype==2:
          inventory.append(carmour)
          carmour=inventory[choice]
          print(f"You equipped the {carmour.name}")
        inventory.pop(choice)
        valid = True
       elif inventory[choice].ispecial==2:
         pmana+=10
         print(f"You now have {pmana} mana")
         inventory.pop(choice)
         valid = True
       elif inventory[choice].ispecial==3:
         php+=inventory[choice].iheal
         print(f"You now have {php} hp")
         inventory.pop(choice)
         valid=True
       elif inventory[choice].ispecial==4:
         print(f"You used the {inventory[choice].name}")
         if random.randint(1,25)==10:
          pdamagemult*=3
          crit=True
          print("Critical hit!")
         damagedealt =round((damage(inventory[choice].iatk*pdamagemult,ctedef)))
         if crit:
            pdamagemult/=3
            crit=False
         if damagedealt<0:
            damagedealt =0
         print(f"You dealt {damagedealt} damage!")
         ehp-=damagedealt
         print(f"The {cenemy.name} now has {ehp} hp")
         inventory.pop(choice)
         valid =True
         if ehp<=0:
            break
       else:
         print("Nothing happened")
def gamble():
  global gold
  choice=""
  while choice !="y" and choice !="n":
   choice = input("You find what seems to be a slot for gold and a die. Play the game? (y/n) ").lower()
   if choice == "y":
     spent=1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
     while spent>gold:
      spent=int(input(f"You have {gold} gold, how much will you spend? "))
     gold-=spent
     dice=random.randint(1,20)
     print(f"You rolled {dice}! The machine spat out {round(spent*(dice/10))} gold")
     gold+=round(spent*(dice/10))
     newencounter()
   elif choice =="n":
     newencounter()
cvalid = False
while not cvalid:
  pclass =int(input("Choose your class: 1: Knight 2: Mage 3: Archer "))
  if pclass==1:
    patk=15
    pmag=4
    pdef =16
    pmaxhp = 60
    pmaxmana = 10
    atkgrwth=3
    maggrwth=1
    defgrwth=3
    hpgrwth=2
    managrwth=1
    cvalid = True
  elif pclass==2:
    patk = 7
    pmag = 15
    pdef = 7
    pmaxhp = 40
    pmaxmana = 25
    atkgrwth=2
    maggrwth=3
    defgrwth=1
    hpgrwth=1
    managrwth=3
    cvalid=True
  elif pclass==3:
    patk=13
    pmag =7
    pdef =10
    pmaxhp=50
    pmaxmana=15
    atkgrwth=2
    maggrwth=2
    defgrwth=2
    hpgrwth=2
    managrwth=2
    cvalid=True
dragonscale=itemstats("Dragon Scale",3,10,75,0,3,True,0,0,2)
cloak = itemstats("Cloak",0,3,50,0,15,True,-1,0,2)
slimeball=itemstats("Slime Ball",0,0,20,0,0,False,0,0,0)
manacrystal=itemstats("Mana Crystal",0,0,30,2,0,False,0,0,0)
ironswrd= itemstats("Iron Sword",10,3,50,0,1,True,0,0,1)
gun=itemstats("Gun",20,0,100,5,0,True,0,0,1)
shield = itemstats("Shield",3,12,50,0,0,True,0,0,1)
swiftdagger=itemstats("Swift Dagger",4,0,75,1,0,True,0,0,1)
rustdagger=itemstats("Rusty Dagger",5,0,20,0,0,True,0,0,1)
club=itemstats("Club",15,0,60,0,0,True,0,0,1)
staff=itemstats("Staff",4,0,75,0,10,True,-1,0,1)
icewand=itemstats("Ice Wand",0,0,100,3,12,True,2,0,1)
bloodvial=itemstats("Blood Vial",0,0,30,3,0,False,0,20,0)
bomb=itemstats("Bomb",50,0,30,4,0,False,0,0,0)
bow = itemstats("Bow",7,0,35,5,0,True,0,0,1)
honey = itemstats("Honey",0,0,20,3,0,False,0,10,0)
fish = itemstats("Fish",0,0,30,3,0,False,0,20,0)
bone = itemstats("Bone",5,0,20,0,0,True,0,0,1)
scythe=itemstats("Reaper Scythe",17,0,110,6,5,True,0,0,1)
lthrarmr=itemstats("Leather Armour",0,3,40,0,0,True,0,0,2)
iceshard=itemstats("Ice Shard",10,0,40,3,0,True,0,0,1)
assknife=itemstats("Assassin Knife",15,0,75,7,0,True,0,0,1)
platearmour=itemstats("Plate Armour",0,15,100,0,0,True,1,0,2)
nothing=itemstats("Nothing",0,0,0,0,0,True,0,0,0)
bees = enemystats("Bee Swarm",17,5,10,15,25,0,0,honey,4)
skeleton = enemystats("Skeleton",20,7,17,10,50,0,0,bone,3)
dragon=enemystats("Dragon",35,20,50,100,150,4,0,dragonscale,20)
slime = enemystats("Slime",16,10,20,10,20,6,0,slimeball,4)
bandit= enemystats("Bandit",20,3,20,40,20,0,0,rustdagger,5)
troll = enemystats("Troll",25,15,20,30,30,1,0,club,7)
mage = enemystats("Mage",10,5,15,30,20,2,0,manacrystal,30)
thingy=enemystats("Thingy",16,5,40,30,30,2,0,0,10)
golem = enemystats("Golem",25,30,30,60,60,1,0,0,5)
icewitch= enemystats("Ice Witch",10,7,20,50,50,2,1,icewand,30)
icegolem=enemystats("Ice Golem",20,20,35,60,50,0,1,iceshard,15)
vampire = enemystats("Vampire",25,10,30,50,50,5,0,bloodvial,20)
mech = enemystats("Mech",25,25,50,100,100,4,0,gun,30)
mimic=enemystats("Mimic",20,15,20,75,50,0,0,ironswrd,10)
bomber=enemystats("Bomber",60,5,5,20,20,7,0,bomb,5)
ghost=enemystats("Ghost",25,0,20,40,40,8,0,0,15)
assassin=enemystats("Assassin",25,10,25,40,40,9,0,assknife,10)
magicmissile = spellstats("Magic Missile",5,0,3,0)
heal=spellstats("Heal",0,round(pmaxhp/2),5,2)
meteorstrike = spellstats("Meteor Strike",30,0,8,0)
lifedrain=spellstats("Life Drain",15,0,6,1)
thing=bees
alive = True
magic = False
frozen=False
efrozen=False
patkmod=0
pdefmod=0#
eatkmod=0
edefmod=0
#while True:
 #y=input()
 #y=y.lower()
# search(y)
pdamagemult=1
edamagemult=1
turncount=0
pstatus =0
crit=False
gold=0
xp=0
level=1
pmana=pmaxmana
php=pmaxhp
inventory=[]
if pclass==3:
  citem=bow
else:
 citem=nothing
carmour = nothing
attacks=1
cenemy=skeleton
ehp=cenemy.emaxhp
enemy=True
run =False
print(f"You encountered a {cenemy.name}!")
while alive==True:
 ctpatk=patk+citem.iatk+patkmod
 ctpdef=pdef+citem.idef+pdefmod
 cteatk=cenemy.eatk+eatkmod
 ctedef=cenemy.edef + edefmod
 if not frozen:
  movechoice()
 else:
   print("You can't move!")
   frozen=False
 if ehp>0 and not run:
  ehit()
  turncount+=1
 if pstatus==1:
   php -= round(pmaxhp/10)
   print(f"You took {round(pmaxhp/10)} poison damage! You now have {php} hp")
   hpcheck()
   if not alive:
     break
 run=False
 if alive:
  if ehp<=0:
   print("You won!")
   time.sleep(1)
   newencounter()
print("You died!")
time.sleep(10)