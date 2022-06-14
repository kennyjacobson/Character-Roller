import json

class Armor():
  def __init__(self):
    self.name = 'No Armor'
    self.price = 0
    self.weight = 0
    self.ac = 11

  def load_from_file(self, path):
    with open(path) as f:
      c = json.load(f)
    self.name = c.get("name")
    self.price = c.get("price")
    self.weight = c.get("weight")
    self.ac = c.get("ac")