# Generated by Django 4.1.4 on 2023-01-16 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='times',
            name='close_t',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='times',
            name='open_t',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Hours',
        ),
    ]