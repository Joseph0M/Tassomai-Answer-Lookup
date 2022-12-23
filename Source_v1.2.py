from csv import unix_dialect
from email.mime import image
import json
import sympy 
from pickletools import string1
from tkinter import *
from tkinter import ttk
import tkinter.font as font
import time
global unicode
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#\\((I)\\)
#(\\(\\text V_1,\\text V_2,\\text n_1\\)
#(\text

def manual(question,data):
    sense = 11
    if len(question) < 11:
        sense = len(question)
    for z in range(sense,0,-1):
        try:
            snip = question[:z]
            pos = []
            answer = []
            for  i  in data:
                x = i[:z]
                #print(x)
                if x == snip:
                    pos.append(i)
            for i in pos:
                for y in data[i]:
                    ans = u'Question:',i,'Answer:',data[i][y]
                    answer.append(ans)
            return answer
        except:
            time.sleep(1)
    return(['No awnser found'])
def ui(data):
    #print(manual(question,data))
    def btn(entry,window,label):
        Fonts = font.Font(family="Segoe UI Variable", size=10)
        question = entry.get()
        question = question.replace('(\\text','')

        try:
            for i in data[question]:
                ans = i
            awnser = u'',data[question][ans]
            print(awnser)
            label.configure(image = '')#,text = '')
            tup = type(awnser) is tuple
            if tup == True:
                awnser = awnser[1]
                count = False
                for i in range(0,len(awnser)):
                    if awnser[i] == '\\':
                        count = True
                if count == True:
                    awnser = awnser[1:]
                    length = len(awnser)
                    awnser = awnser[:length-1]
                    awnser = awnser.replace('\\\\\\\\\\\\\\\\&=','&=')
                    awnser = awnser.replace('\\\\',"\\")
                    awnser = awnser.replace('[','')
                    awnser = awnser.replace(']','')
                    print(awnser)
                    sympy.preview(awnser, viewer='file', filename='images/ans.png', euler=False)
                    img = PhotoImage(file='images/ans.png')      
                    label.configure(image=img)
                    label.image = img
                    print(awnser)
                else:
                    label['text'] = u'{}'.format(awnser)
            entry.delete(0,END)
        except KeyError:
            label['text'] = 'Please wait, searching for awnser...'
            ans = manual(question,data)
            if ans == []:
                label['text'] = 'No awnser found'
            else:
                if len(ans) > 20:
                    label['text'] = 'Too many awnsers found, please be more specific'
                elif len(ans) > 1:
                    label['text'] = '''Multiple answers found, 
    Potential questions and answers lsted below'''
                else:                        
                    for w in ans:    
                        lb = Label(text=w,font=Fonts,bg='white')
                        lb.pack()
            entry.delete(0,END)
    window = Tk(className='Tassomai Awnser Finder')
    def clear(window):
        for i in window.winfo_children():
            i.destroy()
        create(window)
    def create(window):
        window.configure(bg='white')
        Fonts = font.Font(family="Segoe UI Variable", size=10)
        entry = Entry(fg="black", bg="lightgrey", width=50,font=Fonts)
        entry.pack()
        butn = Button(window,text="Find", font=Fonts, command=lambda:btn(entry,window,text))
        butn.pack()
        label = Label(window, text="Answer:", font=Fonts,bg='white')
        label.pack()
        text = Label(text="Enter the question",font=Fonts,bg='white')
        text.pack()
        clr = Button(window,text="Clear",font=Fonts,command=lambda:clear(window))
        clr.pack()
    create(window)
    window.mainloop()

def main():
    f = open('Source/db.json')
    data = json.load(f)
    ui(data)
    f.close()

if __name__ == '__main__':
    main()
