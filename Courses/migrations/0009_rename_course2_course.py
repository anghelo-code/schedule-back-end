# Generated by Django 4.1.4 on 2023-01-17 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0008_course2_alter_time_cod_course_delete_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course2',
            new_name='Course',
        ),
    ]
