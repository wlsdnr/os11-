

def focus(self,text):
    a=1

def text_sorry(self,text):
        here=0
        where=0
        num=0
        count=0

        leng=len(text)
        self.text2.clear()

        for i in range (0,leng):
            if text[i]=="오" and text[i+1]=="해":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+2
                here=where
                self.focus("오해")
                count=count+1


            if text[i]=="본" and text[i+1]=="의" and text[i+2]==" " and text[i+3]=="아" and text[i+4]=="니" and text[i+5]=="게":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+6
                here=where
                self.focus("본의 아니게")
                count+=1
            
            if text[i]=="억" and text[i+1]=="울" :
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+2
                here=where
                self.focus("억울")
                count+=1
            
                

            if text[i]=="앞" and text[i+1]=="으" and text[i+2]=="로" and text[i+3]=="는":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+4
                here=where
                self.focus("앞으로는")
                count+=1

            if text[i]=="앞" and text[i+1]=="으" and text[i+2]=="론":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+3
                here=where
                self.focus("앞으론")
                count+=1

            if text[i]=="하" and text[i+1]=="지" and text[i+2]=="만":
                where=i
                self.text2.insertPlainText(text[here:where])
                where=where+3
                here=where
                self.focus("하지만")
                count+=1
           
        if leng!=where:
            self.text2.insertPlainText(text[where:])

        if count==0:
            self.text3.setText("PASS")