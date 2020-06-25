from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib import messages

from horario.models import Course, Semester
from matricula.models import Theory
from .models import User

from django.shortcuts import render, redirect
from matricula.utils import save_pdf_data


# Create your views here.
def home(request):
    return render(request, 'base/base.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect('laboratorio/matricula/')
        else:
            messages.error(request, 'Usuario o contraseña incorrecto')
    return render(request, 'login/login.html')


def create_users(request):
    # if request.method == 'POST':
    #     ## Logica para agregar los usuarios por curso
    #     # '27_CC-121.pdf'
    #     archivos = ['27_IS-141.pdf', '27_IS-241.pdf', '27_IS-341.pdf', '27_IS-441.pdf',
    #                 '27_IS-443.pdf', '27_IS-445.pdf', '27_IS-451.pdf', '27_IS-453.pdf', '27_IS-545.pdf',
    #                 '27_IS-553.pdf']
    #     for file in archivos:
    #         file = '/home/jhon/Public/developer/testpdf/' + file
    #         data = save_pdf_data(file)
    #         curso = Course.objects.get_or_create(name=data['curso'], initials=data['sigla'], serie=data['serie'])
    #
    #         if curso:
    #             for a in data['alumnos']:
    #                 u = User.objects.get(username=str(a[0]))
    #                 semestre = Semester.objects.get_or_create(semester=data['semestre'])
    #                 Theory.objects.create(course=curso[0], semester=semestre[0], user=u)

    # Logica para gnerar usuarios del pdf
    # archivos = ['27_CC-121.pdf', '27_IS-141.pdf', '27_IS-241.pdf', '27_IS-341.pdf', '27_IS-441.pdf',
    #             '27_IS-443.pdf',
    #             '27_IS-445.pdf', '27_IS-451.pdf', '27_IS-453.pdf', '27_IS-545.pdf', '27_IS-553.pdf']
    # alumnos = []
    # for file in archivos:
    #     file = '/home/jhon/Public/developer/testpdf/' + file
    #     a = save_pdf_data(file)
    #     for item in a:
    #         if item not in alumnos:
    #             alumnos.append(item)
    # for a in alumnos:
    #     User.objects.create_user(str(a[0]), 'prueba@gmail.com', '12345678')
    # print("usuarios creados")
    return render(request, 'base/base.html')
