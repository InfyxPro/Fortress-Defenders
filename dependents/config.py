#This file will define all of the python global variables 

#User input GLOBALS
MAXFPS = 600.0
WIDTH = 1000
HEIGHT = 800
FULLSCREEN = False
DEBUG = True

#Non User input GLOBALS, !!!Do not change these!!!!
PI = 3.14159265359

#functions
def ProjectileParabolic(x): #Works well with Objects.Projectile(imageloads.ArcaneBolt_Animation[0],config.WIDTH/2,config.HEIGHT/2,config.PI*5/3,0,150,100,batch=batch)
    return 0.2*x*x + -17.5*x + 383

# To print the globals
from pprint import pprint
if __name__ == '__main__':
    pprint(globals())