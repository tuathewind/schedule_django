# Generated by Django 5.0.4 on 2024-04-04 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_teacher_number_teacher_schedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='teacher_number',
            new_name='teacher',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='number_teacher',
        ),
    ]
