# Generated by Django 3.0.1 on 2020-04-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('office', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('joining', models.DateField(auto_now_add=True)),
                ('salary', models.BigIntegerField()),
            ],
        ),
    ]
