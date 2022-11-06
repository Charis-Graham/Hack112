from cmu_112_graphics import *
from robot import *
from rounded import *
from extras import *
from color import *
from buttonsNQuestions import *

def appStarted(app):
    print("")
    app.sparkles = False
    app.heart = 0
    app.background = 2
    app.points = 0
    app.mainButtons = loadButtons(app)

    app.heartColor = grey(100)


"""
baseline
happy
sad

facial expression
heart color
background color
sparkles

"""

def timerFired(app):
    updateExtras(app)

def mousePressed(app, event):
    mouseX = event.x
    mouseY = event.y
    for button in app.mainButtons:
        button.checkClicked(mouseX, mouseY, app)
    print(mouseX, mouseY)

def mechanics(app):
    if app.points > 5:
        #happy robot
        pass
    elif app.points > 4:
        #functioning robot
        pass
    else:
        #unhealthy robot
        pass


# draw the windows
def drawWindows(app, canvas):
    drawTopWindow(app, canvas)
    drawSideBar(app, canvas)

# draw the top
def drawTopWindow(app, canvas):
    fillColor = rgbString(32,33,36)
    canvas.create_rectangle(0,0,app.width,app.height//15,
    fill = fillColor, outline = '#181818')

# draw the side
def drawSideBar(app, canvas):
    fillColor = rgbString(32,33,36)
    sideBarMargin = (app.width//5)*2
    canvas.create_rectangle(
        app.width-sideBarMargin,0,
        app.width, app.height,
    fill = fillColor, outline = '#181818')

def redrawAll(app, canvas):
    adjustX = app.width//5
    drawNiceRobot(app, canvas, adjustX)
    drawWindows(app, canvas)
    sampleList = ["Is this a question?", "How goes?", "This is a sentence", 
    "Is your mental health in shambles?", "What's your favorite color?"]
    inBetweenBoxes = app.width//30
    #drawRoundedBoxes(app, canvas, sampleList, inBetweenBoxes, adjustX)
    drawRounded(app, canvas, sampleList, inBetweenBoxes, adjustX)

    #load in the buttons
    for button in app.mainButtons:
        button.drawButton(app, canvas)

    #create the questions
    questionsText, answerButtons = questionInfo(app)
    for key in range(1, len(questionsText)):
        currentQuestion = question(questionsText[key], answerButtons[key])
    
    mechanics(app)




runApp(width=900, height=600)
