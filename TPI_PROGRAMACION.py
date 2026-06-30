import csv

def ingreso_texto(a): #Funcion para validar solo texto
    while True:
        try:  
            texto=input(f"{a}: ").strip().lower()
            if not texto.replace(" ", "").isalpha():
                raise ValueError("Debe ingresar un nombre que solo contenga letras: ")
            return texto
            
        except ValueError as e:
                print(f"Error: {e}")



def ingreso_numero_entero(a):# Funcion para validar solo numero entero positivo
    while True: 
        try:
            numero=int(input(f"{a} "))
            if numero<=0:
                raise ValueError("Debe ingresar un numero mayor a cero")
            return numero 
                
        except ValueError as e:
            print(f"Error: {e}")
        
        
                    

def agregar_pais():# Se agrega un nuevo pais
    
    with open ("paises.csv","r",encoding="utf-8") as archivo:
        lector=csv.DictReader(archivo)
        nombre = ingreso_texto("Ingrese el nombre del país: ")
        for fila in lector: #Se verifica que no este duplicado en la base de datos
            if nombre==fila["nombre"].lower().strip():
                print("Ese pais ya fue cargado")
                return
    
    poblacion = ingreso_numero_entero(f"Ingrese la población de {nombre}: ")
    superficie = ingreso_numero_entero(f"Ingrese la superficie de {nombre}: ")
    continente = ingreso_texto(f"Ingrese el continente donde se ubica {nombre}: ")
    nuevo_pais=[nombre,poblacion,superficie,continente]

    
    with open("paises.csv", "a", encoding="utf-8", newline="") as archivo:
        base=csv.writer(archivo)
        base.writerow(nuevo_pais)

    print("Pais agregado correctamente")
  
  

def actualizar_pais():
    existe=False
    lista_paises=[]
    nombre = ingreso_texto("Ingrese el nombre del país: ")
    with open ("paises.csv","r",encoding="utf-8") as archivo:
        base=csv.DictReader(archivo)
        


        for fila in base: #Se verifica que el pais se encuentre en la base de datos
            if nombre==fila["nombre"].lower().strip():
                poblacion = ingreso_numero_entero(f"Ingrese la población de {nombre}: ")
                superficie = ingreso_numero_entero(f"Ingrese la superficie de {nombre}: ")
                fila["poblacion"]=poblacion
                fila["superficie"]=superficie
                print("Se actulizaron los datos ingresados")
                existe=True
            lista_paises.append(fila)
        if not existe:
            print("El pais no existe en la base de datos")
            return
        
    
    
    with open("paises.csv", "w", encoding="utf-8", newline="") as archivo:
       columnas = ["nombre", "poblacion", "superficie", "continente"]
       escritor = csv.DictWriter(archivo, fieldnames=columnas)
       escritor.writeheader()
       escritor.writerows(lista_paises)
    

def buscar_pais():
    existe=False
    nombre = ingreso_texto("Ingrese el nombre del país: ")
    with open ("paises.csv","r",encoding="utf-8") as archivo:
        base=csv.DictReader(archivo)
        
        for fila in base: #Se verifica que el pais se encuentre en la base de datos e imprime el diccionario
            if fila["nombre"].lower().strip().startswith(nombre):
                print(fila)
                existe=True
            
        if not existe:
            print("El pais no existe en la base de datos")
            return

def filtrar_por_continente():
    existe=False
    continente = ingreso_texto("Ingrese el nombre del continente: ")
    with open ("paises.csv","r",encoding="utf-8") as archivo:
        base=csv.DictReader(archivo)
        
        for fila in base: #Se verifica que el pais se encuentre en la base de datos e imprime el diccionario
            if continente==fila["continente"].lower().strip():
                print(fila)
                existe=True
            
        if not existe:
            print("No existen paises de ese continente registrados")
            return

def filtrar_por_poblacion():
    existe=False
    lim_inf=ingreso_numero_entero("Ingrese el limite inferior del rango de poblacion: ")
    lim_sup=ingreso_numero_entero("Ingrese el limite superior del rango de poblacion: ")
    try:
        if lim_inf>lim_sup:
            raise ValueError("el limite inferior debe ser menor al mayor")
    except ValueError as e:
        print(f"Error: {e}")
        return

    with open ("paises.csv","r",encoding="utf-8") as archivo:
        base=csv.DictReader(archivo)
        
        for fila in base: 
            if lim_inf<=int(fila["poblacion"])<=lim_sup:
                print(fila)
                existe=True
            
        if not existe:
            print("No existen paises con poblacin en ese rango")
            return
    
    

def filtrar_por_superficie():
    existe=False
    lim_inf=ingreso_numero_entero("Ingrese el limite inferior del rango de superficie: ")
    lim_sup=ingreso_numero_entero("Ingrese el limite superior del rango de superficie: ")
    try:
        if lim_inf>lim_sup:
            raise ValueError("el limite inferior debe ser menor al mayor")
    except ValueError as e:
        print(f"Error: {e}")
        return

    with open ("paises.csv","r",encoding="utf-8") as archivo:
        base=csv.DictReader(archivo)
        
        for fila in base: 
            if lim_inf<=int(fila["superficie"])<=lim_sup:
                print(fila)
                existe=True
            
        if not existe:
            print("No existen paises con superficie en ese rango")
            return

def ordenar_por_nombre():
    lista_paises = []
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        base = csv.DictReader(archivo)
        for fila in base:
            lista_paises.append(fila)

    # Bubble sort por nombre
    n = len(lista_paises)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista_paises[j]["nombre"] > lista_paises[j + 1]["nombre"]:
                lista_paises[j], lista_paises[j + 1] = lista_paises[j + 1], lista_paises[j]

    for fila in lista_paises:
        print(fila)

def ordenar_por_poblacion():
    lista_paises = []
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        base = csv.DictReader(archivo)
        for fila in base:
            lista_paises.append(fila)

    # Bubble sort por poblacion
    n = len(lista_paises)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if int(lista_paises[j]["poblacion"]) > int(lista_paises[j + 1]["poblacion"]):
                lista_paises[j], lista_paises[j + 1] = lista_paises[j + 1], lista_paises[j]

    for fila in lista_paises:
        print(fila)

def ordenar_por_superficie():
    lista_paises = []
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        base = csv.DictReader(archivo)
        for fila in base:
            lista_paises.append(fila)

    # Bubble sort por superficie
    n = len(lista_paises)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if int(lista_paises[j]["superficie"]) > int(lista_paises[j + 1]["superficie"]):
                lista_paises[j], lista_paises[j + 1] = lista_paises[j + 1], lista_paises[j]

    for fila in lista_paises:
        print(fila)

def mostrar_estadisticas():
    lista_paises = []
    menor_poblacion=dict()
    mayor_poblacion=dict()
    sumatoria_poblacion=0
    sumatoria_superficie=0
    contador=0
    paises_por_continente={"asia":0,"america":0,"europa":0,"africa":0,"oceania":0}

    with open("paises.csv", "r", encoding="utf-8") as archivo:
        base = csv.DictReader(archivo)
        for fila in base:
            lista_paises.append(fila)
        menor_poblacion=lista_paises[0]
        mayor_poblacion=lista_paises[0]

#Calculo de mayor y menor poblacion
    for i in lista_paises: 
        if int(i["poblacion"])>int(mayor_poblacion["poblacion"]):
            mayor_poblacion=i
        if int(i["poblacion"])<int(menor_poblacion["poblacion"]):
            menor_poblacion=i
    print(f"{mayor_poblacion['nombre']} es el pais con mayor poblacion con {mayor_poblacion['poblacion']} habitantes ")
    print(f"{menor_poblacion['nombre']} es el pais con menor poblacion con {menor_poblacion['poblacion']} habitantes ")

#Calculo de promedios de la poblacion y superficie

    for i in lista_paises: 
        sumatoria_poblacion+= int(i["poblacion"])
        
        sumatoria_superficie+= int(i["superficie"])

        contador+=1

    print(f"La poblacion promedio es {sumatoria_poblacion/contador}")
    print(f"La superficie promedio de los paises es {sumatoria_superficie/contador}")

# Contar cantidad de paises por continente
    for i in lista_paises:
        paises_por_continente[(i["continente"]).lower().strip()]+=1
    print(f"""Paises por contiente:
         {paises_por_continente} """)

# Menu

while True:

    
    opcion = ingreso_numero_entero("""
========= MENÚ =========

1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar 
5. Ordenar
6. Mostrar estadísticas
7. Salir

Seleccione una opción: """)

    

    if opcion == 1:
        agregar_pais()

    elif opcion== 2:
        actualizar_pais()

    elif opcion == 3:
        buscar_pais()

    elif opcion ==4:
        while True:

    
            opcion = ingreso_numero_entero("""
            ========= MENÚ FILTROS =========

            1. Filtrar por continente
            2. Filtrar por poblacion
            3. Filtrar por superficie

            Seleccione una opción: """)

            if opcion == 1:
                filtrar_por_continente()
                break

            elif opcion == 2:
                filtrar_por_poblacion()
                break

            elif opcion == 3:
                filtrar_por_superficie()
                break
            
            else:
                break
            
    elif opcion ==5:
        
        while True:

    
            opcion = ingreso_numero_entero("""
            ========= MENÚ ORDENAR =========

            1. Ordenar por nombre
            2. Ordenar por poblacion
            3. ordenar por superficie

            Seleccione una opción: """)

            if opcion == 1:
                ordenar_por_nombre()
                break

            elif opcion == 2:
                ordenar_por_poblacion()
                break

            elif opcion == 3:
                ordenar_por_superficie()
                break
            
            else:
                break

    elif opcion == 6:
        mostrar_estadisticas()

    elif opcion == 7:
        print("Programa finalizado.")
        break

    else:
        print("De ingresar un numero entero de 1 a 7")

    

