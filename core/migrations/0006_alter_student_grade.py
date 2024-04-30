# Generated by Django 4.2.11 on 2024-04-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_student_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '1 класс'), (2, '2 класс'), (3, '3 класс'), (4, '4 класс'), (5, '5 класс'), (6, '6 класс'), (7, '7 класс'), (8, '8 класс'), (9, '9 класс'), (10, '10 класс'), (11, '11 класс')], default='', max_length=2),
        ),
    ]
