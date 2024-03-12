
#torneo 

puntos1 = 0
puntos2 = 0
puntos3 = 0

contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0


controlBln = True
while controlBln:
    opcion = int(input('>>>>>>OPCIONES<<<<<<<< \n1. equipo1 \n2. equipo2 \n3. equipo3  \n4. equipo4 \n5. salir \n\opcion es ->  '))
    if opcion <1 or opcion >5 :
        print ('ejecucion invalida ')
    if opcion == 1:
        print  (' equipo 1')
        opcion2 = int(input('>>>>>>OPCIONES<<<<< \n1. lanza_falta  \n2. lanza_fuera \n3. lanza_bomba \n\opcion es -> '))
        if opcion2 <1 or opcion2 > 3:
            print ('error, intentelo de nuevo')
        if opcion2 == 1:
            puntos1 = 1
        if opcion2 == 2: 
            puntos2 = 3
        if opcion2 == 3:
            puntos3 = 2
        contador1 = (puntos1 + puntos2 + puntos3)
    if opcion == 2:
        print('equipo 2')
        opcion3 = int(input('>>>>>>OPCIONES<<<<< \n1. lanza_falta  \n2. lanza_fuera \n3. lanza_bomba \n\opcion es -> '))
        if opcion3 <1 or opcion2 > 3:
            print ('error, intentelo de nuevo')
        if opcion3 == 1:
            puntos1 = 1
        if opcion3 == 2: 
            puntos2 = 3
        if opcion3 == 3:
            puntos3 = 2
        contador2 = (puntos1 + puntos2 + puntos3)
    if opcion == 3: 
        print ('equipo 3')
        opcion4 = int(input('>>>>>>OPCIONES<<<<< \n1. lanza_falta  \n2. lanza_fuera \n3. lanza_bomba \n\opcion es -> '))
        if opcion4 <1 or opcion2 > 3:
            print ('error, intentelo de nuevo')
        if opcion4 == 1:
            puntos1 = 1
        if opcion4 == 2: 
            puntos2 = 3
        if opcion4 == 3:
            puntos3 = 2
        contador3 = (puntos1 + puntos2 + puntos3)
    if opcion == 4:
        print('equipo 4')
        opcion5 = int(input('>>>>>>OPCIONES<<<<< \n1. lanza_falta  \n2. lanza_fuera \n3. lanza_bomba \n\opcion es -> '))
        if opcion5 <1 or opcion2 > 3:
            print ('error, intentelo de nuevo')
        if opcion5 == 1:
            puntos1 = 1
        if opcion5 == 2: 
            puntos2 = 3
        if opcion5 == 3:
            puntos3 = 2
        contador4 = (puntos1 + puntos2 + puntos3)
    if opcion  == 5:
        break
print('puntje del equipo  1',contador1)
print('puntaje del equipo 2',contador2)
print('puntaje del equipo 3',contador3)
print('puntaje del  equipo 4',contador4)
 
 
if contador1 >  contador2 and contador1> contador3 and contador1 > contador4:
     print("el equipo uno es el ganador")
elif contador2 > contador1 and contador2 > contador3 and contador2 > contador4 :
      print ("el equipo dos es el ganador ")
elif contador3 > contador1 and contador3 > contador2 and contador3 >contador4:
       print ("el equipo tres es el ganador")
elif contador4 > contador1  and contador4 > contador2 and contador4 > contador3:
      print ("el equipo cuatro es el ganador")

     
        
        
        
        
        
        
       
        
            
            
            