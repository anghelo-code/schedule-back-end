# Generated by Django 4.1.4 on 2023-01-21 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0010_alter_course_credit_course_alter_time_close_t_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
