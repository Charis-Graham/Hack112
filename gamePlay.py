#the questions in the chat
class question:
    def __init__(self, text, possibleAnswers):
        self.text = text
        self.possibleAnswers = possibleAnswers
        self.answer = 0

    def ask(self):
        #post a textbox with self.text
        #post the buttons
        #get the response button
        self.answer = ""
        pass

#list of the questions
questionsText = {
    1: "How are you?",
    2: "How much have you eaten today?",
    3: "Have you drunk water today?",
    4: "How much have you slept today?",
    5: "Have you exercised today?",
    6: "Have you spent time with friends or family today?",
    7: "Have you gone outside today?",
    8: "Have you meditated today?"
}

#list of the possible answers
answerButtons = {
    1: [smileButton, sadButton, mehButton],
    2: [oneButton, twoButton, threeButton],
    3: [fourButton, fourToSixButton, sixMoreButton],
    4: [lessThanSevenButton, sevenToNineButton, ninePlusButton],
    5: [tenMinButton, twentyMinButton, twentyPlusButton],
    6: [yesButton, noButton],
    7: [yesButton, noButton],
    8: [yesButton, noButton]
}

#list of point values
points = {
    1:[0, 0, 0], 
    2:[1, 2, 3],
    3:[1, 2, 3], 
    4:[1, 2, 3],
    5:[1, 2, 3],
    6:[0, 1],
    7:[0, 1],
    8:[0, 1],
}

#main game loop
while True:
    #loops throw each possible question and funds the answer
    answers = []
    for key in range(len(questionsText)):
        currentQuestion = question(questionsText[key], answerButtons[key])
        answers.append(currentQuestion.ask())

    pointCount = sum(answers)

    if pointCount 

    break