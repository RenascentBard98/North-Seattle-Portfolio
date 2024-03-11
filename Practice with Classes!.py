class Character:
   def __init__(self, name, lifespan, attackPower):
      self.name = name
      self.lifespan = lifespan
      self.attackPower = attackPower
      
   def identify(self):
      print("I am " + self.name)
 
   def attack(self, other):
      pass # to be used by all subclasses

class Elf(Character):
   def attack(self, other):
      damage = self.attackPower
      print(f"{self.name} attacks {other.name} with a precise arrow!")
      other.lifespan -= damage
      print(f"{other.name} takes {damage} damage. {other.name}'s lifespan: {other.lifespan}")
   def setTribe(self, tribe):
      self.tribe = tribe
   def claimTribe(self):
      self.identify()
      print("I am a " + self.tribe + " elf.")
      
class Dwarf(Character):
   def attack(self, other):
      damage = self.attackPower
      print(f"{self.name} attacks {other.name} with a might swing of the axe!")
      other.lifespan -= damage
      print(f"{other.name} takes {damage} damage. {other.name}'s lifespan: {other.lifespan}")
   def setBeard(self, beard_color):
      self.beard = beard_color
   def confront(self):
      self.identify()
      print(self.beard + " beard!")


if __name__ == "__main__":
    elf = Elf("Iorweth", 50, 150)
    elf.setTribe("wood")
    elf.claimTribe()

    dwarf = Dwarf("Zoltan", 75, 150)
    dwarf.setBeard("Red")
    dwarf.confront()

    print("--- Battle Begins ---")
    elf.attack(dwarf)
    dwarf.attack(elf)
    print("--- Battle Ends ---")

