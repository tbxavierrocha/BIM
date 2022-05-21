from tkinter import *
from tkinter import messagebox
import tkinter
import getpass
import os
import webbrowser

BIM = tkinter.Tk()

usuario = getpass.getuser()

logo=PhotoImage(file="fig_brain.png")
#logo=PhotoImage(file=".img\\fig_brain.png")
fig1=Label(image=logo, bg='lightgray')

def BIF():
    BIM.destroy()
    import BIF

def BIA():
    BIM.destroy()
    import BIA

def open_ij():
    try:
        os.startfile('C:\\Users\\' + usuario + '\\Desktop\\ImageJ\\ImageJ.exe')
    except:
        webbrowser.open('https://imagej.nih.gov/ij/download.html')
def open_NA():
    try:
        os.startfile('C:\\Users\\' + usuario + '\\Desktop\\NeuroAnalyzer.xlsm')
    except:
        messagebox.showerror('Erro', 'Copy NeuroAnalizer.xlsm file to desktop')    

def destroy():
    res=messagebox.askokcancel('Exit', 'Do you want to quit BIM? ')
    if res == TRUE:
       BIM.destroy() 
    elif res == FALSE:
        pass

class Application():
    def __init__(self):
        self.root = BIM
        self.tela()
        self.frame_tela()
        self.botoes()
        BIM.mainloop()
    def tela(self):
        self.app_width = 700
        self.app_height = 500
        self.screen_width = BIM.winfo_screenwidth()
        self.screen_height = BIM.winfo_screenheight()
        self.xscrn = (self.screen_width / 2) - (self.app_width / 2)
        self.yscrn = (self.screen_height / 2) - (self.app_height / 2)
        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.xscrn)}+{int(self.yscrn)}')
        self.root.title("Brain Image Manager")
        self.root.configure(background='lightgray')
        self.root.resizable(False, False)
        self.root.iconbitmap('minibrain.ico')
        #self.root.iconbitmap('.icon\\minibrain.ico')
        fig1.place(relx= 0.30, rely= 0.05)
    def frame_tela(self):
        self.frame = Frame(self.root)
        self.frame.place(relx=0.00, rely=0.7, relwidth=1, relheight=0.3)
        self.frame.configure(background='lightgray')
    def botoes(self):
        self.bt_BIF = Button(self.frame, text="Filter", font=('verdana, 12'), command=BIF)
        self.bt_BIF.place(relx=0.23, rely=0.03, relwidth=0.16, relheight=0.3)
        self.bt_BIA = Button(self.frame, text="Compare", font=('verdana, 12'), command=BIA)
        self.bt_BIA.place(relx=0.61, rely=0.03, relwidth=0.16, relheight=0.3)
        self.bt_open_ij = Button(self.frame, text="ImageJ", font=('verdana, 12'), command=open_ij)
        self.bt_open_ij.place(relx=0.23, rely=0.5, relwidth=0.16, relheight=0.3)       
        self.bt_open_NA = Button(self.frame, text="NeuroAnalyzer", font=('verdana, 12'), command=open_NA)
        self.bt_open_NA.place(relx=0.61, rely=0.5, relwidth=0.16, relheight=0.3)        
        self.bt_fechar = Button(self.frame, text="Exit", font=('verdana', 12, 'bold'), background='red', command=destroy)
        self.bt_fechar.place(relx=0.420, rely=0.5, relwidth=0.16, relheight=0.3)

class tkinter: messagebox.Message(master=None)
def msg():
    messagebox.showinfo(title="About", message="This system (Brain Image Manager) was developed to treat neurometry images.\nThe goal is to remove brain tissue areas and show only regions with some neuronal activity (colored regions). The images treated here are destined to mask applications developed on ImageJ software and final evaluation on Neuroanalyzer system.\nAnother possibility is the comparison of the generated images, suppressing the common activation areas and showing only their differences.\n\n Good work!\n\n Tulio Brandão Xavier Rocha Developer")
def msg2():  
    messagebox.showinfo(title="Help", message="Filter Button: Opens Brain Image Filter (BIF) window, that allows applying filter maintaining on the image only regions of interest. \n\nCompare Button: Opens Brain Image Analyzer (BIA), which exhibits only image differences.\n\nImageJ Button: Opens ImageJ software for masks application. It is necessary that ImageJ 1.53n be on the desktop.\n\nNeuroAnalyzer Button: Opens Excel® plan for analyzing image data. It is also necessary that the file NeuroAnalyzer.xlsm be on the desktop.")
Menus=Menu(BIM)
Menus=Menu(Menus)
Menus.add_command(label="About", command=msg)
Menus.add_command(label="Help", command=msg2)


BIM.config(menu=Menus)

Application()
