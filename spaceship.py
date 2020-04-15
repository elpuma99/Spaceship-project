## Imports ##
import random

## Classes ##

class Spaceship:
    
    def __init__(self, name, max_health=1, dodge=0):
        self.name = name # Printed name
        self.max_health = max_health # Max health
        self.health = self.max_health # Initialising current health
        self.dodge = dodge # Chance of ships dodging shots in % out of 100
        self._destroyed = False # Ship is not destroyed, as health is above 0

    @property
    def destroyed(self):
        if self.health <= 0:
            self._destroyed = True

        return self._destroyed

    def take_damage(self, damage): 
        # Called when damage is done to the ship health
        
        if self.destroyed:
            print(f'{self.name} already destroyed')
            return
        if damage <= 0:
            print("Invalid damage value, must be 1 or above")
            return
        
        self.health -= damage
        print(f'{self.name} took 1 point of damage!')
        if self.destroyed:
            print(f'{self.name} destroyed!')

    def shot_landed(self):  # TODO: (Potentially) Add accuracy value to shots
        
        # Returns true or false if ship has dodged an incoming attack

        if self.destroyed:
            print(f'{self.name} already destroyed')
            return
        
        if self.dodge < 0 or self.dodge > 100:
            print('Invalid value for dodge, must be between 0 and 100')
            return

        if self.dodge >= 0 and self.dodge <= 100:
            shot_landed_random_int = random.randint(0, 99)
            
            if self.dodge > shot_landed_random_int:
                return False
            
            return True

    def shot(self, damage=1): 
        # Ship is fired at, this method will be called per every shot

        if self.destroyed:
            print(f'{self.name} already destroyed')
            return
        
        # Calculate if ship dodges, if false ship takes damage, else ship dodges shot
        if not self.shot_landed():
            print(f'{self.name} dodged shot!')
            return
        print(f'{self.name} shot lands!')
        self.take_damage(damage)

    # TODO: Shield functionality -> block shots & absorb damage
    
    def fire_weapons(self, target, damage=1):
        # Method to fire all weapons at enemy ship

        if target.destroyed:
            print(f'Target {target.name} is already destroyed')
            return

        print(f'{self.name} fires at {target.name}!')
        target.shot(damage)

        # return NotImplemented
    
    # TODO: Fire at other ships
    # TODO: Fire individual weapons

# TODO: Shield class
# TODO: Weapon class
            
## Local run command ##
if __name__ == "__main__":

    # TODO: Function for printing ship variable information for testing / debugging purposes 
    # TODO: Proper evnnt logging
    # TODO: Test driven development -> test suites etc

    print(f'\n--{__file__}--\n')
    
    # print('\n--TEST 1--\n')

    # spaceship1 = Spaceship('spaceship1', 5)
    # print(f'name: {spaceship1.name}\n'\
    #         f'max health: {spaceship1.max_health}\n'\
    #         f'health: {spaceship1.health}\n'\
    #         f'destroyed: {spaceship1.destroyed}')

    # spaceship1.health = 0
    # print(f'name: {spaceship1.name}\n'\
    #     f'health: {spaceship1.health}\n'\
    #     f'destroyed: {spaceship1.destroyed}')

    # print('\n--TEST 2--\n')

    # ship2 = Spaceship('ship2', 5)

    # ship2.take_damage(0)
    # print(f'name: {ship2.name}\n'\
    #     f'health: {ship2.health}\n')

    # ship2.take_damage(1)
    # print(f'name: {ship2.name}\n'\
    #     f'health: {ship2.health}\n')

    # ship2.take_damage(4)
    # print(f'name: {ship2.name}\n'\
    #     f'health: {ship2.health}\n'\
    #     f'destroyed: {ship2.destroyed}\n'\
    #     f'health: {ship2.health}')
    
    # print('\n--TEST 3--\n')

    # ship3 = Spaceship('ship3', 1)
    
    # ship3.dodge = 0
    # print(f'name: {ship3.name}\n'\
    #     f'dodge: {ship3.dodge}')
    # print(f'shot landed: {ship3.shot_landed()}')
    # print()

    # ship3.dodge = 100
    # print(f'name: {ship3.name}\n'\
    #     f'dodge: {ship3.dodge}')
    # print(f'shot landed: {ship3.shot_landed()}')
    # print()

    # ship3.dodge = -1
    # print(f'name: {ship3.name}\n'\
    #     f'dodge: {ship3.dodge}')
    # print(f'shot landed: {ship3.shot_landed()}')
    # print()
    
    # ship3.dodge = 101
    # print(f'name: {ship3.name}\n'\
    #     f'dodge: {ship3.dodge}\n')
    # print(f'shot landed: {ship3.shot_landed()}')
    # print()

    # ship3.dodge = 99
    # print(f'name: {ship3.name}\n'\
    #     f'dodge: {ship3.dodge}\n')
    # print(f'shot landed: {ship3.shot_landed()}')
    # print()

    # ship3.dodge = 1
    # print(f'name: {ship3.name}\n'\
    #     f'dodge: {ship3.dodge}\n')
    # print(f'shot landed: {ship3.shot_landed()}')
    # print()

    # ship3.dodge = 50
    # print(f'name: {ship3.name}\n'\
    #     f'dodge: {ship3.dodge}\n')
    # print(f'shot landed: {ship3.shot_landed()}')
    # print()

    # print('\n--TEST 4--\n')

    # ship4 = Spaceship('ship4', 2, 0)
    
    # ship4.dodge = 50
    # print(f'name: {ship4.name}\n'\
    #     f'dodge: {ship4.dodge}')
    # print()
    
    # ship4.shot()
    # ship4.shot()
    # ship4.shot()
    # ship4.shot()
    # ship4.shot()
    # print(ship4.health)
    # print()

    # print('\n--TEST 5--\n')

    # target_ship = Spaceship('target-ship', 1, 100)
    # attacker_ship = Spaceship('attacker-ship', 1)

    # attacker_ship.fire_weapons(target_ship)


