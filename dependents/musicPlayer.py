# This file will take care of playing background music for the game. 
import pyglet
import soundload
import config
import random
import time

class backgroundPlayer():
    def __init__(self):
       # Some globals of the pyglet music files
       self.startingScreenMusic = soundload.startingScreenMusic
       self.backgroundmusicList = [[soundload.backgroundmusic1, 0.08] ,\
                                   [soundload.backgroundmusic2,0.15]  ,\
                                   [soundload.backgroundmusic3, 0.1],\
                                   [soundload.backgroundmusic4, 0.2]]
       self.battlesceneMusicList = [soundload.battlescene1,\
                                    soundload.battlescene2]
       
       # Built in needed variables
       random.seed(time.time())
       self.player = pyglet.media.Player()
       self.timer = 0   #In seconds
       self.timeTillNextBackgroundMusic = 0
       self.state = 0 #States: 0 = startingScreenMusic, 1 = backgroundmusicList, 2 = battlesceneMusicList
       self.player.volume = config.MUSICVOLUME

    def update(self, dt):
        #This is to update the clock
        self.timer += dt
        if self.state == 1 and self.timeTillNextBackgroundMusic < self.timer:
            self.playBackgroundMusic()
    
    def playBackgroundMusic(self):
    # This function will randomly play the backgroundmusicList music. However, half the time the music will not be played
        musicIndex = random.randint(0,2*len(self.backgroundmusicList)) # There is a 50% chance it will not play music
        self.player.loop = False
        self.state = 1
        self.player.next_source()

        if musicIndex >= len(self.backgroundmusicList): #if true, don't play music for x time
            self.timeTillNextBackgroundMusic = random.randint(30, 120) + self.timer
        else:
            self.player.volume *= self.backgroundmusicList[musicIndex][1]
            self.player.queue(self.backgroundmusicList[musicIndex][0])
            self.player.play()
            self.timeTillNextBackgroundMusic = self.backgroundmusicList[musicIndex][0].duration + self.timer + 10 # Add a 10 second buffer

    def playStartingScreenMusic(self):
        self.state = 0
        self.player.next_source()
        self.player.loop = True
        self.player.queue(self.startingScreenMusic)
        self.player.play()

    def playBattlesceneMusic(self):
        # Randomly choose the music
        select = random.randint(0,len(self.battlesceneMusicList) - 1)
        self.player.volume *= 0.35
        self.state = 2
        self.player.next_source()
        self.player.loop = True
        self.player.queue(self.battlesceneMusicList[select])
        self.player.play()


if __name__ == '__main__':
    PLAYER = backgroundPlayer()
    PLAYER.playBackgroundMusic()
    def update(dt):
        PLAYER.update(dt)

    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / config.MAXFPS)
    pyglet.app.run()