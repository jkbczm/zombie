import random
import time 
def player_attack():
  player_attack_damage=random.randint(20,40)
  zombie_hp - player_attack_damage
def zombie_attack():
  zombie_attack_damage = random.randint(15,25)
  hp - zombie_attack_damage



print("Welcome in Zombie Game 1.0 Beta ^_^")

print("1.Create new game ")
print("2.game rules")
print("3.Quit game")

reeding = input("Choose option: ")

if reeding=="1":
  print("New game starts")
 
  hp=100
 
  zombie_hp=random.randint(120,150)
  time.sleep(5)
  print("Player hp")
  time.sleep(2)
  print("?")
  print(hp)
  time.sleep(2)
  print("opponent hp")
  time.sleep(2)
  print("?")
  time.sleep(2)
  print(zombie_hp)





























elif reeding =="2":
  print("You have to defeat your opponent - Zombie. The player inflicts the Zombie standard, the Zombie also attacks. If your life level drops to zero, you lose. If the Zombie's health drops to zero, you win. Good luck! - Game developer: jacob")
elif reeding =="3":
  print("See you later!")
else:
  print("Wrong choice . Try again ")