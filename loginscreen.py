from PyQt6 import QtCore, QtGui, QtWidgets
from keyauth import api
from main import AletlerApp
import json
import main
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QFont, QFontDatabase
from keyauth import *
class Ui_Form(object):

    def setupUi(self, Form):
        font_path = "resources/ProggyClean.ttf"

        # QFontDatabase ile fontu yükle
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)

        # Yüklenen fontu kullanarak bir QFont oluştur
        custom_font = QFont(font_family, 12)
        Form.setObjectName("Form")
        Form.setFixedSize(256, 418)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 481, 641))
        font = QtGui.QFont()
        
        self.widget.setFont(custom_font)
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 211, 381))
        font = QtGui.QFont()
        
        self.groupBox.setFont(custom_font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.usernameTextBox = QtWidgets.QLineEdit(parent=self.groupBox)
        self.usernameTextBox.setGeometry(QtCore.QRect(30, 50, 151, 31))
        font = QtGui.QFont()
        
        font.setPointSize(16)
        self.usernameTextBox.setFont(custom_font)
        self.usernameTextBox.setObjectName("usernameTextBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 16))
        font = QtGui.QFont()
        
        self.label.setFont(custom_font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 71, 16))
        font = QtGui.QFont()
        
        self.label_2.setFont(custom_font)
        self.label_2.setObjectName("label_2")
        self.passwordTextBox = QtWidgets.QLineEdit(parent=self.groupBox)
        self.passwordTextBox.setGeometry(QtCore.QRect(30, 110, 151, 31))
        font = QtGui.QFont()
        
        font.setPointSize(16)
        self.passwordTextBox.setFont(custom_font)
        self.passwordTextBox.setObjectName("passwordTextBox")
        self.loginButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.loginButton.setGeometry(QtCore.QRect(30, 290, 151, 51))
        self.loginButton.setObjectName("loginButton")
        self.webHookTextBox = QtWidgets.QLineEdit(parent=self.groupBox)
        self.webHookTextBox.setGeometry(QtCore.QRect(30, 170, 151, 31))
        font = QtGui.QFont()
        
        font.setPointSize(16)
        self.webHookTextBox.setFont(custom_font)
        self.webHookTextBox.setObjectName("webHookTextBox")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 71, 16))
        font = QtGui.QFont()
        
        self.label_3.setFont(custom_font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 71, 16))
        font = QtGui.QFont()
        
        self.label_4.setFont(custom_font)
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(30, 230, 151, 41))
        font = QtGui.QFont()
        
        font.setPointSize(16)
        self.comboBox.setFont(custom_font)
        self.comboBox.setMaxVisibleItems(3)
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.comboBox.addItem("1920x1080")
        self.comboBox.addItem("1366x768")
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setProperty("ObjectName", _translate("Form", "Form"))
        self.widget.setStyleSheet(_translate("Form", "background-color:rgb(12, 12, 12)"))
        self.widget.setProperty("ObjectName", _translate("Form", "widget"))
        self.groupBox.setStyleSheet(_translate("Form", "border: 2px solid turquoise;\n"
"background-color:rgb(8, 8, 8);\n"
"color:white"))
        self.groupBox.setProperty("ObjectName", _translate("Form", "groupBox"))
        self.usernameTextBox.setStyleSheet(_translate("Form", "border: 2px solid turquoise;\n"
"color:white"))
        self.usernameTextBox.setProperty("ObjectName", _translate("Form", "usernameTextBox"))
        self.label.setStyleSheet(_translate("Form", "border: 0px solid turquoise;\n"
"color:turquoise"))
        self.label.setText(_translate("Form", "Username :"))
        self.label.setProperty("ObjectName", _translate("Form", "label"))
        self.label_2.setStyleSheet(_translate("Form", "border: 0px solid turquoise;\n"
"color:turquoise"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.label_2.setProperty("ObjectName", _translate("Form", "label_2"))
        self.passwordTextBox.setStyleSheet(_translate("Form", "border: 2px solid turquoise;\n"
"color:white"))
        self.passwordTextBox.setProperty("ObjectName", _translate("Form", "passwordTextBox"))
        self.loginButton.setStyleSheet(_translate("Form", "border: 2px solid turquoise;\n"
"color:turquoise"))
        self.loginButton.setText(_translate("Form", "Login"))
        self.loginButton.setProperty("ObjectName", _translate("Form", "loginButton"))
        self.webHookTextBox.setStyleSheet(_translate("Form", "border: 2px solid turquoise;\n"
"color:white"))
        self.webHookTextBox.setProperty("ObjectName", _translate("Form", "passwordTextBox"))
        self.label_3.setStyleSheet(_translate("Form", "border: 0px solid turquoise;\n"
"color:turquoise"))
        self.label_3.setText(_translate("Form", "Webhook:"))
        self.label_3.setProperty("ObjectName", _translate("Form", "label_2"))
        self.label_4.setStyleSheet(_translate("Form", "border: 0px solid turquoise;\n"
"color:turquoise"))
        self.label_4.setText(_translate("Form", "Çözünürlük:"))
        self.label_4.setProperty("ObjectName", _translate("Form", "label_2"))



class AletlerApp2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.keyauth = api(
            name="AutoEnchant",
            ownerid="25HmWSrKZx",
            secret="679495f14fd0834875c2e0acb7d9b7f92e270e296ba4edf1a9bcb2a6ec300ebd",
            version="0.3",
            hash_to_check=()
        )

        self.ui.loginButton.clicked.connect(self.login)
        self.read_webhook_settings()

    def read_webhook_settings(self):
        try:
            with open("webhook_settings.json", "r") as json_file:
                data = json.load(json_file)
                webhook_value = data.get("webhook", "")
                self.ui.webHookTextBox.setText(webhook_value)
        except FileNotFoundError:
            # Dosya bulunamazsa veya okuma hatası olursa buraya düşer
            pass

    def login(self):
        username = self.ui.usernameTextBox.text()
        password = self.ui.passwordTextBox.text()
        webhook = self.ui.webHookTextBox.text()

        # Webhook bilgisini JSON dosyasına kaydet
        webhook_data = {"webhook": webhook}
        with open("webhook_settings.json", "w") as json_file:
            json.dump(webhook_data, json_file)
        main.cozunurluk = self.ui.comboBox.currentText()
        self.keyauth.login(username, password)
        self.close()
        self.main_window = main.AletlerApp()
        self.main_window.show()
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AletlerApp2()
    window.show()
    app.exec()