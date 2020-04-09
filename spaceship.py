## Imports ##


## Classes ##

class Spaceship:
    
    def __init__(self, name, max_health):
        self.name = name # Printed name of ship
        self.max_health = max_health # Max health of ship
        self.health = self.max_health # Initialising current health of ship
        # self.dodge = dodge # Chance of ships dodging shots in % out of 100
        self._destroyed = False # Ship is not destroyed, as health is above 0

    @property
    def destroyed(self):
        if self.health <= 0:
            self._destroyed = True

        return self._destroyed

    def take_damage(self, damage):
        if damage <= 0:
            print("Invalid damage value, must be 1 or above")
            return
        
        self.health -= damage



## Local run command ##
if __name__ == "__main__":
    print(f'\n--{__file__} tests--\n')
    
    print('\n--TEST 1--\n')

    spaceship1 = Spaceship('spaceship1', 5)
    print(f'name: {spaceship1.name}\n'\
            f'max health: {spaceship1.max_health}\n'\
            f'health: {spaceship1.health}\n'\
            f'destroyed: {spaceship1.destroyed}')

    print('\n--TEST 2--\n')

    spaceship1.health = 0
    print(f'name: {spaceship1.name}\n'\
        f'health: {spaceship1.health}\n'\
        f'destroyed: {spaceship1.destroyed}')

    print('\n--TEST 3--\n')

    ship2 = Spaceship('ship2', 5)

    ship2.take_damage(0)
    print(f'name: {ship2.name}\n'\
        f'health: {ship2.health}\n')

    print('\n--TEST 4--\n')

    ship2.take_damage(1)
    print(f'name: {ship2.name}\n'\
        f'health: {ship2.health}\n')
    
    print('\n--TEST 5--\n')

    ship2.take_damage(4)
    print(f'name: {ship2.name}\n'\
        f'health: {ship2.health}\n'\
        f'destroyed: {ship2.destroyed}')