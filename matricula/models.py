from django.db import models

from base.models import User
from horario.models import Schedule, Course, Semester


# Create your models here.


class Enrollment(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.schedule, self.user)


class Theory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.course, self.semester, self.user)
