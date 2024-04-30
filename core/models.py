from django.db import models
from datetime import date


class Student(models.Model):
    name = models.CharField(default='', max_length=20, blank=True)
    surname = models.CharField(default='', max_length=20, blank=True)
    middlename = models.CharField(default='', max_length=20, blank=True)
    date_of_birth = models.DateField(default=date.today(), blank=True)

    grades = [(i, f'{i} класс') for i in range(1, 12)]
    grade = models.PositiveIntegerField(default=1, choices=grades, max_length=2, blank=True)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Teacher(models.Model):
    name = models.CharField(default='', max_length=20, blank=True)
    surname = models.CharField(default='', max_length=20, blank=True)
    middlename = models.CharField(default='', max_length=20, blank=True)
    date_of_birth = models.DateField(default=date.today(), blank=True)

    subjects = [('Иностранный язык', 'Иностранный язык'),
               ('Математика', 'Математика'),
               ('Русский язык', 'Русский язык'),
               ('История', 'История'),
               ('Обществознание', 'Обществознание'),
               ('Физическая культура', 'Физическая культура'),
               ('ОБЖ', 'ОБЖ'),
               ('Физика', 'Физика'),
               ('Химия', 'Химия'),
               ('Биология', 'Биология'),
               ('География', 'География'),
               ('Информатика', 'Информатика'),
    ]
    subjects.sort()
    subject = models.CharField(default='', choices=subjects, max_length=20, blank=True)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.middlename}'


class Parent(models.Model):
    name = models.CharField(default='', max_length=20, blank=True)
    surname = models.CharField(default='', max_length=20, blank=True)
    middlename = models.CharField(default='', max_length=20, blank=True)
    child = models.ForeignKey('Student', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'

    def __str__(self):
        return f'{self.surname} {self.name} {self.middlename}'
