import pyglet
import random
from . import Objects
from . import imageloads
from . import config


def Spawn_Gatherer(x, y, batch=None):
    gatherer = []

    new_gatherer = pyglet.sprite.Sprite(img=imageloads.asteroid_image,
                                            x=asteroid_x, y=asteroid_y)

    gatherer.append(new_gatherer)

def Spawn_ArcanBolt(batch=None):
    ArcaneBolt = Objects.Projectile(imageloads.ArcaneBolt_Animation[0],config.WIDTH/2,config.HEIGHT/2,config.PI*5/3,0,150,100,batch=batch)
    ArcaneBolt.scale = 0.2
    return ArcaneBolt

def Spawn_Explosion(batch=None):
    ArcaneBolt = Objects.Projectile(imageloads.FireExplosion_Animation[0],config.WIDTH/2,config.HEIGHT/2,0,0,150,0,batch=batch, duration = imageloads.FireExplosion_Animation[0].get_duration()*1.4)
    ArcaneBolt.scale = 1
    return ArcaneBolt





