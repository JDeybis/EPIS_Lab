
from django.urls import path

from .views import Matricula, schedule_list, matricula_cursos, matricula_confirm
from .reports import reporte_matricula

urlpatterns = [
    path('matricula/', Matricula, name='matricula'),
    path('matricula/confirm', matricula_confirm, name='matricula_confirm'),
    path('matricula/horarios_list/', schedule_list, name='horarios_list'),
    path('matricula/curso_mat', matricula_cursos, name='matricula_cursos'),
    path('matricula/reporte', reporte_matricula, name='reporte_matricula'),
]

