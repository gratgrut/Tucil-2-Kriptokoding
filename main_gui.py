import sys
import vigenere_extended as ve
import rc4
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("gui.ui", self)

        self.comboBox.activated.connect(self.method)

        self.saveButton.clicked.connect(self.saveResult)

    def method(self):
        if (self.comboBox.currentText() == "Encrypt"):
            print("encrypt time")
            try:
                self.generateButton.clicked.disconnect()
            except:
                pass
            self.generateButton.clicked.connect(self.methodEncrypt)
            print("serius lu?")
        elif (self.comboBox.currentText() == "Decrypt"):
            print("decrypt time")
            try:
                self.generateButton.clicked.disconnect()
            except:
                pass
            self.generateButton.clicked.connect(self.methodDecrypt)  
            print("masa ke sini?")

    def methodEncrypt(self):
        print("masuk fungsi encrypt")
        key = self.textEditKey.toPlainText()
        if self.textEditPlaintext.toPlainText() == "":
            text = self.textEditPlaintext_2.toPlainText()
            bin_data = open(text, 'rb').read()
            preencrypted = ve.encryptExtFile(bin_data, key)
            print('herepreenFILE')
            print(preencrypted[0:10])
            encrypted = rc4.encryptRCFile(preencrypted, key)
            print('hereenFILE')
            print(encrypted[0:10])
            with open(text, 'wb') as f:
                final = f.write(encrypted)
            return final
        else:
            text = self.textEditPlaintext.toPlainText()
            preencrypted = ve.encryptExtOrd(text, key)
            print('herepreenORD')
            print(preencrypted[0:10])
            encrypted = rc4.encryptRC4ORD(preencrypted, key)
            print('hereenORD')
            print(encrypted[0:10])
            self.plainTextEdit.setPlainText(str(encrypted))
            return
        
        
    def methodDecrypt(self):
        print("masuk fungsi decrypt")
        key = self.textEditKey.toPlainText()
        if self.textEditPlaintext.toPlainText() == "":
            text = self.textEditPlaintext_2.toPlainText()
            bin_data = open(text, 'rb').read()
            predecrypted = rc4.decryptRC4File(bin_data, key)
            decrypted = ve.decryptExtFile(predecrypted, key)
            with open(text, 'wb') as f:
                final = f.write(decrypted)
            return final
        else:
            text = self.textEditPlaintext.toPlainText()
            predecrypted = rc4.decryptRC4ORD(str(text), key)
            print('herepredecORD')
            print(predecrypted[0:10])
            decrypted = ve.decryptExtOrd(predecrypted, key)
            print('heredecORD')
            print(decrypted[0:10])
            self.plainTextEdit.setPlainText(str(decrypted))
            return    

    
    def saveResult(self):
        with open("hasil.txt", 'w') as f:
            f.write(self.plainTextEdit.toPlainText())

    
def readBytes(file):
    return open(file, 'rb').read()



app = QApplication(sys.argv)
window = Window()
window.show()
window.setWindowTitle("Tucil 2 Chiper")
sys.exit(app.exec())