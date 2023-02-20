cont8 = 0
total = 0
cont_f = 0
acum_f = 0
band = 0
arch1 = open('asistencia.txt', 'r')
arch2 = open('resultados.txt', 'w')
contenido = arch1.readlines()
for i in range(len(contenido)):
    lista = contenido[i].split(',')
    total += 1
    cedula = int(lista[0])
    sexo = lista[1]
    hora_entrada = int(lista[2])
    min_entrada = int(lista[3])
    seg_entrada = int(lista[4])
    hora_salida = int(lista[5])
    min_salida = int(lista[6])
    seg_salida = int(lista[7])
    
    seg_total_entrada = hora_entrada * 3600 + min_entrada * 60 + seg_entrada
    seg_total_salida = hora_salida * 3600 + min_salida * 60 + seg_salida
    
    seg_total = seg_total_salida - seg_total_entrada
    
    seg_durado = seg_total
    
    hora_durado = seg_durado // 3600
    h = seg_durado % 3600
    min_durado = h // 60
    seg_durado = h % 60
    
    print('Cedula: %s \nTiempo durado: %d:%d:%d \n\n' %(cedula,hora_durado,min_durado,seg_durado))
    arch2.write('%s,%d,%d,%d \n'%(cedula,hora_durado,min_durado,seg_durado))
    
    if seg_total / 3600 < 8:
        cont8 += 1
        
    if sexo.lower() == 'f':
        cont_f += 1
        acum_f += seg_total / 3600
    
    if band == 0:
        if sexo.lower() == 'm':
            tiempo_min = seg_total
            band = 1
    elif sexo.lower() == 'm':
        if seg_total < tiempo_min:
            tiempo_min = seg_total
            
porc8 = cont8 * 100 / total
arch2.write(f'{porc8:.2f} \n')
print(f'Porcentaje de trabajadores que traban menos de 8 horas:{porc8:.2f}% \n')
if cont_f != 0:
    prom_f = acum_f / cont_f
    arch2.write(f'{prom_f:.2f}\n')
    print(f'Promedio de tiempo laborado por las trabajadoras: {prom_f:.2f}\n ')
else:
    arch2.write('0\n')
    print('Promedio de tiempo laborado por las trabajadoras: 0\n')
if band != 0:
    
    hora_durado = tiempo_min // 3600
    h = tiempo_min % 3600
    min_durado = h // 60
    seg_durado = h % 60
    
    arch2.write('%d,%d,%d' %(hora_durado,min_durado,seg_durado))
else:
    arch2.write('0,0,0')
arch1.close()
arch2.close()
