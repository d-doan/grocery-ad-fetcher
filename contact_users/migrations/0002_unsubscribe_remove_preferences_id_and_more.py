# Generated by Django 4.1 on 2022-09-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unsubscribe',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='id',
        ),
        migrations.AlterField(
            model_name='preferences',
            name='user_email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
