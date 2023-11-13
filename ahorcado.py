#se importan las siguientes librerias
import random
import string

#se importa el modulo y el nombre de la variable que se va a importar
from palabras import palabras
#importar el diagrama de vidas
from diagrama_ahorcado import vidas_diccionario_visual

#de esta funcion es para obtener una palabra valida de la lista
def obtener_palabra_valida(palabras):
    #Seleccionar una palabra al azar de la lista
    #de palabras validas
    palabra = random.choice(palabras)

    #verificar los caracteres introducidos por el usuario
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    #la retorna en mayusculas
    return palabra.upper()

#se crea una funcion de bienvenida
def ahorcado():
    print("====================================")
    print(" ¡Bienvenido al juego del ahorcado! ")
    print("====================================")
    
    #se busca la palabra de una lista de palabras validas
    palabra = obtener_palabra_valida(palabras)
    
    #se separan las letras por conjunto
    letras_por_adivinar = set(palabra)
    
    #se importan todas las letras del abecedario en mayusculas
    abecedario = set(string.ascii_uppercase)
    
    #se crea un conjunto vacio 
    letras_adivinadas = set()
    
    #las vidas del juego
    vidas = 7
    
    #un bucle que dice las letras usadas y las vidas del usuario
    while len(letras_por_adivinar) > 0 and vidas > 0:
        #Letras adivinadas
        # ' '.join({'A','B','C'}) -> 'A B C'
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
        
        #mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        #mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        #mostrar las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        letra_usuario = input("Escoge una letra: ").upper()        
        
        #si la letra que escribio el usuario esta en el abecedario y no en el conjunto de letras que ya se ingresaron,se añade la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            #si la letra esta en la palabra
            #quitar la letra del conjunto de letras pendientes por adivinar sino,quitar una vida al usuario
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\n tu letra, {letra_usuario} no esta en la palabra.")
        #si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra,Escoge una nueva letra.")
        else:
            print("\nEsta letra no es valida.")            
    #El juego llega a esta linea cuando se adivinan todas las letras de la palabra o cuando se agotan las vidas del usuario
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado!,Perdiste,la palabra era: {palabra}")
    else:
        print(f"¡Haz ganado!¡Adivinaste la palabra {palabra}!")                         

ahorcado()
            
            
            