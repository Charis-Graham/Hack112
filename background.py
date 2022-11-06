# function from https://www.cs.cmu.edu/~112/notes/notes-graphics.html
def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def drawHappyiestBackGround(canvas, app, w, h):
    red = 90
    redRate = 1
    green = 125
    greenRate = 0
    blue = 240
    blueRate = -1
    backgroundIncrement = 5

    # background
    for i in range(100):
        gradientColor = rgbString(red + i // redRate, green + i * greenRate, 
                                blue + i // blueRate)
        canvas.create_rectangle(0, backgroundIncrement * i, w, h, 
                            fill=gradientColor, outline=gradientColor)

def drawHappyBackGround(canvas, app, w, h):
    red = 100
    redRate = 3
    green = 105
    greenRate = 0
    blue = 240
    blueRate = -1
    backgroundIncrement = 5

    # background
    for i in range(100):
        gradientColor = rgbString(red + i // redRate, green + i * greenRate, 
                                blue + i // blueRate)
        canvas.create_rectangle(0, backgroundIncrement * i, w, h, 
                            fill=gradientColor, outline=gradientColor)

def drawSadBackground(canvas, app, w, h):
    red = 20
    redRate = 2
    green = 70
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
