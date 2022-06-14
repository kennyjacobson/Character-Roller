import random
import names
import json
from weapon import Weapon
from armor import Armor

class Character:
  def __init__(self):
    self.strength = 0
    self.intelligence = 0
    self.wisdom = 0
    self.dexterity = 0
    self.constitution = 0 
    self.charisma = 0
    self.race = 'human'
    self.c_class = 'fighter'
    #self.armor_class = 11
    self.hit_point_max = 0
    self.level = 1
    self.movement = 60
    self.name = names.get_last_name()
    self.armor = None
    self.current_weapon = None
    self.current_armor = Armor()

  def load_from_file(self, path):
    with open(path) as f:
      c = json.load(f)
    self.name = c.get("name")
    self.strength = c.get("strength")
    self.intelligence = c.get("intelligence")
    self.wisdom = c.get("wisdom")
    self.dexterity = c.get("dexterity")
    self.constitution = c.get("constitution")
    self.charisma = c.get("charisma")
    self.race = c.get("race")
    self.c_class = c.get("c_class")
    self.hit_point_max = c.get("hit_point_max")
    self.level = c.get("level")
    
  def set_current_weapon(self, weapon):
    self.current_weapon = weapon

  def set_current_weapon_from_file(self, path): 
    weapon = Weapon()
    weapon.load_from_file(path)
    self.current_weapon = weapon

  def set_current_armor_from_file(self, path): 
    armor = Armor()
    armor.load_from_file(path)
    self.current_armor = armor

  def roll_to_hit(self): 
    roll = random.randint(1, 20) 
    return (roll + self.get_attack_bonus(),roll,self.get_attack_bonus())

  def get_attack_bonus(self): 
    if self.c_class == "fighter": 
      if self.level <= 1:
        return 1
      elif self.level <= 3: 
        return 2
      elif self.level <= 4: 
        return 3
      elif self.level <= 6: 
        return 4
      elif self.level <= 7: 
        return 5
      elif self.level <= 10: 
        return 6
      elif self.level <= 12: 
        return 7
      elif self.level <= 15: 
        return 8
      elif self.level <= 17: 
        return 9
      else:
        return 10

  def roll_for_damage(self): 
    if self.current_weapon: 
      return random.randint(self.current_weapon.damage_low, self.current_weapon.damage_high)
  
  def get_ac(self):
    if self.current_armor:
      return self.current_armor.ac

  def get_movement(self):
    # TODO build in race
    if self.armor:  
      return 20
    else:  
      return 60

  def get_ability_bonuses(self):
    return {
      "strength" : self.get_bonus(self.strength),
      "intelligence" : self.get_bonus(self.intelligence),
      "wisdom" : self.get_bonus(self.wisdom),
      "dexterity" : self.get_bonus(self.dexterity),
      "constitution" : self.get_bonus(self.constitution),
      "charisma" : self.get_bonus(self.charisma),
    }
    
  def get_bonus(self, ability_score): 
    if ability_score <= 3:
      return -3
    elif ability_score <= 5:
      return -2
    elif ability_score <= 8:
      return -1
    elif ability_score <= 12:
      return 0
    elif ability_score <= 15:
      return 1
    elif ability_score <= 17:
      return 2
    else:
      return 3
    



  def roll_new(self):
    self.strength = self.roll_best_three_sixes()
    self.intelligence = self.roll_best_three_sixes()
    self.wisdom = self.roll_best_three_sixes()
    self.dexterity = self.roll_best_three_sixes()
    self.constitution = self.roll_best_three_sixes()
    self.charisma = self.roll_best_three_sixes()

    if self.c_class == 'fighter':
      self.hit_point_max = random.randint(4,8)

    filename = f'characters/{self.name.lower()}{self.strength}{self.intelligence}{self.wisdom}{self.dexterity}{self.constitution}{self.charisma}{self.hit_point_max}.json'
    character_dict = {
        "name" : self.name,
        "strength" : self.strength,
        "intelligence" : self.intelligence,
        "wisdom" : self.wisdom,
        "dexterity" : self.dexterity,
        "constitution" : self.constitution,
        "charisma" : self.charisma,
        "hit_point_max" : self.hit_point_max,
        "race" : self.race,
        "c_class" : self.c_class,
        "level" : self.level
    }
    with open(filename,'w') as f:
      json.dump(character_dict, f)

  def load_equipment(self, equipment):
    pass

  def load_weapon(self, weapon):
    pass


  

  def roll_best_three_sixes(self):
    four_dice = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    four_dice.sort()
    three_dice = four_dice[1:]
    total = sum(three_dice)
    return total