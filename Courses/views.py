from django.shortcuts import get_list_or_404
from django.http import JsonResponse, HttpResponse
from .models import Course, Career, Time
from .recoverTable import recuperar_carreras, recuperar_cursos

# Create your views here.
def Careers_v(request):
  careers = list(Career.objects.values())
  return JsonResponse([careers], safe=False)


def Courses_v(request, id_careers):
  courses = get_list_or_404(Course, id_career = int(id_careers))
  arr_courses = {}
  for course in courses:
    arr_time = {}
    times = get_list_or_404(Time, cod_course = course.id)

    for time in times :
      day = time.cod_day.day_name
      arr_time[day] = [
        time.open_t,
        time.close_t
      ]

    arr_courses[course.code] = {
      "nombre": course.name,
      "creditos": course.credit_course,
      "semestre": course.semester,
      "horas": arr_time,
      "aulas": course.clasroom,
    }
    
  return JsonResponse(arr_courses, safe=False)


def CreateTable(request):
  Career.objects.all().delete()
  Course.objects.all().delete()

  diccionario_carreras=recuperar_carreras()

  for i in diccionario_carreras:
    recup_carrera=i
    print(recup_carrera)
    recuperar_cursos(recup_carrera,diccionario_carreras)

  return HttpResponse('<h1>Se Creo las tablas de forma correcta</h1>')
