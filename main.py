#colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#tiempo y random
import time
import random


iniciar_trivia = True #para que inicie
intento = 0 #contador de intentos


print("Bienvenido a mi trivia de superheroes")

time.sleep(1)

print("\nPara empezar, coloca tu nombre ")

nombre=input("\nCual estu nombre: ")


print("\nHola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

print("Recuerda que cada pregunta vale entre 4 a 6 puntos de forma aleatoria, cuando llegues a 30 habras ganado")

input("\nEnter para continuar\n")


while iniciar_trivia == True: #Para que vuelva iniciar si es el caso

  intento = intento + 1  #Le suma 1 al intento 

  spuntos = [] #Puse una listita de los numeros que van saliendo
  
  print(intento,"intento")
  
  print(MAGENTA+"\nPregunta 1:\n"+RESET) #tiene color
  
  print("¿Que animal le dio sus superpoderes a Spiderman?")
  
  time.sleep(1) #hace que pase 1 segundo y despues suelta lo de abajo
  
  print("a) Un perro")
  print("b) Un gato")
  print("c) Una araña ")
  print("d) Una lechuza")
  
  time.sleep(1/2)
  
  respuesta_1 = input("\nTu respuesta: ").lower()#Aqui pones tu respuesta con una letra
    
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input ("Debes responder a, b, c o d.\nIngresa nuevamente tu respuesta: ") #si la respuesta no es una de las letras de la pregunta hace un bucle para que la pongas correctamente
    
  if respuesta_1 == "a": #Si la respuesta es mala
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0) #Aqui agrega 0 puntos a la lista
  elif respuesta_1 == "b":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  elif respuesta_1 == "d":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  else:
    puntos1 = random.randint(4,6) #Le da un valor aleatorio entre 4 y 6 a puntos1
    spuntos.append(puntos1)  # Aqui agrega puntos1 a la lista
    print ("Muy bien", nombre,"!")
    print ("Ganaste", puntos1,"!")
  
  time.sleep(1)
  
  print("tienes" , sum(spuntos) ,"puntos") #esto imprime la suma de los puntos que tienes
  
  #pregunta 2
  print(MAGENTA+"\nPregunta 2:\n"+RESET)
  
  print("Superman es heroe mas conocido de DC , pero tambien es conocido con el nombre de: ")
  
  time.sleep(1)
  
  print("a) El hombre de lata")
  print("b) El caballero de los mares")
  print("c) Agila con dientes ")
  print("d) El hombre de acero")
  
  time.sleep(1/2)
  
  respuesta_2 = input("\nTu respuesta: ").lower()
  
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input ("Debes responder a, b, c o d.\nIngresa nuevamente tu respuesta: ")
  if respuesta_2 == "a":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  elif respuesta_2 == "b":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  elif respuesta_2 == "c":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  else:
    puntos2 = random.randint(4,6)
    spuntos.append(puntos2)
    print ("Muy bien", nombre,"!")
    print ("Ganaste", puntos2,"!")
  
  time.sleep(1)
  
  print("\ntienes" , sum(spuntos) ,"puntos")
  
  #pregunta 3
  print(MAGENTA+"\nPregunta 3:\n"+RESET)
  
  print("La mayoria de super heroes tienen un compañero, ¿Como se llama el compañero de batman?")
  
  time.sleep(1)
  
  print("a) Miguelito 'El Enano'")
  print("b) Khaterine 'Batwoman'")
  print("c) Alfred 'El gato' ")
  print("d) 'b' y 'c' ")
  
  time.sleep(1/2)
  
  respuesta_3 = input("\nTu respuesta: ").lower()
  
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d.\nIngresa nuevamente tu respuesta: ")
  if respuesta_3 == "a":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  elif respuesta_3 == "b":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  elif respuesta_3 == "c":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  else:
    puntos3 = random.randint(4,6)
    spuntos.append(puntos3)
    print ("Muy bien", nombre,"!")
    print ("Ganaste", puntos3,"!")
  time.sleep(1)
  
  print("\ntienes" , sum(spuntos) ,"puntos")
 
  #pregunta 4 
  print(MAGENTA+"\nPregunta 4:\n"+RESET)
  
  print("Los aviones son muy populares en los comics, ¿Que tipo de avion teniene la mujer maravilla")
  
  time.sleep(1)
  
  print("a) Avion invisible")
  print("b) Avion sin pintura")
  print("c) No tenia avion , viajaba en autobus ")
  print("d) Jet privado")
  
  time.sleep(1/2)
  
  respuesta_4 = input("\nTu respuesta: ").lower()
  
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input ("Debes responder a, b, c o d.\nIngresa nuevamente tu respuesta: ")
    time.sleep(1)
  if respuesta_4 == "b":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  elif respuesta_4 == "c":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  elif respuesta_4 == "d":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  else:
    puntos4 = random.randint(4,6)
    spuntos.append(puntos4)
    print ("Muy bien", nombre,"!")
    print ("Ganaste", puntos4,"!")
  
  time.sleep(1/2)
  
  print("\ntienes" , sum(spuntos) ,"puntos")
  
    
  #pregunta 5 tiene respuesta secreta
  print(MAGENTA+"\nPregunta 5:\n"+RESET)
  
  print("El profesor Charles Xavier fundo un grupo de mutante, ¿Como se llamaban? ")
  
  time.sleep(1)
  
  print("a) Los Mutantosos")
  print("b) X-men ")
  print("c) Factor-Mutante ")
  print("d) Unicos y diferentes")
  
  time.sleep(1/2)
  
  respuesta_5 = input("\nTu respuesta: ").lower()
  
  while respuesta_5 not in ("a", "b", "c", "d","x"):#Aqui le agrege x para que se pueda ver
    respuesta_5 = input ("Debes responder a, b, c o d.\nIngresa nuevamente tu respuesta: ")
  if respuesta_5 == "a":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  elif respuesta_5 == "c":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  elif respuesta_5 == "d":
    print ("Incorrecto!\nNo ganas puntos\n")
    spuntos.append(0)
  elif respuesta_5 == "x": #esta es la respuesta secreta ,pero no es correcta
    spuntos.append(0)
    time.sleep(5)
    print (YELLOW+"Sos un grande flaco , pero no la respuesta :'("+RESET)
  else:
    puntos5 = random.randint(4,6)
    spuntos.append(puntos5)
    print ("Muy bien", nombre,"!")
    print ("Ganaste", puntos5,"!")

  time.sleep(1/2)
    
  print("\ntienes" , sum(spuntos) ,"puntos")

  #pregunta 6 pregunta que duplica o divide puntos

  time.sleep(1)
  
  print(CYAN+"\nEsta pregunta va duplicar o dividir tus puntos dependiendo de tu respuesta!!\n"+RESET)

  input("Enter para continuar")
  
  print(MAGENTA+"\nPregunta 6:\n"+RESET)
  
  print("¿Quien dijo?: Un gran poder conlleva una gran responsabilidad")
  
  time.sleep(1)
  
  print("a) Grut ")
  print("b) El tio Ben ")
  print("c) Ben 10 ")
  print("d) Quiksilver")
  
  time.sleep(1/2)
  
  respuesta_6 = input("\nTu respuesta: ").lower()#Dar una respuesta equivocada te quita la mitad de tus puntos
  
  while respuesta_6 not in ("a", "b", "c", "d"):
    respuesta_6 = input ("Debes responder a, b, c o d.\nIngresa nuevamente tu respuesta: ")
  if respuesta_6 == "a":
    print ("Incorrecto!\nPerdiste la mitad de tus puntos\n")
    total=sum(spuntos)/2#Responder mal la pregunta te quita la mitad de tus puntos 
  elif respuesta_6 == "c":
    print ("Incorrecto!\nPerdiste la mitad de tus puntos\n")
    total=sum(spuntos)/2
  elif respuesta_6 == "d":
    print ("Incorrecto!\nPerdiste la mitad de tus puntos\n")
    total=sum(spuntos)/2#devueklve un float
  else:
    total=sum(spuntos)*2#Responderla bien te duplica los puntos
    print ("Muy bien", nombre,"!")
    print ("Duplicaste tus puntos\n")#Devuelve un int

  if respuesta_6 == "a" or "d":#esto lo busque en internet el "or"
    print("Pregunta 1: ",spuntos[0],"\nPregunta 2: ",spuntos[1],"\nPregunta 3: ",spuntos[2],"\nPregunta 4: ",spuntos[3] ,"\nPregunta 5: ",spuntos[4] , "\nY divistes la totalidad de tus puntos")#Aca te muesta la lista y al final que dividiste tus puntos
  elif respuesta_6 == "c":
    print("Pregunta 1: ",spuntos[0],"\nPregunta 2: ",spuntos[1],"\nPregunta 3: ",spuntos[2],"\nPregunta 4: ",spuntos[3] ,"\nPregunta 5: ",spuntos[4] , "\nY divistes la totalidad de tus puntos")
    
  else:
    print("Pregunta 1: ",spuntos[0],"\nPregunta 2: ",spuntos[1],"\nPregunta 3: ",spuntos[2],"\nPregunta 4: ",spuntos[3] ,"\nPregunta 5: ",spuntos[4] , "\nY multiplicaste la totalidad de tus puntos")

  time.sleep(1)

  if total >= 30: #Si sacaste mas de 30 o mas puntos ganas 
    print(GREEN+nombre ,"ganas loquito")
    print("Conseguiste: ",total,"puntos"+RESET)
  else:   #Y si no sacas mas de 30 pierdes :'(
    print(RED+"perdiste",nombre,"podrias volver a intentarlo")
    print("solo llegaste a " , total,"puntos"+RESET) 
  
    print("\n¿Deseas intentar la trivia nuevamente?\n")#Te pregunta si quieres repetir la trivia
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()#Ingresas tu respuesta
  
  if repetir_trivia != "si": #Escribir 'si' repetira la trivia

    print("\nEspero",nombre,"que lo hayas pasado bien, hasta pronto!")
    iniciar_trivia = False #Si escribiste cualquier otra cosa se acabara la trivia pero antes de pondra el mensajito de arriba 
    
  

  
  

