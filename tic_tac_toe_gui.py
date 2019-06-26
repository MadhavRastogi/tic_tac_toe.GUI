from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic___Tac___Toe")

pl_a = StringVar()
pl_b = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)



def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, pl_b, pl_a
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "+"
        bclick = False
        pl_b = p2.get() + " Wins!"
        pl_a = p1.get() + " Wins!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "-"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == '+' and button2['text'] == '+' and button3['text'] == '+' or
        button4['text'] == '+' and button5['text'] == '+' and button6['text'] == '+' or
        button7['text'] =='+' and button8['text'] == '+' and button9['text'] == '+' or
        button1['text'] == '+' and button5['text'] == '+' and button9['text'] == '+' or
        button3['text'] == '+' and button5['text'] == '+' and button7['text'] == '+' or
        button1['text'] == '+' and button2['text'] == '+' and button3['text'] == '+' or
        button1['text'] == '+' and button4['text'] == '+' and button7['text'] == '+' or
        button2['text'] == '+' and button5['text'] == '+' and button8['text'] == '+' or
        button7['text'] == '+' and button6['text'] == '+' and button9['text'] == '+'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pl_a)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Match Drawn")

    elif (button1['text'] == '-' and button2['text'] == '-' and button3['text'] == '-' or
          button4['text'] == '-' and button5['text'] == '-' and button6['text'] == '-' or
          button7['text'] == '-' and button8['text'] == '-' and button9['text'] == '-' or
          button1['text'] == '-' and button5['text'] == '-' and button9['text'] == '-' or
          button3['text'] == '-' and button5['text'] == '-' and button7['text'] == '-' or
          button1['text'] == '-' and button2['text'] == '-' and button3['text'] == '-' or
          button1['text'] == '-' and button4['text'] == '-' and button7['text'] == '-' or
          button2['text'] == '-' and button5['text'] == '-' and button8['text'] == '-' or
          button7['text'] == '-' and button6['text'] == '-' and button9['text'] == '-'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pl_b)


buttons = StringVar()

label = Label( tk, text="Player 1:", font='Algerian', bg='white', fg='brown', height=1, width=8)
label.grid(row=1, column=0)


label = Label( tk, text="Player 2:", font='Algerian', bg='white', fg='brown', height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Algerian', bg='yellow', fg='black', height=6, width=10, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Algerian', bg='yellow', fg='black', height=6, width=10, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Algerian', bg='yellow', fg='black', height=6, width=10, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Algerian', bg='yellow', fg='black', height=6, width=10, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Algerian', bg='yellow', fg='black', height=6, width=10, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Algerian', bg='yellow', fg='black', height=6, width=10, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Algerian', bg='yellow', fg='black', height=6, width=10, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Algerian', bg='yellow', fg='black', height=6, width=10, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Algerian', bg='yellow', fg='black', height=6, width=10, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()