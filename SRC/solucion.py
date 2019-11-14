#-*-coding-8-*-
def construir_diccionario():
    Pais_vuelos = {}
    mes_total={}
    archivo=open("datos_vuelos.csv","r+")
    lineas  = archivo.readlines()
    lineas.pop(0) 
    for l in lineas:
        datos= l.split(",") 
        vuelo= datos[0]
        vuelos = vuelo.split(";")
        mes = datos[2].replace("{"," ")
        mes=str(mes[3:5])
        if mes not in mes_total:
            mes_total[mes]=1
        else :
            mes_total[mes]+=1

        if not mes in Pais_vuelos:
                Pais_vuelos[mes]={}
        else:    
            if vuelo not in Pais_vuelos:
                Pais_vuelos[mes][vuelo]= 1
            else : 
                Pais_vuelos[mes][vuelo]+=1
    
    print(mes_total)
    print (Pais_vuelos,"\n\n")
    archivo.close()
    return mes_total,Pais_vuelos
    


def procentajes():
    mes_total,Pais_vuelos=construir_diccionario()
    procen ={}
    for mes in Pais_vuelos.keys():
        procen[mes]={}
        for vuelo in Pais_vuelos[mes].keys():
            valor=((Pais_vuelos[mes][vuelo]/mes_total[mes])*100)
            if valor>=20:
                procen[mes][vuelo]=valor


    return procen,mes,vuelo 


def escribir ():
    mes,procen=procentajes()
    

    archivo=open("resultados.csv","w+")
    archivo.write("Mes, País, porcentaje  ")
    for mes in procen:
        archivo.write(mes)
        archivo.write("\n")
    


escribir()