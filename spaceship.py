## Imports ##
import random

## Classes ##

class Spaceship:
    
    def __init__(self, name, max_health, dodge=None):
        self.name = name # Printed name of ship
        self.max_health = max_health # Max health of ship
        self.health = self.max_health # Initialising current health of ship
        self.dodge = dodge # Chance of ships dodging shots in % out of 100
        self._destroyed = False # Ship is not destroyed, as health is above 0

    @property
    def destroyed(self):
        if self.health <= 0:
            self._destroyed = True

        return self._destroyed

    def take_damage(self, damage):
        if self.destroyed:
            print(f'{self.name} already destroyed')
            return
        if damage <= 0:
            print("Invalid damage value, must be 1 or above")
            return
        
        self.health -= damage
        if self.destroyed:
            print(f'{self.name} destroyed!')

    def shot_landed(self):  # TODO: (Potentially) Add accuracy value to shots
        
        # Returns true or false if ship has dodged an incoming attack
        
        if self.dodge < 0 or self.dodge > 100:
            print('Invalid value for dodge, must be between 0 and 100')
            return None

        if self.dodge > 0 and self.dodge < 100:
            shot_landed_random_int = random.randint(0, 100)
            
            if self.dodge >= shot_landed_random_int:
                return False
            
            return True

        if self.dodge == 100:
            return False
        
        if self.dodge == 0:
            return True

    # TODO: Shield functionality -> block shots & absorb damage
    # TODO: Fire at other ships

# TODO: Weapon class
# TODO: Shield class
            
## Local run command ##
if __name__ == "__main__":

    # TODO: Test driven development -> test suites etc
    # TODO: Proper evnnt logging
    # TODO: Function for printing ship variable information for testing / debugging purposes 

    print(f'\n--{__file__} tests--\n')
    
    print('\n--TEST 1--\n')

    spaceship1 = Spaceship('spaceship1', 5)
    print(f'name: {spaceship1.name}\n'\
            f'max health: {spaceship1.max_health}\n'\
            f'health: {spaceship1.health}\n'\
            f'destroyed: {spaceship1.destroyed}')

    spaceship1.health = 0
    print(f'name: {spaceship1.name}\n'\
        f'health: {spaceship1.health}\n'\
        f'destroyed: {spaceship1.destroyed}')

    print('\n--TEST 2--\n')

    ship2 = Spaceship('ship2', 5)

    ship2.take_damage(0)
    print(f'name: {ship2.name}\n'\
        f'health: {ship2.health}\n')

    ship2.take_damage(1)
    print(f'name: {ship2.name}\n'\
        f'health: {ship2.health}\n')

    ship2.take_damage(4)
    print(f'name: {ship2.name}\n'\
        f'health: {ship2.health}\n'\
        f'destroyed: {ship2.destroyed}\n'\
        f'health: {ship2.health}')
    
    print('\n--TEST 3--\n')

    ship3 = Spaceship('ship3', 1)
    
    ship3.dodge = 0
    print(f'name: {ship3.name}\n'\
        f'dodge: {ship3.dodge}')
    print(f'shot landed: {ship3.shot_landed()}')
    print()

    ship3.dodge = 100
    print(f'name: {ship3.name}\n'\
        f'dodge: {ship3.dodge}')
    print(f'shot landed: {ship3.shot_landed()}')
    print()

    ship3.dodge = -1
    print(f'name: {ship3.name}\n'\
        f'dodge: {ship3.dodge}')
    print(f'shot landed: {ship3.shot_landed()}')
    print()
    
    ship3.dodge = 101
    print(f'name: {ship3.name}\n'\
        f'dodge: {ship3.dodge}\n')
    print(f'shot landed: {ship3.shot_landed()}')
    print()

    ship3.dodge = 99
    print(f'name: {ship3.name}\n'\
        f'dodge: {ship3.dodge}\n')
    print(f'shot landed: {ship3.shot_landed()}')
    print()

    ship3.dodge = 1
    print(f'name: {ship3.name}\n'\
        f'dodge: {ship3.dodge}\n')
    print(f'shot landed: {ship3.shot_landed()}')
    print()

    ship3.dodge = 50
    print(f'name: {ship3.name}\n'\
        f'dodge: {ship3.dodge}\n')
    print(f'shot landed: {ship3.shot_landed()}')
    print()
