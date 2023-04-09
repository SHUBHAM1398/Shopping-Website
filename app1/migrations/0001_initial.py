# Generated by Django 4.1.7 on 2023-04-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('address', models.TextField(max_length=122)),
                ('city', models.TextField(max_length=122)),
                ('state', models.TextField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]