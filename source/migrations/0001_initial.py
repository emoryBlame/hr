# Generated by Django 2.2.4 on 2019-08-01 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('date_starts', models.DateTimeField(auto_now=True)),
                ('date_ends', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source.Category')),
            ],
        ),
    ]
