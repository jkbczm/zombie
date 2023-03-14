import random
import time 

player_attack_damage=random.randint(20,40)
zombie_attack_damage = random.randint(15,25)
hp=100
zombie_hp=random.randint(120,150)
def player_attack():
 
  zombie_hp - player_attack_damage
def zombie_attack():
 
  hp - zombie_attack_damage



print("Welcome in Zombie Game 1.0 Beta ^_^")

print("1.Create new game ")
print("2.Game rules")
print("3.Quit game")
time.sleep(2)
reeding = input("Choose option: ")

if reeding=="1":
  print("1.Apocalypse")
  print("Coming soon ...")
  time.sleep(2)
  Mode = input("Select mode")
  print("New game starts")
  print("Player hp")
  print("?")
  print(hp)
  print("opponent hp")
  print("?")
  print(zombie_hp)
  time.sleep(5)
  while True :
   if(hp == 0 or hp < 0):
     print ("You lose")
     break
   print("Select action")
   print("1. Attack")
   action = input("Enter action")
  
   if (action == "1"):
    print("Apocalypse start")
    if (hp < 0 or hp == 0 ):
      print("You lose")
      break
    zombie_hp = zombie_hp - player_attack_damage
    print("Zombie hp:" )
    if (zombie_hp < 0):
      zombie_hp = 0
    print(zombie_hp)
    time.sleep(2)
    if (zombie_hp == 0 or zombie_hp < 0):
      print ("You win") 
      break
    hp = hp - zombie_attack_damage
    if(hp<0):
      hp = 0
    print("Your hp :")
    print(hp)
     
   else:
    print("Wrong action")
      
elif reeding =="2":
  print("You have to defeat your opponent - Zombie. The player inflicts the Zombie standard, the Zombie also attacks. If your life level drops to zero, you lose. If the Zombie's health drops to zero, you win. Good luck! - Game developer: jacob")
elif reeding =="3":
  print("See you later!")
else:
  print("Wrong choice . Try again ")