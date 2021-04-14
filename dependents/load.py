import pyglet
import random
import Objects
import imageloads
import config


def Spawn_Gatherer(x, y, batch=None):
    gatherer = []

    new_gatherer = pyglet.sprite.Sprite(img=imageloads.asteroid_image,
                                            x=asteroid_x, y=asteroid_y)

    gatherer.append(new_gatherer)

def Spawn_ArcanBolt(batch=None):
    ArcaneBolt = Objects.Projectile(imageloads.ArcaneBolt_Animation[0],config.WIDTH/2,config.HEIGHT/2,config.PI*5/3,0,150,100,batch=batch)
    ArcaneBolt.scale = 0.2
    return ArcaneBolt





