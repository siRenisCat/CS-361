from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.geometry("400x380")
root.title('Calculator')

class App:
    def __init__(self):
        self.display = StringVar()
        
    def input(self,input):
        content = self.display.get() + str(input)
        self.display.set(content)

    def clear(self):
        self.display.set('')

    def back(self):
        self.display.set(str(self.display.get()[:-1]))

    def calculation(self):
        try:
            self.num = self.display.get()
            result = eval(self.num)
            self.display.set(self.num + '=\n' + str(result))
        except:
            tkinter.messagebox.showerror(message="Invalid Input")

    def log(self):
        self.display(math.log10(float(label.get())))

calc = App()


# --------------Display
label = Label(root,textvariable=calc.display, font=('Arial',25), anchor=SE, relief='raised')
label.place(x=0,y=0,width=400,height=60)


# --------------Button
button_txt = [
              ['C','DEL','%','/'],
              ['7','8','9','*'],
              ['4','5','6','-'],
              ['1','2','3','+'],
              [0,'','.','=']
]

# -------------UI layouts
for row in range(5):
    for col in range(4):
        if button_txt[row][col] =="=":
            button = Button(root, text=button_txt[row][col], font=('Arial','20','bold'), command=calc.calculation)
            button.place(x=100*col,y=60*row+60,width=100,height=60)
        elif button_txt[row][col] =="C":
            button = Button(root, text=button_txt[row][col], font=('Arial','20','bold'), command=calc.clear)
            button.place(x=100*col,y=60*row+60,width=100,height=60)
        elif button_txt[row][col] =="DEL":
            button = Button(root, text=button_txt[row][col], font=('Arial','20','bold'), command=calc.back)
            button.place(x=100*col,y=60*row+60,width=100,height=60)
        else:
            button = Button(root,text=button_txt[row][col], font=('Arial','20','bold'), command=lambda text=button_txt[row][col]:calc.input(text))
            button.place(x=100*col,y=60*row+60,width=100,height=60)

app = Frame(root)

def Exit():
    if tkinter.messagebox.askyesno("Calculator","Do you want to exit?") >0 :
        root.destroy()
        return

def Sci():
    root.resizable(width=False,height=False)
    root.geometry("800x380+0+0")


def Std():
    root.resizable(width=False,height=False)
    root.geometry("400*380")

menubar = Menu(app)

file_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Standard",command=Std)
file_menu.add_command(label="Scientific",command=Sci)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=Exit)

root.config(menu=menubar)
root.mainloop()