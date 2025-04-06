import re

#this is the password generating function(done)
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

#print(passwordGenerator("hello","world"))
 
#validate the input from the use

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


#print(is_valid_password("helloo123"))

#getting input and validate(done)
def getInput():
    a=input("Enter the first input: ")
    b=input("Enter the second input: ")
    
    
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
#here we get the final password

#getInput()  

#help
def l():#list of commands
    print("Here is the list of commands you can use:")
    print("p - password generation process")
    print("h - help")
    print("a - about app")
    print("l - commands list")
    #print("m - more apps")
    #print("g - gui version link")
    print("v - version of app")
    print("exit - exit the app")
    
    #p for generating the password done
    #h help done
    #a about app done
    #c commands list done
    #m more apps 
    #g gui version link
    #v version of app
    #exit
    

#about app
def about():
    print("Hello this is a password manager app. Here you can get your passwords as per the inputs that you give")
    print("For example: your first input is your password and the secondary input is a website name or any company name that you are going to log in.")
    print("This helps those students and professionals who look into every account of their socials and mostly forget their passwords.")
    print("This is a beta version of the app, which is currently being developed in a graphical user interface (GUI).")
    print("author email:kudurlagoutham13@gmail.com")
    print("github link: https://github.com/kudurlagoutham")
    
#how to use
def help():
    print("This is a password manager app. Here you can get your passwords as per the inputs that you give")
    print("Enter the first and second inputs so that it can generate a password")
    print("You can access the commands to tinker with the app by entering 'l'.")
    
    
print("Hello, this is a password-managing app where you can get random passwords based on your inputs that remain constant(assuming you are entering the same inputs)")
print("So, if you want to get started, enter the command 'p' to initiate the password generation process.")
print("If you need any help with the CLI interface, please type 'h' and press enter to get started with commands.")

while(True):
    #greetings
    userInput = input("Enter the command: ")
    if(userInput == "p"):#password generation process
        print("Enter the inputs:")
        print(getInput())
    elif(userInput == "l"):#list of commands
        l()
    elif(userInput == "a"):#about app
        about()
    elif(userInput == "h"):#help
        help()
    elif(userInput == "exit"):#exit
        print("Exiting the app. Goodbye!")
        break
    elif(userInput == "v"):#version of app
        print("Version: 1.0.0 beta")
    else:
        print("I am not a chatbot. Please enter command from the commands list.")

        
        
        
        
     
    

