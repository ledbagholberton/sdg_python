import re
from thefuzz import fuzz


def is_dia (i):
    #print('Valido si ', i, 'es dia')
    string = re.sub('[A-Za-z]+', '', i)
    if 0 < len(string) <= 2:
        return (True)
    else:
        #print(i,' no es dia')
        return (False)
    

def is_mes (i):
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    medida = 0
    medida2 = 0
    mes = 0
    score2 = 70
    #print('Valido si ', i, 'es mes')
    for index, value in enumerate(meses):
        medida = fuzz.token_set_ratio(value, i)
        print('i, index, value & medida', i , index, value, medida)
        if medida > score2:
            score2 = medida
            mes = index
            medida2 = medida
    #print('Mes escogido: ', mes + 1)
    string = re.sub('[A-Za-z]+', '', i)
    #print('mes: ', string)
    if mes != 0:
        return [True, mes]
    else:
        #print(i,' no es mes')
        return [False, 0]

def is_year (i):
    #print('Valido si ', i, 'es año')
    string = re.sub('[A-Za-z]+', '', i)
    #print('año: ', string)
    if len(string) == 4:
        return (True)
    else:
        #print(i,' no es año')
        return (False)

txt1 = 'En Bogotá D.C., a los (8) Días del mes \n  de junio DE 2022'
txt2 = 'Fecha de reanudacion : 13/12/2021'
txt3 = 'Viernes, 03 de diciernbre de 2021'
txt4 = 'En Bogota D. C., a los 28 dlas de Octubre del ano dos mil veintiuno (2.021), '
txt5 = 'AUDIENCIA DEL 3 DE FEBRERO DE 2021'
txt6 = 'FECHA:  15 DE FEBRERO DE 2022 '
txt7 = 'Fecha de reanudacion : 13-12-2021'



dia = ''
mes = ''
year = ''
#remuevo todas las letras y caracteres especiales menos /, -,
string = re.sub('[^A-Za-z0-9 /-]+', '', txt1)
string2 = re.sub('[^0-9/-]+', '', txt1)
print(string, len(string), string2, len(string2))
#lo tokenizo por espacio
token = string.split()
#print(token)
#itero la lista de los tokens
for i in token:
    #print ('i es:', i)
    if is_dia(i):
        dia = i
    elif is_mes(i)[0]:
        mes = is_mes(i)[1] + 1
    elif is_year(i):
        year = i
fecha = dia + '/' + str(mes) + '/' + year
if len(fecha) < 3:
    fecha = string2.replace('-', '/')
print('Fecha: ', fecha)

