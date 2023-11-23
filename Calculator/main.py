import tkinter 

window = tkinter.Tk()

expression = "" 

def GenerateExpression(num):
    global expression 
    expression += str(num) 
    equation.set(expression) 

def PressedEqual():
    try:
        global expression 
        res = str(eval(expression))
        equation.set(res)
        expression = ""
    except:
        equation.set("Error Occured")    
        expression = ""

def clear():
    global expression 
    expression = ""        
    equation.set("")

window.title('Calculator')

window.geometry('500x750')

if __name__ == '__main__':
    window.configure(background="#b5baba")
    equation = tkinter.StringVar()

    field = tkinter.Entry(window , textvariable = equation )
    field.grid(columnspan=10 , ipadx=183 , ipady= 60 , padx=4 , pady=4)

    button1 = tkinter.Button(window , text='1', fg='black', bg='light blue', 
                    command=lambda: GenerateExpression(1), height=1, width=7) 
    button1.grid(row=2, column=0)
    window.mainloop()

    