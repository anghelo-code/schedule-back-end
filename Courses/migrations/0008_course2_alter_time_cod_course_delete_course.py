# Generated by Django 4.1.4 on 2023-01-17 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0007_alter_course_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('credit_course', models.IntegerField()),
                ('semester', models.CharField(max_length=10)),
                ('clasroom', models.CharField(max_length=35)),
                ('id_career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.career')),
            ],
            options={
                'unique_together': {('code', 'id_career')},
            },
        ),
        migrations.AlterField(
            model_name='time',
            name='cod_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.course2'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
