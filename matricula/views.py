from django.http import HttpResponse
from django.shortcuts import render, redirect

import json

# Create your views here.
from django.views.generic import TemplateView, ListView

from horario.models import Course, Laboratory
from .models import Schedule, Enrollment, Theory
from base.models import User


def Matricula(request):
    template_name = "matricula/matricula.html"
    context = {}
    if request.method == "GET":
        mat = [c.course for c in Theory.objects.filter(user=request.user)]
        labs = Schedule.objects.distinct("laboratory").filter(course__in=mat, state=True)
        context['labs'] = labs
    return render(request, template_name, context)


def matricula_confirm(request):
    return render(request, template_name="matricula/matricula_confirm.html")


def matricula_cursos(request):
    if request.is_ajax and request.method == 'POST':
        ids = request.POST.get('ids')
        ids = json.loads(ids)
        for i in ids:
            horario = Schedule.objects.get(id=i)
            limite = horario.laboratory.vacancies
            matr = Enrollment.objects.filter(schedule=horario).count()
            if matr < limite:
                Enrollment.objects.create(schedule=horario, user=request.user)
            request.user.is_enrollment = True
            request.user.save()
        return HttpResponse({"Result": "Datos Guardados"}, status=200)
    return HttpResponse({"error": ""}, status=400)


def schedule_list(request):
    if request.method == 'GET':
        hs = []
        mat = [c.course for c in Theory.objects.filter(user=request.user)]
        horarios = Schedule.objects.filter(course__in=mat, state=True)
        for item in horarios:
            c_matriculados = Enrollment.objects.filter(schedule=item).count()
            h = {
                "id": item.id,
                "curso": item.course.name,
                "sigla": item.course.initials,
                "docente": item.teacher.first_name,
                "horainicio": str(item.start_time),
                "horafin": str(item.end_time),
                "dia": item.day,
                "color": item.course.colour,
                "laboratorio": item.laboratory.description,
                "limite": item.laboratory.vacancies,
                "matriculados": c_matriculados
            }
            hs.append(h)
        # data = serializers.serialize('json', hs)
        return HttpResponse(json.dumps(hs), content_type="application/json")
