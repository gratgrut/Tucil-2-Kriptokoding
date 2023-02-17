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
            encrypted = rc4.encryptRCFile(bin_data, key)
            with open(text, 'wb') as f:
                final = f.write(encrypted)
            return final
        else:
            text = self.textEditPlaintext.toPlainText()
            encrypted = rc4.decryptRC4ORD(text, key)
            self.textEdit.setText(str(encrypted))
        
        
    def methodDecrypt(self):
        key = self.textEditKey.toPlainText()
        if self.textEditPlaintext.toPlainText() == "":
            text = self.textEditPlaintext_2.toPlainText()
            bin_data = readBytes(text)
            decrypted = rc4.decryptRC4File(bin_data, key)
            with open(text, 'wb') as f:
                final = f.write(decrypted)
            return final
        else:
            text = self.textEditPlaintext.toPlainText()
            decrypted = rc4.decryptRC4ORD(text, key)
            self.textEdit.setText(codecs.decode(decrypted))    


    # def methodDecrypt(self):
    #     key = self.textEditKey.toPlainText()
    #     filedirectory= self.textEditPlaintext_2.toPlainText()
    #     bin_data = open(filedirectory, 'rb').read()
    #     decrypted = ve.decryptExt(bin_data, key)
    #     with open(filedirectory, 'wb') as f:
    #         final = f.write(decrypted)


#     def vigenereEn(self):
#         if self.textEditPlaintext.toPlainText() == "":
#             text = readTxt(self.textEditPlaintext_2.toPlainText())
#         else:
#             text = self.textEditPlaintext.toPlainText()
#         key = self.textEditKey.toPlainText()

#         encrypted = va.encryptText(text, key)
#         self.textHasiltanpaspace.setText(encrypted)
#         encryptedSpasi = perLima(encrypted)
#         self.plainTextEdit_4.setText(encryptedSpasi)

#     def vigenereExEn(self):
#         key = self.textEditKey.toPlainText()
#         text = self.textEditPlaintext_2.toPlainText()
#         bin_data = open(text, 'rb').read()
#         encrypted = ve.encryptExt(bin_data, key)
#         with open(text, 'wb') as f:
#             final = f.write(encrypted)
#         return final

#     def playfairEn(self):
#         if self.textEditPlaintext.toPlainText() == "":
#             text = readTxt(self.textEditPlaintext_2.toPlainText())
#         else:
#             text = self.textEditPlaintext.toPlainText()
#         key = self.textEditKey.toPlainText()
#         encrypted = pf.encryptPlayfair(key, text)
#         self.textHasiltanpaspace.setText(encrypted)
#         encryptedSpasi = perLima(encrypted)
#         self.textHasilKelompok.setText(encryptedSpasi)

#     def onetimepadEn(self):

#         if self.textEditPlaintext.toPlainText() == "":
#             text = readTxt(self.textEditPlaintext_2.toPlainText())
#         else:
#             text = self.textEditPlaintext.toPlainText()

#         filename = self.textEditKey.toPlainText() + '.txt'

#         if not (os.path.exists(filename)):
#             otp.generateRandomKey(filename)

#         key = otp.getKey(filename, text)
#         encrypted = va.encryptText(text, key)

#         self.textHasiltanpaspace.setText(encrypted)
#         encryptedSpasi = perLima(encrypted)
#         self.textHasilKelompok.setText(encryptedSpasi) 
  

#     def vigenereDe(self):
#         if self.textEditPlaintext.toPlainText() == "":
#             text = readTxt(self.textEditPlaintext_2.toPlainText())
#         else:
#             text = self.textEditPlaintext.toPlainText()
#         key = self.textEditKey.toPlainText()
#         decrypted = va.decryptText(text, key)
#         self.textHasiltanpaspace.setText(decrypted)
#         decryptedSpasi = perLima(decrypted)
#         self.textHasilKelompok.setText(decryptedSpasi)


#     def vigenereExDe(self):
#         key = self.textEditKey.toPlainText()
#         text = self.textEditPlaintext_2.toPlainText()
#         bin_data = open(text, 'rb').read()
#         decrypted = ve.decryptExt(bin_data, key)
#         with open(text, 'wb') as f:
#             final = f.write(decrypted)
#         return final  

#     def playfairDe(self):
#         if self.textEditPlaintext.toPlainText() == "":
#             text = readTxt(self.textEditPlaintext_2.toPlainText())
#         else:
#             text = self.textEditPlaintext.toPlainText()
#         key = self.textEditKey.toPlainText()
#         decrypted = pf.decryptPlayfair(key, text)
#         self.textHasiltanpaspace.setText(decrypted)
#         decryptedSpasi = perLima(decrypted)
#         self.textHasilKelompok.setText(decryptedSpasi)

#     def onetimepadDe(self):
#         if self.textEditPlaintext.toPlainText() == "":
#             text = readTxt(self.textEditPlaintext_2.toPlainText())
#         else:
#             text = self.textEditPlaintext.toPlainText()

#         filename = self.textEditKey.toPlainText() + '.txt'

#         key = otp.getKey(filename, text)
#         decrypted = va.decryptText(text, key)

#         self.textHasiltanpaspace.setText(decrypted)
#         decryptedSpasi = perLima(decrypted)
#         self.textHasilKelompok.setText(decryptedSpasi)
    
    def saveResult(self):
        with open("hasil.txt", 'w') as f:
            f.write(self.textEdit.toPlainText())

    
def readBytes(file):
    return open(file, 'rb').read()

# def perLima(text):
#     perLima = ""
#     group = 0
#     for i in range(5, len(text), 5):
#         if group != 0:
#             perLima = perLima + " " + (text[group:i])
#         else:
#             perLima = text[group:i]
#         group = i
#     perLima = perLima + " " + (text[group:])
#     return perLima
        


app = QApplication(sys.argv)
window = Window()
window.show()
window.setWindowTitle("Tucil 2 Chiper")
sys.exit(app.exec())