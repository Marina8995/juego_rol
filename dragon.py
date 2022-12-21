# Simula un juego en el que un usuario pelea contra el dragón. Ambos parten con 100 puntos de vida y se atacan entre ellos.
# Las acciones posibles son Atacar Curar y Defender. Atacar quita 10 puntos de vida, curar te da 5 puntos y defender evita que pierdas
# vida en el siguiente ataque del rival. El usuario seleccionará la acción mediante las opciones 1, 2 y 3. Y las acciones del dragón
# se determinaran aleatoriamente.

# Mejoras:
# - Mientras el usuario no seleccione una opcion valida no debe dejarle continuar
# - Los ataques fallaran un 30% de las veces
# - La vida del usuario y del dragon nunca puede superar 100 ni ser inferior a 0
# - 4 opcion: le cura la vida entera pero solo lo puede usar una vez (para el usuario). 
# - El ataque del dragon va a valer 30, pero falla un 40% (siempre)
# - Comentar el codigo
# - Ser capaz de extraer algun codigo en una nueva funcion 



import random

def turno_usuario(vida): # Se puede llamar como quiera ()
    print("\nTu turno")
    print("1. Atacar")
    print("2. Curar")
    print("3. Defender")
    usuario_opcion=int(input("Selecciona una opción: ") )   
    no_es_opcion_1=usuario_opcion!=1
    no_es_opcion_2=usuario_opcion!=2
    no_es_opcion_3=usuario_opcion!=3
    es_opcion_2_y_vida_100=usuario_opcion==2 and vida>95


    while no_es_opcion_1 and no_es_opcion_2 and no_es_opcion_3 or es_opcion_2_y_vida_100:
        if es_opcion_2_y_vida_100:
            print("No puedes elegir la opción 'Curar' porque superarías los 100 puntos")
        else:    
            print("La opción introducida no es correcta")
        usuario_opcion=int(input("Selecciona una opción: ") )  
        no_es_opcion_1=usuario_opcion!=1
        no_es_opcion_2=usuario_opcion!=2
        no_es_opcion_3=usuario_opcion!=3
        es_opcion_2_y_vida_100=usuario_opcion==2 and vida>95 
    return usuario_opcion

def turno_dragon(vida):
    numero_aleatorio = random.randint(1, 3)   
    es_opcion_2_y_vida_100=numero_aleatorio==2 and vida>95

    while es_opcion_2_y_vida_100:
        numero_aleatorio = random.randint(1, 2)
        numero_aleatorio+=1
    else:
         numero_aleatorio = random.randint(1, 3)   

        
        

    print(f"Elección del dragón: {numero_aleatorio}")       

    return numero_aleatorio

def play ():
    vida_usuario=100
    vida_dragon=100 
    dragon_opcion=None



    while vida_usuario>0 and vida_dragon>0:

        usuario_opcion=turno_usuario(vida_usuario) #TURNO USUARIO
        if usuario_opcion==1:
            if dragon_opcion==3:  # Usuario ataca (1), dragón se defiende(3)
                print("Has atacado (1) al dragón pero se ha defendido (3) y no le has hecho daño")
            else:    
                vida_dragon-=10
                print("Has atacado (1) al dragón y le has hecho daño")
        elif usuario_opcion==2:
            if vida_usuario<100:
                vida_usuario+=5
                print("Te has curado (2) y has ganado 5 puntos")
            
        elif usuario_opcion==3:
            print("Te has defendido (3)")    

        print(f"El dragón tiene {vida_dragon} puntos de vida")

        if vida_dragon<=0:
            break

        dragon_opcion=turno_dragon()  #TURNO DRAGON
        if dragon_opcion==1: 
            print("El dragón te ataca (1)")
            if usuario_opcion==3:
                print("...pero no te ha hecho daño porque te defendiste (3)")  
            else:      
                vida_usuario-=10
        
        elif dragon_opcion==2:
            vida_dragon+=5   
            print("El dragón se ha curado (2) y ha ganado 5 puntos") 
        elif dragon_opcion==3:
            print("El dragón se ha defendido (3)")

            print(f"El dragón tiene {vida_dragon} puntos de vida")

        print(f"Tienes {vida_usuario} puntos de vida")  
      


    if vida_usuario<=0:
        print("Has perdido")

    if vida_dragon<=0:
        print("Has ganado")    

play()