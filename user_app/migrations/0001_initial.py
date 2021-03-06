# Generated by Django 2.2 on 2019-12-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('reputation', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
    ]
