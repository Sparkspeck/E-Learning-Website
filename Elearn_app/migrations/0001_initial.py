# Generated by Django 5.0.6 on 2024-06-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fe_name', models.CharField(max_length=100)),
                ('fe_review', models.CharField(max_length=100)),
                ('fe_condent', models.CharField(max_length=100)),
            ],
        ),
    ]
