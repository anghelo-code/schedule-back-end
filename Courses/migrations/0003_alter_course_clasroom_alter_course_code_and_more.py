# Generated by Django 4.1.4 on 2023-01-23 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_alter_career_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='clasroom',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
