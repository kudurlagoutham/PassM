#It is a Password managing app, and it doesn't generate any new password.
#Mixes two inputs such a way that it looks random and
#it is easy to remember one Master Password rather than remembering all passwords.

#In my sense it easy to remember one password and you would enter the app name or any input or any secondary password if you want to.
#You can tinker with validator to increase the password length."""
import string
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]
chars=[]
# getting all possible characters in a list
for i in range(len(all_combi)):
    for k in range(len(all_combi[i])):
        chars.append(all_combi[i][k])
#take sample inputs this is for testing purpose
#in1="idkfdsas"#input("enter the master Password")
#in2="domomers"#input("enter the app name")

def password_generator(in1,in2):
#validate inputs characters length 
    def ivalid(a):
        if(5<len(a)<13):
            return True
        else:
            return False

    while((ivalid(in1)==False) or (ivalid(in2)==False)):
        if(ivalid(in1)==False):
            print("input must be less than 13 and greater than 5 characters")
            in1=input("enter the PASSword")
        
        else:
            print("input must be less than 13 and greater than 5 characters")
            in2=input("enter the PASSword")

#converting string to numbers
    num1=[]
    num2=[]
    sum1=0
    sum2=0
    number1=""
    number2=""
    for i in range(len(in1)):
        num1.append(ord(in1[i]))
        sum1=num1[i]+sum1
    #Mixing numbers
        if(i%2 == 0):
            number1= number1+str(sum1)
        else:
            number1=number1+str(num1[i])
            
    for i in range(len(in2)):
        num2.append(ord(in2[i]))
        sum2=num2[i]+sum2
    #Mixing numbers
        if(i%2 != 0):
            number2= number2+str(sum2)
        else:
            number2=number2+str(num2[i])
#password
#print(num1) ok
#print(num2) ok
#print(number1) ok
#print(number2) ok
    Password=""
    Pass=number1+number2
    pl=len(Pass)
#print(Pass) ok
    
#lets convert the numerical string to Real Password
    for i in range(0,len(Pass),3):
        a=int(Pass[i:i+3])
    
    #The range starts from 99 to 256
        if((a >99) and (a<256)):
            if(a>126 and a<161):
                Password=Password+chr(a+36)
            else:
                Password=Password+chr(a)
    
    #range starts from 256 to 999
        elif(a > 256):
            b=int(Pass[i:i+2])
            if(b > 25 and b < 33):
                Password=Password+chr(10+b)
            else:
                Password=Password+chr(b)
            if(a%2 == 0):
                Password=Password+chr(int("4"+Pass[i+2]))
            else :
                Password=Password+chr(int("5"+Pass[i+2]))
    
    #range starts from 99 to 0
        else:
            if(a >=0 and a < 33):
                Password=Password+chr(33+a)
            else:
                Password=Password+chr(a)
    return Password    

#print(password_generator(in1="password",in2="google")) 
