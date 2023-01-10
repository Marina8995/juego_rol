# Simula un juego en el que un usuario pelea contra el dragón. Ambos parten con 100 puntos de vida y se atacan entre ellos.
# Las acciones posibles son Atacar Curar y Defender. Atacar quita 10 puntos de vida, curar te da 5 puntos y defender evita que pierdas
# vida en el siguiente ataque del rival. El usuario seleccionará la acción mediante las opciones 1, 2 y 3. Y las acciones del dragón
# se determinaran aleatoriamente.

# Mejoras:
# - Mientras el usuario no seleccione una opcion valida no debe dejarle continuar
# - Los ataques del usuario fallaran un 30% de las veces
# - La vida del usuario y del dragon nunca puede superar 100 ni ser inferior a 0
# - 4 opcion: le cura la vida entera pero solo lo puede usar una vez
# - El ataque del dragon va a valer 30, pero falla un 40% 




import random

def turno_usuario(vida, veces_4): 
    print("\nTu turno")
    print("1. Atacar")
    print("2. Curar")
    print("3. Defender")
    print("4. Cura vida entera")
    usuario_opcion=int(input("Selecciona una opción: ") )   
    es_la_opcion_1 = usuario_opcion==1
    es_la_opcion_2 = usuario_opcion==2
    es_la_opcion_3 = usuario_opcion==3
    es_la_opcion_4 = usuario_opcion==4
    es_opcion_2_y_vida_100 = usuario_opcion==2 and vida>95
    es_opcion_4_y_ya_la_ha_usado = usuario_opcion == 4 and veces_4 >= 1
    es_opcion_4_y_vida_100 = usuario_opcion ==4 and vida==100


    while not (es_la_opcion_1 or es_la_opcion_2 or es_la_opcion_3 or es_la_opcion_4) or es_opcion_2_y_vida_100 or es_opcion_4_y_ya_la_ha_usado or es_opcion_4_y_vida_100:
        if es_opcion_2_y_vida_100:
            print("No puedes elegir la opción 'Curar' porque superarías los 100 puntos")
        elif es_opcion_4_y_ya_la_ha_usado:
            print("No puedes usar esta opción porque ya la has usado")
        elif es_opcion_4_y_vida_100:
            print("No puedes usar esta opción porque ya tienes los 100 puntos")     
        else:
            print("La opción introducida no es correcta")  

        usuario_opcion=int(input("Selecciona una opción: ") )  
        es_la_opcion_1 = usuario_opcion==1
        es_la_opcion_2 = usuario_opcion==2
        es_la_opcion_3 = usuario_opcion==3 
        es_la_opcion_4 = usuario_opcion==4
        es_opcion_2_y_vida_100 = usuario_opcion==2 and vida>95 
        es_opcion_4_y_ya_la_ha_usado = usuario_opcion == 4 and veces_4 >= 1
        es_opcion_4_y_vida_100 = usuario_opcion ==4 and vida==100

    return usuario_opcion

def turno_dragon(vida):
    if vida>95:
        dragon_opcion = random.choice([1,3])
    else:
        dragon_opcion = random.choice([1, 2, 3])    
      
        
    print(f"Elección del dragón: {dragon_opcion}")       

    return dragon_opcion


        

  

def play ():
    veces_opcion_4=0
    vida_usuario=100
    vida_dragon=100 
    dragon_opcion=None
    ataque_dragon=30
    ataque_usuario=10
    probabilidad_fallo_dragon=0.4
    probabilidad_fallo_usuario=0.3
    cura_dragon=5
    cura_usuario=5




    while vida_usuario>0 and vida_dragon>0:

        usuario_opcion=turno_usuario(vida_usuario, veces_opcion_4) #TURNO USUARIO
        if usuario_opcion==1:
            if random.random() > probabilidad_fallo_usuario: #Si no falla
                if dragon_opcion==3:  # Usuario ataca (1), dragón se defiende(3)
                    print("Has atacado (1) al dragón pero se ha defendido (3) y no le has hecho daño")
                else:    
                    vida_dragon-=ataque_usuario
                    print("Has atacado (1) al dragón y le has hecho daño")
            else: #Si falla
                print("Tu ataque ha fallado, no has hecho daño al dragón")        

        elif usuario_opcion==2:
            
            vida_usuario+=cura_usuario
            print("Te has curado (2) y has ganado 5 puntos")
            
        elif usuario_opcion==3:
            print("Te has defendido (3)")   

        # TODO: Hacer que el usuario no pierda el turno cuando seleccione opcion 4
        elif usuario_opcion==4:     
            print("Te has curado y tienes el 100% de vida")
            vida_usuario=100
            veces_opcion_4+=1

            


        print(f"El dragón tiene {vida_dragon} puntos de vida")

        if vida_dragon<=0:
            print("Has ganado")    
            break

        dragon_opcion=turno_dragon(vida_dragon)  #TURNO DRAGON
        if dragon_opcion==1: 
            if random.random() > probabilidad_fallo_dragon:  #Si no falla
                print("El dragón te ataca (1)")
                if usuario_opcion==3:
                    print("...pero no te ha hecho daño porque te defendiste (3)")  
                else:      
                    vida_usuario-=ataque_dragon
            else:  #Si falla
                print("El dragón ha fallado y no te ha hecho daño")        
            
        elif dragon_opcion==2:
            vida_dragon+=cura_dragon 
            print("El dragón se ha curado (2) y ha ganado 5 puntos") 
        elif dragon_opcion==3:
            print("El dragón se ha defendido (3)")

            print(f"El dragón tiene {vida_dragon} puntos de vida")

        print(f"Tienes {vida_usuario} puntos de vida")  
      


    if vida_usuario<=0:
        print("Has perdido")

  

play()



