from django.db import models

from base.models import User


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    initials = models.CharField(max_length=10, blank=False, null=False)
    serie = models.CharField(max_length=5, blank=False, null=False)
    state = models.BooleanField(default=True)
    colour = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.initials = self.initials.upper()
        self.serie = self.serie.upper()
        super().save(*args, **kwargs)


class Laboratory(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=150, blank=True, null=True)
    vacancies = models.IntegerField()
    location = models.CharField(max_length=100, blank=True, null=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Semester(models.Model):
    semester = models.CharField(max_length=10, blank=False, null=False)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.semester


class Schedule(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=50, blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)

    def __str__(self):
        return '{} {} {} {}-{}'.format(self.laboratory, self.course, self.day, self.start_time, self.end_time)
