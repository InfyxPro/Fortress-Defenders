# This function will be a helper function to simplify connection of controllers
import pyglet, os, time, pygame, subprocess
from . import config

dirname = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'resources','etc','controller_profiles'))



class Controllers():
    def __init__(self):
        self.listOfButtonMappings = ["A", "B", "Y", "X", "Start", "Select", "Right_Bumper", "Left_Bumper", "Left_Stick", "Right_Stick"]
        self.listOfDpadMappings = ["leftDpad", "rightDpad", "upDpad", "downDpad"]
        self.listOfJoystickMappings = ["Left_Joystick_X", "Left_Joystick_Y", "Right_Joystick_X", "Right_Joystick_Y", "Right_Trigger", "Left_Trigger"]

        # Need this to update the controllers
        pygame.display.init()
        pygame.joystick.init()
        self.deviceList = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        self.amountOfControllersActive = 0
        self.activeControllersList = [[device, 0] for device in self.deviceList] #Device list with a second attribute to show if it is in use
        

    def getInactiveDevice(self): #Return device if available, if not, return False
        for i in range(len(self.activeControllersList)):
            if (self.activeControllersList[i][1] == 0):
                self.activeControllersList[i][1] = 1
                self.amountOfControllersActive += 0
                return self.activeControllersList[i][0]
        return False

    # Only used when adding controllers
    def addControllers(self):
        response = 1
        while response:
            print("Connected devices: ")
            for i in self.deviceList:
                print(i.get_name())
            response = int(input("\nWould you like to re-search for controllers? '1'=yes '0'=no: "))
            print()
        print('\n\n\n')
        response = 0
        while not response:
            index = int(input("Which device would you like to select? Type in a number using zero indexing to select: "))
            try:
                response = int(input("\nIs this the correct controller you selected? " + str(self.deviceList[index].get_name()) + " '1'=yes '0'=no: "))
            except:
                print("The device you selected is out of range, try again...")
        print('\n\n\n')

        # This next part will open a file with the name of the controller and begin the mapping script
        nameOfFile = str(self.deviceList[index].get_name())
        self.deviceList[index].init()
        print(nameOfFile, " Selected!")
        
        listOfButtonMappingsToAdd = []
        listOfDpadMappingsToAdd = []
        listOfJoystickMappingsToAdd = []
        print("Run python controllerHelper.py to help you figure out what buttons are what")
        input("This next part will ask you to press buttons and move joysticks certain ways. Between each request, press enter. Press enter to begin...")

        
        for i in self.listOfButtonMappings:
            response = input("Press "+i+" button and type into terminal to record. Just type the index number: ").strip()
            listOfButtonMappingsToAdd.append(response)

        print("Now for DPAD")
        for i in self.listOfDpadMappings:
            response = input("Press "+i+" button and type into terminal to record. Just type the index number and if negative \
                            For instance, if: getting -1 at index 0, then type: -0 - getting 1 at index 0, then type: 0:").strip()
            listOfDpadMappingsToAdd.append(response)

        print("Now for analog sticks")
        for i in self.listOfJoystickMappings:
            response = input("Move "+i+" button and type into terminal to record. Just type the index number: ").strip()
            listOfJoystickMappingsToAdd.append(response)

        print("Done")

        file = open(os.path.join(dirname,nameOfFile+".txt"), 'w')
        for value in listOfButtonMappingsToAdd:
            file.write(value)
            file.write(" ")
        file.write("\n")
        for value in listOfJoystickMappingsToAdd:
            file.write(value)
            file.write(" ")
        file.write("\n")
        for value in listOfDpadMappingsToAdd:
            file.write(value)
            file.write(" ")
        file.close

        print("Recorded in ",os.path.join(dirname,nameOfFile+".txt"))



    def updateTesting(self):
        buttons = self.deviceList[0].get_numbuttons()
        for i in range(buttons):
            button = self.deviceList[0].get_button(i)
            print(button,end=" ")
        print()

class Controller():
    def __init__(self, Controllers):
        self.Controllers = Controllers
        self.controller = Controllers.getInactiveDevice()
        self.listOfButtonMappings = []
        self.listOfDpadMappings = []
        self.listOfJoystickMappings = []
        self.initializeDeviceMappings()

        self.listOfButtonStates = [0 for i in range(len(self.Controllers.listOfButtonMappings))] # To calculate know if a putton was pressed



    def initializeDeviceMappings(self):
        controllerName = self.controller.get_name()
        file = 0
        try:
            file = open(os.path.join(dirname,controllerName + ".txt"), 'r')
        except:
            #File not found, using default file 
            file = open(os.path.join(dirname,"default.txt"), 'r')

        self.listOfButtonMappings = list(map(int ,file.readline().split()))
        self.listOfJoystickMappings = list(map(int ,file.readline().split()))
        self.listOfDpadMappings = self.initializeDpad(file.readline().split())
        file.close()

    def initializeDpad(self, listOfDpadString):
        newDpadList = []
        for i in listOfDpadString:
            sign = 1
            index = 0
            for letter in i:
                if letter == '-':
                    sign = -1
                else:
                    index = int(letter)
            newDpadList.append((sign, index))
        return newDpadList


    def getPowerLevel(self):
        return self.controller.get_power_level()

    def get_guid(self):
        return self.controller.get_guid()

    def get_button_status(self, button, trigger = "always"):
        # the trigger argument returns when triggers, always, onPress, onRelease
        assert button in self.Controllers.listOfButtonMappings, button + " is not a registered button"
        
        for i in range(len(self.Controllers.listOfButtonMappings)):
            if (self.Controllers.listOfButtonMappings[i] == button):    #Button Found
                if trigger == "always":
                    state = self.controller.get_button(self.listOfButtonMappings[i])
                    self.listOfButtonStates[i] = state
                    return state
                    
                elif trigger == "onPress":
                    if self.listOfButtonStates[i] != self.controller.get_button(self.listOfButtonMappings[i]):
                        state = self.controller.get_button(self.listOfButtonMappings[i])
                        self.listOfButtonStates[i] = state
                        return state
                    else:
                        return 0

    def get_dpad_status(self, dpad):
        assert dpad in self.Controllers.listOfDpadMappings, dpad + " is not a registered dpad command"
        for i in range(len(self.Controllers.listOfDpadMappings)):
            if (self.Controllers.listOfDpadMappings[i] == dpad):    #Button Found
                state = self.controller.get_hat(0)[self.listOfDpadMappings[i][1]] == self.listOfDpadMappings[i][0]
                return state

    def get_analog_inputs(self, input):
        assert input in self.Controllers.listOfJoystickMappings, input + " is not a registered analog input command"
        
        for i in range(len(self.Controllers.listOfJoystickMappings)):
            if (self.Controllers.listOfJoystickMappings[i] == input):    #Button Found
                state = self.controller.get_axis(self.listOfJoystickMappings[i])
                return state



# This will allow you to initialize different controller mapings and save it to a file
# Only have one controller plugged in at a time when doing this
if __name__ == '__main__':
    controller = Controllers()
    controller.addControllers()
    xbox = Controller(controller)
    while 1:
        for event in pygame.event.get(): # User did something.
            pass









