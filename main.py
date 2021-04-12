# Main file for Fortress Defenders 
# Created on 4/9/2021 by Dominik Chraca


import pyglet, os
from dependents import config
from dependents import load

#Globals
dirname = os.path.dirname(os.path.abspath(__file__))
game_window = pyglet.window.Window(config.WIDTH, config.HEIGHT, fullscreen= config.FULLSCREEN)
main_batch = pyglet.graphics.Batch()

counter = pyglet.window.FPSDisplay(window=game_window)

#Global Objects list
game_objects = []


#Functions
@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    counter.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)

    # Get rid of dead objects
    for to_remove in [obj for obj in game_objects if obj.dead]:
        # Remove the object from any batches it is a member of
        to_remove.delete()

        # Remove the object from our list
        game_objects.remove(to_remove)

if __name__ == '__main__':
    game_objects.append(load.Spawn_ArcanBolt(main_batch))

    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / config.MAXFPS)

    pyglet.app.run()