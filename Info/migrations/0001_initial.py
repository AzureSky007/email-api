# Generated by Django 4.2.1 on 2023-06-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('num', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('greet', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]