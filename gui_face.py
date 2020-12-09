import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog 
import os
import count_code
import detect


head = tkinter.Tk()
head.geometry('1400x700')
head.title('CROWD COUNTING')

photo = PhotoImage(file = r"C:\Users\shiva\OneDrive\Desktop\crowd_counting\crowd.gif") 
photo1 = PhotoImage(file = r"C:\Users\shiva\OneDrive\Desktop\crowd_counting\cam.png")
photo2 = PhotoImage(file = r"C:\Users\shiva\OneDrive\Desktop\crowd_counting\live.png")


l1 = tkinter.Label(head, text=" CROWD COUNTING FROM WEBCAM AND IMAGE.",fg='purple',font=("Comic Sans MS", "40"))
l1.grid(row=0,column=1,pady=10)
def labeling(lb):
    l2 = tkinter.Label(head, text=lb,fg='purple',font=("Comic Sans MS", "25"))
    l2.grid(row=1,column=1,pady=10)

def wctask():
    messagebox.showinfo("showinfo", "STARTING WEBCAM! \nPress Esc To Quit")
    count_code.Webcam()

def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("all files","*.*"),("images","*.jpg*"))) 
       
    # Change label contents 
    ##label_file_explorer.configure(text="File Opened: "+filename)
    #count_code.localDetect(filename)
    detect.detect(filename)


def task():
    labeling("-->CHOOSE ONE OF THE OPTION AS INPUT.")
    button.destroy()
    #Create_button("WEBCAM",DO,photo1)
    button2=Button(head,text="LIVE VIDEO",command=wctask,bd = "4",image=photo2 ,compound=BOTTOM,fg="black",bg="light pink",font=("Comic Sans MS","20","bold"))
    button2.grid(row=5, column=1,pady=2)
    button3 =Button(head,text="SELECT IMAGE",command=browseFiles,bd = "4",image=photo1,compound=BOTTOM,fg="black",bg="light pink",font=("Comic Sans MS","20","bold"))
    button3.grid(row=6, column=1,pady=2)
  

def __init__(self,head):
    frame=Frame(head,bg="light blue")
    frame.grid()
def Create_button(name,work):
    button = Button(head,text=name,command=work ,bd = "4",image=photo,compound=BOTTOM,fg="white",bg="black",font=("Comic Sans MS","20","bold"))
    button.grid(row=5, column=1)


labeling("--> PRESS 'START' TO PROCESS.")
button = Button(head,text="START",command=task ,bd = "4",image=photo,compound=BOTTOM,fg="white",bg="black",font=("Comic Sans MS","20","bold"))
button.grid(row=5, column=1)
et = Button(head,text="EXIT",command=head.quit ,bd = "4",compound=BOTTOM,fg="red",bg="black",font=("Comic Sans MS","20","bold"))
et.grid(row=8, column=4)
#Create_button('START',task)
head.mainloop()