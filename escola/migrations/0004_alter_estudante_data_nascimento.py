# Generated by Django 5.0.9 on 2024-09-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_rename_cursos_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='data_nascimento',
            field=models.DateField(auto_now_add=True),
        ),
    ]
