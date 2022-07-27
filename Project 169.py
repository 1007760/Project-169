from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("500x500")
root.title("Project 169")
list1 = ["Label", "Button", "Dropdown"]
ttk = ttk.Combobox(root, state = "readonly", values = list1)
ttk.pack()

class CreateElements :
    def __init__(self) :
        print("This is the CreateElements class.")
        
    def createLabel(self) :
        label = Label(root, text = "A new label has been created in the class function", fg = "red")
        label.pack()
        
    def createButton(self) :
        btn = Button(root, text = "Button", command = self.message)
        btn.pack(padx = 20, pady = 10)
        
    def createDropdown(self) :
        list2 = [1,2,3]
        ttk2 = ttk.Combobox(root, state = "readonly", values = list2)
        ttk2.pack()
        
    def choose(self) :
        global ttk
        element = ttk.get()
        
        if (element == "Label") :
            self.createLabel()
            
        elif (element == "Button") :
            self.createButton()
            
        elif (element == "Dropdown") :
            self.createDropdown()
            
    def message(self) :
        messagebox.showinfo("Info : ", "You clicked the button created using the Button function inside the class.")
        
obj = CreateElements()
btn1 = Button(root, text = "Create Element", command = obj.choose)
btn1.pack()
root.mainloop()