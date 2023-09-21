from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Course, Career, Time, Day
from .forms import CreateNewDay, CreateNewSuperUser, CreateCarrera
from .recoverTable import recuperar_carreras, recuperar_cursos

# Create your views here.
def Careers_v(request):
  careers = list(Career.objects.values())
  return JsonResponse(careers, safe=False)


def Courses_v(request, id_careers):
  courses = get_list_or_404(Course, id_career = int(id_careers))
  arr_courses = []
  for course in courses:
    arr_time = {}
    times = get_list_or_404(Time, cod_course = int(course.id))

    for time in times :
      day = time.cod_day.day_name
      arr_time[day] = [
        time.open_t,
        time.close_t
      ]

    arr_courses.append( {
      "id": course.code,
      "nombre": course.name,
      "creditos": course.credit_course,
      "semestre": course.semester,
      "horas": arr_time,
      "aulas": course.clasroom,
    })
    
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


def ActualizarCarrera(request):
  if request.method == 'GET':
    return render(request, 'actCarrera.html', {
      'form': CreateCarrera()
    })
  else:
    career = get_object_or_404(Career, id=int(request.POST["id"]));
    dic = { career.name: request.POST["link"] }
    recuperar_cursos(career.name,dic);

    return HttpResponse('<h1>Se Actualizo la Carrera de forma Correcta</h1>');



def createDay(request):
  if request.method == 'GET':
    return render(request, 'day.html', {
    'form': CreateNewDay()
  });
  else:
    Day.objects.create(day_name = request.POST["day_name"]);
    return redirect('/careers/')


def create_superuser(request):
  if request.method == 'POST':
    # obtén los datos del formulario
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    # Crea un nuevo usuario
    user = User.objects.create_superuser(username, email, password)
    # Inicia sesión automáticamente
    login(request, user)
    # Redirige a la página de inicio
    return redirect('/admin/')

  # Si el método es GET, simplemente renderiza la plantilla
  return render(request, 'create_superuser.html', {
    'form': CreateNewSuperUser()
  })