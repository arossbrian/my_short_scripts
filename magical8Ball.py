import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is Certain"
    elif answerNumber == 2:
        return "It is decidely SO"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and Ask Again"
    elif answerNumber == 7:
        return  "My reply is No"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"
r= random.randint(1,9)
fortune = getAnswer((r))
print(fortune)