# Testing framework for Spaceship.py

# Imports
import pytest
import spaceship

# Tests

class TestSpaceshipClass:
    
    def test_spaceship_creation(self):
        spaceship1 = spaceship.Spaceship('spaceship1', 5)
        assert spaceship1.name == 'spaceship1'
        assert spaceship1.max_health == 5
        assert spaceship1.health == 5
        assert spaceship1.destroyed == False

    def test_spaceship_destroyed(self):
        test_ship = spaceship.Spaceship('test_ship', 1)
        assert test_ship.destroyed == False
        test_ship.health = 0
        assert test_ship.destroyed == True
        

