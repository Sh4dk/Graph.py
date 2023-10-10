import matplotlib.pyplot as plt
from tkinter import *
def graph2():
    x = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday']
    y = [38, 32, 36, 40, 30, 28, 37]
    plt.bar(x, y)
    plt.ylim(0,100)
    plt.xlabel('Categories')
    plt.ylabel('Celcius')
    plt.title('Maximum daily temperature')
    plt.show()
def graph1():
    x = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    y = [88, 82, 86, 90, 80, 78, 87]
    plt.bar(x, y)
    plt.ylim(0,100)
    plt.xlabel('Categories')
    plt.ylabel('Celcius')
    plt.title('Maximum daily temperature')
    plt.show()
window = Tk()
photo=PhotoImage(file="F:\\Capture.png")
button1=Button(window,
              text="Temperatur in farenheit",
              command=graph1,
              font=("comic sans",30),
              fg="#00FF00",
              bg="black",
              activeforeground="#00FF00", 
              activebackground="black", 
              state=ACTIVE, 
              compound='top') 
button2=Button(window,
              text="Temperatur in Celsius",
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
