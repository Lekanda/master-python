class Calculadora:
    __lista__ = []
 
    def sumar(self, num1, num2):
        return num1+num2
 
    def restar(self, num1, num2):
       return num1-num2
 
    def multiplicar(self, num1, num2):
        return num1*num2
 
    def dividir(self, num1, num2):
        return num1/num2
 
    def agregar(self, entrada):
        self.__lista__.append(entrada)
 
    def calcular(self):
        try:
            calculo = self.__lista__[0]
            for i in range(1,len(self.__lista__)-1):
                #El ceroesimo elemento lo uso para inicializar calculo, por eso comienzo de uno en el rango
                #No hago len(__lista__)) porque necesito que termine antes
                operacion = self.__lista__[i]
                otroValor = self.__lista__[i+1]
                if operacion == 'sumar':
                    calculo = self.sumar(float(calculo), float(otroValor))
                elif operacion == 'restar':
                    calculo =  self.restar(float(calculo), float(otroValor))
                elif operacion == 'multiplicar':
                    calculo = self.multiplicar(float(calculo), float(otroValor))
                elif operacion == 'dividir':
                    calculo = self.dividir(float(calculo), float(otroValor))
                if i==len(self.__lista__):
                    break #salgo antes que llegue al final de la lista porque i+1 no va a existir
            print(f"Lista: {self.__lista__}")
            print(f"resultado: {calculo}")
            print("************ FIN Operacion ***************")
        except:
            calculo = "Error"
        self.__lista__=[] #borro la lista para poder comenzar con otro calculo
        return calculo