from color import *

def drawRounded(app, canvas, questions, inBetweenBoxes, adjustX):
    yPosition = app.width//15
    width = app.width//5
    xPositions = []
    yPositions = []
    for question in questions:
        lineHeight = min(app.height, app.width)//30
        listOfLines = calculateLines(question)
        height = lineHeight * len(listOfLines)

        margin = app.width//30
        xPosition = margin + app.width//5*3

        drawRect(app, canvas, yPosition, width, height)
        drawRoundedBoxBackground(app, canvas,(width//2),height,yPosition)
        drawText(app, canvas, listOfLines, xPosition, 
        yPosition + margin//7, lineHeight)
        #rounded(app, canvas, yPosition, width, height)

        yPosition += height + inBetweenBoxes * 2
        
        xPositions.append(xPosition)
        yPositions.append(yPosition - 2*inBetweenBoxes)
    return xPositions, yPositions


def calculateLines(question):
    # max 18 characters per line
    maxCharacters = 28
    sum = 0
    listOfWords = [""]
    for word in question.split():
        if (len(listOfWords[-1]) + len(word) + 1 <= maxCharacters):
            if (len(listOfWords[-1]) < 1):
                listOfWords[-1] += word
            else:
                listOfWords[-1] += " " + word
        else:
            listOfWords.append(word)
    return listOfWords

def drawText(app, canvas, listOfLines, x, y, size):
    textSize = (size//5)*3 # was 4
    yOffset = 0
    width = app.width//5
    x += width//2
    y += textSize/2

    fillColor = rgbString(231,234,237)
    for line in listOfLines:
        canvas.create_text(x, y + yOffset, text=line,
                        font=f'Gotham {textSize} bold', fill=fillColor)
        yOffset += size

def drawRect(app, canvas, yPosition, width, height):
    margin = app.width//30
    xPosition = margin + app.width//5*3
    canvas.create_rectangle(xPosition,yPosition,xPosition+width,yPosition+height, 
    fill = 'grey', outline = 'black')


def drawRoundedBoxBackground(app, canvas,xSize,ySize,yPosition):
    r = min(app.height, app.width)/80

    margin = app.width//30
    xPosition = margin + app.width//5*3

    xCenter = xPosition + xSize #+ 2* r
    yCenter = yPosition + ySize//2
    w, h = xCenter, yCenter
    xDif = xSize
    yDif = ySize//2

    fillColor = rgbString(89,89,92)

    #canvas.create_rectangle(w-textDim,h-textDim,
    #w+textDim, h+textDim, fill = "white")

    # rounded outline
    canvas.create_oval(w-r -xDif, h-r-yDif,
    w+r-xDif, h+r-yDif, fill = fillColor, outline = fillColor)
    canvas.create_oval(w-r-xDif, h-r+yDif,
    w+r-xDif, h+r+yDif, fill = fillColor, outline = fillColor)
    canvas.create_oval(w-r+xDif, h-r-yDif,
    w+r+xDif, h+r-yDif, fill = fillColor, outline = fillColor)
    canvas.create_oval(w-r+xDif, h-r+yDif,
    w+r+xDif, h+r+yDif, fill = fillColor, outline = fillColor)

    # grey fill
    canvas.create_rectangle(w-xDif-r,h-yDif,
    w+xDif+r,h+yDif, fill= fillColor, outline = fillColor)
    canvas.create_rectangle(w-xDif,h-yDif-r,
    w+xDif,h+yDif+r, fill= fillColor, outline = fillColor)

    # verticle outlines
    canvas.create_line(w-xDif-r,h-yDif,
    w-xDif-r,h+yDif, fill = fillColor)
    canvas.create_line(w+xDif+r,h-yDif,
    w+xDif+r,h+yDif, fill = fillColor)

    # horizontal outlines
    canvas.create_line(w-xDif,h-yDif-r,
    w+xDif,h-yDif-r, fill = fillColor)
    canvas.create_line(w-xDif,h+yDif+r,
    w+xDif,h+yDif+r, fill = fillColor)
