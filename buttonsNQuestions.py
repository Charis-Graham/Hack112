from cmu_112_graphics import *

#BUTTONS
#button creation
def loadButtons(app, size):
    #buttons for the first question
    app.smileButton = Button(app, size, 10, 10, response, False, 
                    (getImage("smile", app)), 0)
    app.frownButton = Button(app, size, 110, 10, response, False, 
                    (getImage("frown", app)), 0)
    app.neutralButton = Button(app, size, 210, 10, response, False, 
                    (getImage("neutral", app)), 0)
    
    #buttons for the second question
    app.noFoodButton = Button(app, size, 10, 70, response, False, 
                    (getImage("nofood", app)), 0)
    app.oneButton = Button(app, size, 110, 70, response, False, 
                    (getImage("one", app)), 1)
    app.twoButton = Button(app, size, 210, 70, response, False, 
                    (getImage("two", app)), 2)
    app.threeButton = Button(app, size, 310, 70, response, False, 
                    (getImage("three", app)), 3)
    
    #buttons for questions 3
    app.yesButtonThree = Button(app, size, 10, 130, response, False,
                    (getImage("check", app)), 1)
    app.noButtonThree = Button(app, size, 110, 130, response, False, 
                    (getImage("no", app)), 0)

    #buttons for questions 3
    app.yesButtonFour = Button(app, size, 10, 190, response, False,
                    (getImage("check", app)), 1)
    app.noButtonFour = Button(app, size, 110, 190, response, False, 
                    (getImage("no", app)), 0)

    #buttons for questions 3
    app.yesButtonFive = Button(app, size, 10, 250, response, False,
                    (getImage("check", app)), 1)
    app.noButtonFive = Button(app, size, 110, 250, response, False, 
                    (getImage("no", app)), 0)
    
    #buttons for questions 3
    app.yesButtonSix = Button(app, size, 10, 310, response, False,
                    (getImage("check", app)), 1)
    app.noButtonSix = Button(app, size, 110, 310, response, False, 
                    (getImage("no", app)), 0)

    #buttons for questions 3
    app.yesButtonSeven = Button(app, size, 10, 370, response, False,
                    (getImage("check", app)), 1)
    app.noButtonSeven = Button(app, size, 110, 370, response, False, 
                    (getImage("no", app)), 0)
    
    #buttons for questions 3
    app.yesButtonEight = Button(app, size, 10, 430, response, False,
                    (getImage("check", app)), 1)
    app.noButtonEight = Button(app, size, 110, 430, response, False, 
                    (getImage("no", app)), 0)
    
    return [app.smileButton, app.frownButton, app.neutralButton, 
            app.noFoodButton, app.oneButton, app.twoButton, app.threeButton,
            app.yesButtonThree, app.noButtonThree, 
            app.yesButtonFour, app.noButtonFour,
            app.yesButtonFive, app.noButtonFive,
            app.yesButtonSix, app.noButtonSix,
            app.yesButtonSeven, app.noButtonSeven,
            app.yesButtonEight, app.noButtonEight]
    
def response(app, point):
    app.points += point

#getImage created by Ollie Arrison
def getImage(name, app):
   imageTitle = "buttons/" + name + ".png"
   imageTitleActive = "buttons/" + name + "-active" + ".png"
 
   image = app.loadImage(imageTitle)
   image = app.scaleImage(image, 1)
 
   imageActive = app.loadImage(imageTitleActive)
   imageActive = app.scaleImage(imageActive, 1)
   return (image, imageActive)

#Button class created by Ollie Arrison
class Button(object):
# x and y refer to the top left corner
# response passes in the function that is called when the button is pressed
# if the future, make the option for rectangular buttons
    def __init__(self, app, size, x, y, response, isActive, images, point):
        self.app = app
        self.size = size
        self.x = x
        self.y = y
        self.response = response
        self.isActive = isActive
        self.images = images
        self.point = point
    
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
            self.response(self.app, self.point)
            self.isActive = True
            self.point = 0
            return True
        return False

    # draw the buttons using the image based on whether is active
    def drawButton(self, app, canvas, x, y):
        self.x = x
        self.y = y + (self.size//4)
        if (self.isActive):
            canvas.create_image(self.x + self.size//2, self.y + self.size//2,
                        image = ImageTk.PhotoImage(self.images[1]))
        else:
            canvas.create_image(self.x + self.size//2, self.y + self.size//2,
                        image = ImageTk.PhotoImage(self.images[0]))

#QUESTIONS
#the questions in the chat
class question:
    def __init__(self, text, possibleAnswers):
        self.text = text
        self.possibleAnswers = possibleAnswers
        self.answer = 0

def questionInfo(app):
    #list of the questions
    #list of questions
    questionList = [
                    "How are you?",
                    "How many meals have you eaten today?",
                    "Have you drunk water today?",
                    "Have you slept today?",
                    "Have you exercised today?",
                    "Have you spent time with friends or family today?",
                    "Have you gone outside today?",
                    "Have you meditated today?"]   

    #list of the possible answers
    answerButtons = [
        [app.smileButton, app.frownButton, app.neutralButton],
        [app.noFoodButton, app.oneButton, app.twoButton, app.threeButton],
        [app.yesButtonThree, app.noButtonThree],
        [app.yesButtonFour, app.noButtonFour],
        [app.yesButtonFive, app.noButtonFive],
        [app.yesButtonSix, app.noButtonSix],
        [app.yesButtonSeven, app.noButtonSeven],
        [app.yesButtonEight, app.noButtonEight]
    ]

    return questionsList, answerButtons
