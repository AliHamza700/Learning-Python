Weapons=["Sword","Axe","Bow","Dagger","AK 47"]# List are mutable unlike strings are imutable 
print(Weapons[0])#sword
Weapons[0]="Spear"
print(Weapons[0])#Spear
print(Weapons[1:4])#Slice of list from index 1 to 3