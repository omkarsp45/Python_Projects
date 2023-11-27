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
        last_expression_str.set(expression)
        equation.set(res)
        expression = str(res)
    except:
        equation.set("Error Occured")  
        last_expression_str.set("")  
        expression = ""

def clear():
    global expression 
    expression = ""        
    equation.set("")
    last_expression_str.set("")

window.title('Calculator')

window.geometry('400x600')

# window.resizable(False , True)  -->Window Resizability 

if __name__ == '__main__':
    window.configure(background="#b5baba")
    equation = tkinter.StringVar()

    last_expression_str = tkinter.StringVar()
    last_expression = tkinter.Entry(window , textvariable = last_expression_str , font=("Arial", 18), justify='left')
    last_expression.grid(columnspan=10 , ipadx=64 , ipady= 20 , padx=(4,0) , pady=(2,0))

    field = tkinter.Entry(window , textvariable = equation , font=("Arial", 18), justify='right')
    field.grid(columnspan=10 , ipadx=64 , ipady= 20 , padx=(4,0) , pady=(1,4))

    button1 = tkinter.Button(window , text='1', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(1), height=2, width=7) 
    button1.grid(row=4, column=0, pady=(0,4))
    button2 = tkinter.Button(window , text='2', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(2), height=2, width=7) 
    button2.grid(row=4, column=1, pady=(0,4))
    button3 = tkinter.Button(window , text='3', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(3), height=2, width=7) 
    button3.grid(row=4, column=2, pady=(0,4))
    button4 = tkinter.Button(window , text='4', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(4), height=2, width=7) 
    button4.grid(row=3, column=0, pady=(0,4))
    button5 = tkinter.Button(window , text='5', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(5), height=2, width=7) 
    button5.grid(row=3, column=1, pady=(0,4))
    button6 = tkinter.Button(window , text='6', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(6), height=2, width=7) 
    button6.grid(row=3, column=2, pady=(0,4))
    button7 = tkinter.Button(window , text='7', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(7), height=2, width=7) 
    button7.grid(row=2, column=0, pady=(0,4))
    button8 = tkinter.Button(window , text='8', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(8), height=2, width=7) 
    button8.grid(row=2, column=1, pady=(0,4))
    button9 = tkinter.Button(window , text='9', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(9), height=2, width=7) 
    button9.grid(row=2, column=2, pady=(0,4))
    button0 = tkinter.Button(window , text='0', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(0), height=2, width=7) 
    button0.grid(row=5, column=1, pady=(0,4))
    buttondot = tkinter.Button(window , text='.', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('.'), height=2, width=7)
    buttondot.grid(row=5, column=0, pady=(0,4))
    buttondot = tkinter.Button(window , text='+', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('+'), height=2, width=7)
    buttondot.grid(row=6, column=0, pady=(0,4))
    buttondot = tkinter.Button(window , text='=', font=("Arial", 15), fg='black', bg='light blue', command=PressedEqual, height=2, width=7)
    buttondot.grid(row=6, column=1, pady=(0,4))
    buttonclear = tkinter.Button(window , text='C', font=("Arial", 15), fg='black', bg='light blue', command=clear , height=2, width=7)
    buttonclear.grid(row=5, column=2, pady=(0,4))
    
    window.mainloop()

    