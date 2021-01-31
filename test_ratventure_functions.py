import pytest
from RatVenture import *

def test_view_stats():
   """This is to test if the Hero Stats gets displayed and if the statistics is correct, dynamic and can respond to changes when the values change"""

   value = herostats()

   #value = townMenu_selection1()

   assert value == player.name + "\nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(player.damage, player.defence, player.hp, player.day)

def test_rest_function():
   """This is to test if rest function is working. By calling this function, health will be 20 and day will be day + 1. Nothing is required for input"""
   value = rest()
   assert value == (20, player.day-1, player.day)

def test_save_function():
       """This is to test if player data can be saved into excel file"""
       value = savegame()
       assert (savedplayer.name == player.name, savedplayer.damage == player.damage, savedplayer.defence == player.defence, savedplayer.hp == player.hp, savedplayer.day == player.day)

def test_resume_function():
      """This is to test if the resumegame function changed the resumeplayer player class attributes to the values of the savedplayer player class"""
      value = resumegame()
      assert (resumeplayer.name == savedplayer.name, resumeplayer.damage == savedplayer.damage, resumeplayer.defence==savedplayer.defence, resumeplayer.hp==savedplayer.hp, resumeplayer.day==savedplayer.day)

def test_move_function_UP():
   """This is to test if the move "up" function is working. When the player feeds input "W", the H (Hero) indicator should move accordingly and the map will be updated"""
   value = moveUp()
   assert value == (player.positionY, player.positionY+1)

def test_move_function_DOWN():
   """This is to test if the move "down" function is working. When the player feeds input "S", the H (Hero) indicator should move accordingly and the map will be updated"""
   value = moveDown()
   assert value == (player.positionY, player.positionY-1)

def test_move_function_LEFT():
   """This is to test if the move "left" function is working. When the player feeds input "A", the H (Hero) indicator should move accordingly and the map will be updated"""
   value = moveLeft()
   assert value == (player.positionX, player.positionX+1)

def test_move_function_RIGHT():
   """This is to test if the move "right" function is working. When the player feeds input "D", the H (Hero) indicator should move accordingly and the map will be updated"""
   value = moveRight()
   assert value == (player.positionX, player.positionX-1)

def test_attack_function():
       """This is to test if the attack function decreases the health of the opponent"""
       value = attack()
       assert rat.hp < 8

