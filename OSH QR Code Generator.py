from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk



root = Tk()
root.title("OPERATION: Sky Hogg QR Code Generator")
root.iconbitmap('c:/Users/colem/Documents/OSH QR Code/appicon.ico')
root.geometry('500x400')

def create_code():
    pass

    input_path = filedialog.asksaveasfilename(title="Save Image", filetypes= (("PNG File", ".png"), ("All Files", "*.*")))

    if input_path:
        if input_path.endswith(".png"):
            get_code = pyqrcode.create(my_text.get(1.0, END))
            get_code.png(input_path, scale=5)
        else:
            input_path = f'{input_path}.png'
            get_code = pyqrcode.create(my_text.get(1.0, END))
            get_code.png(input_path, scale=5)

        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))
        my_label.config(image=get_image)
        
        my_text.delete(1.0, END)
        my_text.insert(1.0, "Finished")


def clear_all():
    my_text.delete(1.0, END)
    my_label.config(image='')

my_text = Text(root, width=35, height=5, font=("Arial", 12))
my_text.pack(pady=10)

my_button = Button(root, text="Create QR Code", command=create_code)
my_button.pack(pady=20)

my_button2 = Button(root, text="Clear", command=clear_all)
my_button2.pack()

my_label = Label(root, text='')
my_label.pack(pady=20)




root.mainloop()
