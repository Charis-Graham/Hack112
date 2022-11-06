from background import *

# robot code is modified from Ollie Arrison's (darrison) week 3 homework

def grey(n):
    return rgbString(n, n, n)

def coor(widthOrHeight, true, scale, dif):
    # adjust the coordinate based on the width, the true adjustment, the scale
    # adjustment, and the dif
    return widthOrHeight/2 - true * scale + dif

def rect(canvas, app, xCenter, yCenter, heightScale, widthScale, color):
    w = app.width
    h = app.height
    scale = 1

    canvas.create_rectangle(coor(w, widthScale, scale, xCenter),
                        coor(h, heightScale, scale, yCenter),
                        coor(w, -widthScale, scale, xCenter),
                        coor(h, -heightScale, scale, yCenter),
                            fill=color, outline='black')


# function from https://www.cs.cmu.edu/~112/notes/notes-graphics.html
def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def oval(canvas, app, xCenter, yCenter, heightScale, widthScale, color):
    w = app.width
    h = app.height
    scale = 1

    canvas.create_oval(coor(w, widthScale, scale, xCenter),
                    coor(h, heightScale, scale, yCenter),
                    coor(w, -widthScale, scale, xCenter),
                    coor(h, -heightScale, scale, yCenter),
                            fill=color, outline='black')

# draws the body, head, and neck of the robot
def drawNiceRobotBase(canvas, app, sX, sY, adjustX):
    shadeColor = grey(50)
    bodyColor = grey(60)

    shadeNeckX = 0 * sX - adjustX
    shadeNeckY = 20 * sY
    shadeNeckW = 60 * sX
    shadeNeckH = 40 * sY

    neckX = 0 * sX - adjustX
    neckY = 50 * sY
    neckW = 60 * sX
    neckH = 40 * sY

    bodyX = 0 * sX - adjustX
    bodyY = 150 * sY
    bodyW = 100 * sX
    bodyH = 125 * sY

    shadeBodyX = 0 * sX - adjustX
    shadeBodyY = 160 * sY
    shadeBodyW = 100 * sX
    shadeBodyH = 125 * sY

    headX = 0 * sX - adjustX
    headY = -100 * sY
    headW = 80 * sX
    headH = 100 * sY

    # shading on neck
    rect(canvas, app, shadeNeckX, shadeNeckY, 
    shadeNeckW, shadeNeckH, shadeColor)
    
    # neck
    rect(canvas, app, neckX, neckY, neckW, neckH, bodyColor)
    
    # shade body
    rect(canvas, app, shadeBodyX, shadeBodyY, shadeBodyW, shadeBodyH, 
    shadeColor)

    # body
    rect(canvas, app, bodyX, bodyY, bodyW, bodyH, bodyColor)

    # head
    rect(canvas, app, headX, headY, headW, headH, bodyColor)

def drawNiceRobotDecor(canvas, app, sX, sY, adjustX):
    w = app.width
    h = app.height

    mouthColor = grey(80)
    eyeColor = grey(130)
    heartColor = app.heartColor

    eyeX = -50 * sX
    eyeY = -110 * sY
    eyeW = 15 * sX
    eyeH = 12 * sY

    mouthHeight = 70 * sY
    mouthLength = 20 * sX

    heartScale = 1
    heartXLoc = -75 * sX - adjustX
    heartYLoc = 130 * sY
    heartInsideX = 0 * sX
    heartMidX = -20 * sX
    heartOutsideX = -40 * sX
    heartInsideY = 0 * sY
    heartMidY = 40 * sY
    heartOutsideY = 60 * sY
    heartCenterY = 45 * sY

    # eyes
    oval(canvas, app, eyeX - adjustX, eyeY, eyeW, eyeH, eyeColor)
    oval(canvas, app, -eyeX - adjustX, eyeY, eyeW, eyeH, eyeColor)

    # mouth
    canvas.create_line(w/2 + mouthLength/2 - adjustX, h/2 - mouthHeight, 
                    w/2 - mouthLength/2 - adjustX, h/2 - mouthHeight, 
                    fill=mouthColor, width = 5)

    # heart
    canvas.create_polygon(coor(w, heartInsideX, heartScale, heartXLoc),
                        coor(h, heartInsideY, heartScale, heartYLoc),
                        coor(w, heartOutsideX, heartScale, heartXLoc), 
                        coor(h, heartMidY, heartScale, heartYLoc),
                        coor(w, heartMidX, heartScale, heartXLoc), 
                        coor(h, heartOutsideY, heartScale, heartYLoc),
                        coor(w, heartInsideX, heartScale, heartXLoc), 
                        coor(h, heartCenterY, heartScale, heartYLoc),
                        coor(w, -heartMidX, heartScale, heartXLoc), 
                        coor(h, heartOutsideY, heartScale, heartYLoc),
                        coor(w, -heartOutsideX, heartScale, heartXLoc), 
                        coor(h, heartMidY, heartScale, heartYLoc),
                        fill=heartColor, outline='black')

    drawRobotLegs(canvas, app, adjustX, sX, sY)

def drawRobotLegs(canvas, app, adjustX, sX, sY):
    legX = 80 * sX
    legY = 240 * sY
    legW = 30 * sX
    legH = 30 * sY

    rect(canvas, app, legX - adjustX, legY, legH, legW, grey(60))
    rect(canvas, app, -legX- adjustX, legY, legH, legW, grey(60))

def drawNiceRobot(app, canvas, adjustX):
    # scale
    initWidth = 900
    initHeight = 600

    # choose the smaller scale
    less = min(app.width/initWidth,app.height/initHeight)
    sX = less
    sY = less

    w = app.width
    h = app.height

    # background constants
    red = 40
    redRate = 2
    green = 46
    greenRate = 0
    blue = 100
    blueRate = -2
    backgroundIncrement = 5

    # background
    for i in range(100):
        gradientColor = rgbString(red + i // redRate, green + i * greenRate, 
                                blue + i // blueRate)
        canvas.create_rectangle(0, backgroundIncrement * i, w, h, 
                            fill=gradientColor, outline=gradientColor)
    
    if app.background == 0:
        drawSadBackground(canvas, app, w, h)
    elif app.background == 1:
        drawHappyBackGround(canvas, app, w, h)
    else:
        drawHappyiestBackGround(canvas, app, w, h)
    # base of robot:
    drawNiceRobotBase(canvas, app, sX, sY, adjustX)

    # decoration:
    drawNiceRobotDecor(canvas, app, sX, sY, adjustX)