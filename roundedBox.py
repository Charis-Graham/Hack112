
def drawRoundedBoxes(app, canvas, questions, inBetween):
    margin = app.width//30

    w, h = app.width//2,app.height//2
    width = app.height//5
    testDim = width
    canvas.create_rectangle(w-testDim,0,
    w+testDim, app.height, fill = "white")

    yOffset = -inBetween

    for question in questions:
        boxWidth = 80
        lineHeight, listOfLines = calculateLines(question)
        boxHeight = lineHeight * len(listOfLines)

        drawRoundedBox(app, canvas, boxHeight, boxWidth, yOffset)

        yOffset += boxHeight*2 + inBetween

        drawText(app, canvas, listOfLines, app.width//2, 
        yOffset - boxHeight, 
        lineHeight)

def drawText(app, canvas, listOfLines, x, y, size):
    textSize = size
    yOffset = 0
    for line in listOfLines:
        canvas.create_text(x, y + yOffset, text=line,
                        font=f'Arial {textSize} bold', fill='black')
        yOffset += size
        print(yOffset)

def calculateLines(question):

    return 20, ["the brown", "fox chased the", "lazy dog"]

def drawRoundedBox(app, canvas, boxHeight, boxWidth, yOffset):
    margin = app.width//30
    width = app.height//5
    w, h = app.width//2,app.height//2


    xCenter = w - (width//2) + margin
    yCenter = h - (width//2) + margin + yOffset
    yTop = margin * 3 + yOffset

    oppositeCenter = w + (width//2) - margin
    oppositeCenter = h + (width//2) - margin

    drawRoundedBoxBackground(app, canvas,boxWidth,boxHeight,xCenter,yTop)



def drawRoundedBoxBackground(app, canvas,xSize,ySize,xCenter,yCenter):
    #w, h = app.width//2,app.height//2
    w, h = xCenter, yCenter
    textDim = 200

    textHeight = ySize
    textWidth = xSize

    r = min(textHeight, textWidth)//4

    xDif = textWidth - 2 * r
    yDif = textHeight - 2 * r

    #canvas.create_rectangle(w-textDim,h-textDim,
    #w+textDim, h+textDim, fill = "white")

    # rounded outline
    canvas.create_oval(w-r -xDif, h-r-yDif,
    w+r-xDif, h+r-yDif, fill = "grey", outline = "black")
    canvas.create_oval(w-r-xDif, h-r+yDif,
    w+r-xDif, h+r+yDif, fill = "grey", outline = "black")
    canvas.create_oval(w-r+xDif, h-r-yDif,
    w+r+xDif, h+r-yDif, fill = "grey", outline = "black")
    canvas.create_oval(w-r+xDif, h-r+yDif,
    w+r+xDif, h+r+yDif, fill = "grey", outline = "black")

    # grey fill
    canvas.create_rectangle(w-xDif-r,h-yDif,
    w+xDif+r,h+yDif, fill= 'grey', outline = 'grey')
    canvas.create_rectangle(w-xDif,h-yDif-r,
    w+xDif,h+yDif+r, fill= 'grey', outline = 'grey')

    # verticle outlines
    canvas.create_line(w-xDif-r,h-yDif,
    w-xDif-r,h+yDif, fill = 'black')
    canvas.create_line(w+xDif+r,h-yDif,
    w+xDif+r,h+yDif, fill = 'black')

    # horizontal outlines
    canvas.create_line(w-xDif,h-yDif-r,
    w+xDif,h-yDif-r, fill = 'black')
    canvas.create_line(w-xDif,h+yDif+r,
    w+xDif,h+yDif+r, fill = 'black')