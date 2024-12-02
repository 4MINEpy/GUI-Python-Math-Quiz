import random
import os

def getUserPoint(name) :
    f = open("userScores.txt","r")
    userList = list()
    for x in f :
        ch = x.split()
        ch[0] = ch[0].replace(',','')
        userList.extend(ch)
    for i in range(len(userList)):
        if(userList[i] == name) : 
            f.close()
            return int(userList[i+1])
    f.close()
    return -1
def updateUserPoints(newUser:  bool, userName, score) :
    if(newUser) :
        f = open("userScores.txt","a")
        f.write(f"{userName}, {score}\n")
        f.close()
    else :
        f1 = open("userScores.tmp","w")
        f2 = open("userScores.txt","r")
        for x in f2 :
            name, current_score = x.strip().split(", ")
            if name == userName :
                f1.write(f"{userName}, {score}\n")
            else :
                f1.write(x)
        f1.close()
        f2.close()
        os.remove("userScores.txt")
        os.rename("userScores.tmp","userScores.txt")

def generateQuestion() :
    operandList = [0, 0, 0, 0, 0] 
    operatorList = ["", "", "", ""] 
    operatorDict = {1: "+", 2: "-", 3: "*", 4: "**" }

    for i in range(len(operandList)) : 
        operandList[i] = random.randint(1,9)
    for i in range(len(operatorList)) : 
        if(operatorList.count("**") == 1) : 
            operatorList[i] = operatorDict[random.randint(1, 3)]
        else :
            operatorList[i] = operatorDict[random.randint(1, 4)]

    questionString = ""

    for i in range(len(operandList) - 1):
        questionString += f"{operandList[i]} {operatorList[i]} "

    questionString += str(operandList[-1])
    questionString = questionString.replace("**","^")
    print(eval(questionString))
    return questionString