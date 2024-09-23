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

        self.next2_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.next3_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.next4_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

        self.next5_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))

        self.next6_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))

        self.next7_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))

        self.next8_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))

        self.next9_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(10))

        self.next10_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(11))

        self.try_again_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.try_again_button.clicked.connect(self.clear_answers)

        # confirm buttons
        self.confirm1_pushButton.clicked.connect(self.confirm_1)
        self.confirm2_pushButton.clicked.connect(self.confirm_2)
        self.confirm3_pushButton.clicked.connect(self.confirm_3)
        self.confirm4_pushButton.clicked.connect(self.confirm_4)
        self.confirm5_pushButton.clicked.connect(self.confirm_5)
        self.confirm6_pushButton.clicked.connect(self.confirm_6)
        self.confirm7_pushButton.clicked.connect(self.confirm_7)
        self.confirm8_pushButton.clicked.connect(self.confirm_8)
        self.confirm9_pushButton.clicked.connect(self.confirm_9)
        self.confirm10_pushButton.clicked.connect(self.confirm_10)


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
    
    def confirm_1(self):
        self.c1A_radioButton.setEnabled(False)
        self.c1B_radioButton.setEnabled(False)
        self.c1C_radioButton.setEnabled(False)
        self.c1D_radioButton.setEnabled(False)

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

    def confirm_2(self):
        self.c2A_radioButton.setEnabled(False)
        self.c2B_radioButton.setEnabled(False)
        self.c2C_radioButton.setEnabled(False)
        self.c2D_radioButton.setEnabled(False)

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

    def confirm_3(self):
        self.c3A_radioButton.setEnabled(False)
        self.c3B_radioButton.setEnabled(False)
        self.c3C_radioButton.setEnabled(False)
        self.c3D_radioButton.setEnabled(False)

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

    def confirm_4(self):
        self.c4A_radioButton.setEnabled(False)
        self.c4B_radioButton.setEnabled(False)
        self.c4C_radioButton.setEnabled(False)
        self.c4D_radioButton.setEnabled(False)

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

    def confirm_5(self):
        self.c5A_radioButton.setEnabled(False)
        self.c5B_radioButton.setEnabled(False)
        self.c5C_radioButton.setEnabled(False)
        self.c5D_radioButton.setEnabled(False)

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

    def confirm_6(self):
        self.c6A_radioButton.setEnabled(False)
        self.c6B_radioButton.setEnabled(False)
        self.c6C_radioButton.setEnabled(False)
        self.c6D_radioButton.setEnabled(False)

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

    def confirm_7(self):
        self.c7A_radioButton.setEnabled(False)
        self.c7B_radioButton.setEnabled(False)
        self.c7C_radioButton.setEnabled(False)
        self.c7D_radioButton.setEnabled(False)

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

    def confirm_8(self):
        self.c8A_radioButton.setEnabled(False)
        self.c8B_radioButton.setEnabled(False)
        self.c8C_radioButton.setEnabled(False)
        self.c8D_radioButton.setEnabled(False)

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

    def confirm_9(self):
        self.c9A_radioButton.setEnabled(False)
        self.c9B_radioButton.setEnabled(False)
        self.c9C_radioButton.setEnabled(False)
        self.c9D_radioButton.setEnabled(False)

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

    def confirm_10(self):
        self.c10A_radioButton.setEnabled(False)
        self.c10B_radioButton.setEnabled(False)
        self.c10C_radioButton.setEnabled(False)
        self.c10D_radioButton.setEnabled(False)

        #button to calculate the results
        self.finish_button.clicked.connect(self.calculate_result)
    
    

    #calculating the result
        

    def calculate_result(self):
        self.score_percent = str((self.score / 10) * 100)
        self.score_lineEdit.setText(f"{self.score_percent}%")
        self.score_label.setText("Your Score:")

    #clear the answers
    def clear_answers(self):
        self.button_group1.setExclusive(False)
        for button in self.button_group1.buttons():
            button.setChecked(False)
        self.button_group1.setExclusive(True)

        self.button_group2.setExclusive(False)
        for button in self.button_group2.buttons():
            button.setChecked(False)
        self.button_group2.setExclusive(True)

        self.button_group3.setExclusive(False)
        for button in self.button_group3.buttons():
            button.setChecked(False)
        self.button_group3.setExclusive(True)

        self.button_group4.setExclusive(False)
        for button in self.button_group4.buttons():
            button.setChecked(False)
        self.button_group4.setExclusive(True)

        self.button_group5.setExclusive(False)
        for button in self.button_group5.buttons():
            button.setChecked(False)
        self.button_group5.setExclusive(True)

        self.button_group6.setExclusive(False)
        for button in self.button_group6.buttons():
            button.setChecked(False)
        self.button_group6.setExclusive(True)

        self.button_group7.setExclusive(False)
        for button in self.button_group7.buttons():
            button.setChecked(False)
        self.button_group7.setExclusive(True)

        self.button_group8.setExclusive(False)
        for button in self.button_group8.buttons():
            button.setChecked(False)
        self.button_group8.setExclusive(True)

        self.button_group9.setExclusive(False)
        for button in self.button_group9.buttons():
            button.setChecked(False)
        self.button_group9.setExclusive(True)

        self.button_group10.setExclusive(False)
        for button in self.button_group10.buttons():
            button.setChecked(False)
        self.button_group10.setExclusive(True)

        self.score_label.clear()
        self.score_lineEdit.clear()

        self.score = 0









    






    
