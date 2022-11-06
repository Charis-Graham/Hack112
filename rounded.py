def drawRounded(app, canvas, questions, inBetweenBoxes, adjustX):
    print("")
    yPosition = app.width//15
    width = app.width//5
    for question in questions:
        lineHeight, listOfLines = calculateLines(question)
        height = lineHeight * len(listOfLines)

        margin = app.width//30
        xPosition = margin + app.width//5*3

        drawRect(app, canvas, yPosition, width, height)
        drawText(app, canvas, listOfLines, xPosition, yPosition, lineHeight)
        yPosition += height + inBetweenBoxes * 2

def calculateLines(question):
    # max 18 characters per line
    maxCharacters = 18
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
    return 20, listOfWords

def drawText(app, canvas, listOfLines, x, y, size):
    textSize = (size//5)*4
    yOffset = 0
    width = app.width//5
    x += width//2
    y += textSize/2
    for line in listOfLines:
        canvas.create_text(x, y + yOffset, text=line,
                        font=f'Times {textSize} bold', fill='black')
        yOffset += size
        print(yOffset)

def drawRect(app, canvas, yPosition, width, height):
    margin = app.width//30
    xPosition = margin + app.width//5*3
    canvas.create_rectangle(xPosition,yPosition,xPosition+width,yPosition+height, 
    fill = 'grey', outline = 'black')