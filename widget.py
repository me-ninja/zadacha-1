from PySide6.QtWidgets import QWidget, QButtonGroup
from ui_wwc_quiz import Ui_Form



class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("WWC Level2 Quiz")

      

        
        #listing through the pages
        self.start_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.next1_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        self.previous2_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.next2_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.previous3_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.next3_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.previous4_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.next4_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

        self.previous5_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.next5_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))

        self.previous6_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.next6_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))

        self.previous7_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.next7_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))

        self.previous8_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        self.next8_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))

        self.previous9_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))
        self.next9_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(10))

        self.previous10_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.next10_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(11))

        self.check_again_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(10))


        #setting the initial score
        # 
        self.score = 0

        #listing the questions to choose
        #question 1
        self.c1A_radioButton.toggled.connect(self.check_question_1)
        self.c1B_radioButton.toggled.connect(self.check_question_1)

        self.c1C_radioButton.toggled.connect(self.check_question_1)
        self.c1D_radioButton.toggled.connect(self.check_question_1)
        
        #add buttom group 1
        self.button_group1 = QButtonGroup()
        self.button_group1.addButton(self.c1A_radioButton)
        self.button_group1.addButton(self.c1B_radioButton)
        self.button_group1.addButton(self.c1C_radioButton)
        self.button_group1.addButton(self.c1D_radioButton)
    
    def check_question_1(self):
        if self.c1B_radioButton.isChecked():
            self.score += 1 
        print(self.score)

        #question 2
        self.c2A_radioButton.toggled.connect(self.check_question_2)
        self.c2B_radioButton.toggled.connect(self.check_question_2)
        self.c2C_radioButton.toggled.connect(self.check_question_2)
        self.c2D_radioButton.toggled.connect(self.check_question_2)

        #add buttom group 2
        self.button_group2 = QButtonGroup()
        self.button_group2.addButton(self.c2A_radioButton)
        self.button_group2.addButton(self.c2B_radioButton)
        self.button_group2.addButton(self.c2C_radioButton)
        self.button_group2.addButton(self.c2D_radioButton)

    def check_question_2(self):
        if self.c2B_radioButton.isChecked():
            self.score += 1
        print(self.score)

        #question 3
        self.c3A_radioButton.toggled.connect(self.check_question_3)
        self.c3B_radioButton.toggled.connect(self.check_question_3)
        self.c3C_radioButton.toggled.connect(self.check_question_3)
        self.c3D_radioButton.toggled.connect(self.check_question_3)

        #add buttom group 3
        self.button_group3 = QButtonGroup()
        self.button_group3.addButton(self.c3A_radioButton)
        self.button_group3.addButton(self.c3B_radioButton)
        self.button_group3.addButton(self.c3C_radioButton)
        self.button_group3.addButton(self.c3D_radioButton)

    def check_question_3(self):
        if self.c3C_radioButton.isChecked():
            self.score += 1
        print(self.score)

        #question 4
        self.c4A_radioButton.toggled.connect(self.check_question_4)
        self.c4B_radioButton.toggled.connect(self.check_question_4)
        self.c4C_radioButton.toggled.connect(self.check_question_4)
        self.c4D_radioButton.toggled.connect(self.check_question_4)

        #add buttom group 4
        self.button_group4 = QButtonGroup()
        self.button_group4.addButton(self.c4A_radioButton)
        self.button_group4.addButton(self.c4B_radioButton)
        self.button_group4.addButton(self.c4C_radioButton)
        self.button_group4.addButton(self.c4D_radioButton)

    def check_question_4(self):
        if self.c4C_radioButton.isChecked():
            self.score += 1
        print(self.score)

        #question 5
        self.c5A_radioButton.toggled.connect(self.check_question_5)
        self.c5B_radioButton.toggled.connect(self.check_question_5)
        self.c5C_radioButton.toggled.connect(self.check_question_5)
        self.c5D_radioButton.toggled.connect(self.check_question_5)

        #add buttom group 5
        self.button_group5 = QButtonGroup()
        self.button_group5.addButton(self.c5A_radioButton)
        self.button_group5.addButton(self.c5B_radioButton)
        self.button_group5.addButton(self.c5C_radioButton)
        self.button_group5.addButton(self.c5D_radioButton)

    def check_question_5(self):
        if self.c5B_radioButton.isChecked():
            self.score += 1
        print(self.score)

        #question 6
        self.c6A_radioButton.toggled.connect(self.check_question_6)
        self.c6B_radioButton.toggled.connect(self.check_question_6)
        self.c6C_radioButton.toggled.connect(self.check_question_6)
        self.c6D_radioButton.toggled.connect(self.check_question_6)

        #add buttom group 6
        self.button_group6 = QButtonGroup()
        self.button_group6.addButton(self.c6A_radioButton)
        self.button_group6.addButton(self.c6B_radioButton)
        self.button_group6.addButton(self.c6C_radioButton)
        self.button_group6.addButton(self.c6D_radioButton)
  
    def check_question_6(self):
        if self.c6C_radioButton.isChecked():
            self.score += 1
        print(self.score)

        #question 7
        self.c7A_radioButton.toggled.connect(self.check_question_7)
        self.c7B_radioButton.toggled.connect(self.check_question_7)
        self.c7C_radioButton.toggled.connect(self.check_question_7)
        self.c7D_radioButton.toggled.connect(self.check_question_7)

        #add buttom group 7
        self.button_group7 = QButtonGroup()
        self.button_group7.addButton(self.c7A_radioButton)
        self.button_group7.addButton(self.c7B_radioButton)
        self.button_group7.addButton(self.c7C_radioButton)
        self.button_group7.addButton(self.c7D_radioButton)

    def check_question_7(self):
        if self.c7B_radioButton.isChecked():
            self.score += 1
        print(self.score)

        self.c8A_radioButton.toggled.connect(self.check_question_8)
        self.c8B_radioButton.toggled.connect(self.check_question_8)
        self.c8C_radioButton.toggled.connect(self.check_question_8)
        self.c8D_radioButton.toggled.connect(self.check_question_8)

        #add buttom group 8
        self.button_group8 = QButtonGroup()
        self.button_group8.addButton(self.c8A_radioButton)
        self.button_group8.addButton(self.c8B_radioButton)
        self.button_group8.addButton(self.c8C_radioButton)
        self.button_group8.addButton(self.c8D_radioButton)

    def check_question_8(self):
        if self.c8B_radioButton.isChecked():
            self.score += 1
        print(self.score)

        self.c9A_radioButton.toggled.connect(self.check_question_9)
        self.c9B_radioButton.toggled.connect(self.check_question_9)
        self.c9C_radioButton.toggled.connect(self.check_question_9)
        self.c9D_radioButton.toggled.connect(self.check_question_9)

        #add buttom group 9
        self.button_group9 = QButtonGroup()
        self.button_group9.addButton(self.c9A_radioButton)
        self.button_group9.addButton(self.c9B_radioButton)
        self.button_group9.addButton(self.c9C_radioButton)
        self.button_group9.addButton(self.c9D_radioButton)

    def check_question_9(self):
        if self.c9A_radioButton.isChecked():
            self.score += 1
        print(self.score)

        self.c10A_radioButton.toggled.connect(self.check_question_10)
        self.c10B_radioButton.toggled.connect(self.check_question_10)
        self.c10C_radioButton.toggled.connect(self.check_question_10)
        self.c10D_radioButton.toggled.connect(self.check_question_10)

        #add buttom group 10
        self.button_group10 = QButtonGroup()
        self.button_group10.addButton(self.c10A_radioButton)
        self.button_group10.addButton(self.c10B_radioButton)
        self.button_group10.addButton(self.c10C_radioButton)
        self.button_group10.addButton(self.c10D_radioButton)

    def check_question_10(self):
        if self.c10A_radioButton.isChecked():
            self.score += 1
        print(self.score)

        #button to calculate the results
        self.finish_button.clicked.connect(self.calculate_result)
    
    

    #calculating the result
        

    def calculate_result(self):
        self.score_percent = str((self.score / 10) * 100)
        self.score_lineEdit.setText(self.score_percent)




    
