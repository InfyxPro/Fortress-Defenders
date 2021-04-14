# This function will be a helper function to simplify connection of controllers
import pyglet, os, config, time

dirname = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'resources','etc'))




class controllers():
    def __init__(self, addController = False):
        self.deviceList = pyglet.input.get_joysticks()
        self.amountOfControllers = len(self.deviceList)
        self.deviceList[0].open()
        
    def begin(self):
        self.deviceList = pyglet.input.get_joysticks()
        self.amountOfControllers = len(self.deviceList)

    def addControllers(self):
        response = 1
        while response:
            print("Connected devices: ")
            for i in self.deviceList:
                print(i.device)
            response = int(input("\nWould you like to re-search for controllers? '1'=yes '0'=no: "))
            print()
        print('\n\n\n')
        response = 0
        while not response:
            index = int(input("Which device would you like to select? Type in a number using zero indexing to select: "))
            try:
                response = int(input("\nIs this the correct controller you selected? " + str(self.deviceList[index].device) + " '1'=yes '0'=no: "))
            except:
                print("The device you selected is out of range, try again...")
        print('\n\n\n')

        # This next part will open a file with the name of the controller and begin the mapping script
        nameOfFile = str(self.deviceList[index].device)
        self.deviceList[index].open
        print(nameOfFile, " Selected!")
        listOfButtonMappings = ["A", "B", "Y", "X", "Start", "Select", "Right Bumper", "Left Bumper", "Left Stick", "Right Stick"]
        listOfDpadMappings = ["left", "right", "up", "down"]
        listOfJoystickMappings = ["Left Joystick Up", "Left Joystick down" ,"Left Joystick right" ,"Left Joystick left" \
                                  "Right Joystick Up", "Right Joystick down" ,"Right Joystick right" ,"Right Joystick left"]

    def updateTesting(self):
        #print(self.deviceList[0].buttons)
        #print(round(self.deviceList[0].hat_x,2), round(self.deviceList[0].hat_y,2), round(self.deviceList[0].rz,2))
        time.sleep(.01)


# This will allow you to initialize different controller mapings and save it to a file
# Only have one controller plugged in at a time when doing this
if __name__ == '__main__':
    controller = controllers(True)
    #controller.addControllers()

    def update(dt):
        controller.updateTesting()

    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / config.MAXFPS)
    pyglet.app.run()
