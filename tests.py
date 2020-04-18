# Testing framework for Spaceship.py

# Imports
import pytest
import spaceship

# Tests

class TestSpaceshipClass:
    
    def test_spaceship_init_method(self):
        spaceship1 = spaceship.Spaceship('spaceship1', 5)
        assert spaceship1.name == 'spaceship1'
        assert spaceship1.max_health == 5
        assert spaceship1.health == 5
        assert spaceship1.destroyed == False

    def test_spaceship_destroyed_property(self):
        test_ship = spaceship.Spaceship('test_ship', 1)
        assert test_ship.destroyed == False
        test_ship.health = 0
        assert test_ship.destroyed == True

    def test_take_damage_method(self):
        ship2 = spaceship.Spaceship('ship2', 5)

        ship2.take_damage(0)
        assert ship2.health == 5

        ship2.take_damage(1)
        assert ship2.health == 4

        ship2.take_damage(4)
        assert ship2.health == 0
        assert ship2.destroyed == True

    def test_dodge_attribute(self):
        ship3 = spaceship.Spaceship('ship3', 1, 0)
        assert ship3.dodge == 0
        assert ship3.shot_landed() == True
        
        ship3.dodge = 100
        assert ship3.shot_landed() == False

        ship3.dodge = -1
        assert ship3.shot_landed() == None
        
        ship3.dodge = 101
        assert ship3.shot_landed() == None

    def test_shot_method(self):
        ship4 = spaceship.Spaceship('ship4', 3)
    
        ship4.dodge = 100
        ship4.shot()
        assert ship4.health == 3

        ship4.dodge = 0
        ship4.shot()
        assert ship4.health == 2

        ship4.shot(2)
        assert ship4.health == 0
        assert ship4.destroyed

    def test_fire_weapons_method(self):
        target_ship = spaceship.Spaceship('target-ship', max_health=3, dodge=100)
        attacker_ship = spaceship.Spaceship('attacker-ship')

        attacker_ship.fire_weapons(target_ship)
        assert target_ship.health == 3

        target_ship.dodge = 0
        attacker_ship.fire_weapons(target_ship)
        assert target_ship.health == 2

        attacker_ship.fire_weapons(target_ship, 2)
        assert target_ship.health == 0
        assert target_ship.destroyed
    
    
# TODO: Test log output
# TODO: Add own logging into each test to help trace each problem