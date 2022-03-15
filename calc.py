 


from ast import Try
from audioop import add
from cProfile import label
from cgitb import text

import imp
import math
from posixpath import split
from this import s
from tkinter import *
from math import *
from pygame import mixer
import speech_recognition 

                 #initializing the mixer module
mixer.init()       


                       # Actions are defined for the buttons
def press(value):
 exp = e.get()
 res = ""
 try:

  
      if value == "=":
         exp = e.get()
         res = str(eval(exp))
         
         
      elif value == "CE":
         e.delete(0,END)
      elif value =="C":
         l = len(exp) - 1
         e.delete(l,END)
         return

      elif value =="cosθ":
         res = cos(radians(eval(exp)))  
      elif value =="sinθ": 
            res = cos(radians(eval(exp))) 
      elif value =="tanθ": 
            res = tan(radians(eval(exp))) 
      elif value =="cosh": 
            res = cosh((eval(exp))) 
      elif value =="sinh": 
            res = sinh(eval(exp))
      elif value =="tanh": 
            res = tanh((eval(exp)))   

      elif value =="π":
         if exp =="":
            res = pi
         else:
            res = eval(exp)*pi

      elif value =="2π":
         if exp =="":
            res = 2*pi
         else:
            res = (eval(exp)*(2*pi))   
      elif value =="√": 
         res = sqrt(eval(exp)) 
      elif value == "ln":
         res = log2(eval(exp))  
      elif value == "log₁₀":
         res = log10(eval(exp))      
      elif value == "x!":
         res = factorial(eval(exp)) 
      elif value == chr(8731):
         res = (eval(exp)**(1/3))  
      elif value == "x\u02b8":
         e.insert(END,'**')  
         return
      elif value == "x\u00B3":
         res = (eval(exp)**3)
      elif value == "x\u00B2":
         res = (eval(exp)**2)
      elif value == "e":
         if exp == "":
            res = math.e
         else:
            res = (eval(exp)*math.e)   
      elif value =="deg":
         res = (degrees(eval(exp)))
      elif value == "rad":
         res = (radians(eval(exp)))
      elif value == chr(247):
         e.insert(END,'/') 
         return
         
      else:
         e.delete(0,END)
         e.insert(0,str(exp)+str(value))
         return
      e.delete(0,END)
      e.insert(0,res)
 except SyntaxError:
    
    pass
operation = {"ADD":add,"PLUS":add,"ADDITION":add,"+":add} 

def add(a,b):
   
   return a+b

def num(t):
   l = []
   for i in t:

      try:
        l.append(float(i))
        
      
      except ValueError:
         pass   
   return l


def audio():
  
   mixer.music.load('mja.mp3')
   mixer.music.play()
   sr= speech_recognition.Recognizer()
   with speech_recognition.Microphone() as a:
      try:

         sr.adjust_for_ambient_noise(a,duration=0.2)
         voice = sr.listen(a)
         t1 = sr.recognize_google(voice)
         #print(text)
         mixer.music.load('mjb.mp3')
         mixer.music.play()
         tl = t1.split()
         print(tl)
         for word in tl:
            if word.upper() in operation.keys():
               print(word.upper())
               k = num(tl)
               print(k)
               s=operation[word.upper()](k[0],k[1])
               print(s)   
               

      except:
         pass


  



   

  

  

  
    
    
    
                                    # we create the window and it is configured
window = Tk()
window.geometry("680x360")
window.title("scientific calculator")
window.configure(bg='black')
logoimage=PhotoImage(file='logo.png')
logo = Label(window,image=logoimage,bg='black')
logo.grid(row=0,column=0)
micimage=PhotoImage(file='microphone.png')
mic = Button(window,image=micimage,bg='black',activebackground='black',bd=0,command=audio)
mic.grid(row=0,column=7)
                               #Entry block is created
e = Entry(window,width=60,bd=10,font=('arial',10,'bold'),fg='white',relief=SUNKEN,bg='black')
e.grid(row=0,column=0,columnspan=8,ipady=10)
                               #buttons are created
button_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
r = 1
c = 0
for i in button_list:
 b1 = Button(window,text=i,width=10,height=3,command=lambda b1=i :press(b1),bg='black',fg='white',activebackground="black")
 
 b1.grid(row=r,column=c)
 c= c+1
 if c>7:
   c = 0
   r = r + 1   


window.mainloop()

 