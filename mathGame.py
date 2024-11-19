import myPythonFunctions
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5 import uic
#Programme principal

def main() :
    name = window.nameInput.text()
    anwser = window.anwserInput.text()
    if(name == "" or anwser == "") :
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical) 
        msg.setText("name and anwser are required fields!!!")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        return
    userName = name
    userScore = myPythonFunctions.getUserPoint(userName)
    newUser = False
    if(userScore == -1) :
        newUser = True
        userScore = 0
    try:
        num = int(anwser)
        if(num == eval(window.equaInput.text())):
            userScore = userScore+1
            myPythonFunctions.updateUserPoints(newUser,userName,userScore)
            window.valArea.setText("Good job!!!")
            window.resArea.setText("")
        else:
            window.valArea.setStyleSheet("color: red;font: 20pt;")
            window.resArea.setStyleSheet("color: red;font: 20pt;")
            window.valArea.setText("Wrong!!!")
            window.resArea.setText("Correct anwser : "+str(eval(window.equaInput.text())))
        

        


    except ValueError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical) 
        msg.setText("anwser should be an int!!!")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        return
    
    window.playAgain.show()
    window.quit.show()

def playAgain() :

    window.resArea.setText("")
    window.valArea.setText("")
    window.anwserInput.setText("")
    window.equaInput.setText(myPythonFunctions.generateQuestion())
    window.playAgain.hide()
    window.quit.hide()

def quit() :
    window.close()

#Running the UI
app = QApplication([])
window = uic.loadUi('mainUI.ui')
window.show()
window.equaInput.setReadOnly(True)
window.equaInput.setText(myPythonFunctions.generateQuestion())
window.playAgain.hide()
window.quit.hide()
window.submit.clicked.connect(main)
window.playAgain.clicked.connect(playAgain)
window.quit.clicked.connect(quit)
app.exec_()