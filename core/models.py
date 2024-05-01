from django.db import models
from datetime import date


class Subject(models.Model):
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
    complexities = [('Базовый', 'Базовый уровень'),
                    ('Продвинутый', 'Продвинутый уровень')]
    subjects.sort()
    name = models.CharField(choices=subjects, max_length=30)
    complexity = models.CharField(choices=complexities, max_length=30)
    members = models.ManyToManyField('Student')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self) -> str:
        return f'{self.name}, {self.complexity} уровень'


class Student(models.Model):
    name = models.CharField(default='', max_length=20)
    surname = models.CharField(default='', max_length=20)
    middlename = models.CharField(default='', max_length=20)
    date_of_birth = models.DateField(default=date.today(), blank=False)

    grades = [(i, f'{i} класс') for i in range(1, 12)]
    grade = models.PositiveIntegerField(default=1, choices=grades)
    parents = models.ManyToManyField('Parent')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Teacher(models.Model):
    name = models.CharField(default='', max_length=20)
    surname = models.CharField(default='', max_length=20)
    middlename = models.CharField(default='', max_length=20)
    date_of_birth = models.DateField(default=date.today(), blank=False)
    subjects = models.ManyToManyField('Subject')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.middlename}'


class Parent(models.Model):
    name = models.CharField(default='', max_length=20)
    surname = models.CharField(default='', max_length=20)
    middlename = models.CharField(default='', max_length=20)

    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'

    def __str__(self):
        return f'{self.surname} {self.name} {self.middlename}'
