# Generated by Django 4.1 on 2022-09-07 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ralphs', models.BooleanField(default=False)),
                ('hmart', models.BooleanField(default=False)),
                ('user_email', models.EmailField(max_length=254)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
