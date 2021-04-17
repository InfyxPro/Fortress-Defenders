# This file will hold all of the objects for the game
import pyglet, math, time
from . import config



class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.globalTime = 0

        # Flag to remove this object from the game_object list
        self.dead = False

        # List of new objects to go in the game_objects list
        self.new_objects = []

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.globalTime += dt



class Projectile(PhysicalObject):
    # This will be for any projectile 

    def __init__(self, img, x_loc, y_loc, rads, speed, distanceToTravel, acceleration = 0, duration = 120, *args, **kwargs):
        super(Projectile, self).__init__(img=img, *args, **kwargs)
        self.velocity_x = speed * math.cos(rads)
        self.velocity_y = speed * math.sin(rads)
        self.img = img

        self.acceleration = acceleration
        self.rads = rads
         
        # Need to be in degrees
        self.rotation = math.degrees(rads)

        self.position = (x_loc, y_loc)

        self.timeAlive = 0
        self.duration = duration

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
        if self.globalTime > self.duration:
            self.dead = True
        

    def traveled_distance(self):
        if (math.dist((self.startingLocationX, self.startingLocationY), self.position) >= self.distanceToTravel):
            return True
        else:
            False


class MovingSprite(PhysicalObject):
    # This will be for any projectile 
    # lastDirection = DownFrames = 0, UpFrames = 1, RightFrames = 2, LeftFrames = 3

    def __init__(self, \
       stillImages, moveDownAnimation, moveUpAnimation,moveRightAnimation, moveLeftAnimation, dyingAnimation,\
       health, damage, speed,\
       *args, **kwargs):
       super(PhysicalObject, self).__init__(img=stillImages[0], *args, **kwargs)

       # Images and Animations
       self.stillImages = stillImages
       self.moveRightAnimation = moveRightAnimation
       self.moveLeftAnimation = moveLeftAnimation
       self.moveUpAnimation = moveUpAnimation
       self.moveDownAnimation = moveDownAnimation
       self.dyingAnimation = dyingAnimation

       # Needed variables for class functionality
       self.lastDirection = 0
       
       # In class attributes
       self.health = health
       self.damage = damage
       self.speed = speed

    def update(self,dt):
        super(Projectile,self).update(dt)
        self.Animation_Selector()

        if self.dead:
            pyglet.sprite.Sprite(img = dyingAnimation)


    def Animation_Selector(self):
        if self.velocity_x == 0 and self.velocity_y == 0: # Stopped moving
            self.image = self.stillImages[self.lastDirection]
        elif abs(self.velocity_x) > abs(self.velocity_y): # Select x
            if self.velocity_x > 0: # Positive, right
                self.image = self.moveRightAnimation
                self.lastDirection = 2
            else: # Negative, left
                self.image = self.moveLeftAnimation
                self.lastDirection = 3
        elif abs(self.velocity_x) < abs(self.velocity_y): # Select y
            if self.velocity_y > 0: # Positive, up
                self.image = self.moveUpAnimation
                self.lastDirection = 1
            else: # Negative, down
                self.image = self.moveDownAnimation
                self.lastDirection = 0









