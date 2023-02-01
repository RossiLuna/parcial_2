'''El último deseo de Timmy Turner fue jugar Batalla Naval con barcos de
verdad, y sus padrinos mágicos cumpliendo con su deber, se lo
concedieron. Una vez iniciada la batalla Timmy comenzó a disparar misiles
a diestra y siniestra contra la flota enemiga, pero debido a su poca
inteligencia, Timmy no tomaba en cuenta la cinemática del lanzamiento
de proyectiles y a veces acertaba y otras veces no.
Esto obligo a Timmy a desear un ingeniero que lo ayudara con el problema;
como resultado del deseo apareció usted.
El problema es el siguiente: el centro de control del barco de Timmy registra
los siguientes datos sobre los barcos de la flota enemiga:
IDENTIFICACIÓN, DISTANCIA DE DICHO BARCO AL BARCO DE TIMMY (EXPRESADO EN METROS) Y VELOCIDAD INICIAL HORIZONTAL
(VOX) DEL MISIL QUE TIMMY LANZÓ CONTRA ÉL (EXPRESADO EN M/S)
Usted debe desarrollar un programa que lea los datos registrados por el centro de control, en el archivo
lanzamientos.txt usando la teoría del lanzamiento de proyectiles, procese la información y genere dos archivos de
nombre destruidos.txt y nodestruidos.txt, con los números de identificación de los barcos que fueron destruidos y no
destruidos respectivamente.
Adicionalmente determine e imprima por pantalla:
• De los barcos destruidos, la identificación del barco que estaba más cerca.
• De los barcos que NO fueron destruidos, porcentaje de misiles que no alcanzaron al
barco enemigo expresado respecto al total de barcos No destruidos.
• Porcentaje de barcos destruidos.
• Velocidad inicial vertical (V0Y) promedio en m/s.
CONSIDERACIONES
Timmy disparó un misil por cada barco enemigo.
• La velocidad inicial (V0) es un dato proporcionado por el manual del lanzamisiles, el cual
especifica que la velocidad inicial del primer lanzamiento es de 250 m/s, y por cada
nuevo lanzamiento ésta disminuye en 1%.
• Los barcos se considerarán destruidos, si la diferencia entre distancia entre el barco de
Timmy y el barco a destruir almacenada en el archivo y el alcance determinado
mediante la fórmula, es en valor absoluto menor a 10-5
o El misil puede caer antes del barco, en cuyo caso se considera que no alcanzó
el barco, o puede caer después del barco en cuyo caso, se considera que
sobrepasó el barco. En ambos casos el barco se considera NO DESTRUIDO
o No puede agregar centinela al archivo de datos, use la función fin de archivo
o Formulas necesarias:'''
from math import sqrt
vo = 250
g = 9.8
misil = 0
n_des = 0
des = 0
total = 0
acum_voy = 0
band = 0
m_id = ''
m_d = ''
arch1 = open('lanzamientos.txt', 'r')
arch2 = open('destruidos.txt', 'w')
arch3 = open('nodestruidos.txt', 'w')
for registro in arch1:
    lista = registro.split(',')
    id = lista[0]
    d = float(lista[1])
    vox = float(lista[2].strip('\n'))
    voy = sqrt((vo ** 2) - (vox ** 2))
    vo -= vo / 100
    tv = 2 * voy / g
    alcance = vox * tv
    acum_voy += voy
    total += 1
    if abs(d - alcance) < 10 ** -5:
        arch2.write(registro)
        des += 1
        if band == 0:
            m_id = id
            m_d = d
            band = 1
        if d < m_d:
            m_d = d
            m_id = id
    else:
        arch3.write(registro)
        if alcance < d:
            misil += 1
        n_des += 1
if n_des != 0:
    porc = (misil / n_des) * 100
else:
    porc = 0
porc2 = (des / total) * 100
prom = acum_voy / total
print('El barco destruido mas cercano es: ', m_id )
print(f'De los barcos NO destruidos el porcentaje de misiles que no alcanzaron su objetivo es: {porc:6.2f} %')
print(f'El porcentaje de barcos destruidos es: {porc2:6.2f} %')
print(f'Promedio de la velocidad vertical es: {prom:6.2f}')
arch1.close()
arch2.close()
arch3.close()
