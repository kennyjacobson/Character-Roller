import json

class Weapon():
  def __init__(self):
    self.name = 'name'
    self.price = 1
    self.size = 'S'
    self.weight = 3
    self.damage_low = 1
    self.damage_high = 10

  def load_from_file(self, path):
    with open(path) as f:
      c = json.load(f)
    self.name = c.get("name")
    self.price = c.get("price")
    self.size = c.get("size")
    self.weight = c.get("weight")
    self.damage_low = c.get("damage_low")
    self.damage_high = c.get("damage_high")