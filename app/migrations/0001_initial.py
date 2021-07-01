# Generated by Django 3.2.5 on 2021-07-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('expiration_date', models.DateField()),
                ('priority', models.CharField(choices=[('A', 'Alta'), ('N', 'Normal'), ('B', 'Baixa')], max_length=1)),
            ],
        ),
    ]