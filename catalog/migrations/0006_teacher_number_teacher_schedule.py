# Generated by Django 5.0.4 on 2024-04-04 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='number_teacher',
            field=models.IntegerField(help_text='Введите порядковый номер преподавателя', null=True),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.CharField(help_text='Введите название предмета', max_length=100)),
                ('class_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.class')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.group')),
                ('number_pair', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.time')),
                ('teacher_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.teacher')),
            ],
        ),
    ]
