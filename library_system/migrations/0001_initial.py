# Generated by Django 3.1.1 on 2020-09-09 17:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('max_limit', models.IntegerField()),
                ('total_fine', models.IntegerField()),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateTimeField(verbose_name=datetime.date(2020, 9, 24))),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_system.book')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_system.student')),
            ],
        ),
    ]
