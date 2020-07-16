import sys
from PyQt5 import QtWidgets
from qtkanobu.mainwindow import design
from qtkanobu.result import resdesign
import random
    
class QtKanobu(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(QtKanobu, self).__init__()
        self.setupUi(self)
        
        self.pushButton_1.clicked.connect(lambda a : self.game(number=0))
        self.pushButton_2.clicked.connect(lambda a : self.game(number=1))
        self.pushButton_3.clicked.connect(lambda a : self.game(number=2))
        
    def game(self, number):
        result = Result(number)
        result.exec_()
        
class Result(QtWidgets.QDialog, resdesign.Ui_Dialog):
    def __init__(self, number):
        super(Result, self).__init__()
        self.setupUi(self)
        
        windowtype = -1
        
        
        bot = random.randint(0, 2)
        
        if number == 0:
            if bot == 0:
                windowtype = 2
            if bot == 1:
                windowtype = 0
            if bot == 2:
                windowtype = 1
                
        elif number == 1:
            if bot == 0:
                windowtype = 1
            elif bot == 1:
                windowtype = 2
            elif bot == 2:
                windowtype = 0
        
        elif number == 2:
            if bot == 0:
                windowtype = 0
            elif bot == 1:
                windowtype = 1
            elif bot == 2:
                windowtype = 2
        
        objects = ["Rock", "Scissors", "Paper"]
        
        if windowtype == 0:
            self.label.setText("<html><head/><body><p><img src=\":/img/img/main/Misc_Birthday_Cake.png\"/></p></body></html>")
            self.label_2.setText("You win!")
        
        elif windowtype == 1:
            self.label.setText("<html><head/><body><p><img src=\":/img/img/main/Misc_R.I.P.png\"/></p></body></html>")
            self.label_2.setText("You lose!")
            
        elif windowtype == 2:
            self.label.setText("<html><head/><body><p><img src=\":/img/img/main/Server_MediaAddonServer.png\"/></p></body></html>")
            self.label_2.setText("Draw!")
            
        self.label_3.setText(objects[number] + " VS. " + objects[bot])
        
        self.pushButton.clicked.connect(self.close)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtKanobu()
    window.show()
    app.exec_()
    
if __file__ == "__main__":
    main()
