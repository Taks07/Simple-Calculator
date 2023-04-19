from tkinter import *
from tkinter import messagebox , font
from PIL import ImageTk, Image

root = Tk()
root.title("Simple Calculator")


#Functions for main window
def Number(n):
    EntryBox.insert(END,n)

def Delete():
    EntryBox.delete(0,END)
    
    global s
    s = ""

def Operation(o):
    text = EntryBox.get()

    global s
    s = o

    if text != "":

        try:
            float(text)

        except:
            messagebox.showerror("Error", "Enter a number!")

        else:
            global n1
            n1 = float(text)



    EntryBox.delete(0,END)
    

def Equals(event = None):
    ZeroFlag = False
    global s
    
    if s != "":
        text = EntryBox.get()
        
        if text != "":
            
            try:
                float(text)

            except:
               messagebox.showerror("Error", "Enter a number!")
               EntryBox.delete(0,END)

            else:
                n2 = float(text)

                if s == "+":
                    result = n1 + n2
                    s = ""

                elif s == "-":
                    result = n1 - n2
                    s = ""

                elif s == "*":
                    result = n1 * n2
                    s = ""

                elif s == "/":
                    try:
                        result = n1 / n2

                    except:
                        messagebox.showerror("Error","You can't divide by 0!")
                        ZeroFlag = True

                    else:
                        result = n1 / n2
                
                    s = ""

                elif s == "^":
                    result = n1 ** n2
                    s = ""

                EntryBox.delete(0,END)
                if not ZeroFlag:
                    if result%1 == 0:
                        result = int(result)
                    EntryBox.insert(0, result)       


#Functions for menu bar
def About():
    topabout = Toplevel(root)
    topabout.title("About")
    topabout.geometry("480x380")

    #Adding images in tkinter. PIL module has to be used as tkinter only supports .gif and .ppm
    img = ImageTk.PhotoImage(Image.open("Flowers.jpg"))
    Picture = Label(topabout, image = img)
    Picture.image = img #A reference to the image is vital
    Picture.grid(column = 0, row = 1)
    
    AboutText = Label(topabout, text = "This program was written to practice the tkinter module in Python.")

    AboutText.grid(column = 0, row = 0, padx = 1, pady = 1)
  
def Colours():
    topcolour = Toplevel(root)
    topcolour.title("Text Colours")

    ColourLabel = Label(topcolour, text = "Change colours")
    RedButton = Button(topcolour, text = "Red", fg = "red", command = lambda: TextColour("red"), padx = 10, pady = 5)
    GreenButton = Button(topcolour, text = "Green", fg = "green", command = lambda: TextColour("green"), padx = 8, pady = 5)
    BlueButton = Button(topcolour, text = "Blue", fg = "blue", command = lambda: TextColour("blue"), padx = 9, pady = 5)
    BlackButton = Button(topcolour, text = "Black", command = lambda: TextColour("black"), padx = 61, pady = 5)

    ColourLabel.grid(column = 0, row = 0, columnspan = 3)
    RedButton.grid(column = 0, row = 1, padx = 1, pady = 1)
    GreenButton.grid(column = 1, row = 1, padx = 1, pady = 1)
    BlueButton.grid(column = 2, row = 1, padx = 1, pady = 1)
    BlackButton.grid(column = 0, row = 2, columnspan = 3, padx = 1, pady = 1)

    topcolour.mainloop()

def FontSize():
    topfontS = Toplevel(root)
    topfontS.title("Font Size")

    FontSLabel = Label(topfontS, text = "Change font size")

    global Slider
    Slider = Scale(topfontS, from_ = 4, to = 20, length = 200, orient = HORIZONTAL, command = CFontSize)
    Slider.set(EntryFont["size"])

    FontSLabel.grid(column = 0, row = 0)
    Slider.grid(column = 0, row = 1)

    topfontS.mainloop()

def FontType():
    topfontT = Toplevel(root)
    topfontT.title("Font Type")

    global F
    F = StringVar()
    
    FontTLabel = Label(topfontT, text = "Change font type")
    HelveticaRButton = Radiobutton(topfontT, text = "Helvetica", variable = F, value = "Helvetica", command = FontSelect)
    TimesRButton = Radiobutton(topfontT, text = "Times New Roman", variable = F, value = "Times", command = FontSelect)  
    CourierRButton = Radiobutton(topfontT, text = "Courier", variable = F, value = "Courier", command = FontSelect)

    HelveticaRButton.select()
    
    FontTLabel.grid(column = 0, row = 0)
    HelveticaRButton.grid(column = 0, row = 1)
    TimesRButton.grid(column = 1, row = 1)  
    CourierRButton.grid(column = 2, row = 1)

 
#Functions for settings
def TextColour(c):
    EntryBox.config(fg = c)

def CFontSize(event = None):
    EntryFont.config(size = Slider.get())

def FontSelect():
    EntryFont.config(family = F.get())

      
#Creating menu bar
menubar = Menu(root)
menubar.add_command(label = "About", command = About)

root.config(menu = menubar)

SettingMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Settings", menu = SettingMenu)

SettingMenu.add_command(label = "Text Colours", command = Colours)

FontMenu = Menu(SettingMenu, tearoff = 0)
SettingMenu.add_cascade(label = "Font", menu = FontMenu)

FontMenu.add_command(label = "Font Size", command = FontSize)
FontMenu.add_command(label = "Font Type", command = FontType)

   
#Defining widgets
EntryFont = font.Font(size = 12)
EntryBox = Entry(root, font = EntryFont)

Button1 = Button(root, padx = 40, pady = 14, text = "1", command = lambda: Number("1"))
Button2 = Button(root, padx = 40, pady = 14,text = "2", command = lambda: Number("2"))
Button3 = Button(root, padx = 40, pady = 14,text = "3", command = lambda: Number("3"))

Button4 = Button(root, padx = 40, pady = 14,text = "4", command = lambda: Number("4"))
Button5 = Button(root, padx = 40, pady = 14,text = "5", command = lambda: Number("5"))                 
Button6 = Button(root, padx = 40, pady = 14,text = "6", command = lambda: Number("6"))                

Button7 = Button(root, padx = 40, pady = 14,text = "7", command = lambda: Number("7"))
Button8 = Button(root,padx = 40, pady = 14,text = "8", command = lambda: Number("8"))
Button9 = Button(root, padx = 40, pady = 14,text = "9", command = lambda: Number("9"))

Button0 = Button(root, padx = 40, pady = 14,text = "0", command = lambda: Number("0"))
ButtonClear = Button(root, padx = 78, pady = 14,text = "Clear", command = Delete)

ButtonAdd = Button(root, padx = 39, pady = 14,text = "+", command = lambda: Operation("+"))
ButtonMinus = Button(root, padx = 40, pady = 14,text = "-", command = lambda: Operation("-"))
ButtonMultiply = Button(root, padx = 40, pady = 14,text = "*", command = lambda: Operation("*"))

ButtonDivide = Button(root, padx = 40, pady = 14,text = "/", command = lambda: Operation("/"))
ButtonPower = Button(root, padx = 39, pady = 14,text = "^", command = lambda: Operation("^"))
ButtonEquals = Button(root, padx = 39, pady = 14,text = "=", command = Equals)


#Placing in window
EntryBox.grid(column = 0, pady = 5, row = 0, columnspan = 3)

Button9.grid(column = 0, row = 1, padx = 1, pady = 1)
Button8.grid(column = 1, row = 1, padx = 1, pady = 1)
Button7.grid(column = 2, row = 1, padx = 1, pady = 1)

Button6.grid(column = 0, row = 2, padx = 1, pady = 1)
Button5.grid(column = 1, row = 2, padx = 1, pady = 1)
Button4.grid(column = 2, row = 2, padx = 1, pady = 1)

Button3.grid(column = 0, row = 3, padx = 1, pady = 1)
Button2.grid(column = 1, row = 3, padx = 1, pady = 1)
Button1.grid(column = 2, row = 3, padx = 1, pady = 1)

Button0.grid(column = 0, row = 4, padx = 1, pady = 1)
ButtonClear.grid(column = 1, row = 4, padx = 1, pady = 1, columnspan = 2)

ButtonAdd.grid(column = 0, row = 5, padx = 1, pady = 1)
ButtonMinus.grid(column = 1, row = 5, padx = 1, pady = 1)
ButtonMultiply.grid(column = 2, row = 5, padx = 1, pady = 1)

ButtonDivide.grid(column = 0, row = 6, padx = 1, pady = 1)
ButtonPower.grid(column = 1, row = 6, padx = 1, pady = 1)
ButtonEquals.grid(column = 2, row = 6, padx = 3, pady = 1)

root.bind("<Return>", Equals)     
root.mainloop()           
