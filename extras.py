def updateExtras(app):
    if app.sparkles:
        print(True)
        #drawSparkle(app, canvas, app.width//2, app.height//2, 20)
    if app.heart == 0:
        app.heartColor = grey(100)
    elif app.heart == 1:
        app.heartColor = rgbString(60,20,20)
    else:
        app.heartColor = rgbString(90,20,20)

def drawSmile(app):
    print("")

def drawSparkle(app, canvas, x, y, size):
    c = [0,3,1,1,0,2,1,-1,0,-2,-1,-1,-2,0,-1,1]
    for i in range(len(c)):
        c[i] *= size

    canvas.create_polygon(c[0]+x,c[1]+y,c[2]+x,c[3]+y,
                        c[4]+x,c[5]+y,c[6]+x,c[7]+y,
                        c[8]+x,c[9]+y,c[10]+x,c[11]+y,
                         fill = "white")


# function from https://www.cs.cmu.edu/~112/notes/notes-graphics.html
def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def grey(n):
    return rgbString(n, n, n)