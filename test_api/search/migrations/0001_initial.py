# Generated by Django 3.1 on 2020-09-02 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
