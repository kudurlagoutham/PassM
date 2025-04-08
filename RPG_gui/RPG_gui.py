import tkinter as tk
from tkinter import *
import re
import pyperclip
from tkinter import messagebox

def passwordGenerator(a,b):
    
    pp=a+b #concatenating the two strings as primary component
    ip=""
    for i in pp:
        ip = ip + str(ord(i))# getting the ascii values of each character for integers which can be easily manipulative
    
    length =len(ip)# the length is being used  for checking the length of the string ip
    
    if(length%2 != 0):
        ip = ip + "1"#adding the length of the ip to make it even since odd+odd=even and even+even=even
        length=length+1
        
    password = ""
    for i in range(int(length/2)):
        t = int(ip[i]+ip[i+1])
        if(t > 32):
            password=password+chr(t)#converting the ascii value to character for the password generation
        else:
            password=password+chr(t+32)#if the ascii value is less than 32 then it is converted to a printable character
        
    return password

def is_valid_password(password):
    # Define special characters set
    special_characters = "!@#$%^&*()-_+=<>?/\\|{}[]~`"
    
    result=[]
    # Minimum length check
    if len(password) < 8 :
        result.append(1) #for length

    # Flags for character types
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
            
            
    # Final validation
    if (has_upper == False):
        result.append(2) # Upper case
    if (has_lower == False):
        result.append(3) # lower case
    if(has_digit == False):
        result.append(4) # digit
    if(has_special == False):
        result.append(5)# special symbol
        
    return result

def getInput(a,b):
    #a=input("Enter the first input: ")
    #b=input("Enter the second input: ")
    
    
    password=passwordGenerator(a,b)#password generator
    validate=is_valid_password(password)#validation status
    
    for i in validate:
        if(i == 1):
            password = password+"Kg0uTh@m"
            return password
        if(i == 2):
            password = password+"K"
        if(i == 3):
            password = password+"g"
        if(i == 4):
            password = password+"0"
        if(i == 5):
            password = password+"@"
    #print(password)
    return password


def generate():
    password = getInput(entry1.get(),entry2.get())
    entry1.delete(0, tk.END) # Clear the entry widget
    entry2.delete(0, tk.END) # Clear the entry widget
    entry3.delete(0, tk.END) # Clear the entry widget
    entry3.insert(0, password)
    pyperclip.copy(password) # Copy the password to the clipboard

def help():
    msg=messagebox.showinfo("Help","This is a password managing app which can generate same password over and over again(assuming you have entered the same characters as inputs).\n You can enter the first input as any app or website name \n And for second password you can use your own password which you can't forget. \n After pressing the generate button you can directly paste the password in any password section of the website or app and also if you want to store it in a text file you can totally do that by using notepad.")
    return msg

    
window=tk.Tk()
window.title("RPG")
window.geometry("1000x1000")
window.configure(bg="white")

#about section where the label describes about the process
greeting = tk.Label(text="Hello This is a password managing app which can generate same password over and over again(assuming you have entered the same characters as inputs).\n You can enter the first input as any app or website name \n And for second password you can use your own password which you can't forget.")
greeting.pack()

label1=tk.Label(text="Enter the app name or website name")
entry1=tk.Entry()

label2=tk.Label(text="Enter the password")

entry2=tk.Entry()

label1.pack()

entry1.pack()

label2.pack()

entry2.pack()

entry3=tk.Entry()
entry3.pack()


submit = tk.Button(window,text="Submit",command=generate)
submit.place(x=500, y=500)
submit.pack()

help = tk.Button(window,text="Help",command=help)
help.pack()



#insert buttons such as
#help button which leads to popup
#about popup with the info required to operate the app
#links(these all must direct the user to their respective links)
#-cli link 
#-about author
#-more apps

help= tk.Button(window,text="Help",command=help)



window.mainloop()

#Functions
