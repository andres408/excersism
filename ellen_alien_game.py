'''Solution to Ellen's Alien Game exercise.'''

class Alien():
     """Create an Alien object with location x_coordinate and y_coordinate.
 
    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.
 
    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    number = 0
    def __init__(self,location):
        self.x_coordinate = location[0]
        self.y_coordinate = location[1]
        self.health = 3

    def hit(self):
        alien.health -=1
    
    def is_alive(self):
        if alien.health > 0:
            return True
        return False

    def teleport(self,x_coordinate,y_coordinate):
        self.x_coordinate += x_coordinate
        self.y_coordinate += y_coordinate
        return self.x_coordinate,self.y_coordinate

    def collision_detection(self):
        pass


    def alien_counter(self):
        Alien.number += 1
        

def start_positions(positions):
    aliens =[]
    for location in positions:
        aliens.append(Alien(location[0],location[1]))
    return aliens

alien=Alien((2,0))
alien.teleport(2,2)
alien.alien_counter()
print(alien.number)
print(alien.health)
print(alien.x_coordinate)
print(alien.y_coordinate)
alien.hit()
alien.hit()
print(alien.health)
print(alien.is_alive())

