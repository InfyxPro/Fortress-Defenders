# This file will hold all of the objects for the game
import pyglet, math
from . import config



class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0

        # Flag to remove this object from the game_object list
        self.dead = False

        # List of new objects to go in the game_objects list
        self.new_objects = []

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt


class Projectile(PhysicalObject):
    # This will be for any projectile 

    def __init__(self, img, x_loc, y_loc, rads, speed, distanceToTravel, acceleration = 0, *args, **kwargs):
        super(PhysicalObject, self).__init__(img=img, *args, **kwargs)
        
        self.velocity_x = speed * math.cos(rads)
        self.velocity_y = speed * math.sin(rads)

        self.acceleration = acceleration
        self.rads = rads
         
        # Need to be in degrees
        self.rotation = math.degrees(rads)

        self.position = (x_loc, y_loc)

        self.timeAlive = 0

        #Some constants
        self.distanceToTravel = distanceToTravel
        self.startingLocationX = x_loc
        self.startingLocationY = y_loc

    def update(self,dt):
        super(Projectile,self).update(dt)
        # This is to add a sling effect if wanted
        if self.acceleration != 0:
            self.timeAlive += dt * self.acceleration
            self.velocity_x  = config.ProjectileParabolic(self.timeAlive) * math.cos(self.rads)
            self.velocity_y  = config.ProjectileParabolic(self.timeAlive) * math.sin(self.rads)

        self.dead = self.traveled_distance()


    def traveled_distance(self):
        if (math.dist((self.startingLocationX, self.startingLocationY), self.position) >= self.distanceToTravel):
            return True
        else:
            False










