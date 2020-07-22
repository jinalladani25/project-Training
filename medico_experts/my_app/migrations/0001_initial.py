# Generated by Django 2.2.6 on 2019-10-14 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('otp', models.IntegerField(default=459)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verfied', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('qualification', models.CharField(blank=True, max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('clinic', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('about_doc', models.CharField(blank=True, max_length=100)),
                ('profile_pic', models.FileField(default='doc_male.png', upload_to='doctorfinder/img/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.User')),
            ],
        ),
    ]