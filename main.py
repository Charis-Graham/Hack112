from cmu_112_graphics import *
from robot import *
from rounded import *
from extras import *
from color import *
from buttonsNQuestions import *

def appStarted(app):
    app.sparkles = False
    app.heart = 0
    app.background = 0
    app.points = 0
    app.mainButtons = loadButtons(app)
    app.smile = 0
    app.eyes = 0
    
    app.heartColor = grey(100)
    app.sparkleCoors = [[1.5,4,10],[5,1.5,2],[3,9,18],
                        [2,1,8],[8,8,18],[7,3,18],
                        [8,1.5,8],[2,8,3],[7,6,18]]


def timerFired(app):
    updateExtras(app)
    updateSparkles(app)
    mechanics(app)

def mousePressed(app, event):
    mouseX = event.x
    mouseY = event.y
    for button in app.mainButtons:
        button.checkClicked(mouseX, mouseY, app)

def mechanics(app):
    if app.points == 9:
        app.sparkles = True
        app.heart = 2
        app.background = 2
        app.smile = 2
        app.eyes = 2
    elif app.points > 5:
        #happy robot
        app.sparkles = False
        app.heart = 2
        app.background = 2
        app.smile = 2
        app.eyes = 2
    elif app.points > 4:
        # functional robot
        app.sparkles = False
        app.heart = 1
        app.background = 1
        app.smile = 1
        app.eyes = 1
    else:
        # unwell robot
        app.heart = 0
        app.background = 0
        app.smile = 0
        app.eyes = 0


# draw the windows
def drawWindows(app, canvas):
    drawSideBar(app, canvas)
    drawTopWindow(app, canvas)

# draw the top
def drawTopWindow(app, canvas):
    fillColor = rgbString(32,33,36)
    canvas.create_rectangle(0,0,app.width,app.height//15,
    fill = fillColor, outline = '#181818')

# draw the side
def drawSideBar(app, canvas):
    fillColor = rgbString(52,53,56)
    sideBarMargin = (app.width//5)*2
    canvas.create_rectangle(
        app.width-sideBarMargin,0,
        app.width, app.height,
    fill = fillColor, outline = '#181818')

def redrawAll(app, canvas):
    adjustX = app.width//5
    drawNiceRobot(app, canvas, adjustX)
#     sampleList = ["Is this a question?", "How goes?", "This is a sentence",
#     "Is your mental health in shambles?", "What's your favorite color?"]
#     inBetweenBoxes = app.width//30
#     #drawRoundedBoxes(app, canvas, sampleList, inBetweenBoxes, adjustX)
#     drawWindows(app, canvas)
#     drawRounded(app, canvas, sampleList, inBetweenBoxes, adjustX)
#     if (app.sparkles):
#         drawSparkles(app, canvas, 0,0,(app.width//5)*3,app.height)

#     #load in the buttons
#     for button in app.mainButtons:
#         button.drawButton(app, canvas)

#     #create the questions
#     questionsText, answerButtons = questionInfo(app)
#     for key in range(1, len(questionsText)):
#         currentQuestion = question(questionsText[key], answerButtons[key])

    #create the questions 
    questionList, answerButtons = questionInfo(app)
    for key in range(0, len(questionList)):
        currentQuestion = question(questionList[key], answerButtons[key])
    
    inBetweenBoxes = app.width//20

    #load the questions onto the screen
    questionOnScreen = []
    for i in range(0, len(questionList)):
        questionOnScreen.append(questionList[i])
        xPositions, yPositions = drawRounded(app, canvas, questionOnScreen, 
                                            inBetweenBoxes, adjustX)
        
        questionText, answerButtons = questionInfo(app)
        for button in answerButtons[i]:
            button.drawButton(app, canvas, xPositions[i], yPositions[i])
  

runApp(width=900, height=600)
