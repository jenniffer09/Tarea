from ast import Try
from optparse import Option
from ssl import Options
from unittest import FunctionTestCase
from Menu import principal
import time
import os
os.system("cls")
var = principal()
lis = ["1)Vid_3","2)Vid_4","3)Vid_5","4)Vid_6","5)Vid_7","6)Vid_8","7)Vid_9","8) Vid_10","9)Vid_11","10)Vid_12","11)Vid_13","12)Vid_14","13)Vid_15","14)Vid_16","15)Vid_17","16)Vid_18","17)Vid_19","18)Vid_20","19)Vid_21","20)Vid_22","21)Vid_23","22)Vid_24","23)Vid_25","24)Vid_26","25)Vid_27","26)Vid_28","27)Vid_2 ",]
opcion = ""
while opcion != "39":
    os.system("cls")
    opcion = var.menu(lis)
    os.system("cls")
    if opcion == "1": 
        print ("Hola Mundo")
        time.sleep(1)
    elif opcion== "2":
        os.system("cls")
        Nombre = "Bryan Piedra"
        print (Nombre) 
        edad=25
        print (edad)
        edad= True
        print (edad)
        sueldo= 205.10
        print (sueldo)
        time.sleep(2)
    elif opcion == "3": 
        os.system("cls") 
        numero1 ="35"
        numero2 ="18"
        print (numero1 + numero2)
        num1 = int (numero1) 
        num2 = int (numero2)
        print (numero1 + numero2)
        sueldo = 1200.43
        sueldoEntero= int (sueldo)
        print (sueldoEntero)
        valor = "450.89"
        ValorDecimal =float (valor)
        print (ValorDecimal*3)
        edad=100
        print(len(str(edad)))
        time.sleep(1)
    elif opcion == "4":
        os.system("cls")
        entero=23
        decimal=31.78
        complejo=12+5j
        # Booleano= True
        """
        Print (entero)
        print (decimal)
        print (boleano)
        """

        num1 =20
        num2 = 4
        print("suma:", (num1+ num2))
        print("resta:", (num1- num2))
        print("multiplicacion:", (num1* num2))
        print("Division:", (num1/ num2))
        print("division exacta:", (num1// num2))
        print("Potencia:", (num1** num2))
        time.sleep(1)
    elif opcion == "5":
        os.system("cls")
        texto1 ="Hola"
        texto2 ="Mundo"
        textoFinal = texto1 + "" + texto2
        print (textoFinal)

        print("El saludo es: %s %s" % (texto1, texto2))

        SaludoFinal="saludo:{0} {1}".format (texto1, texto2)
        print (SaludoFinal)
        saludoFina12="saludo:(x) (y)".format (x=texto1, y=texto2)
        print (saludoFina12)
        time.sleep(1)
    elif opcion == "6":
        os.system("cls")
        texto = "bienveNIdos al canal de uskokrum2010"
        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title()) # Convierte una cadena a un formato de título.
        print(texto.find("al")) # Posición donde encuentra la cadena o porción.
        print(texto.count("e")) # Cantidad de ocurrencias de una letra o porción.

        textoFinal = texto.replace("e", "3")
        print(textoFinal)
        valor = texto.isnumeric() # Arroja true o false dependiendo si es un número.
        print(valor)
        cadenaSeparada = texto.split(" ")
        print(cadenaSeparada)
        time.sleep(1)
    
                    

    elif opcion == "7":
        os.system("cls")
    
        tupla= (1,2,3)
        print (tupla)
        tupla2 =(7, "oscar,true 4,50.1, 16+ 7j ,15,""felicidad,false")
        print (tupla)
        tupla3 =(9,3,4,5,6)
        print (tupla)
        print (tupla2 [1])
 
        print(tupla2[-1]) #Acceder al
        print (tupla2[0:4])
        print(tupla2[-2])

        a,b,c = tupla
        print (a)
        print (b)
        print (c)

        tuplafinal=tupla+tupla3
        print (tuplafinal)

        print (tuplafinal.count(21))
        print (tuplafinal.index(3))
        time.sleep(1)

    elif opcion=="8":

        os.system("cls")
        # Listas: Son estructuras de datos que nos permiten almacenar distintos valores
        # (equivalentes a los arrays en otros lenguajes de programación)

        # Son estructuras dinámicas, pueden MUTAR.        

        lista1 = ["Oscar", 25, 98.3, True, "Flavio", 56.3]
        print(lista1)
        print(lista1[:])
        print(lista1[2])
        print(lista1[-1])

        print(lista1[0:3])
        print(lista1[:2])        
        print(lista1[3:])

        lista1.append("UskoKruM2010")
        print(lista1)

        lista1.insert(4, "Perú")
        print(lista1)

        lista1.extend(["Alejandro", 110, False])
        print(lista1)

        print(lista1.index("Flavio"))

        lista1.remove(56.3)
        print(lista1)

        lista1.pop()
        print(lista1)

        lista2 = ["Chiclayo", "Irma"]
        lista3 = lista1 + lista2
        print(lista3)

        print(lista2 * 4)

        print("UskoKruM2010" in lista1)
        time.sleep(1)
    
    
    elif opcion == "9":

        os.system("cls")
        # Diccionarios: Son estructuras de datos que nos permiten almacenar distintos
        # valores.        

        # Es que los datos se almacenan asociados a una clave única, tenemos una relación
        # clave:valor

        # Los elementos almacenados están en desorden, el orden es indiferente a la forma
        # de almacenamiento.

        miDiccionario = {"España": "Madrid", "Perú": "Lima", "Alemania": "Berlín"}
        print(miDiccionario["Perú"])
        print(miDiccionario)

        miDiccionario["Venezuela"] = "Caracas"
        print(miDiccionario)

        miDiccionario["España"] = "Barcelona"
        print(miDiccionario)

        del miDiccionario["España"]
        print(miDiccionario)

        dic2 = {"García": "Oscar", 25: True, "Sueldo": 150.80}
        print(dic2[25])

        llaves = ("España", "Francia", "Inglaterra")
        dicPaises = {llaves[0]: "Madrid", llaves[1]: "París", llaves[2]: "Londres"}
        print(dicPaises)

        datosPersonales = {"Ape": "García", "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
        print(datosPersonales)
        print(datosPersonales["Anios"])

        print(datosPersonales.get('Apel', "Oscar"))

        print(datosPersonales.keys())
        valores = tuple(datosPersonales.values())
        print(valores)
        time.sleep (1)


    elif opcion == "10":
        os.system ("cls")
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        sueldo = float(input("Ingrese su sueldo: "))
        print("Hola, " + nombre)
        edadFutura = edad + 20
        print("Tu edad es:", edad)
        print("Tu edad (dentro de 20 años) será:", edadFutura)
        print("Tu sueldo es:", sueldo)
        time.sleep(1)

    elif opcion == "11":

        os.system("cls")
        edad=int(input ("Ingrese su edad:"))
        if edad >=18:

         print("Eres Mayor de edad.")
        elif edad==18:

         print("Tienes 18 años!")

        else:

         print("No eres mayor de edad.")
        time.sleep(1)

 

    elif opcion == "12":

        os.system("cls")

        def saludar():

            print("García")

            print("Oscar")

            print("UskoKruM2010")
            return "Hola"
        print(saludar())
        def evaluarSueldoMinimo(sueldo):

            if sueldo >= 850:
                print("Cumples con el sueldo")
            else:
                print("Ganas menos que el sueldo mínimo")
                evaluarSueldoMinimo(100)
        time.sleep(1)

    elif opcion=="13":
       os.system("cls")
    
       #AND: EQUIVALENTE A " SI ADEMAS.."
       # OR:"O SINO.."
       #NOT-Negacion.
       distancia=1200
       numerohermanos=2
       salarioPadres=1500
       tieneBeneficio=False
       if(distancia >100 and numerohermanos>2)or salarioPadres:
        tieneBeneficio=True
        print(not tieneBeneficio)
        if (5>3) and (8 < 6):
         print("Verdad")
        else:      
         print("Es mentira")
         time.sleep(1)

    elif opcion=="14":
      os.system("cls")
      """
      String sexo;
      sexo = (10 > 20) ? "Masculino" : "Femenino";
      """
      sexos = ("Hombre", "Mujer")
      posicion = True
      sexo = sexos[posicion] # Mujer
      print(sexo)
      sexo = sexos[not posicion] # Hombre
      print(sexo)
      time.sleep(1)

    elif opcion=="15":
      os.system("cls")
      # range(): Crea una lista inmutable de números enteros en sucesión aritmética.
      numeros = range(5)  # [0, 1, 2, 3, 4]
      print(numeros[1])
      numeros1 = range(4, 10)  # [4, 5, 6, 7, 8, 9]
      print(numeros1[5])
      numeros2 = range(10, 100, 8)
      print(numeros2[9])  # [10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98 
      time.sleep(1)
    elif opcion=="16":
      os.system("cls")
      # Bucles: Son estructuras de control de flujo que repiten 1 o varias líneas de código.
      #for num in range(0, 20, 2):
      # #print("Valor actual: {0}".format(num))
      for i in range(1, 13):

        print("{0} x {1} es: {2}".format(i, i, (i * i)))
        for nom in ["Karen", "Oscar", "Héctor", "Leonardo"]:
         print("Cantidad de letras de {0} es: {1}".format(nom, len(nom)))
        time.sleep(1)
    elif opcion=="17":
        os.system("cls")
        print("-- Cursos --")
        print("Matematica - Biologia - Lenguaje - Ciencias")

        curso = input("Ingrese el curso deseado: ")

        if curso in ("Matematica", "Biologia", "Lenguaje", "Ciencias"):
         print("Curso {0} seleccionado.".format(curso))
        else:
         print("No existe ese curso...")
         time.sleep(1)
    elif opcion=="18":
        os.system("cls")
        # Factorial: Es el producto de todos los números positivos enteros comprendidos entre 1 y un número.
        # Factorial de 5: 1 * 2 * 3 * 4 * 5 = 12
        # Factorial de 4: 1 * 2 * 3 * 4 = 24
        numero = int(input("Ingrese un número: "))
        factorial = 1
        for n in range(1, (numero + 1)):
            factorial = factorial * n
            print("El factorial de {0} es: {1}".format(numero, factorial))
            time.sleep(1)

    elif opcion=="19":
        os.system("cls")
        # While: Estructura repetitiva que nos permite realizar múltiples iteraciones
        # basándonos en el resultado de una expresión lógica que puede
        # tener como resultado un valor True o False.

        """
        indice = 1
        while indice < 10:
        print("Valor actual: {0}".format(indice))
        indice = indice + 1
        print("Hemos terminado el bucle while.")
        # Continua el programa.
        """

        inicio = 2
        while inicio <= 100:
            print("Número par: {0}".format(inicio))
            inicio += 2
            print("Hemos terminado el bucle while.")
            time.sleep(1)


    elif opcion=="20":
        os.system("cls")
        # Break: Permite salir de un bucle cuando se cumple una condición.

        """
        for numero in range(1, 6):
        if numero == 3:
        break  # Descanso o interrupción en este punto.
        print("El número es: {0}".format(numero))
        print("Bucle terminado.")
        """

         # Continue: Omite una parte del bucle cuando se cumple una condición y
         # continúa con el resto.

        """
        for numero in range(1, 6):
        if numero == 3:
        continue  # Continúa con el resto del bucle.
        print("El número es: {0}".format(numero))
        print("Bucle terminado.")
        """
        # Pass: Permite continuar con una sentencia o función que ya no tiene
        # o aún no tiene un bloque de código útil.
        for numero in range(1, 6):
            if numero <= 3:
        # Aquí no pasa nada y el bucle sigue trabajando.
             pass
        else:
          print("El siguiente valor es mayor a 3:")
          print("El número es: {0}".format(numero))
          print("Bucle terminado.")
          def funcionSinImplementar():
           pass
        time.sleep(1)

    elif opcion=="21":
        os.system("cls")
        # Generadores: Permiten extraer valores de una función y almacenarlo
# (de uno en uno) en objetos iterables (que se pueden recorrer),
# sin la necesidad de almacenar TODOS A LA VEZ en la memoria RAM.

        """
        def generaMultiplos7(limite):
        numero = 1
        listaNumeros = []
        while numero <= limite:
        listaNumeros.append(numero * 7)
        numero = numero + 1
        return listaNumeros  # Retorna toda la lista creada.
        print(generaMultiplos7(10))
        """
        def generadorMultiplos7(limite):

            numero = 1
            while numero <= limite:
                yield numero * 7  # Ceder. La instrucción "yield" genera un objeto iterable.
                numero = numero + 1
        obtieneMultiplos7 = generadorMultiplos7(10)
        """
         print(obtieneMultiplos7)
        for n in obtieneMultiplos7:
        print(n)
        """
        # next(): Retorna el siguiente elemento de un objeto iterable:
        print(next(obtieneMultiplos7))
        print("Acá hay 300 líneas de código...")
        print(next(obtieneMultiplos7))
        print("Acá hay 1000 líneas de código...")
        print(next(obtieneMultiplos7))

        # Son más eficiente que las funciones tradicionales.
        # Muy útiles con listas de valores infinitos.
        # Entre llamada y llamada, el objeto iterable entra en un estado de pausa (suspensión).
        time.sleep(1)

    elif opcion=="22":
        os.system("cls")
        # Cuando indicamos un * adelante del parámetros de una función,
        # estamos indicado que se va a recibir un número indeterminado
        # de parámetros. Además, esos parámetros se recibirán en forma de tupla.

        """
        def devuelveLenguajes(*lenguajes):
        for leng in lenguajes:
        yield leng
        """
        def devuelveLenguajes(*lenguajes):
         for leng in lenguajes:
          yield from leng
        lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        time.sleep(1)
    elif opcion=="23":
        os.system("cls")
        # Excepción: Error en tiempo de ejecución (durante la ejecución de un programa).
        numero1 = 20
        numero2 = 2

        # print("La división de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))
        try:
            resultado = numero1 / numero2
            # except:
        except ZeroDivisionError:
         print("No se puede dividir entre 0...")
        finally:
            print("Yo siempre aparezco.")
            print("Aquí termina mi programa.")
            time.sleep(1)

    elif Option=="24":
     os.system("cls")
     def evaluarNota(nota):
      if nota < 0:
        raise ValueError("Valor incorrecto...")
      elif nota >= 16:
        print("Excelente")
      elif nota >= 11:
        print("Aprobado")
      else:
        print("Desaprobado")
        evaluarNota(-7)
        print("Este es el fin de mi programa.")
        time.sleep(1)

    elif Option=="25":
           os.system("cls")
           from modulos.funciones_matematicas  import multiplicar, sumar
           print(sumar(5, 6))
           print(multiplicar(5, 6))
           time.sleep(1)
    
    elif Options=="26":
        os.system("cls")
        class Persona():
            apellidos = ""
            nombres = ""
            edad = 0
            despierta = False
            def despertar(self):
                self.despierta = True
                print("Buen día.")
            persona1 = Persona()
            persona1.apellidos = "García Fuentes"
            print(persona1.apellidos)
            persona1.despertar()
            print(persona1.despierta)
            persona2 = Persona()
            persona2.apellidos = "Paz Torres"
            print(persona2.apellidos)
            print(persona2.despierta)
            time.sleep(1)

   




      
