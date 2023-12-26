import matplotlib.pyplot as plt
from tkinter import *
def graph2():
    x = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday']
    y = [38, 32, 36, 40, 30, 28, 37]
    plt.bar(x, y)
    plt.ylim(0,100)
    plt.xlabel('Categories')
    plt.ylabel('Celsius')
    plt.title('Maximum daily temperature')
    plt.show()
def graph1():
    x = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    y = [100, 89, 96, 104, 86, 84, 98]
    plt.bar(x, y)
    plt.ylim(0,100)
    plt.xlabel('Categories')
    plt.ylabel('Fahrenheit')
    plt.title('Maximum daily temperature')
    plt.show()
window = Tk()
button1=Button(window,
              text="Temperature in Fahrenheit",
              command=graph1,
              font=("comic sans",30),
              fg="#00FF00",
              bg="black",
              activeforeground="#00FF00", 
              activebackground="black", 
              state=ACTIVE, 
              compound='top') 
button2=Button(window,
              text="Temperature in Celsius",
              command=graph2,
              font=("comic sans",30),
              fg="#00FF00",
              bg="black",
              activeforeground="#00FF00", 
              activebackground="black", 
              state=ACTIVE, 
              compound='bottom') 
button1.pack()
button2.pack()
window.mainloop()

