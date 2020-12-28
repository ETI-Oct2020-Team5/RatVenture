import pytest
from RatVenture import *

def test_view_stats():
   """This is to test if the Hero Stats gets displayed and if the statistics is correct, dynamic and can respond to changes when the values change"""

   value = herostats()

   #value = townMenu_selection1()

   assert value == player.name + "\nDamage: {}\nDefence: {}\nHP: {}".format(player.damage, player.defence, player.hp)

def test_rest_function():
   """This is to test if rest function is working. By calling this function, health will be 20 and day will be day + 1. Nothing is required for input"""
   value = rest()
   assert value == (20, player.day-1, player.day)

def test_save_function():
       """This is to test if player data can be saved into excel file"""
       value = savegame()
       assert value == savedplayer.name + "\nDamage: {}\nDefence: {}\nHP: {}".format(savedplayer.damage, savedplayer.defence, savedplayer.hp)
