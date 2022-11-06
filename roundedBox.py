
def drawRoundedBoxes(app, canvas, questions, inBetween, adjustX):
    topWindowMargin = app.height//15 * 2

    margin = app.width//30
    w, h = app.width//2,app.height//2
    yOffset = topWindowMargin

    for question in questions:
        boxWidth = app.width//8
        lineHeight, listOfLines = calculateLines(question)
        boxHeight = lineHeight * len(listOfLines)
        r = min(boxHeight, boxWidth)//4

        drawRoundedBox(app, canvas, boxHeight, boxWidth, yOffset)
        drawText(app, canvas, listOfLines, app.width//2, 
        yOffset,lineHeight)

        yOffset += boxHeight*2 + inBetween + 2*r


def drawText(app, canvas, listOfLines, x, y, size):
    textSize = size
    x -= app.height//20
    yOffset = 0
    for line in listOfLines:
        canvas.create_text(x, y + yOffset, text=line,
                        font=f'Times {textSize} bold', fill='black')
        yOffset += size
        print(yOffset)

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
    return 15, listOfWords

def drawRoundedBox(app, canvas, boxHeight, boxWidth, yOffset):
    margin = app.width//30
    width = app.height//5
    w, h = app.width//2,app.height//2


    xCenter = w - (width//2) + margin
    yCenter = h - (width//2) + margin + yOffset
    yTop = margin * 3 + yOffset

    oppositeCenter = w + (width//2) - margin
    oppositeCenter = h + (width//2) - margin

    drawRoundedBoxBackground(app, canvas,boxWidth,boxHeight,xCenter,yOffset)



def drawRoundedBoxBackground(app, canvas,xSize,ySize,xCenter,yCenter):
    w, h = xCenter, yCenter

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