import myPythonFunctions

#Programme principal
try:
    userName = input("nom : ")
    userScore = myPythonFunctions.getUserPoint(userName)
    newUser = False
    if(userScore == -1) :
        newUser = True
        userScore = 0
    userChoice = "0"
    while(userChoice != "-1") :
        userScore = userScore + myPythonFunctions.generateQuestion()
        print("UserScore = ",userScore)
        userChoice = input("Tapez -1 pour quitter : ")
    print("passed")
    myPythonFunctions.updateUserPoints(newUser,userName,userScore)

except:
    print("Erreur inattendue!!!")
