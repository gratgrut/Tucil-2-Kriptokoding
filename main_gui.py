import sys
import vigenere_extended as ve
import rc4
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
import os.path
import codecs

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("gui.ui", self)

        self.comboBox.activated.connect(self.method)

        self.saveButton.clicked.connect(self.saveResult)

    def method(self):
        if (self.comboBox.currentText() == "Encrypt"):
            self.generateButton.clicked.connect(self.methodEncrypt)
        elif (self.comboBox.currentText() == "Decrypt"):
            self.generateButton.clicked.connect(self.methodDecrypt)  

    def methodEncrypt(self):
        key = self.textEditKey.toPlainText()
        if self.textEditPlaintext.toPlainText() == "":
            text = self.textEditPlaintext_2.toPlainText()
            bin_data = open(text, 'rb').read()
            preencrypted = ve.encryptExtFile(bin_data, key)
            encrypted = rc4.encryptRCFile(preencrypted, key)
            with open(text, 'wb') as f:
                final = f.write(encrypted)
            return final
        else:
            text = self.textEditPlaintext.toPlainText()
            preencrypted = ve.encryptExtOrd(text, key)
            encrypted = rc4.encryptRC4ORD(preencrypted, key)
            self.plainTextEdit.setPlainText(str(encrypted))
        
        
    def methodDecrypt(self):
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
            decrypted = ve.decryptExtOrd(predecrypted, key)
            self.plainTextEdit.setPlainText(str(decrypted))    

    
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