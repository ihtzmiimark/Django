# Generated by Django 4.2.4 on 2023-08-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Enter first name')),
                ('lastname', models.CharField(max_length=50, verbose_name='Enter last name')),
                ('email', models.CharField(max_length=50, verbose_name='Enter email')),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
