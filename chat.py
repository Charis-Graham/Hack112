from cmu_112_graphics import *

def appStarted(app):
    app.mainButtons = []

#Button class created by Ollie Arrison
class Button(object):
# x and y refer to the top left corner
# response passes in the function that is called when the button is pressed
# if the future, make the option for rectangular buttons
    def __init__(self, app, size, x, y, response, isActive, images, mode):
        self.app = app
        self.size = size
        self.x = x
        self.y = y
        self.response = response
        self.isActive = isActive
        self.images = images
        self.mode = mode
    
    # resets all other buttons
    def resetAllElse(self, app):
        self.isActive = True
        for button in app.mainButtons:
            if self != button:
                button.isActive = False
        

    # check if it has been clicked
    def checkClicked(self,x,y,app):
        x1 = self.x
        x2 = self.x + self.size
        y1 = self.y
        y2 = self.y + self.size
    
        # if it has
        if (x >= x1 and x <= x2) and (y >= y1 and y <= y2):
            #do the response and set iteself to active
            self.response(self.app)
            self.isActive = True
            return True
        return False

    # draw the buttons using the image based on whether is active
    def drawButton(self, app, canvas):
        if (self.isActive):
            canvas.create_image(self.x + self.size//2, self.y + self.size//2,
                        image = ImageTk.PhotoImage(self.images[1]))
        else:
            canvas.create_image(self.x + self.size//2, self.y + self.size//2,
                        image = ImageTk.PhotoImage(self.images[0]))

#text class here

def mousePressed(app, event):
    mouseX = event.x
    mouseY = event.y
    print(mouseX, mouseY)

def keyPressed(app, event):
    return 42

def redrawAll(app, canvas):
    #background
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "lightblue")
    #textboxes

runApp(width=300, height=500)