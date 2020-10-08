import tkinter
import numpy as np

# Parameters for random number generation
k1 = 5500
t1 = 1000
k2 = 5500
t2 = 1030


# Button response for "yes"
def yes():
    # Generate random Z from product of a binomial random variable and negative binomial random variable
    p = np.random.beta(2.0, 2.0)
    x1 = np.random.binomial(k1, p)
    y1 = np.random.negative_binomial(t1, p) + t1
    z = int(x1 * y1)
    # Report Z back to user in the form of a Label widget
    labelresponse.config(text="{}".format(z))
    # If Clear button is not visible, then we place clear button onto grid
    if not clearButton.winfo_viewable():
        clearButton.grid(column=0, row=4, columnspan=2)


# Button response for "no"
def no():
    # Generate random Z from product of a binomial random variable and negative binomial random variable
    p = np.random.beta(2.0, 2.0)
    x2 = np.random.binomial(k2, 1 - p)
    y2 = np.random.negative_binomial(t2, 1 - p) + t2
    z = int(x2 * y2)
    # Report Z back to user in the form of a Label widget
    labelresponse.config(text="{}".format(z))
    # If Clear button is not visible, then we place clear button onto grid
    if not clearButton.winfo_viewable():
        clearButton.grid(column=0, row=4, columnspan=2)


# Button response for "Clear". Erases the generated number and hides the clear button
def clear():
    labelresponse.config(text="")
    clearButton.grid_forget()


mainWindow = tkinter.Tk()
mainWindow.title("Randomized Response Survey")
mainWindow.geometry("1000x800+0+0")
mainWindow.configure(bg='lightblue')

# canvas = tkinter.Canvas(mainWindow, width=300, height=200, bd=0, highlightthickness=0, relief='ridge')
# canvas.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
# img = tkinter.PhotoImage(file="tamuk.png")
# canvas.create_image(0, 0, anchor='nw', image=img)
# canvas.config(bg='lightblue')

mainframe = tkinter.Frame(mainWindow, bg='lightblue')

title = tkinter.Label(mainWindow, text="Randomized Response Survey - JUUL Usage", bg='lightblue', font=('times', 22))
title.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

label = tkinter.Label(mainframe, text="Have you ever used a JUUL?"
                      , bg='lightblue', font=('times', 18))
label.grid(column=0, row=0, columnspan=2)
button1 = tkinter.Button(mainframe, text="Yes", command=yes, width=40, font=('times', 11))
button1.grid(column=0, row=1, sticky='e')
button2 = tkinter.Button(mainframe, text="No", command=no, width=40, font=('times', 11))
button2.grid(column=1, row=1, sticky='w')
label2 = tkinter.Label(mainframe, text="Please report your RANDOM* number to the survey administrator", bg='lightblue',
                       font=('times', 18))
label2.grid(column=0, row=2, columnspan=2)
labelresponse = tkinter.Label(mainframe, text="", bg='lightblue', font=('times', 20), pady=10)
labelresponse.grid(column=0, row=3, columnspan=2)
clearButton = tkinter.Button(mainframe, text="Clear", command=clear, width=60, font=('times', 11))
mainframe.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label3 = tkinter.Label(mainWindow, text="Thank you for your participation.", bg='lightblue', font=('times', 16))
label3.place(relx=0.5, rely=0.88, anchor=tkinter.CENTER)

label4 = tkinter.Label(mainWindow, text="*Each number is randomly generated, and cannot be used to reveal any information about an individual's answer.", bg='lightblue', font=('times', 14))
label4.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)

mainWindow.mainloop()
