# Generated by Django 4.1.3 on 2022-12-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joining_date', models.CharField(max_length=120)),
                ('end_date', models.CharField(max_length=120)),
            ],
        ),
    ]
