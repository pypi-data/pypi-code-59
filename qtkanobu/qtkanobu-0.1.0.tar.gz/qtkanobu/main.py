def main():
    import sys 
    from PyQt5 import QtWidgets
    from qtkanobu.mainwindow.mainwindow import QtKanobu
            
    app = QtWidgets.QApplication(sys.argv)
    window = QtKanobu()
    window.show()
    app.exec_()
    
if __file__ == "__main__":
    main()
