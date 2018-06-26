from PyQt4 import QtGui, QtCore
import sys, os
import ctypes
import platform
import time
import re
import requests
import clipboard
from PyQt4.QtGui import *
import keyboard
import sys
import time
from PyQt4.QtGui import QApplication, QWidget
from PyQt4.QtCore import QTimer, Qt
from Search_intenet import *
import speech_recognition as sr
#from gtts import gTTS
#quiet the endless 'insecurerequest' warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
from pygame import mixer
mixer.init()
import pandas as pd
import re, math
from collections import Counter
df1 = pd.read_csv("new_final.csv",  error_bad_lines=False,usecols=['id','Title','Resolution'])
#print(df1)

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)


infy=0.000000 # equalant to - neg infinty
ans_id=0




class SystemTrayIcon(QtGui.QSystemTrayIcon):
    key1=0
    
    def check_state(self):
        if self.w.windowState() == Qt.WindowMinimized:
            #print "Window is minimised. Restore it."
            try: #used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('ctrl'):#if key 'q' is pressed
                    #print"ctrl"                if keyboard.is_pressed('k') and key==1:
                    #print "key"
                    key1=1
                    #self.w.setWindowState(Qt.WindowNoState)
                if keyboard.is_pressed('k') and key1==1:
                    #print "key"
                    key1=0
                    self.w.setWindowState(Qt.WindowNoState)
            except Exception as e:
                print "oops",e

            
    def updateIcon(self):
        
        self.w.show()
        
        #self.setIcon(QtGui.QIcon("Example2.ico"))
   
    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)
        font = QtGui.QFont()
        font.setPointSize(12)
        #font.setBold(True)
        font.setWeight(75)
        changeicon = menu.addAction("Search")
        exitAction = menu.addAction("Exit")
        self.setContextMenu(menu)
        exitAction.triggered.connect(QtGui.qApp.quit)
        changeicon.triggered.connect(self.updateIcon)
        
        #the po up windows    
        self.w = QWidget()
        x=0
        y=0
##        try:
##            user32 = ctypes.windll.user32
##            screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
##            platforms=platform.system()
##            if(platforms=="Windows"):
##                x=1500
##                y=800
####                x=screensize[0]-300
####                y=screensize[1]-504
##                #print x,y
##            else:
##                x=1500
##                y=800
##        except Exception as e:
##            print "exception",str(e)
        x=1250
        y=200 
        #print x,y
        self.w.move(x,y)
        self.w.setWindowTitle('infomind_search_BOT')
        self.w.resize(650, 730)
        button = QPushButton('Search', self.w)
        button.move(560,630)
        button.resize(80,80)

        button2 = QtGui.QPushButton( self.w)
        icon2 = QIcon("images/if_08_171506.png")
        button2.setIcon(icon2)
        
        
        button2.move(520,630)
        button2.resize(30,30)
       

        #the borowser box
        browser = QTextBrowser(self.w)
        browser.setHtml("""     <!DOCTYPE html>
                                <html>
                                <style>
                                body {g
                               background-color: #ffffff;
                                }
                                </style>
                                <body></body>
                                </html>
                                """)
        browser.move(20,20)
        browser.resize(620,600)

        textbox = QTextEdit(self.w)
        textbox.move(20, 630)
##        textbox.wordWrapMode(True)  
        textbox.resize(490,80)
        paste_text = clipboard.paste()
        if(paste_text):
            paste_text=str(paste_text)
            #print "paste data",paste_text
            textbox.setText(paste_text)

        

            
        def rec_paste():
            
            response=""
            textString = QtCore.QString("""<style>
                    .cll{background-color: #F4FD59    ;color: #000000;float:right;font-family: Trebuchet; font-size: 12px;margin-left:10px;font-weight: lighter;text-align: right; }
                    .time{font-size: 11px ;vertical-align:bottom;color: #999999;}
                    
                                   </style>
                                   <table><tr><td></br></br></td></tr></table>
                               <table  class="cll">
                               <tr>
                                    <td>
                                        Bot: Say something! </td>
                                    <td class="time" > <br>"""+time.strftime('%I:%M %p' )+"""</td>           
                               </tr>
                                 </table>
        <table><tr><td></br></br></td></tr></table>""")
                #print textString
            browser.append(textString)
            time.sleep(5)
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Say something!")
                
                audio = r.listen(source,phrase_time_limit=5)
                # recognize speech using Sphinx/Google
            try:
                response = r.recognize_google(audio)
                print(" you said '" + response + "'")
                textString = QtCore.QString("""<style>
                    .cll{background-color: #F4FD59    ;color: #000000;float:right;font-family: Trebuchet; font-size: 12px;margin-left:10px;font-weight: lighter;text-align: right; }
                    .time{font-size: 11px ;vertical-align:bottom;color: #999999;}
                    
                                   </style>
                                   <table><tr><td></br></br></td></tr></table>
                               <table  class="cll">
                               <tr>
                                    <td>
                                        Bot: I think you said """+ response + "'"+""" </td>
                                    <td class="time" > <br>"""+time.strftime('%I:%M %p' )+"""</td>           
                               </tr>
                                 </table>
        <table><tr><td></br></br></td></tr></table>""")
                #print textString
                browser.append(textString)
            except sr.UnknownValueError:
                print("Sorry could not understand audio")
            except sr.RequestError as e:
                print("Sorry error; {0}".format(e))
            textbox.setText(response)
            
        

        def on_click():
            #textbox.setText("Button clicked.")
            #print (dir(textbox))
            text = unicode(textbox.toPlainText())
##            print text
##            print len(text)
##            print(not text)
            if(not(not text)):
                textString = QtCore.QString("""<style>
                                .container {background-color: #ADFB42  ;width: 100%;color: #000000;float: left;margin-right:40px;font-family:Trebuchet;font-size: 15px ;
                                font-weight: lighter;text-align: left; }
                           .time{font-size: 11px ;vertical-align:bottom;color: #999999;}
                           </style>
                    <table  class="container" style='overflow-x:scroll;height:100px;display:block;'>
                       <tr>
                        <td>
                         Me :  """+text+""" <td class="time" ></br>"""+time.strftime('%I:%M %p' )+"""</td>
                        </td>
                       </tr>   
                    </table>
                    <table><tr><td><br></td></tr></table>""")
                browser.append(textString)

##                return_Res=answers(text)
##                print return_Res
##                print dir(return_Res)
                              

##                #return_Res="hello how can i help you today"
                infy=0.000000 # equalant to - neg infinty
                ans_id=0
                text1=text
                for index, row in df1.iterrows():
                    #print row['id'], row['Title']
                    text2 = row['Title']

                    vector1 = text_to_vector(text1)
                    vector2 = text_to_vector(text2)
                    cosine = get_cosine(vector1, vector2)
                    if(cosine>infy):
                        ans_id=row['id']
                    
                        infy=cosine
                print ans_id
                a=(df1.loc[[ans_id-1]])
                return_Res= (a.iloc[0]['Resolution'])
                
##                print dir(return_Res)
                return_Res2=str(return_Res)
                #</code>
                return_Res2=return_Res.replace('</code>',"")

                return_Res=return_Res2.replace("\n"," ")
                clipboard.copy(return_Res)
                
                if('\n' in return_Res2):
                    print "found"
                    
                #print return_Res2
                textString = QtCore.QString("""<style>
                    .cll{background-color: #F4FD59    ;color: #000000;float:right;font-family: Trebuchet; font-size: 12px;margin-left:10px;font-weight: lighter;text-align: right; }
                    .time{font-size: 11px ;vertical-align:bottom;color: #999999;}
                    
                                   </style>
                                   <table style='overflow-x:auto;'><tr><td></br></br></td></tr></table>
                               <table  class="cll">
                               <tr>
                                    <td>
                                        Bot:"""+return_Res2+""" </td>
                                    <td class="time" > <br>"""+time.strftime('%I:%M %p' )+"""</td>           
                               </tr>
                                 </table>
        <table><tr><td><br></br></td></tr></table>""")
                #print textString '<pre><code>print("Hello, World!")<br /></code></pre><br /><br />'
                return_Res2=(str(return_Res2))
                lst=["//>","</pre>","<code><pre>","<code>","<pre>","</code>","</>"]
##
                return_Res2=' '.join(x for x in return_Res2.split(' ') if x not in lst)
                
                return_Res2=return_Res2.replace('<br />',"\n",len(return_Res2))
                return_Res2=return_Res2.replace('</code>',"",len(return_Res2))
                return_Res2=return_Res2.replace('<code>',"",len(return_Res2))
                return_Res2=return_Res2.replace('</pre>',"",len(return_Res2))
                return_Res2=return_Res2.replace('<pre>',"",len(return_Res2))
##                return_Res2=return_Res.replace('</code>',"",len(return_Res2))
##                return_Res2=return_Res.replace('\n'," ",len(return_Res2))
##                return_Res2=return_Res.replace('<br /> '," ",len(return_Res2))
##                return_Res2=return_Res.replace("<br />"," ",len(return_Res2))
##                return_Res2=return_Res.replace('</pre>',"",len(return_Res2))
##                return_Res2=return_Res.replace('<pre>',"",len(return_Res2))
##                return_Res2=return_Res.replace('<code>',"",len(return_Res2))
##                return_Res2=re.sub('<br /> ', '', return_Res2)
##                lst=["<br /> ","<br />","<br","//>","<br />","<code>","<pre>","</code>","</>"]
##
##                return_Res2=' '.join(x for x in return_Res2.split(' ') if x not in lst)
                
                
                
               
                print return_Res2
                print "##################################"

                browser.append(textString)
            else:
                textString = QtCore.QString("""<style>
                    .cll{background-color: #F4FD59    ;color: #000000;font-family: Trebuchet; font-size: 15px;margin-left:60px;font-weight: lighter;text-align: right; }
                    .time{font-size: 11px ;vertical-align:bottom;color: #999999;}
                                   </style>
                                   
                                   <table ><tr><td></br></br></td></tr></table>
                               <table  class="cll">
                               <tr>
                                    <td>
                                        Bot:Please enter search query </td>
                                        <td class="time" > """+time.strftime('%I:%M %p' )+"""</td>          
                               </tr>
                                 </table>
        <table><tr><td><br><br></td></tr></table> <br><br>""")

                browser.append(textString)
                

            #print text
            

        button.clicked.connect(on_click)
        button2.clicked.connect(rec_paste)
        
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.check_state)
        self.timer.start()




def main():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon(os.path.join('images', 'so-icon.png')), w)
    trayIcon.show()
    key1=0
    
    
    sys.exit(app.exec_()) 
    
    #print dir(trayIcon.w.show())

    

if __name__ == '__main__':
    main()
