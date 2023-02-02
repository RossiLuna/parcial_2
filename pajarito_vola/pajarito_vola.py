'''“Pajarito Vola, C.A.” es una empresa fabricante de paracaídas, que siempre anda en búsqueda de diseños nuevos y de alta tecnologías que le permitan competir en el mercado. Razón por la cual acaba de promover un concurso de diseño de paracaídas, donde el prototipo ganador será el nuevo producto estrella de la empresa.
Dicho concurso consta de varias etapas de selección; la primera de ellas consiste en un análisis teórico del diseño del paracaídas, donde se determina a través de expresiones matemáticas la velocidad de aterrizaje y el tiempo de vuelo del paracaidista. Para la realización de esta selección, se registraron los siguientes datos de todos los participantes, en un archivo de nombre paracaidistas.txt:
Nombre del prototipo, área efectiva del paracaídas (expresada en m2) y categoría del paracaídas
La categoría del paracaídas es un valor numérico entero 1, 2 ó 3.
La empresa desea que usted desarrolle un programa que procesa el archivo de datos paracaidistas.txt y determine y genere dos archivos pasan.txt y nopasan.txt, los cuales deben contener respectivamente los concursantes que pasan a la segunda etapa y los que no, en cada archivo debe escribir: Nombre del Prototipo, valores teóricos calculados de Velocidad de aterrizaje y tiempo de vuelo del paracaidista
Para todos los concursantes, escriba por pantalla:
 Cantidad de concursantes que NO pasan a la segunda etapa y el porcentaje que representan del total de concursantes.
 Velocidad de aterrizaje promedio de los paracaídas por cada una de las categorías (son 3 promedios a calcular).
 Nombre del primer prototipo de paracaídas en ser seleccionado para la segunda etapa.
 De los concursantes seleccionados, el nombre del prototipo y la velocidad de aterrizaje del que obtuvo el menor tiempo de vuelo.
Consideraciones:
 Para calcular el tiempo de vuelo y la velocidad de aterrizaje del paracaidista utilice las siguientes expresiones:
 𝑡𝑣𝑢𝑒𝑙𝑜=1√𝛼∙𝑔ln(𝑒𝛼∙ℎ+√𝑒2∙𝛼∙ℎ−1) (Tiempo de vuelo)[seg]
 𝑣=√𝑔𝛼∙𝑡𝑎𝑛ℎ(𝑡𝑣𝑢𝑒𝑙𝑜√𝛼∙𝑔) (Velocidad de aterrizaje)[m/s]
 Donde:
     𝑔=9,8 𝑚𝑠2⁄ (Aceleración de gravedad)
    𝛼=𝑘∙𝐴𝑡 (Factor de forma del paracaídas)
    𝐴𝑡= Área efectiva del paracaídas
    ℎ=2000 𝑚 (Altura de lanzamiento del paracaidista)
 La constante k utilizada para calcular el factor de forma del paracaídas tiene un valor diferente para cada categoría, tal como se muestra en la siguiente tabla:

Categoría 	k
1			8,06 x 10-3
2			7,17 x 10-3
3			6,27 x 10-3

Los concursantes que pasan a la segunda etapa de selección son aquellos que tienen una velocidad de aterrizaje menor a 47,78 m/s.
'''
from math import sqrt
from math import log
from math import e
from math import tanh
g = 9.8
h = 2000
c_no_pasan = 0
total = 0
acum_v_1 = 0
acum_v_2 = 0
acum_v_3 = 0
cont1 = 0
cont2 = 0
cont3 = 0
band = 0
menor_t = 6000000000000000
nombre_menor = ''
primero_selec = ''
v_menor = 0
arch1 = open('paracaidistas.txt','r')
arch2 = open('pasan.txt','w')
arch3 = open('nopasan.txt','w')

for registro in arch1:
    lista = registro.split(',')
    nombre = lista[0]
    at = float(lista[1])
    categoria = int(lista[2].strip('\n'))
    total += 1
    constante = {1: 8.06 * (10 ** -3), 2: 7.17 * (10 ** -3), 3: 6.27 * (10 ** -3) }
    k = constante.get(categoria)
    a = k * at
    tv = (1 / sqrt(a * g)) * log((e ** (h * a)) + sqrt((e ** (h * a * 2)) - 1))
    v = sqrt(g / a) * tanh(tv * sqrt(a * g))
    
    if v < 47.78:
        arch2.write('%s,%f,%f' % (nombre, v, tv) + '\n')
        if band == 0:
            primero_selec = nombre
            band = 1
        if tv < menor_t:
            menor_t = tv
            nombre_menor = nombre
            v_menor = v       
    else:
        arch3.write('%s,%f,%f' % (nombre, v, tv) + '\n')
        c_no_pasan += 1
    
    
    if categoria == 1:
        acum_v_1 += v
        cont1 += 1
    elif categoria == 2:
        acum_v_2 += v
        cont2 += 1
    elif categoria == 3:
        acum_v_3 += v
        cont3 += 1

porc_no_pasan = (c_no_pasan / total) * 100

print('El porcentaje de los que no pasan es de: %.2f' %(porc_no_pasan) + '%' + '\n')

if cont1 != 0:
    v_prom1 = acum_v_1 / cont1
    print(f'Velocidad promedio de aterrizaje de los prototipos tipo 1 es:{v_prom1:6.2f}  m/s')
else:
    print('No hubo prototipos de categoria 1')

if cont2 != 0:
    v_prom2 = acum_v_2 / cont2
    print(f'Velocidad promedio de aterrizaje de los prototipos tipo 2 es:{v_prom2:6.2f}  m/s')
else:
    print('No hubo prototipos de categoria 2')
    
if cont3 != 0:
    v_prom3 = acum_v_3 / cont3
    print(f'Velocidad promedio de aterrizaje de los prototipos tipo 3 es:{v_prom3:6.2f}  m/s \n')
else:
    print('No hubo prototipos de categoria 3\n')

if primero_selec != '':
    print('El nombre del primer prototipo seleccionado es: ',primero_selec,'\n')
    print('El menor tiempo de vuelo fue de: %s  \nVelocidad de aterrizaje: %.2f  m/s' %(nombre_menor, v_menor))
else:
    print('No hubo seleccionados\n')
    
arch1.close()
arch2.close()
arch3.close()
