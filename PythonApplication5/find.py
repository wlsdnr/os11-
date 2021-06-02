from PyQt5.QtGui import QColor, QTextCursor






def focus(self,text):
    self.text2.setTextColor(QColor(255,0,0))
    self.text2.setFontPointSize(15)
    self.text2.insertPlainText(text)
    self.text2.setFontPointSize(10)
    self.text2.setTextColor(QColor(0,0,0))

def text_sorry(self,text):
        here=0
        where=0
        num=0
        count=0


        jalmot=0
        future=0
        real=0

        solve='문제가 된 이유를 밝혔는가.\n진실된 반성이 있는가.\n문제 해결을 위한 계획이 있는가\n\n\n'
        leng=len(text)
        self.text2.clear()

        for i in range (0,leng):
            if text[i]=="오" and text[i+1]=="해":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+2
                here=where
                focus(self,"오해")
                count=count+1
                if jalmot==0:
                    solve=solve+"자신이 잘못 한 것을 인정하기.\n"
                    jalmot=1


            if text[i]=="본" and text[i+1]=="의" and text[i+2]==" " and text[i+3]=="아" and text[i+4]=="니" and text[i+5]=="게":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+6
                here=where
                focus(self,"본의 아니게")
                count+=1
                if jalmot==0:
                    solve=solve+"자신이 잘못 한 것을 인정하기.\n"
                    jalmot=1
            
            if text[i]=="억" and text[i+1]=="울" :
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+2
                here=where
                focus(self,"억울")
                count+=1
                if jalmot==0:
                    solve=solve+"자신이 잘못 한 것을 인정하기.\n"
                    jalmot=1

            if text[i]=="그" and text[i+1]=="럴":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+2
                here=where
                focus(self,"그럴")
                count+=1
                if jalmot==0:
                    solve=solve+"자신이 잘못 한 것을 인정하기.\n"
                    jalmot=1

            if text[i]=="고" and text[i+1]=="려" and text[i+2]=="해" and text[i+3]=="보" and text[i+4]=="겠" and text[i+5]=="습" and text[i+6]=="니" and text[i+7]=="다":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+8
                here=where
                focus(self,"고려해보겠습니다")
                count+=1
                if future==0:
                    solve=solve+"보다 구체적인 계획을 이야기하기.\n"
                    future=1


            if text[i]=="의" and text[i+1]=="도" and text[i+2]=="가":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+3
                here=where
                focus(self,"의도가")
                count+=1
                if jalmot==0:
                    solve=solve+"자신이 잘못 한 것을 인정하기.\n"
                    jalmot=1

            if text[i]=="의" and text[i+1]=="도" and text[i+2]=="와" and text[i+3]=="는":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+4
                here=where
                focus(self,"의도와는")
                count+=1
                if jalmot==0:
                    solve=solve+"자신이 잘못 한 것을 인정하기.\n"
                    jalmot=1


            if text[i]=="사" and text[i+1]=="실" and text[i+2]==" " and text[i+3]=="여" and text[i+4]=="부" and text[i+5]=="를" and text[i+6]==" " and text[i+7]=="떠" and text[i+8]=="나":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+9
                here=where
                focus(self,"사실 여부를 떠나")
                count+=1
                if real==0:
                    solve=solve+"오해의 여지가 있는 문구 피하기.\n"
                    real=1

            if text[i]=="고" and text[i+1]=="의" and text[i+2]=="가":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+3
                here=where
                focus(self,"고의가")
                count+=1
                if jalmot==0:
                    solve=solve+"자신이 잘못 한 것을 인정하기.\n"
                    jalmot=1
           
            if text[i]=="일" and text[i+1]=="이" and text[i+2]==" " and text[i+3]=="이" and text[i+4]=="렇" and text[i+5]=="게" and text[i+6]==" " and text[i+7]=="된" and text[i+7]==" " and text[i+7]=="점":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+10
                here=where
                focus(self,"일이 이렇게 된 점")
                count+=1
                if future==0:
                    solve=solve+"책임을 회피하지 않기.\n"
                    future=1

            if text[i]=="어" and text[i+1]=="쨌" and text[i+2]=="든":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+3
                here=where
                focus(self,"어쨌든")
                count+=1
                if jalmot==0:
                    solve=solve+"자신이 잘못 한 것을 인정하기.\n"
                    jalmot=1

            if text[i]=="두" and text[i+1]=="려" and text[i+2]=="워":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+3
                here=where
                focus(self,"두려워")
                count+=1
                if jalmot==0:
                    solve=solve+"자신의 감정을 나타내지 않기.\n"
                    jalmot=1 

            if text[i]=="우" and text[i+1]=="울":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+2
                here=where
                focus(self,"우울")
                count+=1
                if jalmot==0:
                    solve=solve+"자신의 감정을 나타내지 않기.\n"
                    jalmot=1

        if leng!=where:
            self.text2.insertPlainText(text[where:])

        if count==0:
            solve=solve+"금지어 적발 횟수:0, PASS"
            self.text3.setText(solve)
        else:
            solve=solve+"금지어 적발 횟수:"+str(count)
            self.text3.setText(solve)