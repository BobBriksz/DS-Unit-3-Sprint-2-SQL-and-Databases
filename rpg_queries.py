"""Sprint 2 Unit 3 SQL day 1 assignment"""
import sqlite3

# for connecting to our database
def connect_to_db(db_name="rpg_db.sqlite3"):
     conn = sqlite3.connect(db_name)
     return conn

# for executing read queries
def execute_query(cursor, query):
      cursor.execute(query)
      return cursor.fetchall()

# queries
TOTAL_CHARACTERS = """
    SELECT COUNT(*)
    FROM charactercreator_character;
"""
# total amount of each class

TOTAL_CLERIC = """
    SELECT COUNT(*)
    FROM charactercreator_character AS ccc, charactercreator_cleric AS cccl
    WHERE ccc.character_id = cccl.character_ptr_id;
"""

TOTAL_FIGHTERS = """
    SELECT COUNT(*)
    FROM charactercreator_character AS ccc, charactercreator_fighter AS ccf
    WHERE ccc.character_id = ccf.character_ptr_id;
"""

TOTAL_MAGES = """
    SELECT COUNT(*)
    FROM charactercreator_character AS ccc, charactercreator_mage AS ccm
    WHERE ccc.character_id = ccm.character_ptr_id;
"""
TOTAL_NECROMANCERS = """
    SELECT COUNT(*)
    FROM charactercreator_character AS ccc, charactercreator_necromancer AS ccn
    WHERE ccc.character_id = ccn.mage_ptr_id;
"""
TOTAL_THEIF = """
    SELECT COUNT(*)
    FROM charactercreator_character AS ccc, charactercreator_thief AS cct
    WHERE ccc.character_id = cct.character_ptr_id;
"""
TOTAL_ITEMS = """
    SELECT COUNT(*)
    FROM armory_item; 
"""

WEAPON_ITEMS = """
    SELECT COUNT(*)
    FROM armory_item, armory_weapon
    WHERE armory_item.item_id = armory_weapon.item_ptr_id; 
"""
NON_WEAPON_ITEMS = """
    SELECT COUNT(*)
    FROM armory_item, armory_weapon
    WHERE armory_item.item_id != armory_weapon.item_ptr_id; 
"""
NUM_ITEMS_PER_CHAR = """
    SELECT character.name,
    COUNT(*) AS `num of items`
    FROM charactercreator_character AS character,
    charactercreator_character_inventory AS inventory
    WHERE character.character_id = inventory.character_id
    GROUP BY character.name
    LIMIT 20;
"""
NUM_WEAPONS_PER_CHAR = """"
    SELECT name,
    COUNT(*) AS `num of weapons`
    FROM charactercreator_character AS character
	INNER JOIN
	charactercreator_character_inventory AS inventory
	ON character.character_id = inventory.character_id
	INNER JOIN
	armory_weapon AS weapon
	ON inventory.item_id = weapon.item_ptr_id
    GROUP BY name
    LIMIT 20;
"""

if __name__ == "__main__":
     conn = connect_to_db()
     curs= conn.cursor()
     
     total_char = execute_query(curs, TOTAL_CHARACTERS)
     print('TOTAL CHARACTERS: ', total_char)

     total_cleric = execute_query(curs, TOTAL_CLERIC)
     print('TOTAL CLERICS: ', total_cleric)

     total_mage = execute_query(curs, TOTAL_MAGES)
     print('TOTAL MAGES: ', total_mage)

     total_fighter = execute_query(curs, TOTAL_FIGHTERS)
     print('TOTAL fighters: ', total_fighter)

     total_necromancer = execute_query(curs, TOTAL_NECROMANCERS)
     print('TOTAL necromancers: ', total_necromancer)

     total_thief = execute_query(curs, TOTAL_THEIF)
     print('total Thieves: ', total_thief)

     total_items = execute_query(curs, TOTAL_ITEMS)
     print('total items: ', total_items)

     weapons = execute_query(curs, WEAPON_ITEMS)
     print('Amount of Weapons: ', weapons)

     num_item_per_char = execute_query(curs, NUM_ITEMS_PER_CHAR)
     print("characters and the amount of items they have:", num_item_per_char)

     num_weapon_per_char = execute_query(curs, NUM_WEAPONS_PER_CHAR)
     print("How many weapons each character has: ", num_weapon_per_char)

     