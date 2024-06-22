import tkinter as tk
import pyperclip as pp
import passm
import string

#window initiation
window = tk.Tk()
window.title("Password Manager")
#img=tk.PhotoImage(file="icon.png")
#window.iconphoto(False,img)
Pass = tk.StringVar()
Password = ''
password=tk.StringVar()
app_name=tk.StringVar()
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]
chars=[]
for i in range(len(all_combi)):
    for k in range(len(all_combi[i])):
        chars.append(all_combi[i][k])
    
#print(chars)
def copy_pass():# working 
    pp.copy(password.get())

#window.geometry("500X600")
#note for password entry
pass_note=tk.Label(text="The password length must be between 5-13")
pass_note.pack()
#password entry
Pass_entry=tk.Entry(window,textvariable=Pass)
Pass_entry.pack()
#getting password from user
# app name note
app_note=tk.Label(text="app name should contain 5-13 characters")
app_note.pack()
#app name entry
app_entry=tk.Entry(window,textvariable=app_name)
app_entry.pack()
#getting app_name
#submit button

#print(Pass.get(),app_name.get())
def Pass_gen():
    Password=passm.password_generator(Pass.get(),app_name.get())
    b=''
    for i in range(len(Password)):
        if(Password[i] in chars):
            b=b+Password[i]
        else:
            b=b+Password[i]
        
    password.set(b)
   


submit = tk.Button(window,command=Pass_gen,text="submit")
submit.pack()
#copy button
copy = tk.Button(window,command=copy_pass,text="Copy password")
copy.pack()
print(Pass.get(),app_name.get())
#Password note
Password_note=tk.Label(text="Your Password")
Password_note.pack()

Password=password.get()       
Password_entry=tk.Entry(window,textvariable=password)
Password_entry.pack()
#Output entry
#Password_entry.insert(0,Password)



window.mainloop()
#lets make length checking function