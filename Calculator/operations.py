def GenerateExpression(expression, num, equation):
    if len(expression) == 1:
        if expression[0] == '0' and str(num) == '.':
            expression = '0.'
            equation.set(expression)
            return
        elif expression[0] == '0':
            expression = str(num)
            equation.set(expression)
            return
    operations = ['+', '-', '/', '*']
    if len(expression) >= 2:
        if expression[-2] in operations:
            if expression[-1] == '0':
                if str(num) != '.':
                    expression = expression[:-1] + str(num)
                    equation.set(expression)
                    return
    if len(expression) >= 1:
        if expression[-1] == '.' and str(num) == '.':
            return
    expression += str(num)
    equation.set(expression)


def clearLastEntryInExpression(expression, equation):
    expression = expression[:-1]
    equation.set(expression)


def PressedEqual(expression, equation, last_expression_str):
    try:
        res = str(eval(expression))
        last_expression_str.set(expression)
        equation.set(res)
        expression = str(res)
    except:
        equation.set("Error Occured")
        last_expression_str.set("")
        expression = ""


def clear(expression, equation, last_expression_str):
    expression = ""
    equation.set("")
    last_expression_str.set("")

