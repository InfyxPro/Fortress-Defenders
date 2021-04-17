# This file will take care of loading all of the image files in the game
import pyglet, os



#                   ********Functions*********

#This function returns a list of the png images pyglet image file.
def image_compiler(path):
    i = 0 #This is the index number for each image
    imageList = []
    while i <= 99:
        try: #Just go until out of bounce
            #This is to make format like this: tile001.png ... tile052.png and so on...
            number = str(i)
            numOfZeros = 3 - len(number)
            number = (numOfZeros * '0') + number

            pathName = 'tile' + number + '.png'
            i += 1

            image = pyglet.image.load(os.path.join(path,pathName))
            imageList.append(image)
        except:
            #nothing hear
            pass

    #For efficiency
    bin = pyglet.image.atlas.TextureBin()
    imageList = [bin.add(image) for image in imageList]
    
    for image in imageList:
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
    return imageList


# This function takes a list of images and creates a gif. 
# Some info:: DataFrame = [Durration, DownFrames, UpFrames, RightFrames, LeftFrames]]
def animation_maker(images, DataFrame = [], isDyingFrame = 0, loop=True):
    animationList = []

    if isDyingFrame == 0:
        duration = DataFrame[0]
        for i in range(1,4):
            (start,end) = DataFrame[i]
            currentFrames = images[start:end+1]
            ani = pyglet.image.Animation.from_image_sequence(currentFrames, duration=duration, loop=loop)
            animationList.append(ani)
    else:
        #Use isDyingFrame as the duration for the DyingFrame
        duration = isDyingFrame
        ani = pyglet.image.Animation.from_image_sequence(images, duration=duration, loop=loop)
        animationList.append(ani)
    return animationList
    



#                   ********Paths*********

#Image directory
dirname = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'resources','images'))

#Gatherer
gathererHandsPath = os.path.join(dirname,"imp1","imp_hands")
gathererHandsPathAttack = os.path.join(gathererHandsPath,"attack")
gathererHandsPathWalk = os.path.join(gathererHandsPath,"walk")
gathererHandsPathdie = os.path.join(gathererHandsPath,"die")

gathererSpearPath = os.path.join(dirname,"imp1","imp_spear")
gathererSpearPathAttack = os.path.join(gathererHandsPath,"attack")
gathererSpearPathWalk = os.path.join(gathererHandsPath,"walk")
gathererSpearPathdie = os.path.join(gathererHandsPath,"die")


#Builder
BuilderHandsPath = os.path.join(dirname,"golem")
BuilderHandsPathAttack = os.path.join(BuilderHandsPath,"attack")
BuilderHandsPathWalk = os.path.join(BuilderHandsPath,"walk")
BuilderHandsPathdie = os.path.join(BuilderHandsPath,"die")


#Warrior
WarriorHandsPath = os.path.join(dirname,"goblin","hand")
WarriorHandsPathAttack = os.path.join(WarriorHandsPath,"attack")
WarriorHandsPathWalk = os.path.join(WarriorHandsPath,"walk")
WarriorHandsPathdie = os.path.join(WarriorHandsPath,"die")

WarriorSwordPath = os.path.join(dirname,"goblin","sword")
WarriorSwordPathAttack = os.path.join(WarriorSwordPath,"attack")
WarriorSwordPathWalk = os.path.join(WarriorSwordPath,"walk")
WarriorSwordPathdie = os.path.join(WarriorSwordPath,"die")

#Projectiles
ArcaneBolt_path = os.path.join(dirname,"Arcane_Effect","bestone")

#FireExplosion
FireExplosion_path = os.path.join(dirname,"FireExplosion")



#                   ********Compiled Image File Names*********
# List Formats
#   DataFrame = [Durration, DownFrames, UpFrames, RightFrames, LeftFrames]
#   FinishedImageAniData_XxxXxx = [[StillImages], [AttackAnimation], [WalkAnimation], [DieAnimation]]   
#       Gatherer 
# Hands
GathererDataFrame = [0.2, (0,3), (4,7), (8,11), (12,15)]
gathererHandsAttackImages = image_compiler(gathererHandsPathAttack)
gathererHandsWalkImages = image_compiler(gathererHandsPathWalk)
gathererHandsDieImages = image_compiler(gathererHandsPathdie)

gathererHandsstillImages = [gathererHandsWalkImages[0], gathererHandsWalkImages[4], gathererHandsWalkImages[8], gathererHandsWalkImages[12]]
gathererHandsAttackAnimation = animation_maker(gathererHandsAttackImages ,GathererDataFrame)
gathererHandsWalkAnimation = animation_maker(gathererHandsWalkImages ,GathererDataFrame)
gathererHandsDieAnimation = animation_maker(gathererHandsDieImages ,GathererDataFrame, isDyingFrame = 0.2)

FinishedImageAniData_gathererHands = [gathererHandsstillImages] + [gathererHandsAttackAnimation] + [gathererHandsWalkAnimation] + [gathererHandsDieAnimation]

# Spear
gathererSpearAttackImages = image_compiler(gathererSpearPathAttack)
gathererSpearWalkImages = image_compiler(gathererSpearPathWalk)
gathererSpearDieImages = image_compiler(gathererSpearPathdie)

gathererSpearstillImages = [gathererSpearWalkImages[0],gathererSpearWalkImages[4],gathererSpearWalkImages[8],gathererSpearWalkImages[12]]
gathererSpearAttackAnimation = animation_maker(gathererSpearAttackImages ,GathererDataFrame)
gathererSpearWalkAnimation = animation_maker(gathererSpearWalkImages ,GathererDataFrame)
gathererSpearDieAnimation = animation_maker(gathererSpearDieImages ,GathererDataFrame, isDyingFrame = 0.2)

FinishedImageAniData_gathererHands = [gathererSpearstillImages] + [gathererSpearAttackAnimation] + [gathererSpearWalkAnimation] + [gathererSpearDieAnimation]

#       Builder
# Hands
BuilderDataFrame = [0.2, (14,20), (0,6), (21,27), (7,13)]
BuilderHandsAttackImages = image_compiler(BuilderHandsPathAttack)
BuilderHandsWalkImages = image_compiler(BuilderHandsPathWalk)
BuilderHandsDieImages = image_compiler(BuilderHandsPathdie)
BuilderHandsstillImages = [BuilderHandsAttackImages[14],BuilderHandsAttackImages[0],BuilderHandsAttackImages[21],BuilderHandsAttackImages[7]]

#       Warrior
# Hands
WarriorDataFrame = [0.2, (0,4), (10,14), (5,9), (15,19)]
WarriorHandsAttackImages = image_compiler(WarriorHandsPathAttack)
WarriorHandsWalkImages = image_compiler(WarriorHandsPathWalk)
WarriorHandsDieImages = image_compiler(WarriorHandsPathdie)
WarriorHandsstillImages = [WarriorHandsAttackImages[0],WarriorHandsAttackImages[10],WarriorHandsAttackImages[5],WarriorHandsAttackImages[15]]
# Sword
WarriorSwordAttackImages = image_compiler(WarriorSwordPathAttack)
WarriorSwordWalkImages = image_compiler(WarriorSwordPathWalk)
WarriorSwordDieImages = image_compiler(WarriorSwordPathdie)
WarriorHandsstillImages = [WarriorSwordAttackImages[0],WarriorSwordAttackImages[10],WarriorSwordAttackImages[5],WarriorSwordAttackImages[15]]


#       Projectiles
#Arcane_bolt
ArcaneBolt_Images = image_compiler(ArcaneBolt_path)
ArcaneBolt_Animation = animation_maker(ArcaneBolt_Images, isDyingFrame = 0.1)

#FireExplosion
FireExplosion_Images = image_compiler(FireExplosion_path)
FireExplosion_Animation = animation_maker(FireExplosion_Images, isDyingFrame = 0.01, loop = False)

# To print the Image files
if __name__ == '__main__':
    pass
