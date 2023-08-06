from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from tkinter import PhotoImage

root=Tk()
root.minsize(900,700)
root.maxsize(900,700)
root.title("Notepad")
root.config(bg="#202020")
root.iconbitmap('icon.ico')

label_filename=Label(text='File name:', font=("Segoe UI", 8, "bold"),bg="#202020", fg="#67b4c3")
label_filename.place(relx=0.45, rely=0.03, anchor=CENTER)

input_filename=Entry(font=("Segoe UI", 8))
input_filename.place(relx=0.58, rely=0.03, anchor=CENTER)

char_label=Label(text='Chars: ', font=("Segoe UI", 8, 'bold'),bg="#202020", fg="#67b4c3")
char_label.place(relx=0.85, rely=0.03, anchor=CENTER)

textarea=Text(font=("Century Gothic", 10),bg="#272727", fg="white", height=38, width=126, padx=10, pady=10, borderwidth=0)
textarea.place(relx=0.5, rely=0.53, anchor=CENTER)

word_label=Label(text="Words: ", font=("Segoe UI", 8, "bold"), bg="#202020", fg="#67b4c3")
word_label.place(relx=0.93, rely=0.03, anchor=CENTER)

sun_image=PhotoImage(file="sun.png")
moon_image=PhotoImage(file='moon.png')

name=""
files=[("Text Files", "*.txt"),
       ("Python Files", "*.py"),
       ("HTML Files", "*.html"),
       ("ALL Files", "."),]

def open_file():
    global name
    global files
    textarea.delete(1.0,END)
    input_filename.delete(0,END)
    text_file=filedialog.askopenfilename(title="Open File", filetypes=files)
    name=text_file.split("/")[-1]
    formatted_name= name.split(".")[0]
    input_filename.insert(END, formatted_name)
    text_file=open(text_file, 'r')
    paragraph=text_file.read()
    textarea.insert(END, paragraph)
    text_file.close()
    char_label.config(text="Chars:")

def save():
    global files
    input_name=input_filename.get()
    data=textarea.get('1.0', END)
    file=asksaveasfile(filetypes=files, defaultextension=files, initialfile=input_name)
    file.write(data)
    textarea.delete(1.0,END)
    input_filename.delete(0,END)
    char_label.config(text="Chars:")
    messagebox.showinfo("Update", "Success")
    file.close()

def close():
    root.destroy()

def update(event):
    char_label.config(text="Chars: "+ str(len(textarea.get("1.0","end-1c"))))
    text_area_input = textarea.get('1.0', END)
    word_count = count_words(text_area_input)
    word_label.config(text="Words:"+str(word_count))


textarea.bind('<KeyPress>', update)
textarea.bind('<KeyRelease>', update)

buttonMode=False

def theme():
    global buttonMode
    if buttonMode==True:
        root.config(background="#202020")
        textarea.config(background="#272727", foreground="white")
        open_button.config(background="#202020", fg="#67b4c3")
        save_button.config(background="#202020", fg="#67b4c3")
        exit_button.config(background="#202020", fg="#67b4c3")
        theme_button.config(background="#202020", fg="#67b4c3")
        label_filename.config(background="#202020", fg="#67b4c3")
        char_label.config(background="#202020", fg="#67b4c3")
        word_label.config(background="#202020", fg="#67b4c3")
        theme_button.config(image=sun_image, bg="#202020")
        buttonMode=False
       
    elif buttonMode == False:
        root.config(background="#FFFFFF")
        textarea.config(bg="#FEF9F3", fg="black")
        open_button.config(background="#FFFFFF", fg="black")
        save_button.config(background="#FFFFFF", fg="black")
        exit_button.config(background="#FFFFFF", fg="black")
        theme_button.config(background="#FFFFFF", fg="black")
        label_filename.config(background="#FFFFFF", fg="black")
        char_label.config(background="#FFFFFF", fg="black")
        word_label.config(background="#FFFFFF", fg="black")
        theme_button.config(image=moon_image, bg="#FFFFFF")


        buttonMode=True

theme_button = Button(image=sun_image, bg="#202020", borderwidth=0, command=theme)
theme_button.place(relx=0.30, rely=0.03, anchor=CENTER)

open_button= Button(text="Open", bg="#202020", borderwidth=0, command=open_file, fg="#67b4c3", font=("Segoe UI",8,"bold"))
open_button.place(relx=0.04, rely=0.03, anchor=CENTER)

save_button= Button(text="Save", bg="#202020", borderwidth=0, command=save,font=("Segoe UI",8,"bold"), fg="#67b4c3")
save_button.place(relx=0.12, rely=0.03, anchor=CENTER)

exit_button= Button(text="Exit",bg="#202020", borderwidth=0, command=close, font=("Segoe UI",8,"bold"), fg="#67b4c3")
exit_button.place(relx=0.20, rely=0.03, anchor=CENTER)

def count_words(text):
    words = text.split()
    return len(words)


root.mainloop()
