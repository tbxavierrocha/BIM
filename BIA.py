from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageChops
import tkinter
import os
import getpass
import subprocess
import cv2 as cv

BIA = tkinter.Tk()

usuario2 = getpass.getuser()
subprocess.call('mkdir C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp', shell=True)

class Funcs2(Toplevel):
    def abrir21(self):
        try:
            filepath2=filedialog.askopenfilename(title="Selecione a imagem", filetypes=(("PNG File", "*.png"),("JPG File", "*.jpg"), ("All Files", "*.*")),)
            global img21
            img21 = Image.open(filepath2)
            img21.save('C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp\\result21.png', format= 'png')
            img21 = ImageTk.PhotoImage(img21)
            global lbl21
            lbl21 = Label(BIA)
            lbl21.place(x=50, y=50)
            lbl21.configure(image=img21, bg='lightgray')
            lbl21.image = img21
        except:
            messagebox.showerror('Erro', 'Select a file!')

    def abrir22(self):
        try:
            filepath21=filedialog.askopenfilename(title="Selecione a imagem", filetypes=(("PNG File", "*.png"),("JPG File", "*.jpg"), ("All Files", "*.*")),)
            global img22
            img22 = Image.open(filepath21)
            img22.save('C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp\\result22.png', format= 'png')
            img22 = ImageTk.PhotoImage(img22)
            global lbl22
            lbl22 = Label(BIA)
            lbl22.place(x=350, y=50)
            lbl22.configure(image=img22, bg='lightgray')
            lbl22.image = img22
        except:
            messagebox.showerror('Erro', 'Select a file!')

    def comparar2(self):
        try:
            img21 = Image.open('C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp\\result21.png')
            img22 = Image.open('C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp\\result22.png')
            global diffs
            diffs = ImageChops.difference(img21, img22)
            if diffs.getbbox():
                diffs.save('C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp\\res_diff.png', format= 'png')
                res_diff = ImageTk.PhotoImage(diffs)
                global lbl23
                lbl23 = Label(BIA)
                lbl23.place(x=750, y=50)
                lbl23.configure(image=res_diff, bg='lightgray')
                lbl23.image = res_diff
        except:
            messagebox.showerror('Erro', 'Select images to compare!')

    def saveas2(self):
        try:
            filepath22 = filedialog.asksaveasfilename(filetypes=( ('image' , '*.png'), ('All', '*.*') ),defaultextension='.png')
            diffs
            diffs.save(filepath22)
        except:pass

    def excluir2(self):
        try:
            if os.path.exists('C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp\\result21.png'):
                os.remove('C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp\\result21.png')
            if os.path.exists('C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp\\result22.png'):
                os.remove('C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp\\result22.png')
            if os.path.exists('C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp\\diffs.png'):
                os.remove('C:\\Users\\' + usuario2 + '\\Desktop\\BIA_temp\\diffs.png')
            lbl21.configure(image="")
            lbl22.configure(image="")
            lbl23.configure(image="") 
        except:pass   

def principal2():
    BIA.destroy()
    import BIM

class Application2(Funcs2):
    def __init__(self):
        self.root2 = BIA
        self.tela2()
        self.frame_tela2()
        self.botoes2()
        BIA.mainloop()
    def tela2(self):
        self.app_width2 = 1050
        self.app_height2 = 500
        self.screen_width2 = BIA.winfo_screenwidth()
        self.screen_height2 = BIA.winfo_screenheight()
        self.xscrn2 = (self.screen_width2 / 2) - (self.app_width2 / 2)
        self.yscrn2 = (self.screen_height2 / 2) - (self.app_height2 / 2)
        self.root2.geometry(f'{self.app_width2}x{self.app_height2}+{int(self.xscrn2)}+{int(self.yscrn2)}')
        self.root2.title("Brain Image Analyzer")
        self.root2.configure(background='lightgray')
        self.root2.resizable(False, False)
        #self.root2.iconbitmap('minibrain.ico')
        self.root2.iconbitmap('.icon\\minibrain.ico')
        
    def frame_tela2(self):
        self.frame2 = Frame(self.root2)
        self.frame2.place(relx=0.02, rely=0.88, relwidth=0.96, relheight=0.1)
    def botoes2(self):
        self.bt_abrir2 = Button(self.frame2, text="Open 1", font=('verdana, 12'), command=self.abrir21)
        self.bt_abrir2.place(relx=0.01, rely=0.03, relwidth=0.10, relheight=0.90)
        self.bt_abrir3 = Button(self.frame2, text="Open 2", font=('verdana, 12'), command=self.abrir22)
        self.bt_abrir3.place(relx=0.12, rely=0.03, relwidth=0.10, relheight=0.90)
        self.bt_comparar = Button(self.frame2, text="Compare", font=('verdana', 12), command=self.comparar2)
        self.bt_comparar.place(relx=0.23, rely=0.03, relwidth=0.10, relheight=0.90)
        self.bt_salvar2 = Button(self.frame2, text="Save", font=('verdana, 12'), command=self.saveas2)
        self.bt_salvar2.place(relx=0.34, rely=0.03, relwidth=0.10, relheight=0.90)
        self.bt_voltar2 = Button(self.frame2, text="Back", font=('verdana', 12, 'bold'), background='gray', command=principal2)
        self.bt_voltar2.place(relx=0.78, rely=0.03, relwidth=0.10, relheight=0.90)  
        self.bt_novo2 = Button(self.frame2, text="New", font=('verdana', 12, 'bold'), background='lightblue', command=self.excluir2)
        self.bt_novo2.place(relx=0.89, rely=0.03, relwidth=0.10, relheight=0.90)
 

class tkinter: messagebox.Message(master=None)

def msg():  
    messagebox.showinfo(title="Help", message="Open Button1: Allows to select an image, for example, before an intervention, create a folder on the desktop named BIA_temp, which stores the images used by the program.\n\nOpen Button2: Allows to select the image to compare, for example, after an intervention.\n\nNew Button: Clear the screen and exclude images stored on BIA_temp folder. This folder must be deleted manually after treating all images.\n\n*Filtered images must be saved on the computer with the Save Button.")

Menus=Menu(BIA)
Menus=Menu(Menus)
Menus.add_command(label="Help", command=msg)

BIA.config(menu=Menus) 

Application2()
