# 64210068 oktay vosoughi
from tkinter import *
import tkinter as tk
def convert():
    value=float(tl_entery.get())#gettin value of user
    dollar_label['text']=f'{value} turkish lira is euqal to {value/14.76} dollar'#putting value in to the label
    print(value,dollar_label)
# clearing insert function
def click(event):
    tl_entery.delete(0,END)
# running tk window
window=tk.Tk()
window.title('tl to dollar')


# turkish lira user input. using justify to align center the placeholder text
tl_entery=tk.Entry( width=40,justify='center')
# to clear the place holder
tl_entery.bind('<Button-1>',click)
#adding placeholer with insert
tl_entery.insert(0,'enter turkish lira to convert')
# pady in packs usees to give margin between every row
tl_entery.pack(pady=5)
# convert button
convert_btn=tk.Button(master=window, text='convert to dollar',width=20,height=1,bg='white',fg='black',command=convert)
convert_btn.pack(pady=5)
# dollar label
dollar_label=tk.Label(master=window, text="",width=100,height=1,bg='white',fg='black')
dollar_label.pack(pady=5)
#display
window.mainloop()
