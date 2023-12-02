import re
import math

def cleanExpression(expression):
    foundSin = re.search(r'sin\(\d+\)', expression)
    foundCos = re.search(r'cos\(\d+\)', expression)
    foundTan = re.search(r'tan\(\d+\)', expression)
    foundLog = re.search(r'log\(\d+\)', expression)
    foundLn = re.search(r'ln\(\d+\)', expression)
    foundSq = re.search(r'\b\d+sq\b' , expression)
    foundSqr = re.search(r'\b\d+sqrt\b' , expression)
    foundByOne = re.search(r'\b\d+byOne\b' , expression)
    foundRaise = re.search(r'\b\d+\^\d+[+\-*/]\b', expression)
    if foundSin:
        expression = expression[:foundSin.start()] + calSin(expression[foundSin.start():foundSin.end()+1]) + expression[foundSin.end()+1:]
    if foundCos:
        expression = expression[:foundCos.start()] + calCos(expression[foundCos.start():foundCos.end()+1]) + expression[foundCos.end()+1:]
    if foundTan:
        x = calTan(expression[foundTan.start():foundTan.end()+1])
        if x == 'Infinity':
           return 'Infinity' 
        expression = expression[:foundTan.start()] + x + expression[foundTan.end()+1:]
    if foundLog:
        expression = expression[:foundLog.start()] + str(calLog(expression[foundLog.start():foundLog.end()+1])) + expression[foundLog.end()+1:]    
    if foundLn:
        expression = expression[:foundLn.start()] + calLn(expression[foundLn.start():foundLn.end()+1]) + expression[foundLn.end()+1:] 
    if foundSq:
        expression = expression[:foundSq.start()] + str(calSq(expression[foundSq.start():foundSq.end()+1])) + expression[foundSq.end()+1:] 
    if foundSqr:
        expression = expression[:foundSqr.start()] + str(calSqr(expression[foundSqr.start():foundSqr.end()+1])) + expression[foundSqr.end()+1:] 
    if foundByOne:
        expression = expression[:foundByOne.start()] + str(calByOne(expression[foundByOne.start():foundByOne.end()+1])) + expression[foundByOne.end()+1:] 
    if foundRaise:
        expression = expression[:foundRaise.start()] + str(calRaise(expression[foundRaise.start():foundRaise.end()+1])) + expression[foundRaise.end()+1:] 
    return expression

def calSin(expression):
    angle = expression[expression.index("(")+1:expression.index(")")]
    angleRad = math.radians(int(angle))
    return str(math.sin(angleRad))

def calCos(expression):
    angle = expression[expression.index("(")+1:expression.index(")")]
    angleRad = math.radians(int(angle))
    return str(math.cos(angleRad))

def calTan(expression):
    angle = expression[expression.index("(")+1:expression.index(")")]
    if angle == '90':
        return 'Infinity'
    angleRad = math.radians(int(angle))
    return str(math.tan(angleRad))

def calLog(expression):
    val = expression[expression.index("(")+1:expression.index(")")]
    return math.log10(int(val))

def calLn(expression):
    val = expression[expression.index("(")+1:expression.index(")")]
    return str(math.log(int(val)))

def calSq(expression):
    val = expression[:expression.index("s")]
    return math.pow(int(val),2)

def calSqr(expression):
    val = expression[:expression.index("s")]
    return math.sqrt(int(val))

def calByOne(expression):
    val = expression[:expression.index("b")]
    return math.pow(int(val),-1)

def calRaise(expression):
    val1 = expression[:expression.index("^")]
    val2 = expression[expression.index("^")+1:]
    return math.pow(int(val1),int(val2))