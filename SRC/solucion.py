#-*-coding-8-*-
def construir_diccionario():
    Pais_vuelos = {}
    mes_total={}
    archivo=open("datos_vuelos.csv","r+")
    lineas=archivo.readlines()
    lineas.pop(0)
    for l in lineas:
        datos= l.split(",") 
        vuelo= datos[0]
        mes = datos[2].replace("{"," ")
        mes=str(mes[3:5])
        if mes not in mes_total:
            mes_total[mes]=1
            Pais_vuelos[mes]={}
        else :
            mes_total[mes]+=1
        if vuelo not in Pais_vuelos[mes].keys():
            Pais_vuelos[mes][vuelo]=1
        elif vuelo in Pais_vuelos[mes].keys():
            Pais_vuelos[mes][vuelo]+=1
    
    print(mes_total)
    print (Pais_vuelos,"\n\n")
    archivo.close()
    return mes_total,Pais_vuelos
    


def procentajes():
    mes_total,Pais_vuelos=construir_diccionario()
    procen ={}
    archivo=open("resultados.csv","w+")
    archivo.write("mes,pais,porcentaje\n")
    
    for mes in Pais_vuelos.keys():
        procen[mes]={}
        for vuelo in Pais_vuelos[mes].keys():
            narch=round((((Pais_vuelos[mes][vuelo])/mes_total[mes])*100),2)
            if narch>=20:
                procen[mes][vuelo]=narch
            elif narch<20:
                procen[mes][vuelo]="No alcanza el %20"
            
            archivo.write(mes)
            archivo.write(",")
            archivo.write(vuelo)
            archivo.write(",")
            archivo.write(str(procen[mes][vuelo]))
            archivo.write("\n")
    archivo.close
    print(procen)
    return procen



procentajes()