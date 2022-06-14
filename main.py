from character import Character
from monster import Monster

player1 = Character()
#player1.roll_new()
player1.load_from_file('characters/amezaga1311141010175.json')
player1.set_current_weapon_from_file('weapons/longsword.json')
player1.set_current_armor_from_file('armor/chainmail.json')



print('Name: ', player1.name)
print('Strength: ', player1.strength)
print('intelligence: ', player1.intelligence)
print('wisdom: ', player1.wisdom)
print('dexterity: ', player1.dexterity)
print('constitution: ', player1.constitution)
print('charisma: ', player1.charisma)
print('Hit Points: ', player1.hit_point_max)
print('Armor Class: ', player1.get_ac())
print('Movment: ', player1.get_movement())
print('Ability Bonuses: ', player1.get_ability_bonuses())
print('Weapons: ', player1.current_weapon.name)
print('Roll to hit: ', player1.roll_to_hit())
print('Roll for damage: ', player1.roll_for_damage())
print('AC: ', player1.get_ac())


monster1 = Monster()
monster1.generate_monster('kobold')
print("-" * 20)
print('Monster Name: ', monster1.name)
print('Monster Hit Points: ', monster1.hit_point_max)
