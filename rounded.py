def drawRounded(app, canvas, questions, inBetweenBoxes, adjustX):
    print("")
    yPosition = app.width//15
    width = app.width//5
    for question in questions:
        lineHeight = min(app.height, app.width)//30
        listOfLines = calculateLines(question)
        height = lineHeight * len(listOfLines)

        margin = app.width//30
        xPosition = margin + app.width//5*3

        drawRect(app, canvas, yPosition, width, height)
        drawRoundedBoxBackground(app, canvas,width//2,height,yPosition)
        drawText(app, canvas, listOfLines, xPosition, 
        yPosition + margin//7, lineHeight)
        #rounded(app, canvas, yPosition, width, height)

        yPosition += height + inBetweenBoxes * 2


def calculateLines(question):
    # max 18 characters per line
    maxCharacters = 25
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
    print(listOfWords)
    return listOfWords

def drawText(app, canvas, listOfLines, x, y, size):
    textSize = (size//5)*3 # was 4
    yOffset = 0
    width = app.width//5
    x += width//2
    y += textSize/2
    for line in listOfLines:
        canvas.create_text(x, y + yOffset, text=line,
                        font=f'System {textSize} bold', fill='white')
        yOffset += size
        print(yOffset)

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

"""
def rounded(app, canvas, yPosition, width, height):
    minRad = min(app.height, app.width)/30
    margin = app.width//30
    xPosition = margin + app.width//5*3

    

    # top left
    if (True):
        centerY = yPosition + (height//2)
    #else:
        centerOneY = yPosition
        centerTwoY = yPosition + height - minRad


        canvas.create_oval(xPosition - minRad/2, centerOneY, 
        xPosition + minRad/2, 
        centerOneY + minRad, fill = 'grey', outline = 'grey')

    print("")
"""