# Generated by Django 5.0.4 on 2024-04-04 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_time_pair_alter_group_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Time_Pair',
            new_name='Time',
        ),
    ]
