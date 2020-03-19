import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon,QImage,QPalette,QBrush
from PyQt5.QtCore import pyqtSlot,QSize
from PyQt5 import QtGui,QtWidgets,QtCore
from sqlitedict import*

class BMI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(500,500,500,500)
        self.title = "BMI Calculator"
        self.setWindowIcon(QIcon('arm.ico'))
        bg = QImage("wall.jpg")
        bg1 = bg.scaled(QSize(500,500))
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(bg1))
        self.setPalette(palette)
        self.textboxlbl = QLabel("<h3>Welcome to BMI Calculator<h3>",self)
        self.textboxlbl.setStyleSheet("color: yellow")
        self.textboxlbl.move(140,20)
        self.textboxlbl.resize(300,20)
        self.textboxlbl1 = QLabel("Please input your data:",self)
        self.textboxlbl1.setStyleSheet("color: yellow")
        self.textboxlbl1.move(175,35)
        self.textboxlbl1.resize(300,20)
        
        self.textbox10 = QLineEdit(self)
        self.textboxlbl10 = QLabel("<h3>First Name:<h3>", self)
        self.textboxlbl10.move(100,79)
        self.textboxlbl0.setStyleSheet("color: yellow")
        self.textbox10.setText("")
        self.textbox10.move(180,70)
        self.textbox10.resize(280,30)
        
        self.textbox20 = QLineEdit(self)
        self.textboxlbl20 = QLabel("<h3>Last Name:<h3>", self)
        self.textboxlb20.setStyleSheet("color: yellow")
        self.textboxlbl20.move(100,119)
        self.textbox20.setText("")
        self.textbox20.move(180,110)
        self.textbox20.resize(280,30)

        self.textbox30 = QLineEdit(self)
        self.textboxlbl30 = QLabel("<h3>Age:<h3>", self)
        self.textboxlbl30.setStyleSheet("color: yellow")
        self.textboxlbl30.move(100,159)
        self.textbox30.setText("")
        self.textbox30.move(180,150)
        self.textbox30.resize(280,30)

        
        self.textbox40 = QLineEdit(self)
        self.textboxlbl40 = QLabel("<h3>Sex:<h3>", self)
        self.textboxlbl40.setStyleSheet("color: yellow")
        self.textboxlbl40.move(100,199)
        self.textbox40.setText("")
        self.textbox40.move(180,190)
        self.textbox40.resize(280,30)

        self.textbox2 = QLineEdit(self)
        self.textboxlbl2 = QLabel("<h3>Height:<h3>", self)
        self.textboxlbl2.move(100,239)
        self.textboxlbl2.setStyleSheet("color: yellow")
        self.textbox2.setText("")
        self.textbox2.move(180,230)
        self.textbox2.resize(280,30)

        self.textbox1 = QLineEdit(self)
        self.textboxlbl1 = QLabel("<h3>Weight:<h3>", self)
        self.textboxlbl1.move(100,279)
        self.textboxlbl1.setStyleSheet("color: yellow")
        self.textbox1.setText("")
        self.textbox1.move(180,270)
        self.textbox1.resize(280,30)

        self.textbox3 = QLineEdit(self)
        self.textboxlbl3 = QLabel("<h3>Your Body Mass Index is:<h3>",self)
        self.textboxlbl3.setStyleSheet("color: yellow")
        self.textboxlbl3.move(20,319)
        self.textboxlbl3.resize(300,20)
        self.textbox3.setText("")
        self.textbox3.move(190,310)
        self.textbox3.resize(280,30)
        
        self.textbox4 = QLineEdit(self)
        self.textboxlbl4 = QLabel("<h3>Your Classification is:<h3>",self)
        self.textboxlbl4.setStyleSheet("color: yellow")
        self.textboxlbl4.move(20,359)
        self.textboxlbl4.resize(300,20)
        self.textbox4.setText("")
        self.textbox4.move(190,350)
        self.textbox4.resize(200,30)
        
        

        self.button = QPushButton('Submit',self)
        self.button.setToolTip("Submit your Information")
        self.button.setStyleSheet("background-color : skyblue")
        self.button.move(80,450)
        self.button.clicked.connect(self.data)
        self.button1 = QPushButton('Clear', self)
        self.button1.setToolTip("Clear all your information")
        self.button1.setStyleSheet("background-color : skyblue")
        self.button1.move(200,450)
        self.button1.clicked.connect(self.clear)
        self.button2 = QPushButton('Back', self)
        self.button2.setStyleSheet("background-color : skyblue")
        self.button2.setToolTip("Back to the main window")
        self.button2.move(320,450)
        self.button2.clicked.connect(self.back)

        
        self.show()

    @pyqtSlot()
    def data(self):
        fn = self.textbox10.text()
        ln = self.textbox20.text()
        age = int(self.textbox30.text())
        sex = self.textbox40.text
        height = float(self.textbox2.text())
        weight = int(self.textbox1.text())
        bmi1 = weight/height**2
        bmi =  self.textbox3.setText(f"{bmi1}")
        if bmi1 < 18.5:
            self.textbox4.setText("Underweight")
        elif (18.6<=bmi2<=24.99):
            self.textbox4.setText("Normal Weight")
        elif(25<=bmi2<=29.99):
            self.textbox4.setText("Overweight")
        else:
            self.textbox4.setText("Obesse")  
        self.submitdata(fn, ln, age, height, weight,sex,bmi1)
    def clear(self):
        self.textbox10.setText("")
        self.textbox20.setText("")
        self.textbox30.setText("")
        self.textbox40.setText("")
        self.textbox2.setText("")
        self.textbox1.setText("")
    def back(self):
        BMI.close(self)
    def submitdata(self, fn, ln, age, height, weight,sex,bmi1):
        submitting = QMessageBox.question(self, "Submitting Data", "Are you sure want to submit this information?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and fn != "" and ln != "" and age != "" and height != "" and weight != "" and sex != "":
            dictionarydb = SqliteDict("Pogi.db", autocommit = True)
            accounts_list = dictionarydb.get('accounts',[])
            d = (f"First Name: {fn} Last Name: {ln} Age: {age} Height: {height} Weight: {weight} Sex: {sex} BMI: {bmi1}")
            accounts_list.append(d)
            dictionarydb['accounts'] = accounts_list
            for i in range(len(dictionarydb['accounts'])):
                print(dictionarydb['accounts'][i])
            QMessageBox.information(self, "Evaluation", "Data Inputted!", QMessageBox.Ok, QMessageBox.Ok)
            ano_data = QMessageBox.question(self,"Adding another data","Do you want to add another data?",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if ano_data == QMessageBox.Yes:
                self.textbox10.setText("")
                self.textbox20.setText("")
                self.textbox30.setText("")
                self.textbox40.setText("")
                self.textbox2.setText("")
                self.textbox1.setText("")
                self.textbox3.setText("")
                self.textbox4.setText("")
            else:
                BMI.close(self)
        
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and fn == "" and ln == "" and age == "" and height == "" and weight == "" and sex == "":
            pass
        elif submitting == QMessageBox.No and fn == "" or ln == "" or age == "" or height == "" or weight == "" and sex == "":
            QMessageBox.warning(self, "Error","Please complete the blanked field", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and fn =="":
            QMessageBox.warning(self,"Error","Please input your First Name", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and ln =="":
            QMessageBox.warning(self,"Error","Please input your Last Name", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and sex =="":
            QMessageBox.warning(self,"Error","Please input your Sex", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and ln =="" and sex == "" and fn == " ":
            QMessageBox.warning(self,"Error","Please input your First Name,Last Name and Sex", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and ln =="" and sex == "":
            QMessageBox.warning(self,"Error","Please input your Last Name and Sex", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and fn =="" and ln == "":
            QMessageBox.warning(self,"Error","Please input your First Name and Last Name", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and sex =="" and fn == "":
            QMessageBox.warning(self,"Error","Please input your First Name and Sex", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and fn == "" and ln == "" and age == "" and height == "" and weight == "" and sex == "":
            pass
        elif submitting == QMessageBox.No and fn == "" or ln == "" or age == "" or height == "" or weight == "" and sex == "":
            QMessageBox.warning(self, "Error","Please complete the blanked field", QMessageBox.Ok, QMessageBox.Ok)
    
class Male(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMR Window")
        self.setGeometry(500,500,500,500)
        self.setWindowIcon(QIcon('user.png'))
        bg = QImage("wall.jpg")
        bg1 = bg.scaled(QSize(500,500))
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(bg1))
        self.setPalette(palette)
        self.textboxlbl = QLabel("<h3>Welcome to BMR Calculator<h3>",self)
        self.textboxlbl.setStyleSheet("color: yellow")
        self.textboxlbl.move(150,20)
        self.textboxlbl.resize(300,20)
        self.textboxlbl1 = QLabel("Please input your data:",self)
        self.textboxlbl1.setStyleSheet("color: yellow")
        self.textboxlbl1.move(175,35)
        self.textboxlbl1.resize(300,20)

        self.textbox10 = QLineEdit(self)
        self.textboxlbl10 = QLabel("<h3>First Name:<h3>", self)
        self.textboxlbl10.setStyleSheet("color: yellow")
        self.textboxlbl10.move(100,79)
        self.textbox10.setText("")
        self.textbox10.move(180,70)
        self.textbox10.resize(280,30)
        
        self.textbox20 = QLineEdit(self)
        self.textboxlbl20 = QLabel("<h3>Last Name:<h3>", self)
        self.textboxlbl20.setStyleSheet("color: yellow")
        self.textboxlbl20.move(100,119)
        self.textbox20.setText("")
        self.textbox20.move(180,110)
        self.textbox20.resize(280,30)

        self.textbox30 = QLineEdit(self)
        self.textboxlbl30 = QLabel("<h3>Age:<h3>", self)
        self.textboxlbl30.setStyleSheet("color: yellow")
        self.textboxlbl30.move(100,159)
        self.textbox30.setText("")
        self.textbox30.move(180,150)
        self.textbox30.resize(280,30)
    
        self.textbox2 = QLineEdit(self)
        self.textboxlbl2 = QLabel("<h3>Height(cm):<h3>", self)
        self.textboxlbl2.setStyleSheet("color: yellow")
        self.textboxlbl2.move(100,199)
        self.textbox2.setText("")
        self.textbox2.move(180,190)
        self.textbox2.resize(280,30)

        self.textbox1 = QLineEdit(self)
        self.textboxlbl1 = QLabel("<h3>Weight(kg):<h3>", self)
        self.textboxlbl1.setStyleSheet("color: yellow")
        self.textboxlbl1.move(100,248)
        self.textbox1.setText("")
        self.textbox1.move(180,240)
        self.textbox1.resize(280,30)

        self.textbox3 = QLineEdit(self)
        self.textboxlbl3 = QLabel("<h3>Your Basal Metabolic Rate is:<h3>",self)
        self.textboxlbl3.setStyleSheet("color: yellow")
        self.textboxlbl3.move(20,309)
        self.textboxlbl3.resize(390,20)
        self.textbox3.setText("")
        self.textbox3.move(215,300)
        self.textbox3.resize(245,30)
        

        self.button = QPushButton('Submit',self)
        self.button.setStyleSheet("background-color : skyblue")
        self.button.setToolTip("Submit your Information")
        self.button.move(80,450)
        self.button.clicked.connect(self.data)
        self.button1 = QPushButton('Clear', self)
        self.button1.setToolTip("Clear all your information")
        self.button1.setStyleSheet("background-color : skyblue")
        self.button1.move(200,450)
        self.button1.clicked.connect(self.clear)
        self.button2 = QPushButton('Back', self)
        self.button2.setToolTip("Back to the main window")
        self.button2.setStyleSheet("background-color : skyblue")
        self.button2.move(320,450)
        self.button2.clicked.connect(self.back)


        

        self.show()
        

    @pyqtSlot()
    def data(self):
        fn = self.textbox10.text()
        ln = self.textbox20.text()
        age = int(self.textbox30.text())
        height = float(self.textbox2.text())
        weight = int(self.textbox1.text())

        bmr = ((10 * weight) + (6.25 * height)-(5*age)+5)
        bmr1 = self.textbox3.setText(f"{bmr}")

        self.submitdata(fn, ln, age, height, weight,bmr)

    def clear(self):
        self.textbox10.setText("")
        self.textbox20.setText("")
        self.textbox30.setText("")
        self.textbox2.setText("")
        self.textbox1.setText("")
        self.textbox3.setText("")
    def back(self):
        BMR.close(self)
    def submitdata(self, fn, ln, age, height, weight,bmr):
        submitting = QMessageBox.question(self, "Submitting Data", "Are you sure want to submit this information?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and fn != "" and ln != "" and age != "" and height != "" and weight != "" :
            dictionarydb = SqliteDict("BMRMale.db", autocommit = True)
            accounts_list = dictionarydb.get('accounts',[])
            d = (f"First Name: {fn} Last Name: {ln} Age: {age} Height: {height} Weight: {weight} BMR: {bmr}")
            accounts_list.append(d)
            dictionarydb['accounts'] = accounts_list
            for i in range(len(dictionarydb['accounts'])):
                print(dictionarydb['accounts'][i])
            QMessageBox.information(self, "Evaluation", "Data Inputted!", QMessageBox.Ok, QMessageBox.Ok)
            ano_data = QMessageBox.question(self,"Adding another data","Do you want to add another data?",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if ano_data == QMessageBox.Yes:
                  self.textbox10.setText("")
                  self.textbox20.setText("")
                  self.textbox30.setText("")
                  self.textbox40.setText("")
                  self.textbox2.setText("")
                  self.textbox1.setText("")
                  self.textbox3.setText("")
            else:
                BMR.close(self) 
        elif submitting == QMessageBox.Yes and fn =="":
            QMessageBox.warning(self,"Error","Please input your First Name", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and ln =="":
            QMessageBox.warning(self,"Error","Please input your Last Name", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and fn =="" and ln == "":
            QMessageBox.warning(self,"Error","Please input your First Name and Last Name", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and fn == "" and ln == "" and age == "" and height == "" and weight == "":
            pass
        elif submitting == QMessageBox.No and fn == "" or ln == "" or age == "" or height == "" or weight == "":
            QMessageBox.warning(self, "Error","Please complete the blanked field", QMessageBox.Ok, QMessageBox.Ok)

class Female(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Female BMR Window")
        self.setGeometry(500,500,500,500)
        self.setWindowIcon(QIcon('user.png'))
        bg = QImage("wall.jpg")
        bg1 = bg.scaled(QSize(500,500))
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(bg1))
        self.setPalette(palette)
        self.textboxlbl = QLabel("<h3>Female BMR Calculator<h3>",self)
        self.textboxlbl.setStyleSheet("color: yellow")
        self.textboxlbl.move(150,20)
        self.textboxlbl.resize(300,20)
        self.textboxlbl1 = QLabel("Please input your data:",self)
        self.textboxlbl1.setStyleSheet("color: yellow")
        self.textboxlbl1.move(175,35)
        self.textboxlbl1.resize(300,20)

        self.textbox10 = QLineEdit(self)
        self.textboxlbl10 = QLabel("<h3>First Name:<h3>", self)
        self.textboxlbl10.setStyleSheet("color: yellow")
        self.textboxlbl10.move(100,79)
        self.textbox10.setText("")
        self.textbox10.move(180,70)
        self.textbox10.resize(280,30)
        
        self.textbox20 = QLineEdit(self)
        self.textboxlbl20 = QLabel("<h3>Last Name:<h3>", self)
        self.textboxlbl20.setStyleSheet("color: yellow")
        self.textboxlbl20.move(100,119)
        self.textbox20.setText("")
        self.textbox20.move(180,110)
        self.textbox20.resize(280,30)

        self.textbox30 = QLineEdit(self)
        self.textboxlbl30 = QLabel("<h3>Age:<h3>", self)
        self.textboxlbl30.setStyleSheet("color: yellow")
        self.textboxlbl30.move(100,159)
        self.textbox30.setText("")
        self.textbox30.move(180,150)
        self.textbox30.resize(280,30)
    
        self.textbox2 = QLineEdit(self)
        self.textboxlbl2 = QLabel("<h3>Height(cm):<h3>", self)
        self.textboxlbl2.setStyleSheet("color: yellow")
        self.textboxlbl2.move(100,199)
        self.textbox2.setText("")
        self.textbox2.move(180,190)
        self.textbox2.resize(280,30)

        self.textbox1 = QLineEdit(self)
        self.textboxlbl1 = QLabel("<h3>Weight(kg):<h3>", self)
        self.textboxlbl1.setStyleSheet("color: yellow")
        self.textboxlbl1.move(100,248)
        self.textbox1.setText("")
        self.textbox1.move(180,240)
        self.textbox1.resize(280,30)

        self.textbox3 = QLineEdit(self)
        self.textboxlbl3 = QLabel("<h3>Your Basal Metabolic Rate is:<h3>",self)
        self.textboxlbl3.setStyleSheet("color: yellow")
        self.textboxlbl3.move(20,309)
        self.textboxlbl3.resize(390,20)
        self.textbox3.setText("")
        self.textbox3.move(215,300)
        self.textbox3.resize(245,30)
        

        self.button = QPushButton('Submit',self)
        self.button.setStyleSheet("background-color : skyblue")
        self.button.setToolTip("Submit your Information")
        self.button.move(80,450)
        self.button.clicked.connect(self.data)
        self.button1 = QPushButton('Clear', self)
        self.button1.setToolTip("Clear all your information")
        self.button1.setStyleSheet("background-color : skyblue")
        self.button1.move(200,450)
        self.button1.clicked.connect(self.clear)
        self.button2 = QPushButton('Back', self)
        self.button2.setToolTip("Back to the main window")
        self.button2.setStyleSheet("background-color : skyblue")
        self.button2.move(320,450)
        self.button2.clicked.connect(self.back)


        

        self.show()
        

    @pyqtSlot()
    def data(self):
        fn = self.textbox10.text()
        ln = self.textbox20.text()
        age = int(self.textbox30.text())
        height = float(self.textbox2.text())
        weight = int(self.textbox1.text())

        bmr = ((10 * weight) + (6.25 * height)-(5*age)-161)
        bmr1 = self.textbox3.setText(f"{bmr}")
        self.submitdata(fn, ln, age, height, weight,bmr)

    def clear(self):
        self.textbox10.setText("")
        self.textbox20.setText("")
        self.textbox30.setText("")
        self.textbox2.setText("")
        self.textbox1.setText("")
        self.textbox3.setText("")
    def back(self):
        Female.close(self)
    def submitdata(self, fn, ln, age, height, weight,bmr):
        submitting = QMessageBox.question(self, "Submitting Data", "Are you sure want to submit this information?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if submitting == QMessageBox.Yes and fn != "" and ln != "" and age != "" and height != "" and weight != "" :
            dictionarydb = SqliteDict("BMRFemale.db", autocommit = True)
            accounts_list = dictionarydb.get('accounts',[])
            d = (f"First Name: {fn} Last Name: {ln} Age: {age} Height: {height} Weight: {weight} BMR: {bmr}")
            accounts_list.append(d)
            dictionarydb['accounts'] = accounts_list
            for i in range(len(dictionarydb['accounts'])):
                print(dictionarydb['accounts'][i])
            QMessageBox.information(self, "Evaluation", "Data Inputted!", QMessageBox.Ok, QMessageBox.Ok)
            ano_data = QMessageBox.question(self,"Adding another data","Do you want to add another data?",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if ano_data == QMessageBox.Yes:
                  self.textbox10.setText("")
                  self.textbox20.setText("")
                  self.textbox30.setText("")
                  self.textbox2.setText("")
                  self.textbox1.setText("")
                  self.textbox3.setText("")
            else:
                Female.close(self) 
        elif submitting == QMessageBox.Yes and fn =="":
            QMessageBox.warning(self,"Error","Please input your First Name", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and ln =="":
            QMessageBox.warning(self,"Error","Please input your Last Name", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and fn =="" and ln == "":
            QMessageBox.warning(self,"Error","Please input your First Name and Last Name", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and fn == "" and ln == "" and age == "" and height == "" and weight == "":
            pass
        elif submitting == QMessageBox.No and fn == "" or ln == "" or age == "" or height == "" or weight == "":
            QMessageBox.warning(self, "Error","Please complete the blanked field", QMessageBox.Ok, QMessageBox.Ok)
        
class BMR(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Main BMR Window"
        self.x = 500
        self.y = 400
        self.width = 500
        self.height = 400
        self.setWindowIcon(QIcon('user.png'))


        self.button = QPushButton('Male',self)
        self.button.setToolTip("Boy")
        self.button.setStyleSheet("background-color : skyblue; font: Bold")
        self.button.move(100,130)
        self.button.resize(300,50)
        self.button.clicked.connect(self.male1)
        
        self.button1 = QPushButton('Female',self)
        self.button1.setToolTip("Girl")
        self.button1.setStyleSheet("background-color : skyblue; font: Bold")
        self.button1.move(100,230)
        self.button1.resize(300,50)
        self.button1.clicked.connect(self.female1)

        self.button2 = QPushButton('Back',self)
        self.button2.setToolTip("Going to main window")
        self.button2.setStyleSheet("background-color : skyblue; font: Bold")
        self.button2.move(100,330)
        self.button2.resize(300,50)
        self.button2.clicked.connect(self.back1)

        self.main_window()


    def main_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('user.png'))
        bg = QImage("qq.jpg")
        bg1 = bg.scaled(QSize(500,400))
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(bg1))
        self.setPalette(palette)
        
        self.textboxlbl = QLabel("<h3>Welcome to BMR Calculator<h3>", self)
        self.textboxlbl.setFont(QtGui.QFont("Arial",15,QtGui.QFont.Bold))
        self.textboxlbl.setStyleSheet("color: k")
        self.textboxlbl.move(90,30)
        self.textboxlbl.resize(350,30)
        self.textboxlbl1 = QLabel("Before you proceed, Please click your sexual identity",self)
        self.textboxlbl1.setFont(QtGui.QFont("Arial",8,QtGui.QFont.Bold))
        self.textboxlbl1.setStyleSheet("color: k")
        self.textboxlbl1.move(105,95)
        self.textboxlbl1.resize(300,20)
        self.textboxlbl2 = QLabel("There is a seperate formula in getting the BMR of Male and Female",self)
        self.textboxlbl2.setFont(QtGui.QFont("Arial",9,QtGui.QFont.Bold))
        self.textboxlbl2.setStyleSheet("color: k")
        self.textboxlbl2.move(65,67)
        self.textboxlbl2.resize(500,20)
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)

        self.show()

    def male1(self):
        self.w = Male()
        self.w.show
    def female1(self):
        self.w = Female()
        self.w.show()
    def back1(self):
        BMR.close(self)
    

class Display_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Main Display Window"
        self.x = 500
        self.y = 400
        self.width = 500
        self.height = 400
        self.setWindowIcon(QIcon('user.png'))
        bg = QImage("qwe.jpg")
        bg1 = bg.scaled(QSize(500,400))
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(bg1))
        self.setPalette(palette)


        self.button = QPushButton('BMI DATABASE',self)
        self.button.setToolTip("Display all information in BMI database")
        self.button.setStyleSheet("background-color : skyblue; font: Bold")
        self.button.move(100,80)
        self.button.resize(300,50)
        self.button.clicked.connect(self.window2)
        
        self.button1 = QPushButton('MALE BMR DATABASE',self)
        self.button1.setToolTip("Display all information of MALE BMR database")
        self.button1.setStyleSheet("background-color : skyblue; font: Bold")
        self.button1.move(100,150)
        self.button1.resize(300,50)
        self.button1.clicked.connect(self.window3)

        self.button2 = QPushButton('FEMALE BMR DATABASE',self)
        self.button2.setToolTip("Display all information of FEMALE BMR database")
        self.button2.setStyleSheet("background-color : skyblue; font: Bold")
        self.button2.move(100,220)
        self.button2.resize(300,50)
        self.button2.clicked.connect(self.window4)

        self.button3 = QPushButton('BACK',self)
        self.button3.setToolTip("Going back to the Main Window")
        self.button3.setStyleSheet("background-color : skyblue; font: Bold")
        self.button3.move(100,290)
        self.button3.resize(300,50)
        self.button3.clicked.connect(self.window5)
        


        self.main_window()


    def main_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('user.png'))
        
        self.textboxlbl = QLabel("<h3>HI! What Information Do You Want To See?<h3>", self)
        self.textboxlbl.setFont(QtGui.QFont("Arial",12,QtGui.QFont.Bold))
        self.textboxlbl.setStyleSheet("color: yellow")
        self.textboxlbl.move(50,10)
        self.textboxlbl.resize(500,100)
        self.show()

    def window2(self):
        self.w = BMI_data()
        self.w.show
    def window3(self):
        self.w = MaleBMR_data()
        self.w.show()
    def window4(self):
        self.w = FemaleBMR_data()
        self.w.show()
    def window5(self):
         Display_Window.close(self)
        

class BMI_data(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Database"
        self.x = 700
        self.y = 600
        self.width = 700
        self.height = 600
        self.setWindowIcon(QIcon('user.png'))
        bg = QImage("wall.jpg")
        bg1 = bg.scaled(QSize(500,700))
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(bg1))
        self.setPalette(palette)

        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle(self.title)

        self.textbox = QLineEdit(self)
        self.textbox.setText("")
        self.textbox.resize(550,200)
        self.textbox.move(100,50)

        self.button = QPushButton("Show", self)
        self.button.setStyleSheet("background-color : skyblue; font: Bold")
        self.button.move(130,360)
        self.button.resize(500,50)
        self.button.setToolTip("Show BMI Database")
        self.button.clicked.connect(self.show1)

        self.button1 = QPushButton("Clear", self)
        self.button1.setStyleSheet("background-color : skyblue; font: Bold")
        self.button1.move(130, 430)
        self.button1.resize(500,50)
        self.button1.setToolTip("Clear BMI Database")
        self.button1.clicked.connect(self.del1)

        self.button2 = QPushButton("Back", self)
        self.button2.setStyleSheet("background-color : skyblue; font: Bold")
        self.button2.move(130, 500)
        self.button2.resize(500,50)
        self.button2.setToolTip("Going back to Main Display window")
        self.button2.clicked.connect(self.back)

        self.show()
    
    @pyqtSlot()
    def del1(self):
        dictionarydb = SqliteDict("BMI.db", autocommit=True)
        accounts_list = dictionarydb.get('accounts')
        if accounts_list == []:
            QMessageBox.information(self, "Clear", "All data Cleared!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            accounts_list.pop()
            dictionarydb['accounts'] = accounts_list
            self.textbox.setText("")
        
    def show1(self):
         dictionarydb = SqliteDict("BMI.db", autocommit=True)
         accounts_list = dictionarydb.get('accounts')
         dictionarydb['accounts'] = accounts_list
         self.textbox.setText(f"{dictionarydb['accounts']}")
    
    def back(self):
        BMI_data.close(self)

class MaleBMR_data(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Database"
        self.x = 700
        self.y = 600
        self.width = 700
        self.height = 600
        self.setWindowIcon(QIcon('user.png'))
        bg = QImage("wall.jpg")
        bg1 = bg.scaled(QSize(500,700))
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(bg1))
        self.setPalette(palette)

        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle(self.title)

        self.textbox = QLineEdit(self)
        self.textbox.setText("")
        self.textbox.resize(550,200)
        self.textbox.move(100,50)

        self.button = QPushButton("Show", self)
        self.button.setStyleSheet("background-color : skyblue; font: Bold")
        self.button.move(130,360)
        self.button.resize(500,50)
        self.button.setToolTip("Show Male BMR Database")
        self.button.clicked.connect(self.show1)

        self.button1 = QPushButton("Clear", self)
        self.button1.setStyleSheet("background-color : skyblue; font: Bold")
        self.button1.move(130, 430)
        self.button1.resize(500,50)
        self.button1.setToolTip("Clear Male Database")
        self.button1.clicked.connect(self.del1)

        self.button2 = QPushButton("Back", self)
        self.button2.setStyleSheet("background-color : skyblue; font: Bold")
        self.button2.move(130, 500)
        self.button2.resize(500,50)
        self.button2.setToolTip("Going back to Main Display window")
        self.button2.clicked.connect(self.back)

        self.show()
    
    @pyqtSlot()
    def del1(self):
        dictionarydb = SqliteDict("BMRMale.db", autocommit=True)
        accounts_list = dictionarydb.get('accounts')
        if accounts_list == []:
            QMessageBox.information(self, "Clear", "All data Cleared!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            accounts_list.pop()
            dictionarydb['accounts'] = accounts_list
            self.textbox.setText("")
        
    def show1(self):
         dictionarydb = SqliteDict("BMRMale.db", autocommit=True)
         accounts_list = dictionarydb.get('accounts')
         dictionarydb['accounts'] = accounts_list
         self.textbox.setText(f"{dictionarydb['accounts']}")
    
    def back(self):
        MaleBMR_data.close(self)

class FemaleBMR_data(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Database"
        self.x = 700
        self.y = 600
        self.width = 700
        self.height = 600
        self.setWindowIcon(QIcon('user.png'))
        bg = QImage("wall.jpg")
        bg1 = bg.scaled(QSize(500,700))
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(bg1))
        self.setPalette(palette)

        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle(self.title)

        self.textbox = QLineEdit(self)
        self.textbox.setText("")
        self.textbox.resize(550,200)
        self.textbox.move(100,50)

        self.button = QPushButton("Show", self)
        self.button.setStyleSheet("background-color : skyblue; font: Bold")
        self.button.move(130,360)
        self.button.resize(500,50)
        self.button.setToolTip("Show Female BMR Database")
        self.button.clicked.connect(self.show1)

        self.button1 = QPushButton("Clear", self)
        self.button1.setStyleSheet("background-color : skyblue; font: Bold")
        self.button1.move(130, 430)
        self.button1.resize(500,50)
        self.button1.setToolTip("Clear Female BMR Database")
        self.button1.clicked.connect(self.del1)

        self.button2 = QPushButton("Back", self)
        self.button2.setStyleSheet("background-color : skyblue; font: Bold")
        self.button2.move(130, 500)
        self.button2.resize(500,50)
        self.button2.setToolTip("Going back to Main Display window")
        self.button2.clicked.connect(self.back)

        self.show()
    
    @pyqtSlot()
    def del1(self):
        dictionarydb = SqliteDict("BMRFemale.db", autocommit=True)
        accounts_list = dictionarydb.get('accounts')
        if accounts_list == []:
            QMessageBox.information(self, "Clear", "All data Cleared!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            accounts_list.pop()
            dictionarydb['accounts'] = accounts_list
            self.textbox.setText("")
        
    def show1(self):
         dictionarydb = SqliteDict("BMRFemale.db", autocommit=True)
         accounts_list = dictionarydb.get('accounts')
         dictionarydb['accounts'] = accounts_list
         self.textbox.setText(f"{dictionarydb['accounts']}")
    
    def back(self):
        FemaleBMR_data.close(self)


class BMIandBmrCalc(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Main Window"
        bg = QImage("body.jpg")
        bg1 = bg.scaled(QSize(700,500))
        self.setWindowIcon(QIcon('user.png'))
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(bg1))
        self.setPalette(palette)
        self.x = 800
        self.y = 500
        self.width = 700
        self.height = 500


        self.button = QPushButton('Body Mass Index(BMI)',self)
        self.button.setStyleSheet("background-color : skyblue; font: Bold")
        self.button.setToolTip("Computes your BMI(Body Mass Index)")
        self.button.move(100,200)
        self.button.resize(500,50)
        self.button.clicked.connect(self.window2)
        
        self.button1 = QPushButton('Basal Metabolic Rate(BMR)',self)
        self.button1.setStyleSheet("background-color : skyblue; font: Bold")
        self.button1.setToolTip("Computes your BMR(Basal Metabolic Rate)")
        self.button1.move(100,300)
        self.button1.resize(500,50)
        self.button1.clicked.connect(self.window3)

        self.button2 = QPushButton('Display all information',self)
        self.button2.setStyleSheet("background-color : skyblue; font: Bold")
        self.button2.setToolTip("Display the inputted information")
        self.button2.move(100,400)
        self.button2.resize(500,50)
        self.button2.clicked.connect(self.window4)
        
        self.button3 = QPushButton('Exit', self)    
        self.button3.setToolTip("Exit to the System")
        self.button3.move(305,465)
        self.button3.resize(100,30)
        self.button3.setStyleSheet("background-color : skyblue; font: Bold")
        self.button3.clicked.connect(QApplication.instance().quit)


        self.main_window()


    def main_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('user.png'))
        
        self.textboxlbl = QLabel("<h3>Welcome to BMI and BMR Calculator<h3>", self)
        self.textboxlbl.move(95,10)
        self.textboxlbl.resize(700,200)
        self.textboxlbl.setFont(QtGui.QFont("Arial",18,QtGui.QFont.Bold))
        self.textboxlbl.setStyleSheet("color: khaki")
        self.textboxlbl1 = QLabel("What do you want to compute?",self)
        self.textboxlbl1.setFont(QtGui.QFont("Times",12))
        self.textboxlbl1.setStyleSheet("color: khaki")
        self.textboxlbl1.move(235,130)
        self.textboxlbl1.resize(300,20)
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)

        self.show()

    def window2(self):
        self.w = BMI()
        self.w.show
    def window3(self):
        self.w = BMR()
        self.w.show()
    def window4(self):
        self.w = Display_Window()
        self.w.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BMIandBmrCalc()
    sys.exit(app.exec_())
       
