from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter
import os
import getpass
import subprocess
import cv2 as cv
import numpy as np

BIF = tkinter.Tk()

usuario1 = getpass.getuser()
subprocess.call('mkdir C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp', shell=True)

class Funcs1(Toplevel):
    def abrir1(self):
        try:
            filepath1=filedialog.askopenfilename(title="Selecione a imagem", filetypes=(("PNG File", "*.png"),("JPG File", "*.jpg"), ("All Files", "*.*")))
            global img1
            img1 = Image.open(filepath1)
            res=messagebox.askyesno('Flip', 'Do you want to flip image? ')
            if res == TRUE:
                img1 = img1.transpose(Image.FLIP_LEFT_RIGHT)
            elif res == FALSE:
                pass
            img1.save('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result.png', format= 'png')
            img1 = ImageTk.PhotoImage(img1)
            global lbl1
            lbl1 = Label(BIF)
            lbl1.place(x=50, y=50)
            lbl1.configure(image=img1, bg='lightgray')
            lbl1.image = img1
        except:
            messagebox.showerror('Error', 'Select a file!')

    def filtrar1(self):
        try:   
            img1 = cv.imread('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result.png')
            hh, ww = img1.shape[:2]
            lower1 = np.array([160, 200, 200])
            upper1 = np.array([255, 255, 255])
            thresh1 = cv.inRange(img1, lower1, upper1)
            kernel1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (20,20))
            morph1 = cv.morphologyEx(thresh1, cv.MORPH_CLOSE, kernel1)
            mask1 = 255 - thresh1
            result1 = cv.bitwise_and(img1, img1, mask=mask1)
            cv.imwrite('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result1.png', result1)
            
            img12 = cv.imread('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result1.png')
            hh, ww = img12.shape[:2]
            lower12 = np.array([78, 105, 170])
            upper12 = np.array([195, 218, 255])
            thresh12 = cv.inRange(img12, lower12, upper12)
            kernel12 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (20,20))
            morph12 = cv.morphologyEx(thresh12, cv.MORPH_CLOSE, kernel12)
            mask12 = 255 - thresh12
            global result2
            result2 = cv.bitwise_and(img12, img12, mask=mask12)
            cv.imwrite('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result2.png', result2)
            
            img13 = Image.open('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result2.png')
            img13 = ImageTk.PhotoImage(img13) 
            global lbl12
            lbl12 = Label(BIF)
            lbl12.place(x=350, y=50)
            lbl12.configure(image=img13, bg='lightgray')
            lbl12.image = img13
        except:
            messagebox.showerror('Error', 'Open a file!')    

    def saveas1(self):
        try:
            filepath12 = filedialog.asksaveasfilename(filetypes=( ('image' , '*.png'), ('All', '*.*') ),defaultextension='.png')
            result2
            cv.imwrite(filepath12, result2)
        except:pass
    
    def excluir1(self):
        try:
            if os.path.exists('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result.png'):
                os.remove('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result.png')
            if os.path.exists('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result1.png'):
                os.remove('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result1.png')
            if os.path.exists('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result2.png'):
                os.remove('C:\\Users\\' + usuario1 + '\\Desktop\\BIF_temp\\result2.png')
            lbl1.configure(image="")
            lbl12.configure(image="") 
        except:pass

def principal1():
    BIF.destroy()
    import BIM
    
class Application1(Funcs1):
    
    def __init__(self):
        self.root1 = BIF
        self.tela1()
        self.frame_tela1()
        self.botoes1()
        BIF.mainloop()
    def tela1(self):
        self.app_width1 = 700
        self.app_height1 = 500
        self.screen_width1 = BIF.winfo_screenwidth()
        self.screen_height1 = BIF.winfo_screenheight()
        self.xscrn1 = (self.screen_width1 / 2) - (self.app_width1 / 2)
        self.yscrn1 = (self.screen_height1 / 2) - (self.app_height1 / 2)
        self.root1.geometry(f'{self.app_width1}x{self.app_height1}+{int(self.xscrn1)}+{int(self.yscrn1)}')
        self.root1.title("Brain Image Filter")
        self.root1.configure(background='lightgray')
        self.root1.resizable(False, False)
        self.root1.iconbitmap('minibrain.ico')
        #self.root1.iconbitmap('.icon\\minibrain.ico')

    def frame_tela1(self):
        self.frame1 = Frame(self.root1)
        self.frame1.place(relx=0.02, rely=0.88, relwidth=0.96, relheight=0.1)
    def botoes1(self):
        self.bt_abrir1 = Button(self.frame1, text="Open", font=('verdana, 12'), command=self.abrir1)
        self.bt_abrir1.place(relx=0.01, rely=0.03, relwidth=0.15, relheight=0.90)
        self.bt_filtrar = Button(self.frame1, text="Filter", font=('verdana, 12'), command=self.filtrar1)
        self.bt_filtrar.place(relx=0.17, rely=0.03, relwidth=0.15, relheight=0.90)
        self.bt_salvar1 = Button(self.frame1, text="Save", font=('verdana, 12'), command=self.saveas1)
        self.bt_salvar1.place(relx=0.33, rely=0.03, relwidth=0.15, relheight=0.90)
        self.bt_novo1 = Button(self.frame1, text="New", font=('verdana', 12, 'bold'), background='lightblue', command=self.excluir1)
        self.bt_novo1.place(relx=0.84, rely=0.03, relwidth=0.15, relheight=0.90)
        self.bt_voltar1 = Button(self.frame1, text="Back", font=('verdana', 12, 'bold'), background='gray', command=principal1)
        self.bt_voltar1.place(relx=0.68, rely=0.03, relwidth=0.15, relheight=0.90)

class tkinter: messagebox.Message(master=None)

def msg():  
    messagebox.showinfo(title="Help", message="Open Button: Allows to select an image to be filtered and create a folder on the desktop named BIF_temp, which stores the images used by the program. As the main purpose is the application of the masks on ImageJ which was drawn only on the left sagittal plan, it is necessary to flip the images referring to the right side.\n\nFilter Button: Apply color filters at images and show the result.\n\nNew Button: Clear the screen and exclude images stored on BIF_temp folder. This folder must be deleted manually after treating all images.\n\n*Filtered images must be saved on the computer with the Save Button.")

Menus=Menu(BIF)
Menus=Menu(Menus)
Menus.add_command(label="Help", command=msg)

BIF.config(menu=Menus)

Application1()


