
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QGridLayout, QTextEdit, QMainWindow
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QColor, QTextCursor

from hanspell import spell_checker
"""
result = spell_checker.check(u'이문장은 한글로 작성됬습니다.')
resss=result.checked
res = result.as_dict()
print(resss)
"""

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


        grid.addWidget(self.text,0,0)
        grid.addWidget(self.text2,0,2)
        

        btn=QPushButton('맞춤법 검사',self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.text_spell_check)

        btn2=QPushButton('나가기',self)
        btn2.resize(btn.sizeHint())
        btn2.clicked.connect(self.text_sorry_check)


        grid.addWidget(btn,0,1)
        btn2.move(463,270)


        self.setWindowTitle('사과문 검사기 beta')
        self.setGeometry(300,100,1000,500)
        self.show()

    
    def text_spell_check(self):
        text=self.text.toPlainText()
        result = spell_checker.check(text)
        ress=result.checked
        self.text2.setText(ress)

    def text_sorry_check(self):
        here=0
        where=0
        text=self.text.toPlainText()
        if "오해" in text:
            index_1=text.index('오해')
            self.text2.setTextColor(QColor(255,0,0))
            self.text2.append('오해')
            self.text2.setTextColor(QColor(0,0,0))
        self.text2.setText(text)
        self.text2.append('오해')

        


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())