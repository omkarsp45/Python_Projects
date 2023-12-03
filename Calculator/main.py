import tkinter 
from operations import cleanExpression

window = tkinter.Tk()
expression = "" 

def GenerateExpression(num):
    global expression
    expression = cleanExpression(expression)
    if len(expression)==1:
        if expression[0] == '0' and str(num)=='.':
            expression = '0.'
            equation.set(expression)
            return
        elif expression[0] == '0':
            expression = str(num)
            equation.set(expression)
            return    
    operations = ['+','-','/','*']
    if len(expression)>=2:
        if expression[-2] in operations:
            if expression[-1] == '0':
                if str(num) != '.':
                    expression = expression[:-1] + str(num)
                    equation.set(expression)
                    return
    if len(expression)>=1:
        if expression[-1] == '.' and str(num)== '.':
            return
    expression += str(num)
    equation.set(expression)

def clearLastEntry():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def PressedEqual():
    try:
        global expression
        expression = cleanExpression(expression)
        res = str(eval(expression))
        last_expression_str.set(expression)
        equation.set(res)
        expression = str(res)
    except ZeroDivisionError:
        equation.set("Error: Division By Zero")
    except:
        equation.set("Error Occured")  
        last_expression_str.set("")  
        expression = ""


def clear():
    global expression 
    expression = ""        
    equation.set("")
    last_expression_str.set("")


switcher = True
def switchBool():
    global switcher 
    switcher = not switcher 
    drawButtons()      

def drawButtons():
    button1 = tkinter.Button(window , text='1', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(1), height=2, width=7) 
    button1.grid(row=6, column=0, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='2', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(2), height=2, width=7) 
    button1.grid(row=6, column=1, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='3', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(3), height=2, width=7) 
    button1.grid(row=6, column=2, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='4', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(4), height=2, width=7) 
    button1.grid(row=5, column=0, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='5', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(5), height=2, width=7) 
    button1.grid(row=5, column=1, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='6', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(6), height=2, width=7) 
    button1.grid(row=5, column=2, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='7', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(7), height=2, width=7) 
    button1.grid(row=4, column=0, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='8', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(8), height=2, width=7) 
    button1.grid(row=4, column=1, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='9', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(9), height=2, width=7) 
    button1.grid(row=4, column=2, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='0', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(0), height=2, width=7) 
    button1.grid(row=7, column=1, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='.', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('.'), height=2, width=7)
    button1.grid(row=7, column=0, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='+', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('+'), height=2, width=7)
    button1.grid(row=5, column=3, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='=', font=("Arial", 15), fg='black', bg='light blue', command=PressedEqual, height=2, width=7)
    button1.grid(row=6, column=3, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text='C', font=("Arial", 15), fg='black', bg='light blue', command=clear , height=2, width=7)
    button1.grid(row=7, column=2, pady=(0,4), padx=(1,3))
    button1 = tkinter.Button(window , text="DEL", font=("Arial", 15), fg='black', bg='light blue', command=clearLastEntry , height=2, width=7)
    button1.grid(row=7, column=3, pady=(0,4), padx=(1,3))
    switch = tkinter.Button(window , text="switch" , font=("Arial", 15), fg='black', bg='light blue', command = switchBool, height=2, width=7)
    switch.grid(row=2, column=0, pady=(0,4), padx=(1,3))
    if switcher:
        button1 = tkinter.Button(window, text="x²", font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('sq'), height=2, width=7)
        button1.grid(row=2, column=1, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text="√x", font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('sqrt'), height=2, width=7)
        button1.grid(row=2, column=2, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text="1/x", font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('byOne'), height=2, width=7)
        button1.grid(row=2, column=3, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text="x^y", font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('^'), height=2, width=7)
        button1.grid(row=3, column=0, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text='*', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('*') , height=2, width=7)
        button1.grid(row=3, column=3, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text='/', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('/'), height=2, width=7)
        button1.grid(row=3, column=2, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text='mod', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('%'), height=2, width=7)
        button1.grid(row=3, column=1, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window , text='-', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('-'), height=2, width=7)
        button1.grid(row=4, column=3, pady=(0,4), padx=(1,3))
    else:
        button1 = tkinter.Button(window , text='π', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(3.14159265), height=2, width=7)
        button1.grid(row=4, column=3, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text="sin", font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('sin('), height=2, width=7)
        button1.grid(row=2, column=1, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text="cos", font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('cos('), height=2, width=7)
        button1.grid(row=2, column=2, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text="tan", font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('tan('), height=2, width=7)
        button1.grid(row=2, column=3, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text="log", font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('log('), height=2, width=7)
        button1.grid(row=3, column=0, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text='ln', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('ln('), height=2, width=7)
        button1.grid(row=3, column=1, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text='(', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression('(') , height=2, width=7)
        button1.grid(row=3, column=2, pady=(0,4), padx=(1,3))
        button1 = tkinter.Button(window, text=')', font=("Arial", 15), fg='black', bg='light blue', command=lambda: GenerateExpression(')') , height=2, width=7)
        button1.grid(row=3, column=3, pady=(0,4), padx=(1,3))

window.title('Calculator')
window.geometry('364x550')

if __name__ == '__main__':
    window.configure(background="#b5baba")
    equation = tkinter.StringVar()

    last_expression_str = tkinter.StringVar()
    last_expression = tkinter.Entry(window , textvariable = last_expression_str , font=("Arial", 18), justify='left', state='disabled')
    last_expression.grid(columnspan=10 , ipadx=46 , ipady= 20 , padx=(0,0) , pady=(2,0))

    field = tkinter.Entry(window , textvariable = equation , font=("Arial", 18), justify='right', state='disabled')
    field.grid(columnspan=10 , ipadx=46 , ipady= 20 , padx=(0,0) , pady=(1,4))

    drawButtons()
    window.mainloop()

