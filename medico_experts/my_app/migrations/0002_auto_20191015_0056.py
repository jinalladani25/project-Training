# Generated by Django 2.2.6 on 2019-10-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='qualification',
            new_name='certifications',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='city',
            new_name='residency',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='state',
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital_affiliations',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='internship',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='medical_school',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
