from color import *

def updateExtras(app):
    if app.heart == 0:
        app.heartColor = grey(100)
    elif app.heart == 1:
        app.heartColor = rgbString(60,20,20)
    else:
        app.heartColor = rgbString(90,20,20)

def drawSmile(app):
    print("")

def updateSparkles(app):
    for sparkI in range(len(app.sparkleCoors)):
        current = app.sparkleCoors[sparkI][2]
        app.sparkleCoors[sparkI][2] = (current + 5) % 20

def drawSparkles(app, canvas,x1,y1,x2,y2):
    w = (x2 - x1)//10
    h = (y2 - y1)//10
    for spark in app.sparkleCoors:
        drawSparkle(app, canvas, w*spark[0], h*spark[1], spark[2])

def drawSparkle(app, canvas, x, y, size):
    c = [0,1,1,0,0,-1,-1,0]
    for i in range(len(c)):
        c[i] *= size

    canvas.create_polygon(c[0]+x,c[1]+y,c[2]+x,c[3]+y,
                        c[4]+x,c[5]+y,c[6]+x,c[7]+y,
                         fill = "white")

def eyesColor(app):
    if app.eyes == 0:
        return grey(130)
    elif app.eyes == 1:
        return grey(160)
    else:
        return grey(200)

def drawSmile(app, canvas,sX, sY, adjustX):

    w = app.width
    h = app.height

    mouthColor = grey(80)

    mouthHeight = 70 * sY
    mouthLength = 20 * sX

    if app.smile >= 1:
        canvas.create_line(w/2 + mouthLength/2 - adjustX, h/2 - mouthHeight, 
                    w/2 + mouthLength/2 - adjustX, h/2 - mouthHeight - mouthLength//4, 
                    fill=mouthColor, width = 5)
    if app.smile == 2:
        print("hi")
        canvas.create_line(w/2 - mouthLength/2 - adjustX, h/2 - mouthHeight, 
                    w/2 - mouthLength/2 - adjustX, h/2 - mouthHeight - mouthLength//4, 
                    fill=mouthColor, width = 5)