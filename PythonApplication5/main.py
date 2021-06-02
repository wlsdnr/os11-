
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QGridLayout, QTextEdit, QMainWindow, QLabel
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QColor, QTextCursor

from find import text_sorry
from hanspell import spell_checker

import clipboard




class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid=QGridLayout()
        self.setLayout(grid)

        self.text=QTextEdit()
        self.text.setAcceptRichText(False)

        self.text2=QTextEdit()
        self.text2.setAcceptRichText(False)

        self.text3=QLabel('')

        self.text.setMaximumWidth(350)
        self.text2.setMaximumWidth(350)

        grid.addWidget(self.text,0,0,1,1)
        grid.addWidget(self.text2,0,1,1,1)
        grid.addWidget(self.text3,0,2,1,1)
        

        btn=QPushButton('맞춤법 검사',self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.text_spell_check)

        btn2=QPushButton('사과문 검사',self)
        btn2.resize(btn.sizeHint())
        btn2.clicked.connect(self.text_sorry_check)

        btn3=QPushButton('입력칸에 붙여넣기',self)
        btn3.resize(btn.sizeHint())
        btn3.clicked.connect(self.text_move)

        btn4=QPushButton('비우기',self)
        btn4.resize(btn.sizeHint())
        btn4.clicked.connect(self.clear_1)

        btn5=QPushButton('비우기',self)
        btn5.resize(btn.sizeHint())
        btn5.clicked.connect(self.clear_2)
        
        btn6=QPushButton('클립보드에 복사',self)
        btn6.resize(btn.sizeHint())
        btn6.clicked.connect(self.copy)

        grid.addWidget(btn,1,0,1,1)
        grid.addWidget(btn2,1,1,1,1)
        grid.addWidget(btn3,1,2,1,1)

        grid.addWidget(btn4,2,0,1,1)
        grid.addWidget(btn5,2,1,1,1)
        grid.addWidget(btn6,2,2,1,1)

        self.setWindowTitle('사과문 검사기 beta')
        self.setGeometry(300,100,1000,500)
        self.show()




    def text_spell_check(self):
        text=self.text.toPlainText()
        result=spell_checker.check(text)
        ress=result.checked
        self.text2.insertPlainText(ress)

    def text_sorry_check(self):
        self.text3.clear()
        text=self.text.toPlainText()
        text_sorry(self,text)


    def text_move(self):
        self.text.setText(clipboard.paste())

    def clear_1(self):
        self.text.clear()

    def clear_2(self):
        self.text2.clear()

    def copy(self):
        text=self.text2.toPlainText()
        clipboard.copy(text)



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())