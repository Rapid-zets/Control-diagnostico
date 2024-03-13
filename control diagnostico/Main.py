#Nombre y explique brevemente los pilares de la POO.
#1-abstraccion: forma en la que se pueden seleccionar solo los datos importantes y necesarios, omitiendo la complejidad. innecesaria De este modo es parecido a como se utiliza un control ya que puedes interactuar con las acciones sin preocuparte de entender los detalles internos.
#2-Encapsulamiento: forma que permite ocultar los detalles internos de como se implementan y protegerlos del acceso no autorizado con eso permitiendo controlar cómo se accede y modifica la información sin cambiar o visualizar la base.
#3-polimosfirmo: Es lo que permite que objetos que son distintos puedan responder a una misma accion pero en su propia forma, por ejemplo llamar a multiples mostrar_datos de diferentes clases.
#4-Herencia:Es lo que permite que una clase hereda atributos y acciones de otra clase padre de modo que heredan caracteristicas en comun, pero podiendo agregar nuevos atributos.

#Explique y ejemplifique el concepto de clase: es una especie de modelo en el que se puede representar diferentes instancias, cosas u objetos de forma general, definiendo sus caracteristicas con atributos y metodos que realiza. 
#Explique y ejemplifique el concepto de objeto.es una instancia especifica de una clase que tiene sus propias características y puede realizar acciones específicas. permiten representar entidades del mundo real en el código de manera organizada.
from Profesion import Profesion
def Main():
    profesiones = { "ingeniero": Profesion("Ingeniero"), 
                   "abogado": Profesion("Abogado"),
                   "otra": Profesion("Otra")  }
    while True:
        nom = input("ingrese su nombre:")
        edades = int(input("ingrese su edad: "))
        while edades < 1:
            print("//"*10)
            print("Error")
            edades = int(input("ingrese una edad correcta (mayor a 0): "))
            

        sex = str(input("ingrese su sexo (masculino(M) o femenino(F)):")).lower()
        
        while sex != "f" and sex != "m":
            print("//"*10)
            print("Error")
            sex = input(" ingrese un valor correspondiente(M o F):").lower()
        profes = input("Ingrese si su profesion es “Ingeniero”,” Abogado” u “Otra”").lower()
        
        while profes not in profesiones:
            print("//"*10)
            print("Error")
            profes = input("Ingrese si su profesion es “Ingeniero”,” Abogado” u “Otra”").lower()
        sueldo = float(input(f"Ingrese su sueldo: "))
        

    
        profesion_persona = profesiones[profes]
        profesion_persona.set_sueldo(sueldo)
        cantidad = profesion_persona.get_Cantidad_p() + 1
        profesion_persona.set_Cantidad_P(cantidad)

        continuar = input("¿Desea continuar con otra persona? (s/n): ")
        if continuar.lower() != 's':
            break

    
    total_ingenieros = profesiones["ingeniero"].get_Cantidad_p()
    total_abogados = profesiones["abogado"].get_Cantidad_p()
    total_otra = profesiones["otra"].get_Cantidad_p()
    total_personas = sum(prof.get_Cantidad_p() for prof in profesiones.values())
    

    if total_personas > 0:
        porcentaje_ingenieros = (total_ingenieros / total_personas) * 100
        porcentaje_abogados = (total_abogados / total_personas) * 100
        porcentaje_otra = (total_otra / total_personas) * 100   
        if total_ingenieros > 0:
            prom_sueldo_ingenieros = profesiones["ingeniero"].get_sueldo() / total_ingenieros
        else:
            prom_sueldo_ingenieros = 0
        if total_abogados > 0:
            prom_sueldo_abogados = profesiones["abogado"].get_sueldo() / total_abogados
        else:
            prom_sueldo_abogados = 0
        if total_otra > 0:
            prom_sueldo_otra = profesiones["otra"].get_sueldo() / total_otra
        else:
            prom_sueldo_otra = 0
        print(">"*40)
        print("Porcentaje")
        print(f"Porcentaje de Ingenieros: {porcentaje_ingenieros:.2f}%")
        print(f"Porcentaje de Abogados: {porcentaje_abogados:.2f}%")
        print(f"Porcentaje de Otra: {porcentaje_otra:.2f}%")
        print(">"*40)
        print(">"*40)
        print("Promedio")
        print(f"Promedio de sueldo Ingenieros: {prom_sueldo_ingenieros:.2f}")
        print(f"Promedio de sueldo Abogados: {prom_sueldo_abogados:.2f}")
        print(f"Promedio de sueldo Otra: {prom_sueldo_otra:.2f}")
        print(">"*40)
    else:
        print("No hay informacion de encuestas.")
Main()

