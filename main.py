from cmu_112_graphics import *
from robot import *
from roundedBox import *
from rounded import *
from extras import *

def appStarted(app):
    print("")
    app.sparkles = False
    app.heart =2

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

# draw the windows
def drawWindows(app, canvas):
    drawTopWindow(app, canvas)
    drawSideBar(app, canvas)

# draw the top
def drawTopWindow(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height//15,
    fill = '#181818', outline = '#181818')

# draw the side
def drawSideBar(app, canvas):
    sideBarMargin = (app.width//5)*2
    canvas.create_rectangle(
        app.width-sideBarMargin,0,
        app.width, app.height,
    fill = '#181818', outline = '#181818')

def redrawAll(app, canvas):
    adjustX = app.width//5
    drawNiceRobot(app, canvas, adjustX)
    drawWindows(app, canvas)
    sampleList = ["Is this a question?", "How goes?", "This is a sentence", 
    "Is your mental health in shambles?", "What's your favorite color?"]
    inBetweenBoxes = app.width//30
    #drawRoundedBoxes(app, canvas, sampleList, inBetweenBoxes, adjustX)
    drawRounded(app, canvas, sampleList, inBetweenBoxes, adjustX)

runApp(width=900, height=600)