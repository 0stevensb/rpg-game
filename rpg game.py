import random
import time
import os
class enemystats():
    def __init__(self,name,eatk,edef,emaxhp,goldrp,expdrp,especial1,especial2,itemdrop,emag):
        self.name =name
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
  def __init__(self,name,iatk,idef,goldcst,ispecial1,ispecial2,imag,equippable,manacstmod,iheal,itype,components,plus,imana):
    self.name=name
    self.type =2
    self.iatk=iatk
    self.idef=idef
    self.goldcst=goldcst
    self.ispecial1=ispecial1
    self.ispecial2=ispecial2
    self.imag = imag
    self.equippable=equippable
    self.manacostmod=manacstmod
    self.iheal=iheal
    self.itype = itype
    self.components=components
    self.plus=plus
    self.imana=imana
class spellstats():
  def __init__(self,name,spdamage,spheal,spmanacost,spspecial):
    self.name=name
    self.spdamage=spdamage
    self.spheal=spheal
    self.spmanacost = spmanacost
    self.spspecial=spspecial
def enemyencounter():
   global enemy,cenemy
   enemy=True
   z=random.randint(1,21)
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
   elif z==17:
     cenemy=spikeball
   elif z==18:
     cenemy=demon
   elif z ==19:
     cenemy=mercenary
   elif z==20:
     cenemy=ent
   elif z ==21:
     cenemy=miner
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
    global ehp, pdamagemult,crit,ctpdef,cteatk,pstatus,efrozen,estatus,php,pmag,patkmod,edefmod
    attacks=1
    if citem.ispecial1==1:
      attacks+=1
    if pclass==4:
      attacks+=1
    for i in range(attacks):
     if php>0:
      ctpatk=patk+citem.iatk+patkmod+carmour.iatk
      ctedef=cenemy.edef + edefmod
      if (random.randint(1,25)==10 and citem.ispecial1!=7) or (random.randint(1,5)==5 and citem.ispecial1==7):
        pdamagemult*=3
        crit=True
        print("Critical hit!")
      if citem.ispecial1==13 and cenemy.especial2==2:
        pdamagemult*=2
      if citem.ispecial1==9:
        damagedealt=round(damage(round((ctpatk+pmag+citem.imag+carmour.imag)/2)*pdamagemult,round((ctedef+cenemy.emag)/2)))
      elif citem.ispecial1==10:
        damagedealt =round(damage(ctpatk*pdamagemult,cenemy.emag))
      elif citem.ispecial1==15:
        damagedealt=round(damage(pmag+citem.imag+carmour.imag*pdamagemult,cenemy.emag))
      else:
        damagedealt =round(damage(ctpatk*pdamagemult,ctedef))
      if crit:
        pdamagemult/=3
        crit=False
      if random.randint(1,2)==1 and citem.ispecial2==1:
          estatus=2
          print(f"The {cenemy.name} was burned!")
      if citem.ispecial1==13 and cenemy.especial2==2:
        pdamagemult/=2
      if damagedealt<0 or (cenemy.especial1==8 and citem.ispecial1!=15):
        damagedealt =0
      print(f"You dealt {damagedealt} damage!")
      ehp-=damagedealt
      if cenemy.especial1==6 and random.randint(1,4)==1 and pstatus==0 and citem.ispecial1!=5 and citem.ispecial1!=15:
        print("You were poisoned!")
        pstatus = 1
      if cenemy.especial1==10 and citem.ispecial1!=5:
        php-=5
        print(f"You took 5 damage due to spikes! You now have {php} hp")
        hpcheck()
      if citem.ispecial1==8 and random.randint(1,3)==3 and cenemy.especial2!=1 and cenemy.especial1!=8:
        efrozen+=1
        print(f"The {cenemy.name} was frozen!")
      if citem.ispecial1==12 and cenemy.especial1!=6 and random.randint(1,3)==2 and estatus==0 and cenemy.especial1!=8:
        estatus=1
        print(f"The {cenemy.name} was poisoned!")
      if citem.ispecial1==14 and damagedealt>0:
        php+=round(damagedealt/2)
        print(f"You healed {round(damagedealt/2)} hp!")
        patkmod+=1
      print(f"The {cenemy.name} now has {ehp} hp")
      if ehp<=0:
        break
def ehit():
  global php,edamagemult,crit,ctpatk,ctedef,frozen,efrozen,ehp,eatkmod,edefmod,pstatus,pdefmod,pmagdefmod
  ctpatk=patk+citem.iatk+patkmod+carmour.iatk
  ctpdef=pdef+citem.idef+pdefmod+carmour.idef
  cteatk=cenemy.eatk+eatkmod
  ctedef=cenemy.edef + edefmod
  if (cenemy.especial1!=1 or turncount%2==0) and efrozen==0:
   if (random.randint(1,25)==10 and cenemy.especial1!=9) or (random.randint(1,5)==5 and cenemy.especial1==9):
      crit=True
      edamagemult*=3
      print("Critical hit!")
    
   if cenemy.especial1==2 or (cenemy.especial1==4 and random.randint(1,3)==3): 
    damagedealt=round(damage(cenemy.emag*edamagemult,pmag+citem.imag+carmour.imag+pmagdefmod))
   else:
     if estatus==2:
       edamagemult/=2
     damagedealt =round(damage(cteatk*edamagemult,ctpdef))
     if estatus==2:
       edamagemult*=2
   if crit:
    edamagemult/=3
    crit=False
   if damagedealt<0:
      damagedealt =0
   print(f"The {cenemy.name} dealt {damagedealt} damage!")
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
     frozen+=1
     print("You were frozen!")
   if cenemy.especial1 == 7:
     ehp=0
     print(f"The {cenemy.name} exploded!")
     hpcheck()
  
  else:
    print(f"The {cenemy.name} did nothing....")
    if efrozen<0:
     efrozen-=1
  pdefmod=0
  pmagdefmod=0
  hpcheck()
def chest():
  global gold,citem,cenemy,ehp,turncount,alive,enemy,php
  choice=""
  while choice != "y" and choice!="n":
   choice = input("You found a chest! Open it? (y/n) ")
   if choice =="y":
     x=random.randint(1,6)
     if x  ==1:
       gold+=50
       os.system("clear")
       print("It contained 50 gold!")
       time.sleep(1)
       newencounter()
     elif x<=3:
       os.system("clear")
       x=random.randint(1,14)
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
       elif x ==8:
         y=magicsword
       elif x == 9:
         y=plasmasword
       elif x == 10:
         y=crossbow
       elif x == 11:
         y=icebomb
       elif x == 12:
         y=toxdagger
       elif x == 13:
         y=silverblade
       elif x == 14:
         y=smokebomb
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
       else:
        inventory.append(y)
        time.sleep(1)
       newencounter() 
     elif x==4:
       print("It's a mimic!")
       cenemy=mimic
       ehp=cenemy.emaxhp
       turncount=0
       enemy=True
     elif x==5:
       os.system("clear")
       print("It's a trap!")
       php-= 10 
       print("You took 10 damage")
       hpcheck()
       if alive ==False:
         break
       time.sleep(1)
       newencounter()
     elif x==6:
       os.system("clear")
       print("It's empty...")
       time.sleep(1)
       newencounter()
   elif choice =="n":
     os.system("clear")
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
  os.system("clear")
  newencounter()
def newencounter():
  global gold,xp,ehp,cenemy,php,level,patk,pdef,pmaxhp,enemy,edamagemult,turncount,citem,pmag,pmaxmana,pmana,patkmod,pdefmod,eatkmod,edefmod,atkgrwth,defgrwth,maggrwth,managrwth,hpgrwth,efrozen,carmour,emaxhp,estatus,run
  efrozen=0
  estatus=0
  if enemy:
   if citem.ispecial1==6:
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
    if pclass==2:
     g=random.randint(1,3)
    else:
      g=random.randint(1,4)
    if g==1 and len(spells)<12:
      valid = False
      while not valid:
       y=random.randint(1,12)
       if y==1:
         newspell=heal
       elif y==2:
         newspell=meteorstrike
       elif y==3:
         newspell=lifedrain
       elif y==4:
         newspell=judgement
       elif y==5:
         newspell=thunderbolt
       elif y==6:
         newspell=fireball
       elif y==7:
         newspell=magicmissile
       elif y==8:
         newspell=barrier
       elif y==9:
         newspell=blizzard
       elif y ==10:
         newspell=sludge
       elif y==11:
         newspell=teleport
       elif y==12:
         newspell=selfdestruct
       if not newspell in spells:
         valid = True
         spells.append(newspell)
         print(f"You learned {newspell.name}!")
         
   time.sleep(1)
  enemy=False
  if not run:
   os.system("clear")
  y= random.randint(1,6)
  if y==1:
    if pick in inventory or citem==pick:
     y=random.randint(1,10)
    else:
      y=random.randint(1,9)
    if y<=2:
     shop()
    elif y<=4:
      chest()
    elif y<=6:
      workshop()
    elif y==7:
      bombshop()
    elif y==8:
      fishinghole()
    elif y==9:
     gamble()
    elif y==10:
      mine()
  else:
   enemyencounter()
   ehp=cenemy.emaxhp
   print(f"You encountered a {cenemy.name}! You have {php}/{pmaxhp} hp")
   turncount=0
def mine():
  print("You found a large deposit of various ores!")
  for x in range(random.randint(2,5)):
   inventory.append(iron)
  for x in range(random.randint(1,3)):
    inventory.append(silver)
  for x in range(3):
    inventory.append(coal)
  time.sleep(1)
  os.system("clear")
  newencounter()
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
            x=random.randint(1,6)
            if x<=3:
              inventory.append(bomb)
            elif x==4:
             inventory.append(icebomb)
            elif x==5:
              inventory.append(toxbomb)
            elif x==6:
              inventory.append(smokebomb)
            gold-=60
            bought+=1
          else:
            print("Insufficent gold")
        elif choice2 =="n":
          exit = True    
      os.system("clear")
      newencounter()  
    if choice =="n":
     os.system("clear")
     print("You have enough issues as is")  
     newencounter()
def shop():
  global gold,xp,patk,php,pmaxhp,citem,pstatus,carmour
  os.system("clear")
  print("You found a shop!")
  exit = False
  stock=[]
  for x in range(6):
      valid = False
      while not valid:
        y=random.randint(1,17)
        if y==1:
          newitem=healpot
        elif y==2:
          newitem=ironswrd
        elif y==3:
          newitem=shield
        elif y==4:
          newitem = bomb
        elif y==5:
          newitem=lthrarmr
        elif y ==6:
          newitem=platearmour
        elif y ==7:
          newitem=swiftdagger
        elif y==8:
          newitem=bomb
        elif y == 9:
          newitem=bow
        elif y==10:
          newitem=crossbow
        elif y ==11:
          newitem=staff
        elif y==12:
          newitem=honey
        elif y ==13:
          newitem=shield
        elif y==14:
          newitem=gun
        elif y==15:
          newitem=cloak
        elif y==16:
          newitem=mace
        elif y==17:
          newitem=manacrystal
        elif y==18:
          newitem=manapot
        if newitem not in stock:
          stock.append(newitem)
          valid = True
  while not exit:
    if len(stock)==0:
      exit=True
      os.system("clear")
      newencounter()
    print(f"You have {gold} gold and {php}/{pmaxhp} hp. Your current equipped weapon is {citem.name} and armour is {carmour.name}")
    print("The shop is selling:")
    for x in range(len(stock)):
        print(f"{x+1}: {stock[x].name} ({stock[x].goldcst*2} gold)")
    choice = int(input("Which item would you like to buy? 0 to exit, -1 to sell "))-1
    if choice>= 0 and choice <= len(stock):
        if gold>=stock[choice].goldcst*2:
         print(f"You bought the {stock[choice].name} for {stock[choice].goldcst*2} gold!")
         gold-=stock[choice].goldcst*2
         if stock[choice].equippable:
          if stock[choice].itype==1:
            if citem!=nothing:
              inventory.append(citem)
            citem=stock[choice]
          elif stock[choice].itype==2:
            if carmour!=nothing:
              inventory.append(carmour)
            carmour=stock[choice]
          os.system("clear")
          print(f"You equipped the {stock[choice].name}!")
         else:
            inventory.append(stock[choice])
         stock.pop(choice)
        else:
          print("Insufficient gold!")
    elif choice==-1:
      exit=True
      os.system("clear")
      newencounter()
    elif choice ==-2:
      os.system("clear")
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
def spellchoice():
  global cspell, magic
  valid = False
  while not valid:
    
    for i in range(len(spells)):
      print(f"{i+1}: {spells[i].name} ({spells[i].spmanacost+citem.manacostmod+carmour.manacostmod} mana)")
    choice = int(input(f"What spell will you use? You have {pmana} mana. 0 to exit "))-1
    if choice == -1:
        os.system("clear")
        valid = True
        movechoice()
    elif choice <= len(spells)-1:
      if pmana >=spells[choice].spmanacost+citem.manacostmod+carmour.manacostmod:
       cspell =spells[choice]
       magic = True
       valid = True
      else:
        print("Insuffient mana")
    if magic == True:
      pmaghit()
def pmaghit():
    global ehp, pdamagemult,crit,ctpdef,cteatk,pmag,emag,magic,pmana,citem,php,efrozen,pstatus,carmour,estatus,pmagdefmod,pdefmod,run,enemy
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
      if (citem.ispecial1==3 or cspell.spspecial==6) and random.randint(1,3)==3:
       efrozen+=1
       print(f"The {cenemy.name} was frozen!")
      if cspell.spspecial==4 and random.randint(1,3)==3 and estatus ==0:
        print(f"The {cenemy.name} was burned!")
        estatus=2
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
    if cspell.spspecial==3:
      ehp =0
    if cspell.spspecial==5:
      pdefmod+=round(pmag/2)
      pmagdefmod+=round(pmag/2)
      print("You shielded yourself!")
    if cspell.spspecial==7 and cenemy.especial1!=6 and random.randint(1,3)==2 and estatus==0:
       estatus=1
       print(f"The {cenemy.name} was poisoned!")
    if cspell.spspecial==8:
         os.system("clear")
         print("You escaped!")
         run=True
         enemy=False
         newencounter()
    if cspell.spspecial==9:
      php-=round(damagedealt/2)
      print(f"You took {round(damagedealt/2)} recoil damage!")
      print(f"You have {php} hp")
      hpcheck()
    magic =False
def movechoice():
  global enemy,pdefmod,run,citem,pmana,pdamagemult,ctedef,ehp,php,crit,carmour,efrozen,estatus,pstatus
  valid = False
  while not valid:
   choice = input("What will you do? 1: Attack 2: Defend 3: Magic 4: Run 5: Rest 6: Inventory ")
   os.system("clear")
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
     if random.randint(1,4)<4:
       os.system("clear")
       print("You escaped!")
       run=True
       enemy=False
       newencounter()
     else:
       print("You couldn't escape!")
   elif choice == "5":
     valid=True
     print("You rested!")
     php+=10
     pmana+=5
     if php>pmaxhp:
       php=pmaxhp
     if pmana>pmaxmana:
       pmana=pmaxmana
     print(f"You now have {php} hp and {pmana} mana")
   elif choice =="6":
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
       elif inventory[choice].ispecial1==2:
         pmana+=inventory[choice].imana
         print(f"You now have {pmana} mana")
         inventory.pop(choice)
         valid = True
       elif inventory[choice].ispecial1==3:
         php+=inventory[choice].iheal
         if inventory[choice]==healpot and pstatus!=0:
           pstatus=0
           print("Your staus was cured!")
         print(f"You now have {php} hp")
         inventory.pop(choice)
         valid=True
       elif inventory[choice].ispecial1==15:
         os.system("clear")
         print("You escaped!")
         run=True
         enemy=False
         inventory.pop(choice)
         newencounter()
       elif inventory[choice].ispecial1==4 or inventory[choice].ispecial1==12 or inventory[choice].ispecial1==14:
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
         if inventory[choice].ispecial1==12:
          efrozen+=2
          print("The enemy was frozen!")
         elif inventory[choice].ispecial1==14:
          estatus=1
          print("The enemy was poisoned!")
         print(f"The {cenemy.name} now has {ehp} hp")
         inventory.pop(choice)
         valid =True
         if ehp<=0:
            break
       else:
         print("Nothing happened")
     else:
       os.system("clear")    
def gamble():
  global gold
  choice=""
  while choice !="y" and choice !="n":
   choice = input("You find what seems to be a slot for gold and a die. Play the game? (y/n) ").lower()
   if choice == "y":
     spent=-1
     while spent>gold or spent==-1:
      spent=int(input(f"You have {gold} gold, how much will you spend? "))
     gold-=spent
     dice=random.randint(1,20)
     os.system("clear")
     print(f"You rolled {dice}! The machine spat out {round(spent*(dice/10))} gold")
     gold+=round(spent*(dice/10))
     time.sleep(1)
     newencounter()
   elif choice =="n":
     os.system("clear")
     newencounter()
def workshop():
  choice =""
  while choice !="y" and choice!="n":
    choice=input("You find what appears to be an abandoned workshop. Check it out? (y/n) ")
  if choice =="n":
    os.system("clear")
    newencounter()
  elif choice=="y":
    exit = False
    while not exit:
      choice = int(input("You spot a crafting bench (1) and a setup for disassembling items (2). Will you use them or leave? (3) "))
      if choice ==3:
        exit=True
        os.system("clear")
        newencounter()
      elif choice ==1:
        crafting()
      elif choice ==2:
        disassemble()
def crafting():
  global citem,carmour,citem
  craftinv=inventory.copy()
  craftitems=[]
  craft=False
  succesfulcraft=False
  numcraft=1
  while len(craftitems)<4 and not craft:
   print("Inventory:")
   for x in range(len(craftinv)):
        print(f"{x+1}: {craftinv[x].name}")
   choice = int(input("Which items would you like to craft with? 0 to craft, -1 to exit "))-1
   if choice != -1 and choice!=-2:
    craftitems.append(craftinv.pop(choice))
   if choice==-1:
     craft=True
     if len(craftitems)==2 and craftitems[0]==craftitems[1] and craftitems[0].plus !=0:
       succesfulcraft=True
       crafteditem=craftitems[0].plus
       for x in range(2):
         inventory.pop(inventory.index(craftitems[0]))
     elif craftitems.count(iron)==3:
       succesfulcraft=True
       crafteditem=greatsword
       for x in range(2):
         inventory.pop(inventory.index(iron))
     elif craftitems.count(iron)==1 and craftitems.count(coal)==1:
       succesfulcraft=True
       crafteditem=steel
       inventory.pop(inventory.index(iron))
       inventory.pop(inventory.index(coal))
     elif craftitems.count(dagger)==1 and craftitems.count(slimeball)==1:
       succesfulcraft=True
       crafteditem=toxdagger
       inventory.pop(inventory.index(dagger))
       inventory.pop(inventory.index(slimeball))
     elif craftitems.count(bomb)==1 and craftitems.count(slimeball)==1:
       succesfulcraft=True
       crafteditem=toxbomb
       inventory.pop(inventory.index(bomb))
       inventory.pop(inventory.index(slimeball))
       numcraft=2
     elif craftitems.count(iron)==2:
       succesfulcraft=True
       crafteditem=ironswrd
       for x in range(2):
         inventory.pop(inventory.index(iron))
     elif craftitems.count(wood)==1 and craftitems.count(manacrystal)==1:
       succesfulcraft=True
       crafteditem=staff
       inventory.pop(inventory.index(wood))
       inventory.pop(inventory.index(manacrystal))
     elif craftitems.count(wood)==1 and craftitems.count(spikybarb)==1:
       succesfulcraft=True
       crafteditem=mace
       inventory.pop(inventory.index(wood))
       inventory.pop(inventory.index(spikybarb))
     elif craftitems.count(wood)==1 and craftitems.count(iron)==1:
       succesfulcraft=True
       crafteditem=crossbow
       inventory.pop(inventory.index(wood))
       inventory.pop(inventory.index(iron))
     elif craftitems.count(wood)==1:
       succesfulcraft=True
       crafteditem=shield
       inventory.pop(inventory.index(wood))
     elif craftitems.count(healpot)==1 and craftitems.count(honey)==1:
       succesfulcraft=True
       crafteditem=bighealpot
       inventory.pop(inventory.index(healpot))
       inventory.pop(inventory.index(honey)) 
     elif craftitems.count(dagger)==1 and craftitems.count(bloodvial)==1:
       succesfulcraft=True
       crafteditem=vampknife
       inventory.pop(inventory.index(dagger))
       inventory.pop(inventory.index(bloodvial)) 
     elif craftitems.count(steel)==2:
       succesfulcraft=True
       crafteditem=gun
       for x in range(2):
         inventory.pop(inventory.index(steel))
     elif craftitems.count(silver)==1 and craftitems.count(iceshard)==1:
       succesfulcraft=True
       crafteditem=icewand
       inventory.pop(inventory.index(silver))
       inventory.pop(inventory.index(iceshard))
     elif craftitems.count(silver)==1 and craftitems.count(coal)==1:
       succesfulcraft=True
       crafteditem=flamethrower
       inventory.pop(inventory.index(steel))
       inventory.pop(inventory.index(coal))
     elif craftitems.count(iron)==1:
       succesfulcraft=True
       crafteditem=dagger
       inventory.pop(inventory.index(iron))
     elif craftitems.count(silver)==2:
       succesfulcraft=True
       crafteditem=silverblade
       for x in range(2):
         inventory.pop(inventory.index(silver))
     if succesfulcraft==True:
       for x in range(numcraft):
        print(f"You crafted a {crafteditem.name}!") 
        if crafteditem.equippable:
          if crafteditem.itype==1:
            if citem!=nothing:
              inventory.append(citem)
            citem=crafteditem
          elif crafteditem.itype==2:
            if carmour!=nothing:
              inventory.append(carmour)
            carmour=crafteditem
          print(f"You equipped the {crafteditem.name}!")
        else:
            inventory.append(crafteditem)
       numcraft=1
       time.sleep(1)
       os.system("clear")
     else:
       print("That doesn't make anything...")   
       time.sleep(1)
       os.system("clear")
def disassemble():
  global carmour,citem
  print(f"Current weapon: {citem.name} Current armour: {carmour.name}")
  print("Inventory:")
  for x in range(len(inventory)):
        print(f"{x+1}: {inventory[x].name}")
  choice = int(input("Which items would you like to disassemble? 0 to exit, -1 for current weapon, -2 for current armour "))-1
  if choice >=0:
   if len(inventory[choice].components)>0:
    for x in range(len(inventory[choice].components)):
     inventory.append((inventory[choice].components)[x])
     print(f"You got {inventory[choice].components[x].name}")
    inventory.pop(choice)
    time.sleep(1)
    os.system("clear")
   else:
     print("That item cannot be disassembled")
  elif choice ==-2:
    if len(citem.components)>0:
     for x in range(len(citem.components)):
      inventory.append((citem.components)[x])
      print(f"You got {citem.components[x].name}")
     citem=nothing
     time.sleep(1)
     os.system("clear")
    else:
     print("That item cannot be disassembled")
  elif choice ==-3:
    if len(carmour.components)>0:
     for x in range(len(carmour.components)):
      inventory.append((carmour.components)[x])
      print(f"You got {carmour.components[x].name}")
     carmour=nothing
     time.sleep(1)
     os.system("clear")
    else:
     print("That item cannot be disassembled")

cvalid = False
while not cvalid:
  pclass =int(input("Choose your class: 1: Knight 2: Mage 3: Archer 4: Rogue "))
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
  elif pclass ==4:
    patk=10
    pmag=8
    pdef=6
    pmaxhp=40
    pmaxmana=15
    atkgrwth=3
    maggrwth=2
    defgrwth=1
    hpgrwth=1
    managrwth=2
    cvalid=True
slimeball=itemstats("Slime Ball",0,0,20,0,0,0,False,0,0,0,[],0,0)
iron=itemstats("Iron",0,0,20,0,0,0,False,0,0,0,[],0,0)
steel=itemstats("Steel",0,0,40,0,0,0,False,0,0,0,[],0,0)
wood=itemstats("Wood",0,0,10,0,0,0,False,0,0,0,[],0,0)
silver=itemstats("Silver",0,0,50,0,0,0,False,0,0,0,[],0,0)
coal=itemstats("Coal",0,0,10,0,0,0,False,0,0,0,[],0,0)
manacrystal=itemstats("Mana Crystal",0,0,30,2,0,0,False,0,0,0,[],0,10)
dscaleplus=itemstats("Dragon Scale+",5,15,150,0,0,6,True,-1,0,2,[],0,0)
dragonscale=itemstats("Dragon Scale",3,10,75,0,0,3,True,0,0,2,[],dscaleplus,0)
greatswordplus =itemstats("Greatsword+",20,7,200,0,0,0,True,0,0,1,[steel,iron],0,0)
greatsword =itemstats("Greatsword",15,5,100,0,0,0,True,0,0,1,[iron,iron],greatswordplus,0)
cloakplus = itemstats("Cloak+",0,8,100,0,0,20,True,-2,0,2,[],0,0)
cloak = itemstats("Cloak",0,3,50,0,0,15,True,-1,0,2,[manacrystal],cloakplus,0)
ironswrd= itemstats("Iron Sword",10,3,50,0,0,0,True,0,0,1,[iron],greatsword,0)
gunplus=itemstats("Gun+",25,0,200,5,0,0,True,0,0,1,[steel],0,0)
gun=itemstats("Gun",30,0,100,5,0,0,True,0,0,1,[iron],gunplus,0)
shieldplus = itemstats("Shield+",6,17,100,0,0,0,True,0,0,1,[steel],0,0)
shield = itemstats("Shield",3,12,50,0,0,0,True,0,0,1,[iron],shieldplus,0)
swiftplus=itemstats("Swift Dagger+",8,0,200,1,0,0,True,0,0,1,[steel],0,0)
swiftdagger=itemstats("Swift Dagger",4,0,100,1,0,0,True,0,0,1,[iron],swiftplus,0)
daggerplus=itemstats("Dagger+",10,0,70,0,0,0,True,0,0,1,[steel],0,0)
dagger=itemstats("Dagger",7,0,35,0,0,0,True,0,0,1,[iron],daggerplus,0)
rustdagger=itemstats("Rusty Dagger",5,0,20,0,0,0,True,0,0,1,[iron],dagger,0)
clubplus=itemstats("Club+",20,0,120,0,0,0,True,0,0,1,[wood,wood],0,0)
club=itemstats("Club",15,0,60,0,0,0,True,0,0,1,[wood],clubplus,0)
staffplus=itemstats("Staff+",6,0,150,0,0,15,True,-2,0,1,[wood,manacrystal],0,0)
staff=itemstats("Staff",4,0,75,0,0,10,True,-1,0,1,[wood],staffplus,0)
icewandplus=itemstats("Ice Wand+",0,0,200,3,0,16,True,2,0,0,[manacrystal],0,0)
icewand=itemstats("Ice Wand",0,0,100,3,0,12,True,2,0,1,[manacrystal],icewandplus,0)
bloodvial=itemstats("Blood Vial",0,0,30,3,0,0,False,0,20,0,[],0,0)
bomb=itemstats("Bomb",50,0,30,4,0,0,False,0,0,0,[],0,0)
icebomb=itemstats("Ice Bomb",10,0,60,12,0,0,False,0,0,0,[],0,0)
toxbomb=itemstats("Toxic Bomb",5,0,40,14,0,0,False,0,0,0,[],0,0)
smokebomb=itemstats("Smoke Bomb",0,0,60,15,0,0,False,0,0,0,[],0,0)
bowplus = itemstats("Bow+",10,0,70,5,0,0,True,0,0,1,[wood,wood],0,0)
bow = itemstats("Bow",7,0,35,5,0,0,True,0,0,1,[wood],bowplus,0)
crossbowplus = itemstats("Crossbow+",15,0,140,5,0,0,True,0,0,1,[wood,steel],0,0)
crossbow = itemstats("Crossbow",12,0,75,5,0,0,True,0,0,1,[wood],crossbowplus,0)
honey = itemstats("Honey",0,0,20,3,0,0,False,0,10,0,[],0,0)
fish = itemstats("Fish",0,0,30,3,0,0,False,0,20,0,[],0,0)
bone = itemstats("Bone",5,0,20,0,0,0,True,0,0,1,[],0,0)
scytheplus=itemstats("Reaper Scythe+",23,0,220,6,0,10,True,0,0,1,[steel,steel],0,0)
scythe=itemstats("Reaper Scythe",17,0,110,6,0,5,True,0,0,1,[steel],scytheplus,0)
lthrplus=itemstats("Leather Armour+",0,6,80,0,0,0,True,0,0,2,[],0,0)
lthrarmr=itemstats("Leather Armour",0,3,40,0,0,0,True,0,0,2,[],lthrplus,0)
iceshard=itemstats("Ice Shard",10,0,40,8,0,0,True,0,0,1,[],0,0)
assknifeplus=itemstats("Assassin Knife+",20,0,150,7,0,0,True,0,0,1,[steel],0,0)
assknife=itemstats("Assassin Knife",15,0,75,7,0,0,True,0,0,1,[iron],assknifeplus,0)
magicplus=itemstats("Magic Sword+",15,0,250,9,0,15,True,0,0,1,[steel,manacrystal],0,0)
magicsword=itemstats("Magic Sword",12,0,125,9,0,12,True,0,0,1,[iron,manacrystal],magicplus,0)
mechplus=itemstats("Mech Suit+",20,20,400,0,0,20,True,0,0,2,[steel,steel,manacrystal],0,0)
mechsuit=itemstats("Mech Suit",15,15,200,0,0,15,True,0,0,2,[steel,steel],mechplus,0)
plateplus=itemstats("Plate Armour+",2,20,200,0,0,0,True,1,0,2,[steel],0,0)
platearmour=itemstats("Plate Armour",0,15,100,0,0,0,True,1,0,2,[iron],plateplus,0)
plasmaplus=itemstats("Plasma Sword+",17,1,200,12,0,0,True,0,0,1,[steel,steel],0,0)
plasmasword=itemstats("Plasma Sword",14,1,100,10,0,0,True,0,0,1,[steel],plasmaplus,0)
spikybarb=itemstats("Spiky Barb",0,0,0,11,0,0,False,0,0,0,[],0,0)
toxdaggerplus=itemstats("Toxic Dagger+",10,0,150,12,0,0,True,0,0,1,[steel],0,0)
toxdagger=itemstats("Toxic Dagger",7,0,75,12,0,0,True,0,0,1,[iron],toxdaggerplus,0)
silverplus=itemstats("Silver Blade+",15,1,150,13,0,2,True,0,0,1,[silver,silver],0,0)
silverblade=itemstats("Silver Blade",10,1,75,13,0,2,True,0,0,1,[silver],silverplus,0)
healpot = itemstats("Health Potion",0,0,40,3,0,0,False,0,30,0,[],0,0)
bighealpot=itemstats("Big Health Potion",0,0,80,3,0,0,False,0,100,0,[],0,0)
manapot=itemstats("Mana Potion",0,0,70,2,0,0,False,0,30,0,[],0,50)
maceplus = itemstats("Mace+",15,0,100,0,0,0,True,0,0,1,[steel],0,0)
mace = itemstats("Mace",10,0,50,0,0,0,True,0,0,1,[iron],maceplus,0)
vampplus=itemstats("Vampire Knife+",13,0,200,14,0,2,True,0,0,1,[steel],0,0)
vampknife=itemstats("Vampire Knife",9,0,100,14,0,1,True,0,0,1,[iron],vampplus,0)
pick=itemstats("Pickaxe",6,0,40,0,0,0,True,0,0,1,[iron],0,0)
flamethrowerplus=itemstats("Flamethrower+",0,0,200,15,1,20,True,0,0,1,[steel,coal],0,0)
flamethrower=itemstats("Flamethrower",0,0,100,15,1,15,True,0,0,1,[steel],flamethrowerplus,0)
nothing=itemstats("Nothing",0,0,0,0,0,0,True,0,0,0,[],0,0)
bees = enemystats("Bee Swarm",17,5,10,15,25,0,0,honey,4)
skeleton = enemystats("Skeleton",20,7,17,10,50,0,0,bone,3)
dragon=enemystats("Dragon",35,20,50,100,150,4,0,dragonscale,20)
slime = enemystats("Slime",16,10,20,10,20,6,0,slimeball,4)
bandit= enemystats("Bandit",23,3,20,40,20,0,0,rustdagger,5)
troll = enemystats("Troll",25,15,20,30,30,1,0,club,7)
mage = enemystats("Mage",10,5,15,30,20,2,0,manacrystal,30)
thingy=enemystats("Thingy",16,5,40,30,30,3,0,0,10)
golem = enemystats("Golem",30,30,30,60,60,1,0,iron,5)
icewitch= enemystats("Ice Witch",10,7,20,50,50,2,1,icewand,30)
icegolem=enemystats("Ice Golem",20,20,35,60,50,0,1,iceshard,10)
vampire = enemystats("Vampire",25,10,30,50,70,5,2,bloodvial,20)
mech = enemystats("Mech",25,25,50,100,100,4,0,mechsuit,30)
mimic=enemystats("Mimic",20,15,20,75,50,0,0,ironswrd,10)
bomber=enemystats("Bomber",60,5,5,20,20,7,0,bomb,5)
ghost=enemystats("Ghost",25,0,20,40,40,8,0,0,15)
assassin=enemystats("Assassin",25,10,25,40,40,9,0,assknife,10)
spikeball=enemystats("Spike Ball",15,15,20,30,30,10,0,spikybarb,5)
demon=enemystats("Demon",20,15,40,60,60,4,2,0,25)
mercenary=enemystats("Mercenary",20,10,30,70,50,0,0,crossbow,10)
ent=enemystats("Ent",25,15,30,50,40,0,0,wood,10)
miner=enemystats("Miner",17,10,20,30,20,0,0,pick,5)
magicmissile = spellstats("Magic Missile",5,0,3,0)
thunderbolt = spellstats("Thunderbolt",7,0,4,0)
heal=spellstats("Heal",0,round(pmaxhp/2),5,2)
meteorstrike = spellstats("Meteor Strike",30,0,8,0)
lifedrain=spellstats("Life Drain",10,0,6,1)
judgement = spellstats("Judgement",0,0,20,3)
fireball= spellstats("Fireball",10,0,5,4)
barrier = spellstats("Barrier",0,0,5,5)
blizzard = spellstats("Blizzard",20,0,7,6)
sludge=spellstats("Sludge Blast",9,0,7,7)
teleport=spellstats("Teleport",0,0,9,8)
selfdestruct=spellstats("Self Destruct",50,0,10,9)
thing=bees
alive = True
magic = False
frozen=0
efrozen=0
patkmod=0
pdefmod=0#
eatkmod=0
edefmod=0
pmagdefmod=0
#while True:
 #y=input()
 #y=y.lower()
# search(y)
pdamagemult=1
edamagemult=1
turncount=0
pstatus =0
estatus = 0
crit=False
gold=50
xp=0
level=1
pmana=pmaxmana
php=pmaxhp
inventory=[]
spells=[]
citem=nothing
carmour=nothing
if pclass==2:
 spells.append(magicmissile)
elif pclass==3:
  citem=bow
elif pclass==4:
 citem=vampknife
attacks=1
enemyencounter()
ehp=cenemy.emaxhp
run =False
asdfj=True
print(f"You encountered a {cenemy.name}!")
while alive==True:
 ctpatk=patk+citem.iatk+patkmod+carmour.iatk
 ctpdef=pdef+citem.idef+pdefmod+carmour.idef
 cteatk=cenemy.eatk+eatkmod
 ctedef=cenemy.edef + edefmod
 if frozen==0:
  movechoice()
 else:
   print("You can't move!")
   frozen-=1
 if ehp>0 and not run:
  ehit()
  turncount+=1
 if pstatus==1:
   php -= round(pmaxhp/10)
   print(f"You took {round(pmaxhp/10)} poison damage! You now have {php} hp") 
 for x in range(inventory.count(spikybarb)): 
   php-=4
   print(f"The spiky barb dealt 4 damage to you! You now have {php} hp") 
 hpcheck()
 if not alive:
     break
 run=False
 if estatus==1:
  ehp -= round(cenemy.emaxhp/6)
  print(f"The {cenemy.name} took {round(cenemy.emaxhp/6)} poison damage! It now has {ehp} hp")
 elif estatus==2:
   ehp-= round(cenemy.emaxhp/8)
   print(f"The {cenemy.name} took {round(cenemy.emaxhp/8)} burn damage! It now has {ehp} hp")
    
 if alive:
  if ehp<=0:
   print("You won!")
   newencounter()
print("You died!")
time.sleep(5)