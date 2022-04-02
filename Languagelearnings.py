from tkinter import *
import xlrd
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True
from random import random, sample

window=Tk()
window.title("Let's learn Languages!")
window.geometry('500x500+700+200')

location = 'words.xlsx'
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)
global value

def showanswer():
    global value
    global label2
    label2 = Label(window, text = sheet.cell_value(value,0), wraplength=300, justify="left",font=15)
    label2.pack(padx = 20, pady = 50)
    label.pack_forget()
    show_answer_button.pack_forget()
    #print(sheet.nrows)
    #print(int(100000*random()%sheet.nrows))
    global nextbutton
    nextbutton = Button(window, text='Next', command=next)
    nextbutton.pack(side=BOTTOM, pady=10)

def next():
    global label2
    label2.pack_forget()
    global nextbutton
    nextbutton.pack_forget()
    start()



def start():
    global value
    value = int(100000*random()%sheet.nrows)
    value = value
    global label 
    label = Label(window, text = sheet.cell_value(value,1), wraplength=300, justify="left", font=30)
    label.pack(padx = 20, pady = 50)
    startbutton.pack_forget()
    global show_answer_button
    show_answer_button = Button(window, text = 'Show answer', command=showanswer)
    show_answer_button.pack(side=BOTTOM, pady=10)
#    print(sheet.cell_value(0, 0))
#    print(sheet.cell_value(0, 1))
        


startbutton = Button(window, text = 'Start', command=start)
startbutton.pack(side=BOTTOM, pady=10)
#print(int(100000*random()%sheet.nrows))
window.mainloop()

