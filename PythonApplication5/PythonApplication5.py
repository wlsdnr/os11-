
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QGridLayout, QTextEdit, QMainWindow
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QColor, QTextCursor

from hanspell import spell_checker


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

        grid.addWidget(self.text,1,0)
        grid.addWidget(self.text2,1,1)
        

        btn=QPushButton('맞춤법 검사',self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.text_spell_check)

        btn2=QPushButton('사과문 검사',self)
        btn2.resize(btn.sizeHint())
        btn2.clicked.connect(self.text_sorry_check)


        grid.addWidget(btn,0,0)
        grid.addWidget(btn2,0,1)


        self.setWindowTitle('사과문 검사기 beta')
        self.setGeometry(300,100,1000,500)
        self.show()

    
    def text_spell_check(self):
        text=self.text.toPlainText()
        result=spell_checker.check(text)
        ress=result.checked
        self.text2.setText(ress)
        
    def text_sorry_check(self):
        here=0
        where=0
        num=0
        

        text=self.text.toPlainText()
        leng=len(text)
        self.text.clear()

        for i in range (0,leng):
            if text[i]=="오" and text[i+1]=="해":
                where=i
                self.text.insertPlainText(text[here:where])
                where=where+2
                here=where
                self.focus("오해")


            if text[i]=="본" and text[i+1]=="의" and text[i+2]==" " and text[i+3]=="아" and text[i+4]=="니" and text[i+5]=="게":
                where=i
                self.text.insertPlainText(text[here:where])
                where=where+6
                here=where
                self.focus("본의 아니게")


            if text[i]=="억" and text[i+1]=="울" :
                where=i
                self.text.insertPlainText(text[here:where])
                where=where+2
                here=where
                self.focus("억울")
            
                

            if text[i]=="앞" and text[i+1]=="으" and text[i+2]=="로" and text[i+3]=="는":
                where=i
                self.text.insertPlainText(text[here:where])
                where=where+4
                here=where
                self.focus("앞으로는")

            if text[i]=="앞" and text[i+1]=="으" and text[i+2]=="론":
                where=i
                self.text.insertPlainText(text[here:where])
                where=where+3
                here=where
                self.focus("앞으론")

            if text[i]=="하" and text[i+1]=="지" and text[i+2]=="만":
                where=i
                self.text.insertPlainText(text[here:where])
                where=where+3
                here=where
                self.focus("하지만")
           


        if leng!=where:
            self.text.insertPlainText(text[where:])



    def focus(self,a):
        self.text.setTextColor(QColor(255,0,0))
        self.text.setFontPointSize(15)
        self.text.insertPlainText(a)
        self.text.setFontPointSize(10)
        self.text.setTextColor(QColor(0,0,0))


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())