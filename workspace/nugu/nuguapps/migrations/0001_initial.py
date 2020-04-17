# Generated by Django 2.1.7 on 2019-04-04 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=20)),
                ('typical', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('start', models.TextField()),
                ('end', models.TextField()),
                ('term', models.TextField()),
                ('first_result', models.TextField()),
                ('interview_date', models.TextField()),
                ('final_result', models.TextField()),
            ],
        ),
    ]