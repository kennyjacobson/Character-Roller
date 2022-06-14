import json
import random
import names

class Monster():  
  def __init__(self):
    self.name = 'steve'
    self.type = 'generic'
    self.ac = 10
    self.hit_dice_low = 1
    self.hit_dice_high = 4
    self.hit_point_max = 1
    self.movement = 30
    self.damage_low =1
    self.damage_high = 4
    self.morale = 6
    self.treasure_type = ["p","q","c"]
    self.xp = 10

  def load_from_file(self,path):
    with open(path) as f:
      m = json.load(f)
    self.type = m.get("type")
    self.ac = m.get("ac")
    self.hit_dice_low = m.get("hit_dice_low")
    self.hit_dice_high = m.get("hit_dice_high")
    self.movement = m.get("movement")
    self.damage_low = m.get("damage_low")
    self.damage_high = m.get("damage_high")
    self.morale = m.get("morale")
    self.treasure_type = m.get("treasure_type")
    self.xp = m.get("xp")
    self.hit_point_max = m.get("hit_point_max")
    self.name = m.get("name")

  def generate_monster(self, monster_name):
    self.load_from_file(f"monster_templates/{monster_name}.json")
    self.hit_point_max = random.randint(self.hit_dice_low, self.hit_dice_high)
    self.name = names.get_first_name()
    filename = f'monsters/{self.type.lower()}{self.name.lower()}{self.hit_point_max}.json'
    monster_dict = {
        "type" : self.type,
        "ac" : self.ac,
        "hit_dice_low" : self.hit_dice_low,
        "hit_dice_high" : self.hit_dice_high,
        "movement" : self.movement,
        "damage_low" : self.damage_low,
        "damage_high" : self.damage_high,
        "morale" : self.morale,
        "treasure_type" : self.treasure_type,
        "xp" : self.xp,
        "hit_point_max" : self.hit_point_max,
        "name" : self.name
    }
    with open(filename,'w') as f:
      json.dump(monster_dict, f)
