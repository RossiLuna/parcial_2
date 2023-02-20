arch1 = open('serie2023.txt', 'r')
arch2 = open('resultados.txt', 'w')
contenido = arch1.readlines()
linea = 0
d = {}
for i in range(len(contenido)):
    lista = contenido[i].split(',')
    equipo1 = lista[0]
    equipo2 = lista[1]
    ca1 = int(lista[2])
    ca2 = int(lista[3])
    entradas = int(lista[4])
    errores = int(lista[5])
    
    #Equipo1
    if d.get(equipo1,-1) == -1:
        d[equipo1] = [1,0,ca2,errores,ca1]
    else:
        h = (d.get(equipo1))[0] #juegos
        h += 1
        (d.get(equipo1))[0] = h
        
        y = (d.get(equipo1))[2] #carreras permitidas
        y += ca2
        (d.get(equipo1))[2] = y
        
        x = (d.get(equipo1))[3] #errores
        x += errores
        (d.get(equipo1))[3] = x
        
        w = (d.get(equipo1))[4] #carreras anotadas
        w += ca1
        (d.get(equipo1))[4] = w
        
    #Equipo2    
    if d.get(equipo2,-1) == -1:
        d[equipo2] = [1,0,ca1,errores,ca2]
    else:
        h = (d.get(equipo2))[0] #juegos
        h += 1
        (d.get(equipo2))[0] = h
        
        y = (d.get(equipo2))[2] #carreras permitidas
        y += ca1
        (d.get(equipo2))[2] = y
        
        x = (d.get(equipo1))[3] #errores
        x += errores
        (d.get(equipo1))[3] = x
        
        w = (d.get(equipo2))[4] #carreras anotadas
        w += ca2
        (d.get(equipo2))[4] = w
    #Equipo ganador por ining
    if ca1 > ca2:              
        g = (d.get(equipo1))[1]
        g += 1
        (d.get(equipo1))[1] = g
    
    else:
        g = (d.get(equipo2))[1]
        g += 1
        (d.get(equipo2))[1] = g
          

z = list(d.keys())  #equipos
r = list(d.values()) #datos de equipos
print(z)
print(r,'\n \n')

carano_mayor = -1
mayor_ganados = -1
while linea < len(z):
    equipo = z[linea]
    juegos = r[linea][0]
    ganados = r[linea][1]
    caper = r[linea][2]
    total_errores = r[linea][3]
    carano = r[linea][4]
    linea += 1
    
    arch2.write('%s,%d,%d,%d \n' %(equipo,caper,juegos,total_errores))
    
    juegos_perdidos = juegos - ganados
    print('Equipo: %s,Juegos ganados: %d, juegos perdidos: %d ' %(equipo,ganados,juegos_perdidos))
    por_vic = ganados * 100 / juegos
    print(f'Porcentaje de victorias:{por_vic:6.2f} % \n')

    
    if ganados > mayor_ganados:
        ganador = equipo
        mayor_ganados = ganados
    elif ganados == mayor_ganados and carano > carano_mayor:
        ganador = equipo
        caper_menor = carano
        
print('Equipo ganador: ' + ganador.title())   
  
arch2.close()
arch1.close()
