
def holaMundo (nombre):
    return f"hola: {nombre}"

def calculadora(num1,num2,ope):
    if ope == "+" :
        resultado=num1+num2
        return(resultado)
    elif ope=="-":
        resultado=num1-num2
        return(resultado)
    elif ope=="*":
        resultado=num1*num2
        return(resultado)
    elif ope=="/":
        resultado=num1/num2
        return(resultado)
