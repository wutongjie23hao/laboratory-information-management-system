from PySide import QtGui
class LoginDialog(QtGui.QDialog): 
    def __init__(self, parent=None): 
        QtGui.QDialog.__init__(self, parent) 
        self.setWindowTitle('login')
        self.user = QtGui.QLineEdit(self) 
        self.user.move(10, 20) 
        self.user.setText('admin') 
        self.pwd = QtGui.QLineEdit(self) 
        self.pwd.move(10, 60) 
        self.pwd.setText('admin') 
        self.pwd.setEchoMode(QtGui.QLineEdit.Password) 
        self.loginBtn = QtGui.QPushButton('Login', self) 
        self.loginBtn.move(100, 90) 
        self.loginBtn.clicked.connect(self.login) 
    def login(self): 
        if self.user.text() == 'admin' and self.pwd.text() == 'admin': 
            self.accept() 
        else: 
            QtGui.QMessageBox.critical(self, 'Error', 'User name or password error') 

if __name__ == '__main__': 
    import sys 
    app = QtGui.QApplication(sys.argv) 
    dialog = LoginDialog() 
    if dialog.exec_(): 
        win = QtGui.QMainWindow() 
        win.setWindowTitle('MainWindow')
        win.show() 
        sys.exit(app.exec_()) 
