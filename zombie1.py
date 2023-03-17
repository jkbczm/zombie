import random
odczyt = input("Wybierz opcję: ")
if odczyt=="1":
  print("Nowa gra rozpoczęta")
  hp=100
  zombie_hp=random.randint(120,150)
  while True:
    print("Twoje hp ", hp)
    print("Zombie hp", zombie_hp)
    print("1.Atak")
    print("2.Ucieczka")
    wybor_akcji = input("Wybierz akcje")
    if wybor_akcji == 1:
      dmg_pl = random.randint(20,40)
      dmg_zombie = random.randint(15,25)
      print("Twoje hp", hp, "Hp zombie",zombie_hp)
      print("Zadałeś",dmg_pl)
      zombie_hp - dmg_pl
      hp - dmg_zombie
      print("Zombie zadał ci ", dmg_zombie)
      if hp <= 0 :
        print("Wygrałeś")
        break   
      if zombie_hp <= 0:
        print("Przegrałeś")
        break
elif odczyt=="2":
  print("Musisz pokonać przeciwnika - Zombie. Gracz zadaje obrażenia Zombie, Zombie również atakuje gracza. Jeśli poziom Twojego życia spadnie do zera to przegrywasz. Jeśli poziom życia Zombie spadnie do zera to wygrywasz. Powodzenia! - Twórca gry: jkbczm")
elif odczyt=="3":
  print("Do zobaczenia ponownie!")
else:
  print("Zły wybór! Spróbuj ponownie.")