import requests
from bs4 import BeautifulSoup
from .models import Career, Course, Time, Day

def recuperar_carreras():
  # Recuperar información del catálogo
  a = requests.get('http://ccomputo.unsaac.edu.pe/?op=catalog')
  asoup = BeautifulSoup(a.text, 'html.parser')
  carreras = asoup.find('table', id="hor-minimalist-b")

  # Recuperar los nombres
  lista_carreras = []
  k = 0

  for i in carreras.find_all('tr'):
    text = i.text
    if k > 0 and k < 10:
      lista_carreras.append(text[1:-6])
      Career.objects.create(name=text[1:-6])
    elif k > 0 and k >= 10:
      lista_carreras.append(text[2:-6])
      Career.objects.create(name=text[2:-6])
    k += 1
    
  # Recuperaar los links
  links = []
  for i in carreras.find_all('a', href=True):
    if i['href'][0] == 'i':
      links.append(i['href'])

  print(lista_carreras)
  # Juntar en un diccionario
  diccionario_carreras = {}
  for i in range(len(lista_carreras)-1):
    diccionario_carreras[lista_carreras[i]] = 'http://ccomputo.unsaac.edu.pe/'+links[i]
  return diccionario_carreras

def recuperar_cursos(recup_carrera, diccionario_carreras):
  # Recuperar información del link correspondiente
  r = requests.get(str(diccionario_carreras[recup_carrera]))
  soup = BeautifulSoup(r.text, 'html.parser')
  table = soup.find('table', id="hor-minimalist-b")
  lista = []

  for i in range(200):
    lista.append(str(i))
  diccionario = {}
  flag = 0
  cursoid = ''

  for i in table.find_all('tr'):
    text = i.text.split('\n')
    # Recuperar nombre
    if text[1] in lista:
      diccionario[text[2]] = {
        'nombre': text[3], 
        'creditos': text[4], 
        'semestre': text[7], 
        'horas': {}, 
        'aulas': ''}
      
      cursoid = text[2]
      flag = 1

    if flag == 1:
      flag = 0

    else:
      # Recuperar horas
      if text[1] != '\xa0':
        cadena = (text[0].split('['))
        if len(cadena) > 1:
          dia=cadena[0][-2:]
          hora = cadena[1].split('-')
          horas = [dia, int(hora[0]), int(hora[1][:-1])]
          recuperar_aula(cursoid, dia, text[2], diccionario)
          crear_fechas(cursoid, horas, diccionario)

  aux = Career.objects.get(name=recup_carrera)
  for key, value in diccionario.items():
    if value['creditos'] == 'CUALITATIVA':
      value['creditos'] = 200
    elif value['creditos'] == ' EL EMPRENDIMIENTO':
      value['creditos'] = 400
    aux2 = Course.objects.create(
      code = key,
      name = value['nombre'],
      credit_course = value['creditos'],
      semester = value['semestre'],
      clasroom = value['aulas'],
      id_career = aux
    )
    for tiKey, tiValue in value['horas'].items():
      if tiKey == '':
        tiKey = 'None'

      Time.objects.create(
        cod_course = aux2,
        cod_day = Day.objects.get(day_name=tiKey),
        open_t = tiValue[0],
        close_t = tiValue[1]
      )



def crear_fechas(cursoid, horas, diccionario):
  diccionario[cursoid]['horas'][horas[0]]=[horas[1], horas[2]]



def recuperar_aula(cursoid,dia,value, diccionario):
  diccionario[cursoid]['aulas']+=dia+': '+value[:-2]+' '


