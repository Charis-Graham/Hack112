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
    app.sparkles = True
    app.heart = 2
    app.background = 2
    app.sparkleCoors = [[1.5,4,10],[5,1.5,2],[3,9,18],
                        [2,1,8],[8,8,18],[7,3,18],
                        [8,1.5,8],[2,8,3],[7,6,18]]



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
    updateSparkles(app)

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
    
    #create the questions
    questionsText, answerButtons = questionInfo(app)
    for key in range(1, len(questionsText)):
        currentQuestion = question(questionsText[key], answerButtons[key])
    
    #list of questions
    questionList = ["",
                    "How are you?",
                    "How many meals have you eaten today?",
                    "Have you drunk water today?",
                    "Have you slept today?",
                    "Have you exercised today?",
                    "Have you spent time with friends or family today?",
                    "Have you gone outside today?",
                    "Have you meditated today?"]
    inBetweenBoxes = app.width//30

    #load the questions onto the screen
    questionOnScreen = []
    for i in range(1, len(questionList)):
        questionOnScreen.append(questionList[i])
        drawRounded(app, canvas, questionOnScreen, inBetweenBoxes, adjustX)
        
        # #load in the buttons
        # for button in app.mainButtons:
        #     button.drawButton(app, canvas)
        
        questionText, answerButtons = questionInfo(app)
        for button in answerButtons[i]:
            button.drawButton(app, canvas)
  

    drawSparkles(app, canvas, 0,0,(app.width//5)*3,app.height)


    mechanics(app)




runApp(width=900, height=600)
