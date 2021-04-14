# This file will take care of loading all of the sound files in the game
import pyglet, os



#                   ********Functions*********







#                   ********Paths*********

#Image directory
dirname = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'resources','audioFiles'))



# Music These files will be streamed from the source to save RAM space
dirname_music = os.path.join(dirname,'music')
backgroundmusic1 = pyglet.media.load(os.path.join(dirname_music,'backgroundmusic1.mp3'))
backgroundmusic2 = pyglet.media.load(os.path.join(dirname_music,'backgroundmusic2.mp3'))
backgroundmusic3 = pyglet.media.load(os.path.join(dirname_music,'backgroundmusic3.wav'))
backgroundmusic4 = pyglet.media.load(os.path.join(dirname_music,'backgroundmusic4.wav'))
battlescene1 = pyglet.media.load(os.path.join(dirname_music,'battlescene1.wav'))
battlescene2 = pyglet.media.load(os.path.join(dirname_music,'battlescene2.wav'))
startingScreenMusic = pyglet.media.load(os.path.join(dirname_music,'startingScreenMusic.wav'))



# Sounds These files will sit in memory for fast pace use
dirname_sounds = os.path.join(dirname,'sounds')
arcaneattack = pyglet.media.load(os.path.join(dirname_sounds,'arcaneattack.wav'), streaming=False)
buidlingwall = pyglet.media.load(os.path.join(dirname_sounds,'buidlingwall.mp3'), streaming=False)
dyingman1 = pyglet.media.load(os.path.join(dirname_sounds,'dyingman1.wav'), streaming=False)
dyingman2 = pyglet.media.load(os.path.join(dirname_sounds,'dyingman2.wav'), streaming=False)
dyingman3 = pyglet.media.load(os.path.join(dirname_sounds,'dyingman3.wav'), streaming=False)
fireattack = pyglet.media.load(os.path.join(dirname_sounds,'fireattack.wav'), streaming=False)
fireimpact = pyglet.media.load(os.path.join(dirname_sounds,'fireimpact.wav'), streaming=False)
gatheringmetal = pyglet.media.load(os.path.join(dirname_sounds,'gatheringmetal.mp3'), streaming=False)
gatheringwood = pyglet.media.load(os.path.join(dirname_sounds,'gatheringwood.wav'), streaming=False)
hitbyice = pyglet.media.load(os.path.join(dirname_sounds,'hitbyice.wav'), streaming=False)
hitbyspell = pyglet.media.load(os.path.join(dirname_sounds,'hitbyspell.wav'), streaming=False)
iceattack = pyglet.media.load(os.path.join(dirname_sounds,'iceattack.wav'), streaming=False)
knifeattack = pyglet.media.load(os.path.join(dirname_sounds,'knifeattack.wav'), streaming=False)
levelup = pyglet.media.load(os.path.join(dirname_sounds,'levelup.wav'), streaming=False)
MakeBuidling = pyglet.media.load(os.path.join(dirname_sounds,'MakeBuidling.wav'), streaming=False)
punchwam = pyglet.media.load(os.path.join(dirname_sounds,'punchwam.wav'), streaming=False)
smallexplosion = pyglet.media.load(os.path.join(dirname_sounds,'smallexplosion.wav'), streaming=False)
twistedspellexplosion = pyglet.media.load(os.path.join(dirname_sounds,'twistedspellexplosion.wav'), streaming=False)
